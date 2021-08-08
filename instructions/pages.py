from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Prolific(Page):
    template_name = "ledr/SimplePage.html"
    form_model = 'player'
    form_fields = ['prolific_id']

    def vars_for_template(self):
        return {'button_text': "Confirm"}


class PilotIntro(Page):
    def vars_for_template(self):
        return{'button_text': "Begin survey"}


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
    Prolific,
    #PilotIntro,
    Introduction,
    Consent,
    Comprehension,
]
