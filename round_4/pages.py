from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Decision(Page):
    template_name = "round_4/Decision.html"

    def vars_for_template(self):
        return {'title': "A bit about you...",
                'button_text': "Next"}

class Results(Page):
    pass


page_sequence = [
    Decision
]
