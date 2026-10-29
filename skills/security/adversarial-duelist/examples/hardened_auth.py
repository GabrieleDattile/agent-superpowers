"""
Hardened version of process_transaction that handles adversarial vectors gracefully.
"""
import math

def process_transaction(user_id: str, amount: float):
    # Guard 1: Type check & None check
    if not isinstance(user_id, str) or not user_id.strip():
        raise ValueError("Invalid user_id")
        
    # Guard 2: Numeric boundary validation
    if not isinstance(amount, (int, float)) or math.isnan(amount) or math.isinf(amount):
        raise ValueError("Amount must be a finite number")
        
    if amount <= 0:
        raise ValueError("Amount must be strictly positive")
        
    fee = 100.0 / amount
    return fee > 0
