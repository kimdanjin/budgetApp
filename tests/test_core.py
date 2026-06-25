from budget.core import add_transaction


def test_add_transaction_increases_length() -> None:
    transactions = []

    result = add_transaction(
        transactions,
        date="2026-01-05",
        transaction_type="지출",
        category="식비",
        description="점심식사",
        amount=-12000,
        memo="",
    )

    assert len(result) == 1
