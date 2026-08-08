import os
import requests

# توکن از Secret گیت‌هاب خوانده می‌شود
token = os.environ['GH_TOKEN']
headers = {"Authorization": f"bearer {token}"}

# دریافت اطلاعات پایه با GraphQL
query = """
query {
  viewer {
    login
    name
    bio
    contributionsCollection {
      totalCommitContributions
    }
    pullRequests(first: 1) {
      totalCount
    }
    issues(first: 1) {
      totalCount
    }
    repositories(first: 1, privacy: PUBLIC) {
      totalCount
    }
    followers {
      totalCount
    }
    repositoriesContributedTo(first: 1, contributionTypes: [COMMIT, ISSUE, PULL_REQUEST, REPOSITORY]) {
      totalCount
    }
  }
}
"""

response = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
data = response.json()['data']['viewer']

name = data['name'] or data['login']
bio = data['bio'] or "سازندهٔ نرم‌افزار"
commits = data['contributionsCollection']['totalCommitContributions']
repos = data['repositories']['totalCount']
followers = data['followers']['totalCount']
prs = data['pullRequests']['totalCount']
issues = data['issues']['totalCount']
contrib_repos = data['repositoriesContributedTo']['totalCount']

# محاسبهٔ تعداد ستاره‌ها (REST API)
stars = 0
page = 1
while True:
    repos_resp = requests.get(
        f'https://api.github.com/users/MKarimi21/repos?per_page=100&page={page}',
        headers=headers
    )
    if repos_resp.status_code != 200:
        break
    page_repos = repos_resp.json()
    if not page_repos:
        break
    for repo in page_repos:
        stars += repo['stargazers_count']
    page += 1

# خواندن قالب و جایگزینی
with open('intro_template.svg', 'r', encoding='utf-8') as f:
    svg = f.read()

svg = svg.replace('{{ NAME }}', name)
svg = svg.replace('{{ BIO }}', bio)
svg = svg.replace('{{ COMMITS }}', str(commits))
svg = svg.replace('{{ STARS }}', str(stars))
svg = svg.replace('{{ PRS }}', str(prs))
svg = svg.replace('{{ ISSUES }}', str(issues))
svg = svg.replace('{{ REPOS }}', str(repos))
svg = svg.replace('{{ FOLLOWERS }}', str(followers))
svg = svg.replace('{{ CONTRIB_REPOS }}', str(contrib_repos))

# نوشتن فایل نهایی
with open('intro.svg', 'w', encoding='utf-8') as f:
    f.write(svg)

print("intro.svg ساخته شد.")
