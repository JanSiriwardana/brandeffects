from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, MenuItem


class Beers_instructions(Page):
    template_name = "beers/Beers_instructions.html"

    def vars_for_template(self):
        return {'title': "Round...",
                'button_text': "Next"}


class Decision(Page):
    def vars_for_template(self):
        items = list(MenuItem.objects.filter(player=self.player))
        return {
            'items': items,
            'attributes': [
                [item.attributes()[i].value for item in items]
                for i in [0,1,2]
            ]
        }


class Results(Page):
    pass


page_sequence = [
    #Beers_instructions,
    Decision
]
