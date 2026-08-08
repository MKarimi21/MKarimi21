import datetime
from dateutil import relativedelta
import requests
import os
from lxml import etree
import time
import hashlib

HEADERS = {'authorization': 'token ' + os.environ['ACCESS_TOKEN']}
USER_NAME = os.environ['USER_NAME']
OWNER_ID = None

def simple_request(func_name, query, variables):
    request = requests.post('https://api.github.com/graphql', 
                           json={'query': query, 'variables': variables}, 
                           headers=HEADERS)
    if request.status_code == 200:
        return request
    raise Exception(f"{func_name} failed with status {request.status_code}")

def user_getter(username):
    query = '''
    query($login: String!){
        user(login: $login) {
            id
            createdAt
        }
    }'''
    variables = {'login': username}
    request = simple_request('user_getter', query, variables)
    return request.json()['data']['user']['id'], request.json()['data']['user']['createdAt']

def graph_repos_stars(count_type, owner_affiliation, cursor=None):
    query = '''
    query ($owner_affiliation: [RepositoryAffiliation], $login: String!, $cursor: String) {
        user(login: $login) {
            repositories(first: 100, after: $cursor, ownerAffiliations: $owner_affiliation) {
                totalCount
                edges {
                    node {
                        stargazers {
                            totalCount
                        }
                    }
                }
                pageInfo {
                    endCursor
                    hasNextPage
                }
            }
        }
    }'''
    variables = {'owner_affiliation': owner_affiliation, 'login': USER_NAME, 'cursor': cursor}
    request = simple_request('graph_repos_stars', query, variables)
    
    if count_type == 'repos':
        return request.json()['data']['user']['repositories']['totalCount']
    elif count_type == 'stars':
        total_stars = 0
        for edge in request.json()['data']['user']['repositories']['edges']:
            total_stars += edge['node']['stargazers']['totalCount']
        return total_stars

def graph_commits(start_date, end_date):
    query = '''
    query($start_date: DateTime!, $end_date: DateTime!, $login: String!) {
        user(login: $login) {
            contributionsCollection(from: $start_date, to: $end_date) {
                contributionCalendar {
                    totalContributions
                }
            }
        }
    }'''
    variables = {'start_date': start_date, 'end_date': end_date, 'login': USER_NAME}
    request = simple_request('graph_commits', query, variables)
    return int(request.json()['data']['user']['contributionsCollection']['contributionCalendar']['totalContributions'])

def follower_getter(username):
    query = '''
    query($login: String!){
        user(login: $login) {
            followers {
                totalCount
            }
        }
    }'''
    request = simple_request('follower_getter', query, {'login': username})
    return int(request.json()['data']['user']['followers']['totalCount'])

def svg_overwrite(filename, commit_data, star_data, repo_data, contrib_data, follower_data, loc_data):
    tree = etree.parse(filename)
    root = tree.getroot()
    
    justify_format(root, 'commit_data', commit_data, 22)
    justify_format(root, 'star_data', star_data, 14)
    justify_format(root, 'repo_data', repo_data, 6)
    justify_format(root, 'contrib_data', contrib_data)
    justify_format(root, 'follower_data', follower_data, 10)
    justify_format(root, 'loc_data', loc_data[2], 9)
    justify_format(root, 'loc_add', loc_data[0])
    justify_format(root, 'loc_del', loc_data[1], 7)
    
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def justify_format(root, element_id, new_text, length=0):
    if isinstance(new_text, int):
        new_text = f"{'{:,}'.format(new_text)}"
    new_text = str(new_text)
    
    find_and_replace(root, element_id, new_text)
    
    just_len = max(0, length - len(new_text))
    if just_len <= 2:
        dot_map = {0: '', 1: ' ', 2: '. '}
        dot_string = dot_map[just_len]
    else:
        dot_string = ' ' + ('.' * just_len) + ' '
    
    find_and_replace(root, f"{element_id}_dots", dot_string)

def find_and_replace(root, element_id, new_text):
    element = root.find(f".//*[@id='{element_id}']")
    if element is not None:
        element.text = new_text

if __name__ == '__main__':
    # Get user data
    user_id, acc_date = user_getter(USER_NAME)
    OWNER_ID = user_id
    
    # Get all stats
    commit_data = graph_commits('2020-01-01T00:00:00Z', datetime.datetime.now().isoformat() + 'Z')
    star_data = graph_repos_stars('stars', ['OWNER'])
    repo_data = graph_repos_stars('repos', ['OWNER'])
    contrib_data = graph_repos_stars('repos', ['OWNER', 'COLLABORATOR', 'ORGANIZATION_MEMBER'])
    follower_data = follower_getter(USER_NAME)
    
    # Sample LOC data (0, 0, 0 for simplicity)
    loc_data = [0, 0, 0, True]
    
    print(f"Commits: {commit_data}")
    print(f"Stars: {star_data}")
    print(f"Repos: {repo_data}")
    print(f"Contributions: {contrib_data}")
    print(f"Followers: {follower_data}")
    
    # Update SVGs
    svg_overwrite('dark_mode.svg', commit_data, star_data, repo_data, contrib_data, follower_data, loc_data)
    svg_overwrite('light_mode.svg', commit_data, star_data, repo_data, contrib_data, follower_data, loc_data)
    
    print("✅ SVG files updated successfully!")
