from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def vars_for_template(self):
        return {'button_text': "Go on to next page"}


class Comprehension(Page):
    pass


page_sequence = [
    Introduction,
    Comprehension,
]
