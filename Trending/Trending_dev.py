import requests
from bs4 import BeautifulSoup
import urllib2
import pandas as pd
from prettytable import PrettyTable
from color_code import color


def getDev(url):
    dev_file = urllib2.urlopen(url)
    dev_html = dev_file.read()
    dev_file.close()

    soup = BeautifulSoup(dev_html, "html.parser")

    name = []

    for h2 in soup.find_all("h2", attrs={"class" : "user-leaderboard-list-name"}):
        for a in h2.find_all("a"):
            name.append(a.contents[0])

    name = map(lambda s: s.strip(), name)
    # print len(name)

    RANK = color.PURPLE + color.BOLD + "RANK" + color.END
    USER = color.YELLOW + color.BOLD + "USER" + color.END

    ex = [RANK, USER]
    t = PrettyTable(ex)
    for i in range(0, len(name)):
        rank = color.PURPLE + color.BOLD + str(i + 1) + color.END
        nm = color.YELLOW + color.BOLD + str(name[i]) + color.END
        t.add_row([rank, nm])

    print t

url = "https://github.com/trending/developers?since=daily"
getDev(url)

