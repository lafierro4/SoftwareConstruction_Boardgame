import pygame, os,random
import unittest
from Game_Engine.Player import Player  
from Game_Engine.Property import Property


class TestCases(unittest.TestCase):

    
    def test_transfer_money(self):
        player1 = Player(name="Player1", token=pygame.Surface((50, 50)), space_size=10)
        player2 = Player(name="Player2", token=pygame.Surface((50, 50)), space_size=10)
        
        player1.balance = 1000
        player2.balance = 500

        # Test transferring money from player1 to player2
        player1.transfer_money(player2, 200)
        self.assertEqual(player1.balance, 800)
        self.assertEqual(player2.balance, 700)

        # Test transferring money when player1 doesn't have sufficient balance
        player1.transfer_money(player2, 1000)
        self.assertEqual(player1.balance, 800)  # Balance should not go below 0
        self.assertEqual(player2.balance, 700)

    def test_add_property(self):
        player = Player(name="TestPlayer", token=pygame.Surface((50, 50)), space_size=10)

        # Test adding a property to the player's assets
        property_item = "Mediterranean Meals"  # You can replace this with an actual Property object
        player.add_property(property_item)
        self.assertIn(property_item, player._assets)

        # Test adding multiple properties to the player's assets
        properties = ["Skipping Railroad", "Vermont Vacation", "Sir Charles' Sanctuary"]  # Replace with actual Property objects
        for prop in properties:
            player.add_property(prop)
        self.assertEqual(len(player._assets) - 1, len(properties))

    def test_is_owned(self):
        # Test when the property has no owner
        property1 = Property(name="Property1", property_type="property", color="#ff0000", price=200, rent_values=[20, 30, 40])
        self.assertFalse(property1.is_owned())

        # Test when the property has an owner
        player = Player(name="Owner", token=None, space_size=0) # type: ignore
        property1.change_owner(player)
        self.assertTrue(property1.is_owned())

    def test_calculate_rent_property(self):
        # Create a Player instance for testing
        player_instance = Player(name="TestPlayer", token=None, space_size=10) # type: ignore

        # Create a Property instance with rent values [100, 200, 300]
        property_instance = Property(name="TestProperty", property_type="property", color="#FF0000", price=500, rent_values=[100, 200, 300])

        # Set the property type to "property"
        property_instance._square_type = "property"

        # Set the number of houses to 2
        property_instance._num_houses = 2

        # Call _calculate_rent and assert the result
        result = property_instance.calculate_rent(player_instance)
        self.assertEqual(result, 300)  # Expecting the third value in the rent_values list
    
    def test_action_property_owned_by_other_player(self):
        # Create two Player instances for testing
        player_instance_1 = Player(name="TestPlayer1", token=None, space_size=10) # type: ignore
        player_instance_2 = Player(name="TestPlayer2", token=None, space_size=10) # type: ignore
        player_instance_1.balance = 1000  # Set an initial balance for player 1

        # Create a Property instance with dummy values
        property_instance = Property(name="TestProperty", property_type="property", color="#FF0000", price=200)

        # Mock the is_owned method to return True
        property_instance.is_owned = lambda: True

        # Mock the _calculate_rent and transfer_money methods
        property_instance.calculate_rent = lambda player: 100  # Assume a fixed rent value
        player_instance_1.transfer_money = lambda owner, amount: setattr(player_instance_1, "_balance", player_instance_1.balance - amount)

        # Set the property owner to player 2
        property_instance._owner = player_instance_2

        # Call the action method
        property_instance.action(player_instance_1)

        # Assert that rent is calculated and paid to the property owner
        self.assertEqual(player_instance_1.balance, 900)  # Initial balance (1000) - Rent (100)





if __name__ == '__main__':
    unittest.main()

