"""
Sample target logic with an edge case bug:
VIP discounts should be 20%, but applying weekend discounts accidentally overrides it to 5%.
"""

def calculate_discount(price: float, is_vip: bool, is_weekend: bool) -> float:
    discount = 0.0
    if is_vip:
        discount = 0.20 # 20%
    if is_weekend:
        # BUG: It replaces discount instead of applying whichever is higher or compounding
        discount = 0.05
    return price * (1.0 - discount)
