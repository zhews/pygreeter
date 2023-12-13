from prometheus_client import Counter

generic_counter = Counter(
    "pygreeter_greetings_generic_total", "Greetings without a name specified."
)
specific_counter = Counter(
    "pygreeter_greetings_specific_total", "Greetings with a name specified."
)


def greet(name: str) -> str:
    cleaned_name = name.strip()
    if len(cleaned_name) == 0:
        generic_counter.inc()
        return "Hello World!"
    specific_counter.inc()
    return f"Hello {name}!"
