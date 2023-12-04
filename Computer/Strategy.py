from random import random, choices
import pygame, os
from Game_Engine import Player, Property
class Strategy:
    buy_property = 0.8
    buy_house = 0.1
    
    @staticmethod
    def should_buy_property(property_object:Property.Property, player:Player.Player):
        return player.balance >= property_object.price and random() < Strategy.buy_property
    @staticmethod
    def make_random_choice(options, weights):
        return choices(options, weights=weights)[0]
    
    @staticmethod
    def ai_buy_house(property_asset: Property.Property):
        if property_asset.space_type == "property":    
            if  property_asset.num_houses <= 4:
                num_houses_to_buy = Strategy.make_random_choice([0, 1, 2, 3, 4], [0.4, 0.5, 0.4, 0.2, 0.1])
                for _ in range(num_houses_to_buy):
                    result = property_asset.build_house()
            else:
                return