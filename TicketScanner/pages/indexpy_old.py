import pynecone as pc
from pcconfig import config

from TicketScanner.core.state import State
from TicketScanner.util.gapi.sheets import gs


class IndexState(State):
    cell: str


docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading("Welcome to Pynecone!", font_size="2em"),
            pc.box("Get started by editing ", pc.code(filename, font_size="1em")),
            pc.link(
                "Check out our docs!",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": "rgb(107,99,246)",
                },
            ),
            pc.input(
                on_blur=IndexState.set_cell,
                placeholder="Type here...",
                font_size="2em"
            ),
            spacing="1.5em",
            font_size="2em",
        ),
        padding_top="10%",
    )
