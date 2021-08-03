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
    prolific_id = models.StringField(
        label="Please enter your Prolific ID",
        blank=False,
    )

    consent = models.IntegerField(
        label="Please select your choice below",
        choices=[
            [1, "Agree"],
            [2, "Disagree"],
            ],
        widget=widgets.RadioSelect,
        blank=False,
    )

    comprehension_1 = models.IntegerField(
        label="How many choice sets will you face in round 2?",
        choices=[
            [1, "3"],
            [2, "8"],
            [3, "10"],
        ],
        widget=widgets.RadioSelect,
        blank=False
    )

    comprehension_2 = models.IntegerField(
        label="How many rounds in total are there?",
        choices=[
            [1, "3"],
            [2, "4"],
            [3, "5"],
        ],
        widget=widgets.RadioSelect,
        blank=False
    )

    comprehension_3 = models.IntegerField(
        label="Which of these is NOT a product type you will see?",
        choices=[
            [1, "Beer"],
            [2, "Shampoo"],
            [3, "Broadband service providers"],
        ],
        widget=widgets.RadioSelect,
        blank=False
    )


def custom_export(players):
    yield['session', 'participant_code', 'prolific_id', 'consent', 'comp_1', 'comp_2', 'comp_3']
    for p in players:
        yield (
            p.session.code, p.participant.code, p.prolific_id, p.consent, p.comprehension_1, p.comprehension_2,
            p.comprehension_3 
        )


