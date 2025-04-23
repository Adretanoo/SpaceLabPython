from hello_handler import HelloHandler
from default_handler import DefaultHandler
from help_handler import HelpHandler


hello = HelloHandler()
help = HelpHandler()
default = DefaultHandler()

hello.set_next(help).set_next(default)

print(hello.handle("па"))