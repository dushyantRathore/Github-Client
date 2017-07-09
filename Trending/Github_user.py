import requests
from bs4 import BeautifulSoup
import urllib2
import pandas as pd
import numpy as np
from prettytable import PrettyTable
from color_code import color

# Stats Type List
Username = color.GREEN + color.BOLD + "Username" + color.END
Repositories = color.GREEN + color.BOLD + "Repositories" + color.END
Stars = color.GREEN + color.BOLD + "Stars" + color.END
Followers = color.GREEN + color.BOLD + "Followers" + color.END
Following = color.GREEN + color.BOLD + "Following" + color.END

sequence = [Username, Repositories, Stars, Followers, Following]


def getDetails(dic):

    url = "https://github.com/" + str(dic["username"])

    # print url

    user_file = urllib2.urlopen(url)
    user_html = user_file.read()
    user_file.close()

    soup = BeautifulSoup(user_html, 'html.parser')

    # Find all occurrences of the needed span class
    data = soup.find_all('span', attrs={'class': 'Counter'})

    l=[]
    l.append(str(dic["username"]))

    for i in data:
        l.append(i.text)


    # Strip useless text from list elements
    l = map(lambda s: s.strip(), l)

    t = PrettyTable(sequence)
    t.add_row([l[0], l[1], l[2], l[3], l[4]])

    print t

