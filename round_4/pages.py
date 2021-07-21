from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    template_name = "round_4/Instructions.html"

    def vars_for_template(self):
        return {'button_text': 'Next'}

class Decision(Page):
    template_name = "round_4/Decision.html"

    def vars_for_template(self):
        beer_price = Constants.beer_price[self.round_number - 1]
        movie_price = Constants.movie_price[self.round_number - 1]
        broadband_price = Constants.broadband_price[self.round_number - 1]
        ABV = Constants.ABV[self.round_number - 1]
        year_of_release = Constants.year_of_release[self.round_number - 1]
        speed = Constants.speed[self.round_number - 1]
        container = Constants.container[self.round_number - 1]
        genre = Constants.genre[self.round_number - 1]
        contract_length = Constants.contract_length[self.round_number - 1]
        volume = Constants.volume[self.round_number - 1]
        rating = Constants.rating[self.round_number - 1]
        data_cap = Constants.data_cap[self.round_number - 1]
        return {'title': "A bit about you...",
                'beer_price': beer_price,
                'movie_price': movie_price,
                'broadband_price': broadband_price,
                'ABV': ABV,
                'year_of_release': year_of_release,
                'speed': speed,
                'container': container,
                'genre': genre,
                'contract_length': contract_length,
                'volume': volume,
                'rating': rating,
                'data_cap': data_cap,
                'button_text': "Next"}


class Results(Page):
    pass


page_sequence = [
    Instructions,
    Decision
]
