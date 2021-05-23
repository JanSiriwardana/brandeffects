from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Beers_instructions(Page):
    template_name = "beers/Beers_instructions.html"

    def vars_for_template(self):
        return {'title': "Round...",
                'button_text': "Next"}


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Beers_instructions, ResultsWaitPage, Results]
