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
    name_in_url = 'Practice'
    players_per_group = None

    beers = [{'Brand': 'Bud Light', 'ABV': '4.2%', 'Container': 'Can', 'Volume/unit': '16-oz'},
             {'Brand': 'Coors Light', 'ABV': '4.2%', 'Container': 'Can', 'Volume/unit': '12-oz'},
             {'Brand': 'Miller Lite', 'ABV': '4.2%', 'Container': 'Bottle', 'Volume/unit': '12-oz'},
             {'Brand': 'Budweiser', 'ABV': '5.0%', 'Container': 'Can', 'Volume/unit': '12-oz'},
             {'Brand': 'Michelob Ultra', 'ABV': '4.2%', 'Container': 'Bottle', 'Volume/unit': '16-oz'},
             {'Brand': 'Corona Extra', 'ABV': '4.5%', 'Container': 'Bottle', 'Volume/unit': '12-oz'},
             {'Brand': 'Modelo Especial', 'ABV': '4.5%', 'Container': 'Bottle', 'Volume/unit': '12-oz'},
             {'Brand': 'Natural Light', 'ABV': '4.2%', 'Container': 'Can', 'Volume/unit': '12-oz'},
             {'Brand': 'Busch Light', 'ABV': '4.5%', 'Container': 'Can', 'Volume/unit': '12-oz'},
             {'Brand': 'Busch', 'ABV': '4.3%', 'Container': 'Can', 'Volume/unit': '12-oz'},
             {'Brand': 'Heineken', 'ABV': '5.0%', 'Container': 'Bottle', 'Volume/unit': '12-oz'},
             {'Brand': 'Keystone Light', 'ABV': '4.1%', 'Container': 'Bottle', 'Volume/unit': '15-oz'},
             {'Brand': 'Miller High Life', 'ABV': '4.6%', 'Container': 'Bottle', 'Volume/unit': '12-oz'},
             {'Brand': 'Stella Artois', 'ABV': '4.8%', 'Container': 'Bottle', 'Volume/unit': '11.2-oz'},
             {'Brand': 'Pabst Blue Ribbon', 'ABV': '4.7%', 'Container': 'Can', 'Volume/unit': '12-oz'},
             {'Brand': 'Blue Moon', 'ABV': '5.2%', 'Container': 'Bottle', 'Volume/unit': '12-oz'},
             {'Brand': 'Dos Equis', 'ABV': '4.2%', 'Container': 'Bottle', 'Volume/unit': '12-oz'},
             {'Brand': 'Coors Banquet', 'ABV': '5.0%', 'Container': 'Can', 'Volume/unit': '12-oz'}]

    prices = ['$6.49', '$7.99', '$10.99']

    characteristics = ["Brand", "ABV", "Container", "Volume/unit", "Price"]

    options = ['A', 'B', 'C', 'D']

    num_rounds_per_product = 2
    num_rounds = num_rounds_per_product
    num_items = 4


class Subsession(BaseSubsession):
    def creating_session(self):

        products = Constants.beers

        for player in self.get_players():
            # TODO: This generates draws 'with replacement' from the set
            # of possible products.  Re-write to first create the set
            # of possible products and then draw from those...

            menu = random.sample(products, Constants.num_items)
            for item in menu:
                item['Price/6-pack'] = random.choice(Constants.prices)
            for (alt_name, alt) in zip(Constants.options, menu):
                index = menu.index(alt)
                item = MenuItem(player=player,
                                product_number=products.index(alt),
                                product_name=alt_name)
                item.save()

                for (name, value) in alt.items():
                    attrib = MenuItemAttribute(item=item,
                                               attribute=name,
                                               value=value)
                    attrib.save()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    brand = models.StringField()
    required_choice = models.StringField()
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


def custom_export(players):
    yield['session', 'participant_code', 'id_in_group', 'round', 'choice', 'prod_number', 'attribute1',
          'attribute2', 'attribute3', 'attribute4', 'attribute5']
    for p in players:
        items = list(MenuItem.objects.filter(player=p))
        for item in items:
            attributes = list(MenuItemAttribute.objects.filter(item=item))
            yield (
                [p.session.code, p.participant.code, p.id_in_group, p.round_number, p.choice] +
                [item.product_number] + [attrib.value for attrib in attributes] + [p.required_choice]
            )
