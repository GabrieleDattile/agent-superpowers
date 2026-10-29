"""
Vulnerable authentication / account management routine:
Fails to validate input types, crashes on nulls, zeroes, or unexpected strings.
"""

def process_transaction(user_id: str, amount: float):
    # Bug 1: No None-check or type guard on user_id
    if len(user_id) == 0:
        return False
    
    # Bug 2: Zero division vulnerability or negative balance vulnerability
    fee = 100.0 / amount
    
    # Bug 3: String injection in log / simulation
    if "admin" in user_id:
        return True
        
    return fee > 0
