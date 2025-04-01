from datetime import datetime
from suspension_insights.models import Payment, Client


def test_payment_model():
    payment = Payment(
        id=1,
        payment_type="CASH",
        payment_amount=100.0,
        created=datetime(2025, 3, 1, 12, 0, 0),
        status="SUCCESSFUL",
        agent_user_id=42,
        device_id=101
    )

    assert payment.id == 1
    assert payment.payment_type == "CASH"
    assert payment.payment_amount == 100.0
    assert payment.created == datetime(2025, 3, 1, 12, 0, 0)
    assert payment.status == "SUCCESSFUL"
    assert payment.agent_user_id == 42
    assert payment.device_id == 101


def test_client_model():
    payment1 = Payment(1, "CASH", 100.0, datetime(2025, 3, 1), "SUCCESSFUL", 42, 101)
    payment2 = Payment(2, "CARD", 200.0, datetime(2025, 3, 15), "SUCCESSFUL", 42, 101)

    client = Client(device_id=101, payments=[payment1, payment2])

    assert client.device_id == 101
    assert len(client.payments) == 2
    assert client.payments[0].payment_type == "CASH"
    assert client.payments[1].payment_type == "CARD"
