import click

from src.app.config import get_settings
from src.app.context import LocalContext, Context


def build_cli() -> click.Command:
    pass_context = click.make_pass_decorator(LocalContext)

    @click.group()
    @click.pass_context
    @click.option('--env', '-e', 'env_for_dynaconf', default='testing', help='Set environment for Dynaconf')
    def cli(ctx: click.Context, env_for_dynaconf: str):
        settings = get_settings(env_for_dynaconf=env_for_dynaconf)
        ctx.obj = LocalContext(settings=settings)

    @cli.command('single-table-emulator')
    @pass_context
    @click.option('--table-name', 'table_name', help='Sep up table_name_for_emulation', required=True)
    def emulate_single_table(context: Context, table_name: str):
        return context.data_emulator_for_single_table.execute(table=table_name)

    return cli
