from .services import GetIndexes, ParsePrice
# from ..indexesview.celery import app
from celery import shared_task

@shared_task
def refresh_indexes():
    url = 'https://api.coingecko.com/api/v3/indexes?per_page=250'
    get_indexes = GetIndexes()
    get_indexes.get_max_number_page(url)
    get_indexes.parse_index(url, False)
    parse_price = ParsePrice(get_indexes.get_ptice())
    parse_price.parse_price_and_write_to_db()

    return True