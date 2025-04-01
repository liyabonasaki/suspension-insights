from datetime import datetime, timedelta
from suspension_insights.calculator import calculate_days_from_suspension
from suspension_insights.models import Payment

def test_calculate_days_from_suspension():
    reference_date = datetime(2025, 3, 31)
    payments = [
        Payment(1, "CASH", 100, reference_date - timedelta(days=50), "SUCCESSFUL", 1, 101),
        Payment(2, "CARD", 200, reference_date - timedelta(days=10), "SUCCESSFUL", 2, 102)
    ]
    result = calculate_days_from_suspension(payments, reference_date)
    assert result[101] == 40
    assert result[102] == 80
