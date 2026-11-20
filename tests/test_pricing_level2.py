import pytest

from orderlab.pricing_level2 import final_total


@pytest.mark.parametrize(
    "price, qty, discount, expected",
    [
        (10_000, 2, 0, 23_000),
        (49_999, 1, 0, 52_999),
        (50_000, 1, 0, 50_000),
        (50_001, 1, 0, 50_001),
        (10_000, 2, 10, 21_000),
        (50_000, 1, 10, 48_000),
        (0, 3, 0, 0),
        (10_000, 2, 100, 0),
    ],
)
def test_final_total(price, qty, discount, expected):
    assert final_total(price, qty, discount) == expected


@pytest.mark.parametrize("discount", [-1, 101])
def test_invalid_discount(discount):
    with pytest.raises(ValueError, match="invalid discount"):
        final_total(10_000, 2, discount)
