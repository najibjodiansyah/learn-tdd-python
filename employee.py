"""
Very advanced Employee management system.
"""

from dataclasses import dataclass

@dataclass
class Employee:
    """Basic representation of an Employee."""

    name: str
    employee_id: int
    pay_rate: float = 100
    hours_worked: float = 0.0
    has_commission: bool = True
    commission: float = 100.0
    contracts_landed: int = 0

    def compute_payout(self) -> float:
        """ Compute how much the employee should be paid. """
        reise NotImplementedError()
