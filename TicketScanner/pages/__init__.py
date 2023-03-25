from pcconfig import config

from TicketScanner.core import Route
from TicketScanner.pages.index import index

routes = [
    Route(path='/', title=config.app_name, component=index)
]
