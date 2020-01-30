from unittest import TestCase

import Dominion
import testUtility


def setupTestData(self):
    self.player_names = ['TestPlayer1', 'TestPlayer2', 'TestPlayer3']
    self.player = Dominion.Player('TestPlayer')
    self.nV = 12
    self.nC = 30
    self.box = testUtility.GetBoxes(self.nV)
    self.supply_order = testUtility.GetSupplyOrder()
    self.supply = testUtility.getSupply(self.box, 10)
    testUtility.fillSupply(self.supply, (60 - len(self.player_names) * 7), 40, 30, self.nV, self.nV, self.nV, self.nC)


class TestGameOver(TestCase):
    def test_gameover(self):
        setupTestData(self)

        # beginning of game, should return False
        assert(not Dominion.gameover(self.supply))

        # end of game condition 1, supply has 3 empty stacks
        self.supply['Copper'] = [Dominion.Copper()]*0
        self.supply['Gold'] = [Dominion.Gold()]*0
        self.supply['Estate'] = [Dominion.Estate()]*0

        assert(Dominion.gameover(self.supply))

        # reset supply
        setupTestData(self)

        # test end game condition 2, Province stack is empty
        self.supply['Province'] = [Dominion.Province()]*0

        assert(Dominion.gameover(self.supply))

class TestAction_card(TestCase):
    def test_init(self):
        testCard = Dominion.Action_card('TestCard', '1', 2, 1, 3, 4)

        assert (testCard.name == "TestCard")
        assert (testCard.category == 'action')
        assert (testCard.cost == '1')
        assert (testCard.buypower == 0)
        assert (testCard.vpoints == 0)
        assert (testCard.actions == 2)
        assert (testCard.cards == 1)
        assert (testCard.buys == 3)
        assert (testCard.coins == 4)

    def test_use(self):
        # set up default test data
        setupTestData(self)

        # add test Action Card to hand
        testCard = Dominion.Action_card('TestCard', '1', 2, 1, 3, 4)
        self.player.hand.append(testCard)

        # get hand length to compare to after Action_card.use()
        handLength = len(self.player.hand)

        # execute Action_card.use() to test function
        testCard.use(self.player, trash=[])

        # confirm function executed properly
        assert (testCard in self.player.played)  # one card is added to the player.played list in use
        assert (handLength - len(self.player.hand) == 1)  # one card is removed from the player's hand

    def test_augment(self):
        # set up default test data
        setupTestData(self)

        # add test Action Card to hand
        testCard = Dominion.Action_card('TestCard', '1', 2, 1, 3, 4)
        self.player.hand.append(testCard)
        self.player.actions = 0
        self.player.buys = 0
        self.player.purse = 0

        beforeAugmentLength = len(self.player.hand)

        testCard.augment(self.player)
        assert (self.player.actions == 2)
        assert (self.player.buys == 3)
        assert (self.player.purse == 4)
        assert (len(self.player.hand) == (beforeAugmentLength + 1))

class TestPlayer(TestCase):
    def test_draw(self):
        setupTestData(self)

        # make the player's deck empty so that the deck is replenished on draw (increases code coverage)
        self.player.discard = self.player.deck
        self.player.deck = []

        # test draw to player.hand with deck size of 5 and hand size of 5 (default)
        self.player.draw()
        assert(len(self.player.deck) == 4)
        assert(len(self.player.hand) == 6)

    def test_action_balance(self):
        setupTestData(self)

        # give the player two action cards
        testCard1 = Dominion.Action_card('TestCard1', '1', 2, 1, 3, 4)
        testCard2 = Dominion.Action_card('TestCard2', '1', 3, 1, 3, 4)
        actionCards = [testCard1, testCard2]
        self.player.hand.extend(actionCards)

        # give the player 1 victory card
        testCard3 = Dominion.Victory_card('TestCard3', 1, 2)
        self.player.hand.append(testCard3)

        # calculated expected values
        expectedBalance = (0 - 1 + testCard1.actions) - 1 + testCard2.actions
        expectedActionBalance = (70 * expectedBalance) / len(self.player.stack())

        # get actual value
        actualActionBalance = self.player.action_balance()

        assert(actualActionBalance == expectedActionBalance)

    def test_calcpoints(self):
        setupTestData(self)

        result = self.player.calcpoints()
        assert(result == 3)  # default start of game point score

        self.player.hand.append(Dominion.Gardens())
        result = self.player.calcpoints()
        assert(result == 4)

        # add 10 action cards (0 victory points) to test if the n//10 * #gardens is working properly
        for i in range(0, 10):
            self.player.hand.append(Dominion.Action_card('TestCard1', '1', 2, 1, 3, 4))
        result = self.player.calcpoints()
        assert(result == 5)

    def test_cardsummary(self):
        setupTestData(self)

        # default start of game summary
        summary = self.player.cardsummary()
        assert(summary['Estate'] == 3)
        assert(summary['VICTORY POINTS'] == 3)
        assert(summary['Copper'] == 7)

        self.player.hand.append(Dominion.Gardens())
        summary = self.player.cardsummary()
        assert(summary['Estate'] == 3)
        assert(summary['Copper'] == 7)
        assert(summary['VICTORY POINTS'] == 4)
        assert(summary['Gardens'] == 1)
