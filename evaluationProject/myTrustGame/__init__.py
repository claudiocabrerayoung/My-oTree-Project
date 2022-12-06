from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'trust'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    TRUSTOR_ROLE = 'Trustor'
    TRUSTEE_ROLE = 'Trustee'
    NUM_ROUNDS = 2
    INSTRUCTIONS_TEMPLATE = 'myTrusteGame/instructions.html'
    # Initial amount allocated to each player
    ENDOWMENT = cu(100)
    MULTIPLIER = 3

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    sent_amount = models.CurrencyField(
    min = 0,
    max = C.ENDOWMENT,
    doc = """"Amount sent by P1""",
    label = "Please enter an amount from 0 to 100:",    
    )
    sent_back_amount = models.CurrencyField(doc = """"Amount sent back by P2""", min = cu(0))


class Player(BasePlayer):
    name = models.StringField(label = "Your name:")
    age = models.IntegerField(label = "Your age:")

# PAGES
class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
