from orderlab.pricing import subtotal


def final_total(price: int, qty: int, discount: int) -> int:
    if not 0 <= discount <= 100:
        raise ValueError("invalid discount")

    amount = subtotal(price, qty)
    amount -= amount * discount // 100
    shipping = 3_000 if 0 < amount < 50_000 else 0

    return amount + shipping
