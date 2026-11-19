"""JuiceBar order price. The specification (S1-S5) is in the worksheet, step A0.
Do not read the tests to learn the rules. Read the specification.
"""

SMALL = 40
LARGE = 60
BULK_OFF = 50
MEMBER_OFF = 15


def bottle_price(size):
    """Price in TL of one bottle of the given size."""
    if size == "S":
        return SMALL
    if size == "L":
        return LARGE
    raise ValueError("unknown size")


def order_price(qty, size, member=False, coupon=False):
    """Price in TL of an order of `qty` bottles of one size."""
    if qty < 1 or qty > 20:
        raise ValueError("quantity must be 1 to 20")
    price = qty * bottle_price(size)
    if qty >= 10:
        price = price - BULK_OFF
    if coupon:
        price = price * 90 // 100
    if member:
        price = price - MEMBER_OFF
    return price
