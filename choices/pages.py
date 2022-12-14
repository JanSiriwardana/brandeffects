from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, MenuItem
import math


class Instructions(Page):
    template_name = "choices/Instructions.html"

    def vars_for_template(self):
        round_number = int(math.ceil(self.round_number / Constants.num_rounds_per_product))
        type = [list(MenuItem.objects.filter(player=self.player))[0]]
        return {'title': "Round...",
                'round_number': round_number,
                'type': type,
                'button_text': "Next"}

    def is_displayed(self):
        return (self.round_number - 1) % Constants.num_rounds_per_product == 0


class Decision(Page):
    form_model = 'player'
    form_fields = ['choice']

    def vars_for_template(self):
        choice_set = self.round_number
        type = [list(MenuItem.objects.filter(player=self.player))[0]]
        items = list(MenuItem.objects.filter(player=self.player))
        return {
            'choice_set': choice_set,
            'type': type,
            'items': items,
            'attributes': {
                attrib_name: [item.get_attribute(attrib_name).value for item in items]
                for attrib_name in Constants.beers[0]
            }
        }


class Results(Page):
    pass


page_sequence = [
    Instructions,
    Decision
]
