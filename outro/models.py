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


author = 'LEDR Team'

doc = """
Standard welcome pages for LEDR experiments
"""


class Constants(BaseConstants):
    name_in_url = 'outro'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    instructions = models.IntegerField(
        label="Where the instructions clear?",
        choices=[
            [1, "Yes"],
            [2, "No"]
        ],
        widget=widgets.RadioSelect,
    )

    if_no = models.LongStringField(
        label="If you answered 'no' to the previous question, please describe how we could make the instructions more clear",
        blank=True,
    )

    browser = models.StringField(
        label="Which browser are you using?"
    )

    technical = models.IntegerField(
        label="Did you experience any technical issues?",
        choices=[
            [1, "Yes"],
            [2, "No"]
        ],
        widget=widgets.RadioSelect,
    )

    if_yes = models.LongStringField(
        label="If you answered 'yes' to the previous question, please describes the issues you experienced",
        blank=True,
    )

    comments = models.LongStringField(
        label="Finally, if you have any other comments you wish to share with the researchers, please do so here",
        blank=True,
    )


def custom_export(players):
    yield['session', 'participant_code', 'instructions', 'if_no', 'browser', 'technical', 'if_yes', 'comments']
    for p in players:
        yield(
            p.session.code, p.participant.code, p.instructions, p.if_no, p.browser, p.technical, p.if_yes, p.comments
        )