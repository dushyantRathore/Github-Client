import requests
from bs4 import BeautifulSoup
import urllib2
import pandas as pd
from prettytable import PrettyTable

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def getRepo(url):
    repo_file = urllib2.urlopen(url)
    repo_html = repo_file.read()
    repo_file.close()

    soup = BeautifulSoup(repo_html, "html.parser")

    name = []
    desc = []

    for div in soup.find_all("div", attrs={"class" : "d-inline-block col-9 mb-1"}):
        # x = color.YELLOW + color.BOLD + str(div.text) + color.END
        name.append(div.text)

    for div in soup.find_all("div", attrs={"class" : "py-1"}):
        desc.append(div.text)

    name = map(lambda s: s.strip(), name)
    desc = map(lambda s: s.strip(), desc)

    # print name
    # print desc

    RANK = color.PURPLE + color.BOLD + "RANK" + color.END
    USER_REPO = color.YELLOW + color.BOLD + "USER/REPO" + color.END

    ex = [RANK, USER_REPO]
    t = PrettyTable(ex)
    for i in range(0,len(name)):
        rank = color.PURPLE + color.BOLD + str(i+1) + color.END
        t.add_row([rank, name[i]])

    print t


url = "https://github.com/trending?since=daily"
getRepo(url)