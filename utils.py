from json import loads


def num_of_round(round_str: str) -> int:
    s = round_str.lstrip("Regular Season - ")
    return int(s)


def is_allowed_round(round_number: str) -> bool:
    if 6 < int(round_number) < 33:
        return True
    return False


def dict_from_json(file_name: str) -> dict:
    with open(file_name) as f:
        as_dict = loads(f.read())
        return as_dict


def response_from_json(file_name: str) -> dict:
    d = dict_from_json(file_name=file_name)
    return d['response']
