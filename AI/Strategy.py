from random import random
import pygame, os
from Game_Engine.GameboardManager import Gameboard, Player, Property
class Strategy:
    buy_property = 0.8
    gameboard = Gameboard()
    
    @staticmethod
    def should_buy_property(property_object:Property, player:Player):
        return player.balance >= property_object.price and random() < Strategy.buy_property
   

  