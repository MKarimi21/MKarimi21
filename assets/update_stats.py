import os
import requests
import datetime
from dateutil import relativedelta

USERNAME = "MKarimi21"
TOKEN = os.environ.get("ACCESS_TOKEN")

def get_github_stats():
    headers = {'authorization': 'bearer ' + TOKEN} if TOKEN else {}
    query = '''
    query {
      user(login: "%s") {
        repositories(first: 100, ownerAffiliations: OWNER) { totalCount }
        followers { totalCount }
      }
    }''' % USERNAME
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        data = request.json()['data']['user']
        return data['repositories']['totalCount'], data['followers']['totalCount']
    return 0, 0

def calculate_age():
    # ==========================================
    # تاریخ تولد خود را اینجا به میلادی وارد کنید
    birthday = datetime.datetime(1995, 1, 1) 
    # ==========================================
    diff = relativedelta.relativedelta(datetime.datetime.today(), birthday)
    return f"{diff.years} years, {diff.months} months, {diff.days} days"

def update_svg():
    repos, followers = get_github_stats()
    age = calculate_age()

    with open('stats.svg', 'r', encoding='utf-8') as f:
        svg_content = f.read()

    # جایگزینی متغیرها در فایل SVG
    svg_content = svg_content.replace('__AGE__', age)
    svg_content = svg_content.replace('__REPOS__', str(repos))
    svg_content = svg_content.replace('__FOLLOWERS__', str(followers))

    with open('stats.svg', 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print("SVG updated successfully!")

if __name__ == '__main__':
    update_svg()
