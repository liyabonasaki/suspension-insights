from collections import defaultdict
from .calculator import calculate_days_from_suspension
from .models import Payment
from datetime import datetime
import pandas as pd


def generate_reports(payments: list[Payment], output_folder: str, reference_date: datetime):
    import os
    os.makedirs(output_folder, exist_ok=True)

    days_from_suspension = calculate_days_from_suspension(payments, reference_date)
    df_suspension = pd.DataFrame(days_from_suspension.items(), columns=['device_id', 'days_from_suspension'])
    df_suspension.sort_values(by='days_from_suspension', ascending=False).to_csv(
        f"{output_folder}/days_from_suspension_report.csv", index=False)

    agent_collections = defaultdict(lambda: defaultdict(lambda: defaultdict(float)))
    payment_totals = defaultdict(float)

    for payment in payments:
        date_str = payment.created.date().isoformat()
        agent_collections[payment.agent_user_id][date_str][payment.payment_type] += payment.payment_amount
        payment_totals[payment.payment_type] += payment.payment_amount

    agent_rows = []
    for agent, dates in agent_collections.items():
        for date, payments in dates.items():
            for payment_type, amount in payments.items():
                agent_rows.append([agent, date, payment_type, amount])

    df_agent = pd.DataFrame(agent_rows, columns=['agent_user_id', 'date', 'payment_type', 'total_amount'])
    df_agent.sort_values(by=['agent_user_id', 'date']).to_csv(f"{output_folder}/agent_collection_report.csv",
                                                              index=False)

    df_payment_type = pd.DataFrame(payment_totals.items(), columns=['payment_type', 'total_amount'])
    df_payment_type.sort_values(by='payment_type').to_csv(f"{output_folder}/payment_type_report.csv", index=False)