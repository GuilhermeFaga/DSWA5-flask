from enum import Enum, unique


class Templates:
    @unique
    class Base(Enum):
        BASE = "base.html.jinja"

    @unique
    class App(Enum):
        INDEX = "index.html.jinja"
        USER = "user.html.jinja"
        CONTEXTO = "contexto.html.jinja"
        FORM = "form.html.jinja"

    @unique
    class Errors(Enum):
        NOT_FOUND = "404.html.jinja"
        SERVER_ERROR = "500.html.jinja"
