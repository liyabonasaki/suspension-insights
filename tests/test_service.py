import pytest
import os
import pandas as pd
from datetime import datetime, timedelta
from suspension_insights.service import generate_reports
from suspension_insights.models import Payment

@pytest.fixture
def sample_payments():
    reference_date = datetime(2025, 3, 31)
    return [
        Payment(1, "CASH", 100, reference_date - timedelta(days=50), "SUCCESSFUL", 1, 101),
        Payment(2, "CARD", 200, reference_date - timedelta(days=10), "SUCCESSFUL", 2, 102)
    ]

def test_generate_reports(tmp_path, sample_payments):
    output_folder = tmp_path / "output_reports"
    generate_reports(sample_payments, str(output_folder), datetime(2025, 3, 31))

    assert os.path.exists(output_folder / "days_from_suspension_report.csv")
    assert os.path.exists(output_folder / "agent_collection_report.csv")
    assert os.path.exists(output_folder / "payment_type_report.csv")

    df_suspension = pd.read_csv(output_folder / "days_from_suspension_report.csv")
    assert not df_suspension.empty
    assert df_suspension.iloc[0]["days_from_suspension"] == 80  # Most recent payment
