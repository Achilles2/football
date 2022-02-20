from json import loads


def round_num(round_str: str):
    s = round_str.lstrip("Regular Season - ")
    return int(s)


def is_allowed_round(round_number):
    if 6 < int(round_number) < 33:
        return True
    return False


def response_from_json(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        as_str = ''.join(lines)
        as_dict = loads(as_str)
        return as_dict['response']
