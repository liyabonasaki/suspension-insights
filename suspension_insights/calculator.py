from datetime import datetime, timedelta
from .models import Payment


def calculate_days_from_suspension(payments: list[Payment], reference_date: datetime) -> dict:
    client_last_payment = {}

    for payment in payments:
        if payment.device_id not in client_last_payment or payment.created > client_last_payment[payment.device_id]:
            client_last_payment[payment.device_id] = payment.created

    days_from_suspension = {}

    for device_id, last_payment in client_last_payment.items():
        days_since_payment = (reference_date - last_payment).days
        remaining_days = max(90 - days_since_payment, 0)
        days_from_suspension[device_id] = remaining_days

    return days_from_suspension