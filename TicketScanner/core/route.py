"""Manage routing for the application."""

import inspect
from typing import Callable

import pynecone as pc
from pynecone.base import Base


class Route(Base):
    """A page route."""

    path: str
    title: str | None = None
    component: pc.Component | Callable[[], pc.Component]


def get_path(component_fn: Callable):
    module = inspect.getmodule(component_fn)

    # Create a path based on the module name.
    return module.__name__.replace(".", "/").replace("_", "-").split("TicketScanner/pages")[1]