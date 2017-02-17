import click
import Trending_repo as tr
import Trending_dev as td
import Github_user as gu

@click.command()
@click.option('--repo', '-r', default="today", help="Lists the trending repositories.")
@click.option('--dev', '-d', is_flag=True, help="Lists the trending developers.")
@click.option('--username', '-user', default="dushyantRathore", help='Lists the details of a user on Github')


def cli(repo,dev,username):

    if repo:
        if repo == "today":
            url = "https://github.com/trending?since=daily"
            tr.getRepo(url)
        elif repo == "week":
            url = "https://github.com/trending?since=weekly"
            tr.getRepo(url)
        elif repo =="month":
            url = "https://github.com/trending?since=monthly"
            tr.getRepo(url)

    elif dev:
        url = "https://github.com/trending/developers?since=daily"
        td.getDev(url)

    elif username:
        gu.getDetails(username)


if __name__ == '__main__':
    cli()