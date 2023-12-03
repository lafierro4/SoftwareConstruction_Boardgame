# Holds Classes and Methods that the User Interface use to allow the User to interact with the system
# It also loads and holds images that the User Interface can refer to to draw onto the Screen

import pygame,os
from typing import List
from Game_Engine.BoardSpace import BoardSpace
from Game_Engine.Property import Property
from Game_Engine.Square import Square

class Button():
	"""
        Origanal Pygame Button Code https://github.com/harsitbaral/ButtonPygame/blob/main/pygamebuttonyoutube.py \n
		Modified for Cloneopoly \n
		Allows for the making of buttons for the game's User Interface
	"""
	def __init__(self, pos, text_input, font, base_color, hover_color , image = None):
		"""
			pos: Screen Cordinates for Button, ints, (x,y) format
			image: Background Image file for the Button may be None
			text_input: Buttton Text
			font: Pygame Font object for text
			base_color: The color that the button will appear as when not being selected
			hover_color: The color that the button will appear as when it is selected or hovered
		"""
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hover_color = base_color, hover_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center= (self.x_pos,self.y_pos))
	

	def update(self,screen):
		"""
			Updates Button to show render in current screen, or updates if any change is made to Button
			screen: Current Screen
		"""
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def check_clicked(self, position):
		"""
			Checks if the Button is clicked
			screen: Current Screen
			position: Current Mouse Position to compare if it overlaps with Button
		"""
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def change_color(self, position):
		"""
			Changes the Buttons Color when the mouse cursor overlaps its position
			screen: Current Screen
			position: Current Mouse Position to compare if it overlaps with Button
		"""
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hover_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)


class ImageButton(Button):
	"""
		Button subclass designede for Image Only Buttons
	"""
	def __init__(self, pos, image:pygame.Surface):
		"""
			Button Constructor for an Image only Button
			pos: Screen Cordinates for Button, ints, (x,y) format1
			image: Background Image file location for the Button
		"""
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))

	def update(self, screen):
		screen.blit(self.image, self.rect)


def hex_to_rgb(hex_code) -> tuple[int, int, int]:
    hex_code = hex_code.lstrip("#")
    r, g, b = int(hex_code[0:2], 16), int(hex_code[2:4], 16), int(hex_code[4:6], 16)
    return r, g, b

def board_spaces() -> List[BoardSpace]:
	return [
            Square("Go","corner"),
            Property("Mediterranean Meals", "property", "#a37759", 60, [2, 10, 30, 90, 160, 250], 50),
            Square("Lice Tax", "tax"),
            Property("Baltic Breezeway", "property", "#a37759", 60, [4, 20, 60, 180, 320, 450], 50),
            Square("Income Tax", "tax"),
            Property("Skipping Railroad", "property", "#000000", 200, [25, 50, 100, 200]), 
            Property("Oriental Oasis", "property", "#e8a541", 100, [6, 30, 90, 270, 400, 550], 50),
            Square("Apple Tax", "tax"),
            Property("Vermont Vacation", "property", "#e8a541", 100, [6, 30, 90, 270, 400, 550], 50),
            Property("Connecticut Courtyard", "property", "#e8a541", 120, [8, 40, 100, 300, 450, 600],  50),
            Square("Jail", "jail"),
            Property("Sir Charles' Sanctuary", "property", "#a14685", 140, [10, 50, 150, 450, 625, 750],  100),
            Property("Electric Company", "utility", "#a37759", 150),
            Property("United Estates", "property", "#a14685", 140, [10, 50, 150, 450, 625, 750],  100),
            Property("Virginia Vineyards", "property", "#a14685", 160, [12, 60, 180, 500, 700, 900], 100),
            Property("Quarter Railroad", "property", "#000000", 200, [25, 50, 100, 200],100),
            Property("Saintly James' Square", "property", "#ef756d", 180, [14, 70, 200, 550, 750, 950], 100),
            Square("Charity Tax", "tax"),
            Property("Tunessee Avenue", "property", "#ef756d", 180, [14, 70, 200, 550, 750, 950], 100),
            Property("Big Apple Avenue", "property", "#ef756d", 200, [16, 80, 220, 600, 800, 1000], 100),
            Square("Free Parking", "corner"),
            Property("Kentucky Fried Avenue", "property", "#ca6e47", 220, [18, 90, 250, 700, 875, 1050], 150),
            Square("Bad Hair Tax", "tax"),
            Property("Indy Car Avenue", "property", "#ca6e47", 220, [18, 90, 250, 700, 875, 1050], 150),
            Property("Illusion Avenue", "property", "#ca6e47", 240, [20, 100, 300, 750, 925, 1100],  150),
            Property("R. R. Railroad", "property", "#000000", 200, [25, 50, 100, 200]),
            Property("Atlantic Adventure", "property", "#2277a2", 260, [22, 110, 330, 800, 975, 1150], 150),
            Property("Ventilation Avenue", "property", "#2277a2", 260, [22, 110, 330, 800, 975, 1150], 150),
            Property("Water Works", "utility", "#a37759", 150),
            Property("Marvin's Magic Meadow", "property", "#2277a2", 280, [24, 120, 360, 850, 1025, 1200], 150),
            Square("Go To Jail", "go_to_jail"),
            Property("Pacific Playground", "property", "#55a95d", 300, [26, 130, 390, 900, 1100, 1275], 200),
            Property("Northern Charm Avenue", "property", "#55a95d", 300, [26, 130, 390, 900, 1100, 1275], 200),
            Square("Juice Tax", "tax"),
            Property("Penny-sylvania Avenue", "property", "#55a95d", 320, [28, 150, 450, 1000, 1200, 1400], 200),
            Property("Longline Railroad", "property", "#000000", 200, [25, 50, 100, 200]),
            Square("Candy Tax", "tax"),
            Property("Parking Place", "property", "#e34537", 350, [35, 175, 500, 1100, 1300, 1500], 200),
            Square("Luxury Tax", "tax"),
            Property("Bored Walk", "property", "#e34537", 400, [50, 200, 600, 1400, 1700, 2000], 200),
        ]

def token_image_paths():
	file_paths = [os.path.join("assets", "images", "car.png"),os.path.join("assets", "images", "penguin.png"),
                    os.path.join("assets", "images", "cat.png"), os.path.join("assets", "images", "battleship.png"),
                    os.path.join("assets", "images", "duck.png"), os.path.join("assets", "images", "dog.png"),  os.path.join("assets", "images", "hat.png")
                 ]
	return file_paths    
	
def token_image_surface(size):
    token_surfaces = []
    file_paths = token_image_paths()
    for path in file_paths:
        token_surfaces.append(pygame.transform.smoothscale(pygame.image.load(path).convert_alpha(),(size,size)))
    return token_surfaces