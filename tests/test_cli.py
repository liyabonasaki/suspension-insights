import pytest
from click.testing import CliRunner
from suspension_insights.cli import main


@pytest.fixture
def runner():
    return CliRunner()


def test_cli_execution(mocker, runner, tmp_path):
    input_file = tmp_path / "input.csv"
    output_folder = tmp_path / "output"

    # Create an empty CSV file
    input_file.write_text("id,payment_type,payment_amount,created,status,agent_user_id,device_id\n")

    mocker.patch("suspension_insights.repository.read_payments", return_value=[])
    mocker.patch("suspension_insights.service.generate_reports")

    result = runner.invoke(main, [str(input_file), str(output_folder)])

    assert result.exit_code == 0
