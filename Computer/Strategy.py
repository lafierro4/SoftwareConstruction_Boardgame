from random import random
import pygame, os
from Game_Engine import Player, Property
class Strategy:
    buy_property = 0.8
    
    @staticmethod
    def should_buy_property(property_object:Property.Property, player:Player.Player):
        return player.balance >= property_object.price and random() < Strategy.buy_property
   

  