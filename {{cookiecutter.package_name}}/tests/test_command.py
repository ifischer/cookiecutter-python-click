from click.testing import CliRunner

from {{ cookiecutter.module_name }}.commands import cli


def test_hello_world():
    runner = CliRunner()
    result = runner.invoke(cli)
    assert result.exit_code == 0
