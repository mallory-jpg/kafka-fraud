from random import choices, randint
from string import ascii_letters, digits

account_chars: str = digits + ascii_letters
def _random_account_id():
    """Return a random account number string made of 12 characters."""
    return "".join(choices(account_chars, k=12))

def _random_amount():
    """Return a random float between 1.00 and 1000.00."""
    return randint(100, 1000000) / 100

def create_random_transaction():
    """Create a fake, randomised transaction dictionary."""
    return {
        "source": _random_account_id(),
        "target": _random_account_id(),
        "amount": _random_amount(),
        # Keep it simple: it's all dollars
        "currency": "USD",
    }