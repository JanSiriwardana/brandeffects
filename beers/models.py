import random

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
    num_items = 3
    attributes = {
        'Price': [ "1.00", "2.00", "3.00" ],
        'ABV': [ "2%", "3%", "4%" ],
        'Container': [ "Bottle", "Can" ],
        'Volume': ["330 mL", "500 mL", "1 L" ]
    }


class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            # TODO: This generates draws 'with replacement' from the set
            # of possible products.  Re-write to first create the set
            # of possible products and then draw from those...
            for item_number in range(Constants.num_items):
                item = MenuItem(player=player,
                                product_number=item_number,
                                product_type="beer",
                                product_name=str(item_number))
                item.save()
                for name, values in Constants.attributes.items():
                    attrib = MenuItemAttribute(item=item,
                                               attribute=name,
                                               value=random.choice(values))
                    attrib.save()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


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