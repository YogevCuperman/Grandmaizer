def id_check(prompt: str) -> bool:
    prompt = ''.join(prompt.split())
    return len(prompt) == 9 and prompt.isnumeric()
