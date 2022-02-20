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
        as_dict = loads(f.read())
        return as_dict['response']
