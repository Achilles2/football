def round_num(round_str: str):
    s = round_str.lstrip("Regular Season - ")
    return int(s)

def round_in_range(round_number):
    if 6 < int(round_number) < 33:
        return True
    return False