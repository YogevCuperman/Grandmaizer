def id_check(prompt: list):
    prompt = prompt.split()
    digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    id = ''
    if len(prompt) != 9:
        return -1
    for number in prompt:
        if number in digits:
            id += str(digits.index(number))
        else:
            return -1
    return id
