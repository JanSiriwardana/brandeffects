from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def vars_for_template(self):
        return {'button_text': "Go on to next page"}


class Consent(Page):
    form_model = 'player'
    form_fields = ['consent']

    def vars_for_template(self):
        return {'button_text': "Confirm"}


class QuestionPage(Page):
    form_model = 'player'
    template_name = "ledr/SimplePage.html"

    def vars_for_template(self):
        return {'title': "Please answer the following questions"}


class Comprehension(QuestionPage):
    form_fields = ['comprehension_1', 'comprehension_2', 'comprehension_3']


page_sequence = [
    Introduction,
    Consent,
    Comprehension,
]
