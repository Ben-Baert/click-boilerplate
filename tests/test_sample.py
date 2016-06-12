from reponame.commands.cmd_sample import cli as sample
from click.testing import CliRunner


def test_sample():
    runner = CliRunner()
    result = runner.invoke(sample, ['Ben'])
    assert result.exit_code == 0
    assert result.output == "Hello Ben\n"
