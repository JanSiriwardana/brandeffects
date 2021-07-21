from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'round_4'
    players_per_group = None
    num_rounds = 3

    beer_price = [1, 2, 3]
    movie_price = [4, 5, 6]
    broadband_price = [7, 8, 9]

    ABV = ['A', 'B', 'C']
    year_of_release = ['D', 'E', 'F']
    speed = ['G', 'H', 'I']
    container = ['J', 'K', 'L']
    genre = ['M', 'N', 'O']
    contract_length = ['P', 'Q', 'R']
    volume = ['S', 'T', 'U']
    rating = ['V', 'W', 'X']
    data_cap = ['Y', 'Z', '1']

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    choice = models.IntegerField()
