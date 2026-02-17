from typing import List, Dict, Any

def sort_by_date(transactions: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список транзакций по дате ('date').
    """
    return sorted(transactions, key=lambda x: x['date'], reverse=reverse)
