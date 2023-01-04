import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.cardgame = CardGame()
        self.card1 = Card ("heart", 1)
        self.card2 = Card ("spade", 4)
        self.card3 = Card ("diamond", 10)
        self.card4 = Card ("club", 3)
        self.cards = [self.card1, self.card2, self.card3, self.card4]
        
    
    def test_can_check_for_ace(self):
        result = self.cardgame.check_for_ace(self.card1)
        self.assertEqual(True, result)
        
    def test_find_highest_card(self):
        result = self.cardgame.highest_card(self.card2, self.card3)
        self.assertEqual(self.card3, result)
        
    def test_value_of_cards_total(self):
        result = self.cardgame.cards_total(self.cards)
        self.assertEqual("You have a total of 18", result)
        