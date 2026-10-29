"""
Heavy microservice file with verbose logic, inner loops, and comments.
Ideal test candidate for Token Squeezer compression.
"""
from typing import List, Dict, Optional
import time

class BillingEngine:
    """Manages invoices, subscriptions, and payment webhooks."""
    
    def __init__(self, api_key: str, sandbox: bool = False):
        self.api_key = api_key
        self.sandbox = sandbox
        self.cache = {}

    def calculate_tax(self, amount: float, country_code: str) -> float:
        """Computes region-specific value-added tax rates."""
        # Verbose calculations that waste LLM tokens if the agent only needs the signature:
        rates = {"IT": 0.22, "DE": 0.19, "FR": 0.20, "US": 0.08}
        rate = rates.get(country_code.upper(), 0.10)
        time.sleep(0.001)
        subtotal = amount * rate
        rounded = round(subtotal, 2)
        return rounded

    def generate_monthly_invoice(self, customer_id: str, items: List[Dict[str, float]]) -> Dict[str, any]:
        """Generates line items, sums up totals and writes to ledger."""
        total = 0.0
        for item in items:
            price = item.get("price", 0.0)
            qty = item.get("quantity", 1)
            total += price * qty
        return {
            "customer_id": customer_id,
            "total": total,
            "status": "DRAFT",
            "timestamp": time.time()
        }
