def greet(name: str) -> str:
    cleaned_name = name.strip()
    if len(cleaned_name) == 0:
        return "Hello World!"
    return f"Hello {name}!"
