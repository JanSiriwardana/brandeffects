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
MUI test instructions, consent and comprehension questions
"""


class Constants(BaseConstants):
    name_in_url = 'instructions'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.IntegerField(
        label="Please select your choice below",
        choices=[
            [1, "Agree"],
            [2, "Disagree"],
            ],
        widget=widgets.RadioSelect,
        blank=False,
    )
