"""Core budget transaction functions."""

from typing import Any


Transaction = dict[str, Any]


def add_transaction(
    transactions: list[Transaction],
    date: str,
    transaction_type: str,
    category: str,
    description: str,
    amount: int,
    memo: str,
) -> list[Transaction]:
    """Return transactions with one new budget transaction appended."""
    transaction: Transaction = {
        "date": date,
        "type": transaction_type,
        "category": category,
        "description": description,
        "amount": amount,
        "memo": memo,
    }

    return [*transactions, transaction]
