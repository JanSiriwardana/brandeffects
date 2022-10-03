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

    ethnicity = models.IntegerField(
        label="Which of the following best describes you?",
        choices=[
            [1, "Asian or Pacific Islander"],
            [2, "Black or African American"],
            [3, "Hispanic or Latino"],
            [4, "Native American or Alaskan Native"],
            [5, "White or Caucasian"],
            [6, "Multiracial or Biracial"],
            [7, "A race/ethnicity not listed here"]
        ],
        widget=widgets.RadioSelect,
        blank=False,
    )

    income = models.IntegerField(
        label="What is your net monthly income in dollars? Please include any loans, stipends or allowances you receive",
        blank=False,
    )

    state = models.IntegerField(
        label="In which state do you currently reside?",
        choices=[[1, "Alabama"],
                 [2, "Alaska"],
                 [3, "Arizona"],
                 [4, "Arkansas"],
                 [5, "California"],
                 [6, "Colorado"],
                 [7, "Connecticut"],
                 [8, "Delaware"],
                 [9, "District of Columbia"],
                 [10, "Florida"],
                 [11, "Georgia"],
                 [12, "Hawaii"],
                 [13, "Idaho"],
                 [14, "Illinois"],
                 [15, "Indiana"],
                 [16, "Iowa"],
                 [17, "Kansas"],
                 [18, "Kentucky"],
                 [19, "Louisiana"],
                 [20, "Maine"],
                 [21, "Maryland"],
                 [22, "Massachusetts"],
                 [23, "Michigan"],
                 [24, "Minnesota"],
                 [25, "Mississippi"],
                 [26, "Missouri"],
                 [27, "Montana"],
                 [28, "Nebraska"],
                 [29, "Nevada"],
                 [30, "New Hampshire"],
                 [31, "New Jersey"],
                 [32, "New Mexico"],
                 [33, "New York"],
                 [34, "North Carolina"],
                 [35, "North Dakota"],
                 [36, "Ohio"],
                 [37, "Oklahoma"],
                 [38, "Oregon"],
                 [39, "Pennsylvania"],
                 [40, "Rhode Island"],
                 [41, "South Carolina"],
                 [42, "South Dakota"],
                 [43, "Tennessee"],
                 [44, "Texas"],
                 [45, "Utah"],
                 [46, "Vermont"],
                 [47, "Virginia"],
                 [48, "Washington"],
                 [49, "West Virginia"],
                 [50, "Wisconsin"],
                 [51, "Wyoming"]
                ],
        blank=False,
    )


def custom_export(players):
    yield['session', 'participant_code', 'id_in_group', 'gender', 'age', 'state', 'ethnicity', 'income']
    for p in players:
        yield (
            p.session.code, p.participant.code, p.id_in_group, p.gender, p.age, p.state, p.ethnicity, p.income
        )
