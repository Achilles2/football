from json import loads
from pandas import DataFrame

FILE_NAME = 'league39_season2021.json'

with open(FILE_NAME) as f:
    lines = f.readlines()
    as_str = ''.join(lines)
    as_dict = loads(as_str)

response = as_dict['response']

all_games = []

visited_teams = []

for g in response:
    _host = g["teams"]["home"]['name']
    _hosted = g["teams"]["away"]['name']
    goals_host = g["goals"]["home"]
    goals_hosted = g["goals"]["away"]
    all_games.append([_host, _hosted, goals_host, goals_hosted])

    if _host not in visited_teams:
        visited_teams.append(_host)

TOTAL_TEAMS = len(visited_teams)
visited_teams.sort()

GF_as_host_list = [0] * TOTAL_TEAMS
GF_as_away_list = [0] * TOTAL_TEAMS
GA_as_host_list = [0] * TOTAL_TEAMS
GA_as_away_list = [0] * TOTAL_TEAMS
GF_tot_list = [0] * TOTAL_TEAMS
GA_tot_list = [0] * TOTAL_TEAMS


def host(game):
    return game["teams"]["home"]['name']


def guest(game):
    return game["teams"]["away"]["name"]


def host_goals(game):
    return game["goals"]["home"]


def guest_goals(game):
    return game["goals"]["away"]


def is_host(team, game):
    return team == host(game)


def is_guest(team, game):
    return team == guest(game)


def GF_as_host(game, team):
    if is_host(team, game):
        goals = host_goals(game)
        if goals:
            return goals
    return 0


def GF_as_away(game, team):
    if is_guest(team, game):
        goals = guest_goals(game)
        if goals:
            return goals
    return 0


def GA_as_host(game, team):
    if is_host(team, game):
        goals = guest_goals(game)
        if goals:
            return goals
    return 0


def GA_as_away(game, team):
    if is_guest(team, game):
        goals = host_goals(game)
        if goals:
            return goals
    return 0


def GF_tot(game, team):
    host = is_host(team, game)
    if host:
        goals1 = host_goals(game)
        if goals1:
            return goals1
    elif is_guest(team, game):
        goals = guest_goals(game)
        if goals:
            return goals
    return 0


def GA_tot(game, team):
    host = is_host(team, game)
    if host:
        goals = guest_goals(game)
        if goals:
            return goals
    elif is_guest(team, game):
        goals1 = host_goals(game)
        if goals1:
            return goals1
    return 0


def create_results():
    for index, team in enumerate(visited_teams):
        for game in response:
            GF_as_host_list[index] += GF_as_host(team=team, game=game)
            GF_as_away_list[index] += GF_as_away(team=team, game=game)
            GA_as_host_list[index] += GA_as_host(team=team, game=game)
            GA_as_away_list[index] += GA_as_away(team=team, game=game)
            GF_tot_list[index] += GF_tot(team=team, game=game)
            GA_tot_list[index] += GA_tot(team=team, game=game)


def print_results():
    print(GF_as_host_list)
    print(GF_as_away_list)
    print(GA_as_host_list)
    print(GA_as_away_list)
    print(GF_tot_list)
    print(GA_tot_list)


create_results()
print_results()

data = {"team": visited_teams,
        "GF_as_host": GF_as_host_list,
        "GF_as_hosted": GF_as_away_list,
        "GA_as_host": GA_as_host_list,
        "GA_as_hosted": GA_as_away_list,
        "GF_total": GF_tot_list,
        "GA_total": GA_tot_list}

df = DataFrame(data)

print(df)
