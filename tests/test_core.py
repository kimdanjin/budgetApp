from budget.core import add_transaction


def test_add_transaction_increases_length() -> None:
    transactions = []

    result = add_transaction(
        transactions,
        date="2026-01-15",
        transaction_type="지출",
        category="쇼핑",
        description="온라인쇼핑",
        amount=-45000,
        memo="",
    )

    assert len(result) == 1


def test_add_transaction_stores_negative_amount() -> None:
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

    assert result[0]["amount"] == -12000
    assert result[0]["type"] == "지출"


def test_add_transaction_stores_positive_amount() -> None:
    transactions = []

    result = add_transaction(
        transactions,
        date="2026-01-07",
        transaction_type="수입",
        category="급여",
        description="월급",
        amount=3500000,
        memo="1월급여",
    )

    assert result[0]["amount"] == 3500000
    assert result[0]["type"] == "수입"


def test_add_transaction_allows_empty_description() -> None:
    transactions = []

    result = add_transaction(
        transactions,
        date="2026-01-30",
        transaction_type="지출",
        category="기타",
        description="",
        amount=-1000,
        memo="설명 없음",
    )

    assert result[0]["description"] == ""
