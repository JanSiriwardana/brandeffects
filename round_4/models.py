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

    beer_price = ["$10.99", "$7.99", "$6.49"]
    movie_price = ["$3.99", "$9.99", "$6.99"]
    broadband_price = ["$30", "$20", "$40"]

    ABV = ['5.5%', '4.6%', '3.6%']
    decade_of_release = ['1990', '2010', '2000']
    speed = ['50 Mb/s', '25 Mb/s', '100 Mb/s']
    container = ['Bottle', 'Can', 'Can']
    genre = ['Drama', 'Drama', 'Comedy']
    contract_length = ['12 months', '24 months', '12 months']
    volume = ['16-oz', '12-oz', '8.4-oz']
    rating = ['4 stars', '9 stars', '6 stars']
    data_cap = ['300GB', '100GB', '1000GB']

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    choice = models.IntegerField()


def custom_export(players):
    yield['session', 'participant_code', 'id_in_group', 'round', 'choice']
    for p in players:
        yield (
            p.session.code, p.participant.code, p.id_in_group, p.round_number, p.choice,
        )