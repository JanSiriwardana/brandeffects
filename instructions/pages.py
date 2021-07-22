from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def vars_for_template(self):
        return {'button_text': "Next"}


class Consent(Page):
    form_model = 'player'
    form_fields = ['consent']

    def vars_for_template(self):
        return {'button_text': "Confirm"}


class Comprehension(Page):
    form_model = 'player'
    form_fields = ['comprehension_1', 'comprehension_2', 'comprehension_3']



page_sequence = [
    Introduction,
    Consent,
    Comprehension,
]
