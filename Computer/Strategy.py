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