import pandas as pd
from suspension_insights.models import Payment

def read_payments(file_path: str) -> list[Payment]:
    df = pd.read_csv(file_path, parse_dates=['created'])
    payments = [
        Payment(
            id=row['id'],
            payment_type=row['payment_type'],
            payment_amount=row['payment_amount'],
            created=row['created'],
            status=row['status'],
            agent_user_id=row['agent_user_id'],
            device_id=row['device_id']
        )
        for _, row in df.iterrows()
    ]
    return payments