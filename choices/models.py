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
    name_in_url = 'Choices'
    players_per_group = None

    brands = {
        "beers": ["Heineken", "Stella Artois", "Budweiser", "Corona", "Busch", "Coors", "Miller", "Modelo",
                  "Samuel Adams"],
        "movies": ["Netflix", "Prime Video", "Disney+", "Hulu", "HBOMax", "AppleTV+", "Paramount+", "Youtube Premium",
                   "Peacock"],
        "broadband": ["Frontier", "Verizon", "Altice", "Mediacom", "CharterSpectrum", "CenturyLink", "AT&T", "Cox",
                      "Xfinity"]
    }
    attributes = {
        "beers": {
            "Price/6 pack": ["$6.49", "$7.99", "$10.99"],
            "ABV": ["3.6%", "4.6%", "5.5%"],
            "Container": ["Can", "Bottle"],
            "Volume per container": ["8.4-oz", "12-oz", "16-oz"]
        },
        "movies": {
            "Price": ["$3.99", "$6.99", "$9.99"],
            "Decade of release": ["1990", "2000", "2010"],
            "Genre": ["Drama", "Comedy"],
            "Rating (out of 10)": ["4", "6", "9"]
        },
        "broadband": {
            "Price/month": ["$20", "$30", "$40"],
            "Speed": ["25 Mb/s", "50 MB/s", "100 MB/s"],
            "Contract length": ["12 months", "24 months"],
            "Data cap": ["100GB", "300GB", "1000GB"]
        }
    }

    options = ['A', 'B', 'C', 'D']

    num_rounds_per_product = 9
    num_products = len(attributes.keys())
    num_rounds = num_products * num_rounds_per_product
    num_items = 4


class Subsession(BaseSubsession):
    def creating_session(self):
        if (self.round_number - 1) % Constants.num_rounds_per_product == 0:
            for product_type in Constants.brands.keys():
                random.shuffle(Constants.brands[product_type])
            

        products = {
            product_type: [
                {k: v
                 for k, v in zip(Constants.attributes[product_type].keys(), product)}
                for product in itertools.product(*Constants.attributes[product_type].values())
            ]
            for product_type in Constants.attributes.keys()
        }

        for player in self.get_players():
            # TODO: This generates draws 'with replacement' from the set
            # of possible products.  Re-write to first create the set
            # of possible products and then draw from those...
            product_type = player.get_product_type()
            if player.id_in_group % 3 == 0:
                player.brand = Constants.brands[product_type][(player.id_in_group * player.round_number +
                                                              player.round_number + 1) % Constants.num_rounds_per_product]
            else:
                player.brand = Constants.brands[product_type][(player.id_in_group * player.round_number +
                                                               player.id_in_group) % Constants.num_rounds_per_product]
            if player.round_number == 3:
                player.required_choice = "B"
            elif player.round_number == 15:
                player.required_choice = "A"
            elif player.round_number == 22:
                player.required_choice = "C"
            menu = random.sample(products[product_type], Constants.num_items)
            for (alt_name, alt) in zip(Constants.options, menu):
                index = menu.index(alt)
                item = MenuItem(player=player,
                                product_number=products[product_type].index(alt),
                                product_type=product_type,
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

    def get_product_type(self):
        orderings = list(itertools.permutations(Constants.attributes.keys()))
        ordering = orderings[(self.id_in_group - 1) % len(orderings)]
        return ordering[(self.round_number - 1) // Constants.num_rounds_per_product]


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
    yield['session', 'participant_code', 'id_in_group', 'round', 'choice', 'brand', 'type', 'prod_number', 'attribute1',
          'attribute2', 'attribute3', 'attribute4', 'required choice']
    for p in players:
        items = list(MenuItem.objects.filter(player=p))
        for item in items:
            attributes = list(MenuItemAttribute.objects.filter(item=item))
            yield (
                [p.session.code, p.participant.code, p.id_in_group, p.round_number, p.choice, p.brand] + [item.product_type,
                item.product_number] + [attrib.value for attrib in attributes] + [p.required_choice]
            )
