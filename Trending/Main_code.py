import click
import Trending_repo as tr
import Trending_dev as td
import Github_user as gu

@click.command()
@click.option('--repo', '-r', is_flag=True, help="Lists the trending repositories.")
@click.option('--dev', '-d', is_flag=True, help="Lists the trending developers.")
@click.option('--username', '-user', default="dushyantRathore", help='Lists the details of a user on Github')


def cli(repo,dev,username):
    if repo:
        url = "https://github.com/trending?since=daily"
        tr.getRepo(url)

    elif dev:
        url = "https://github.com/trending/developers?since=daily"
        td.getDev(url)

    elif username:
        gu.getDetails(username)


if __name__ == '__main__':
    cli()