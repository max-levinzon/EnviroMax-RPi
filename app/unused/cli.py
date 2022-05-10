import typer

from mock.mock_data import *
from data_handler import data

command = typer.Typer()
sub_commands = typer.Typer()
mock_commands = typer.Typer()
command.add_typer(sub_commands, name="action")
command.add_typer(mock_commands, name="mock")


@sub_commands.command()
def init_db():
    typer.echo(f"Initializing Data !")


@mock_commands.command()
def init_db(name: str = typer.Argument('mock_name')):
    typer.echo(f"Initializing Data !")
    db = data.fireData(name=name)
    db.init_db()
    db2 = data.fireData(name='mock_name_2')
    db2.init_db()


@mock_commands.command()
def add_device(mock_count: int = typer.Argument(100), db_name: str = typer.Argument('mock_name')):
    typer.echo(f"Mocking devices")
    db = data.fireData(name=db_name).get_app(name=db_name)
    device_ref = db.db_instance.child('Devices')
    devices = mock_device(mock_count, device_ref)
    mock_data(devices, mock_count, 2, device_ref)

# @command.command()
# def sell(item: str):
#     typer.echo(f"Selling item: {item}")


if __name__ == "__main__":
    command()
