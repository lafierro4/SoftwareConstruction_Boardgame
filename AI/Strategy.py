from random import random
import pygame, os
from Game_Engine.GameboardManager import Gameboard, Player, Property
class Strategy:
    buy_property = 0.3
    gameboard = Gameboard()
    
    
    def should_buy_property(self, property_object:Property, player:Player):
        return player.balance >= property_object.price and random() < self.buy_property
   
    def dice_numbers(self):
        return sum(self.gameboard.roll_dice())
