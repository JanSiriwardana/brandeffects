import random
import itertools

from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    ExtraModel,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""



class Constants(BaseConstants):
    name_in_url = 'beers'
    players_per_group = None
    num_rounds = 2
    num_items = 4

    Price = ["£3.00", "£5.00", "£7.00"]
    ABV = ["3.2%", "4.0%", "5.5%"]
    Can = ["Can", "Bottle"]
    Vol = ["3.3cl", "4.4cl", "5.0cl"]

    full_fact = list(itertools.product(Price, ABV, Can, Vol))
    full_fact_transpose = list(zip(*full_fact))

    levels = ['Price', 'ABV', 'Container', 'Volume']
    zip_attributes = zip(levels, full_fact_transpose)
    attributes = dict(zip_attributes)

    option = ['A', 'B', 'C', 'D']
    # TODO: from list of brands select one at random without replacement
    # for each round

    brands = ['Amstel', 'Budweiser', 'Carslberg', 'Corona']

class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            # TODO: This generates draws 'with replacement' from the set
            # of possible products.  Re-write to first create the set
            # of possible products and then draw from those...
            menu = random.sample(range(0, len(Constants.full_fact)), Constants.num_items)
            for alt in menu:
                index = menu.index(alt)
                item = MenuItem(player=player,
                                product_number=alt,
                                product_type="beer",
                                product_name=Constants.option[index])
                item.save()

                for name, values in Constants.attributes.items():
                    attrib = MenuItemAttribute(item=item,
                                               attribute=name,
                                               value=values[alt])
                    attrib.save()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    choice = models.IntegerField(label="Your choice")


class MenuItem(ExtraModel):
    player = models.Link(Player)
    product_number = models.IntegerField()
    product_type = models.StringField()
    product_name = models.StringField()

    def attributes(self):
        return list(MenuItemAttribute.objects.filter(item=self))

    def get_attribute(self, attrib_name):
        return MenuItemAttribute.objects.filter(item=self, attribute=attrib_name)[0]


class MenuItemAttribute(ExtraModel):
    item = models.Link(MenuItem)
    attribute = models.StringField()
    value = models.StringField()