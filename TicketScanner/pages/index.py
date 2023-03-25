import pynecone as pc
from pcconfig import config

from TicketScanner.core.state import State
from TicketScanner.util.gapi import gs


class IndexState(State):
    code: str = ""
    result: str = ""

    def re_focus(self):
        pass

    def on_key_down(self, key):
        if key == "Enter" and self.code != '':
            self.result = gs.process_code(self.code)
            self.code = ''


def navbar() -> pc.Component:
    return pc.box(
        pc.hstack(
            pc.image(src="favicon.ico"),
            pc.heading(config.app_name),
        ),
        bg="rgba(255,255,255, 0.9)",
        backdrop_filter="blur(10px)",
        padding_y=["0.8em", "0.8em", "0.5em"],
        border_bottom="0.05em solid rgba(100, 116, 139, .2)",
        position="sticky",
        width="100%",
        top="0px",
        z_index="99",
    )


def content() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading("Happy Ugadi", font_size="3em"),
            # pc.html("<input onblur='this.focus()' autofocus />"),
            pc.input(
                width="300px",
                font_size="1em",
                on_change=IndexState.set_code,
                on_key_down=IndexState.on_key_down,
            ),
            pc.text(IndexState.result, font_size="1em"),
            spacing=".5em",
            # font_size="1em",
        ),
        padding_top="10%",
    )


def index() -> pc.Component:
    return pc.box(
        navbar(),
        content()
    )
