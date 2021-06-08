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
    num_attribs = 3


class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            for item_number in range(Constants.num_items):
                item = MenuItem(player=player,
                                product_number=item_number,
                                product_type="beer",
                                product_name=str(item_number))
                item.save()
                for attrib_number in range(Constants.num_attribs):
                    attrib = MenuItemAttribute(item=item,
                                               attribute=str(attrib_number),
                                               value=str(random.random()))
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


class MenuItemAttribute(ExtraModel):
    item = models.Link(MenuItem)
    attribute = models.StringField()
    value = models.StringField()