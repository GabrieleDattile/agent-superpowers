"""
Minimal Reproducible Example (MRE) created by Ghost-Runner:
Asserts VIP customers get at least 20% discount even on weekends.
"""
from buggy_discount import calculate_discount

def test_vip_weekend_discount():
    price = 100.0
    final_price = calculate_discount(price, is_vip=True, is_weekend=True)
    # VIP discount should yield 80.0, but buggy code returns 95.0
    assert final_price == 80.0, f"Expected 80.0 for VIP on weekend, but got {final_price}"

if __name__ == "__main__":
    test_vip_weekend_discount()
    print("Test passed!")
