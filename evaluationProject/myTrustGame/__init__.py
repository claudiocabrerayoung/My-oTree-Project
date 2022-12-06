from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'myTrustGame'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    TRUSTOR_ROLE = 'Trustor'
    TRUSTEE_ROLE = 'Trustee'
    NUM_ROUNDS = 2
    INSTRUCTIONS_TEMPLATE = 'myTrustGame/instructions.html'
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


# FUNCTIONS

#On Subsessions
def creating_session(subsession: Subsession):
    # .group_randomly will enable the randomization
    #of the player's allocation to groups, as well as
    #the role's allocation to players.
    subsession.group_randomly(fixed_id_in_group=False)

#On Groups
def sent_back_amount_max(group: Group):
    return group.sent_amount + C.MULTIPLIER

def set_payoffs(group:Group):
    p1 = group.get_player_by_role("Trustor")
    p2 = group.get_player_by_role("Trustee")
    p1.payoff = C.ENDOWMENT = group.sent_amount + group.sent_back_amount
    p2.payoff = group.sent_amount * C.MULTIPLIER - group.sent_back_amount

# On Players

# PAGES
class Introduction(Page):
    pass


class Send(Page):
    """
    This page is only for P1
    P1 sends amount (all, some or none) to P2
    This amount is tripled by experimenter,
    e.g. if sent amount by P1 is 5, amount received by P2 is 15
    """

    form_model = "group"
    form_fields = ["sent_amount"]

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 1

class SendBackWaitPage(WaitPage):
    pass


class SendBack(Page):
    """"
    This page is only for P2
    P2 sends back some amount (of the tripled amount received) to P1
    """
    form_model = "group"
    form_fields = ["sent_back_amount"]

    @staticmethod
    def is_displayer(player: Player):
        return player.id_in_group == 2
    
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group

        tripled_amount = group.sent_amount * C.MULTIPLIER
        return dict(tripled_amount = tripled_amount)


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    """
    This page displays the earnings of each player
    """

    @staticmethod
    def vars_for_template(player: Player):
        group = player.group

        return dict(tripled_amount = group.sent_amount * C.MULTIPLIER)

page_sequence = [
    Introduction,
    Send,
    SendBackWaitPage,
    SendBack,
    ResultsWaitPage,
    Results
]