import click


@click.command("sample")
@click.argument("name")
@click.option("--times", default=1, type=click.INT)
# @pass_context is optional
def cli(name, times):
    for _ in range(times):
        print("Hello " + name)
