def id_check(prompt: str) -> bool:
    if prompt is None:
        return False
    prompt = ''.join(prompt.split())
    return len(prompt) == 9 and prompt.isnumeric() and validate_israeli_id(prompt)


def validate_israeli_id(id_number):
    # mult every other num and put in arr
    arr = []
    for i in range(len(id_number)):
        n = int(id_number[i])
        if i % 2 == 0:
            arr.append(n)
        else:
            n2 = n * 2
            if n2 > 9:
                n1 = 1 + (n2 % 10)
                arr.append(n1)
            else:
                arr.append(n2)

            # Sum up all the numbers from the previous step
    total = 0
    for k in arr:
        total += k

    if total % 10 == 0:
        return True
    else:
        return False
