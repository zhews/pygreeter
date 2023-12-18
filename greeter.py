from opentelemetry import trace
from random import randrange
from time import sleep
from prometheus_client import Counter

generic_counter = Counter(
    "pygreeter_greetings_generic_total", "Greetings without a name specified."
)
specific_counter = Counter(
    "pygreeter_greetings_specific_total", "Greetings with a name specified."
)

tracer = trace.get_tracer("pygreeter.greeter")


def greet(name: str) -> str:
    cleaned_name = name.strip()
    if len(cleaned_name) == 0:
        generic_counter.inc()
        return "Hello World!"

    with tracer.start_as_current_span("validate-name"):
        validate_name(cleaned_name)

    specific_counter.inc()
    return f"Hello {name}!"


def validate_name(_: str) -> None:
    seconds = randrange(0, 4)
    sleep(seconds)
