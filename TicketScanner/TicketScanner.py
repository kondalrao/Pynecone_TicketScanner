"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
import pynecone as pc

from TicketScanner.pages import routes
from TicketScanner.core.state import State


# Add state and page to the app.
app = pc.App(state=State)

# Add the pages to the app.
for route in routes:
    app.add_page(
        route.component,
        route.path,
        route.title
    )

app.compile()
