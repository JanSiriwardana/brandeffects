from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, MenuItem


class Instructions(Page):
    template_name = "choices/Instructions.html"

    def vars_for_template(self):
        type = [list(MenuItem.objects.filter(player=self.player))[0]]
        return {'title': "Round...",
                'type': type,
                'button_text': "Next"}

    def is_displayed(self):
        return (self.round_number - 1) % Constants.num_rounds_per_product == 0


class Decision(Page):
    def vars_for_template(self):
        items = list(MenuItem.objects.filter(player=self.player))
        return {
            'items': items,
            'attributes': {
                attrib_name: [item.get_attribute(attrib_name).value for item in items]
                for attrib_name in Constants.attributes[items[0].product_type]
            }
        }


class Results(Page):
    pass


page_sequence = [
    Instructions,
    Decision
]
