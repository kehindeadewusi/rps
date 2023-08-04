def state_num(state: str):
    if not state:
        return -1

    state = state.lower()

    if state == "oyo":
        return 0
    elif state == "lagos":
        return 1
    elif state == "aba":
        return 2
    elif state == "kano":
        return 3

    return 100
