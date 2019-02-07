from click.testing import CliRunner

from example_module.commands import cli


def test_hello_world():
    runner = CliRunner()
    result = runner.invoke(cli)
    assert result.exit_code == 0
