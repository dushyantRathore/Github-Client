import requests
from bs4 import BeautifulSoup
import urllib2
import pandas as pd
from prettytable import PrettyTable
from color_code import color


def getRepo(dic):

    if dic["lang"] != "all" :
        url = "https://github.com/trending/" + str(dic["lang"]) + "?since=" + str(dic["time"])
    else:
        url = "https://github.com/trending?since=" + str(dic["time"])

    # print url

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
        nm = color.YELLOW + color.BOLD + str(name[i]) + color.END
        t.add_row([rank, nm])

    print t


