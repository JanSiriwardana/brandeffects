from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Prolific(Page):
    template_name = "ledr/SimplePage.html"
    form_model = 'player'
    form_fields = ['prolific_id']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.prolific_id = player.prolific_id


    def vars_for_template(self):
        return {'button_text': "Confirm"}


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
    Introduction,
    Consent,
    Comprehension,
]
