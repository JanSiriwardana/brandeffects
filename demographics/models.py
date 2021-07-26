from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
)


author = 'LEDR team'

doc = """
Standard LEDR demographics inventory
"""


class Constants(BaseConstants):
    name_in_url = 'aboutyou'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gender = models.IntegerField(
        label="What gender do you identify as?",
        choices=[
            [1, "Male"],
            [2, "Female"],
            [3, "Other"],
            [4, "Prefer not to say"]
        ],
        widget=widgets.RadioSelect,
        blank=False,
    )

    age = models.IntegerField(
        label="How old are you?",
        blank=False,
    )

    countryborn = models.StringField(
        label="Which country (or countries) were you a citizen of when you were born?",
        blank=True,
    )

    countrynow = models.StringField(
        label="In which country is your current permanent residence? "
              "(If you are in the UK on a student visa, this is where 'home' is.)",
        blank=True,
    )

    department = models.StringField(
        label="In which School are you currently enrolled? (For example, BIO, ECO, EDU, ...)",
        blank=True,
    )

    degree = models.IntegerField(
        label="What type of degree course are you currently enrolled on?",
        choices=[
            [1, 'INTO'],
            [2, 'Bachelor'],
            [3, 'PG Diploma'],
            [4, 'Master'],
            [5, 'PhD'],
            [6, 'I am a member of staff'],
            [7, 'Other degree course or affiliation'],
            [8, 'Prefer not to say']
        ],
        widget=widgets.RadioSelect,
        blank=True,
    )

    timeuea = models.IntegerField(
        label="How long have you been at UEA?",
        choices=[
            [1, "This is my first year"],
            [2, "This is my second year"],
            [3, "This is my third year"],
            [4, "This is my fourth year"],
            [5, "I have been here more than four years"],
            [6, "Prefer not to say"]
            ],
        widget=widgets.RadioSelect,
        blank=True,
    )

    state = models.IntegerField(
        label="In which state do you currently reside?",
        choices=["Alabama",
                 "Alaska",
                 "Arizona",
                 "Arkansas",
                 "California",
                 "Colorado",
                 "Connecticut",
                 "Delaware",
                 "District of Columbia",
                 "Florida",
                 "Georgia",
                 "Hawaii",
                 "Idaho",
                 "Illinois",
                 "Indiana",
                 "Iowa",
                 "Kansas",
                 "Kentucky",
                 "Louisiana",
                 "Maine",
                 "Maryland",
                 "Massachusetts",
                 "Michigan",
                 "Minnesota",
                 "Mississippi",
                 "Missouri",
                 "Montana",
                 "Nebraska",
                 "Nevada",
                 "New Hampshire",
                 "New Jersey",
                 "New Mexico",
                 "New York",
                 "North Carolina",
                 "North Dakota",
                 "Ohio",
                 "Oklahoma",
                 "Oregon",
                 "Pennsylvania",
                 "Rhode Island",
                 "South Carolina",
                 "South Dakota",
                 "Tennessee",
                 "Texas",
                 "Utah",
                 "Vermont",
                 "Virginia",
                 "Washington",
                 "West Virginia",
                 "Wisconsin",
                 "Wyoming"
                ],
        blank=False,
    )
