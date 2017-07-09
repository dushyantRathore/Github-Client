import click
import Trending_repo as tr
import Trending_dev as td
import Github_user as gu
import sys


def cli():
    x = sys.argv

    dic = {}

    # For trending repositories

    type = x[1].lower()

    if type == "--repo":

        dic["type"] = "repo"
        dic["time"] = x[3]
        dic["lang"] = x[5]

        tr.getRepo(dic)

    elif type == "--dev":
        dic["type"] = "dev"
        dic["time"] = x[3]
        dic["lang"] = x[5]

        td.getDev(dic)

    elif type == "--user":
        dic["username"] = x[2]

        gu.getDetails(dic)


    # print dic


if __name__ == '__main__':
    cli()