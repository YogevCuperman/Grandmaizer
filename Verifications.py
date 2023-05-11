## TODO: ALL ##

def id_check(prompt: str) -> int:
    prompt = prompt.split()
    digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    id = ''
    if len(prompt) != 9:
        return None
    for number in prompt:
        if number in digits:
            id += str(digits.index(number))
        else:
            return None
    return id

def age_check(prompt: str) -> int:
    prompt = prompt.split()
    if len(prompt) == 0 or len(prompt) > 2:
        return None

def number_check(words: str) -> int:
    digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen']
    tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninty']

    if len(words) < 1:
        return None
    if len(words) == 1:
        if words in digits:
            return digits.index(words)
        elif words in tens:
            pass
