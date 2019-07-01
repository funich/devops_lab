import argparse
import requests
import calendar
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--version', action='version', version='version 1.0',
                    help='Prints the version of program')
parser.add_argument("-o", "--owner", help="Owner of repository",
                    default='alenaPy')
parser.add_argument("-r", "--repo", help="Name of repository",
                    default='devops_lab')
parser.add_argument('-a', '--all', help='Show all parameters', action='store_true')
parser.add_argument('-cm', '--commit', action='store_true', default='commits',
                    help='Show the number of commits, date and names for repository')
parser.add_argument('-br', '--branches', action='store_true', default='branches',
                    help='Show number of branches, names and protections')
parser.add_argument("-pu", "--pull", action='store_true', default='pulls',
                    help="Show number of pull requests and create date")
parser.add_argument("-pc", "--pullclose", action='store_true',
                    help="Show pull requests is closed")
parser.add_argument("-wd", "--weekday", action='store_true',
                    help="Day of week pull request created")
parser.add_argument("-un", "--uname", type=str, required=True,
                    help="User name for authorization github")
parser.add_argument("-ut", "--utoken", type=str, required=True,
                    help="User token for authorization github")

args = parser.parse_args()
urlowner = args.owner
urlrepo = args.repo
urloptions = args.pull
username = args.uname
token = args.utoken
url = ''


def urlin(urlowner, urlrepo, urloptions):
    global url
    url = "https://api.github.com/repos/%s/%s/%s" % (urlowner, urlrepo, urloptions)


if args.commit or args.all:
    urloptions = 'commits'
    urlin(urlowner, urlrepo, urloptions)
    r = requests.get(url, auth=(username, token))
    lenstr = len(r.json())
    print("\nYou have %d commits:" % lenstr)
    for i in range(lenstr):
        idate = r.json()[i]['commit']['author']['date']
        imessage = r.json()[i]['commit']['message']
        print(idate + " - " + imessage)

if args.branches or args.all:
    urloptions = 'branches'
    urlin(urlowner, urlrepo, urloptions)
    r = requests.get(url, auth=(username, token))
    lenstr = len(r.json())
    print("\nYou have %d branches:" % lenstr)
    for i in range(lenstr):
        iname = r.json()[i]['name']
        iprotected = str(r.json()[i]['protected'])
        print(iname + " - Protected: " + iprotected)

if args.pull or args.all:
    urloptions = 'pulls?page=1&per_page=100&state=all'
    urlin(urlowner, urlrepo, urloptions)
    r = requests.get(url, auth=(username, token))
    lenstr = len(r.json())
    print("\nYou have last %d pulls:" % lenstr)
    for i in range(lenstr):
        ititle = r.json()[i]['title']
        icreatedat = r.json()[i]['created_at']
        print(icreatedat + " - " + ititle, end='')

        if args.pullclose or args.all:
            iclosedate = r.json()[i]['closed_at']
            print(" - Pull closed: " + str(iclosedate), end='')

        if args.weekday or args.all:
            iweekday = datetime.strptime(icreatedat, "%Y-%m-%dT%H:%M:%SZ")
            print(" - Created day of week:", calendar.day_name[datetime.weekday(iweekday)], end='')
        print()
