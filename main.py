import datetime as dt
from decimal import Decimal
from typing import Dict, List, Optional, Tuple

DATE_FORMAT = '%Y-%m-%d'

def add(items: dict, title: str, amount: Decimal, expiration_date: Optional[str] = None) -> None:
    """Adds a new batch of a product to the inventory."""
    if title not in items:
        items[title] = []
    
    exp_date = None
    if expiration_date:
        exp_date = dt.datetime.strptime(expiration_date, DATE_FORMAT).date()
        
    items[title].append({
        'amount': amount, 
        'expiration_date': exp_date
    })

def add_by_note(items: dict, note: str) -> None:
    """Parses a natural language note and adds the item to the inventory."""
    parts = note.split()
    last_part = parts[-1]
    
    if '-' in last_part:
        expiration_date = last_part
        amount = Decimal(parts[-2])
        title = ' '.join(parts[:-2])
    else:
        expiration_date = None 
        amount = Decimal(last_part)
        title = ' '.join(parts[:-1])

    add(items, title, amount, expiration_date)

def find(items: dict, needle: str) -> List[str]:
    """Finds items in the inventory by a partial string match."""
    needle_lower = needle.lower()
    return [title for title in items if needle_lower in title.lower()]
    
def amount(items: dict, needle: str) -> Decimal:
    """Calculates the total amount of a specific item currently in stock."""
    total_count = Decimal('0')
    needle_lower = needle.lower()
    
    for title, batches in items.items():
        if needle_lower in title.lower():
            for batch in batches:
                total_count += batch['amount']
                
    return total_count

def expire(items: dict, in_advance_days: int = 0) -> List[Tuple[str, Decimal]]:
    """Returns a list of items that are expiring within the given number of days."""
    result = []
    target_date = dt.date.today() + dt.timedelta(days=int(in_advance_days))
    
    for title, batches in items.items():
        expired_amount = Decimal('0')
        
        for batch in batches:
            exp_date = batch['expiration_date']
            if exp_date and exp_date <= target_date:
                expired_amount += batch['amount']
                
        if expired_amount > Decimal('0'):
            result.append((title, expired_amount))
            
    return result

if __name__ == "__main__":
    # Example of usage:
    goods = {}
    add_by_note(goods, 'Eggs 10 2026-10-20')
    add_by_note(goods, 'Milk 2 2026-10-15')
    print("Expiring soon:", expire(goods, 20))