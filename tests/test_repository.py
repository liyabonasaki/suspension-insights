import pytest
import pandas as pd
from io import StringIO
from datetime import datetime
from suspension_insights.repository import read_payments
from suspension_insights.models import Payment


@pytest.fixture
def sample_csv():
    return StringIO("""id,payment_type,payment_amount,created,status,agent_user_id,device_id
1,CASH,100,2025-03-01 12:00:00,SUCCESSFUL,1,101
2,CARD,200,2025-03-15 12:00:00,SUCCESSFUL,2,102
""")


def test_read_payments(mocker, sample_csv):
    mocker.patch("pandas.read_csv", return_value=pd.read_csv(sample_csv, parse_dates=["created"]))

    payments = read_payments("fake_path.csv")  # Path is mocked
    assert len(payments) == 2
    assert isinstance(payments[0], Payment)
    assert payments[0].device_id == 101
    assert payments[1].payment_amount == 200
