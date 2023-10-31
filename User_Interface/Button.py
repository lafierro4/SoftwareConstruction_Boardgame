import pygame


class Button():
	"""
        Origanal Pygame Button Code https://github.com/harsitbaral/ButtonPygame/blob/main/pygamebuttonyoutube.py \n
		Modified for Cloneopoly \n
		Allows for the making of buttons for the game's User Interface
	"""
	def __init__(self, image , pos, text_input, font, base_color, hover_color):
		"""
			image: Background Image file for the Button may be None
			pos: Screen Cordinates for Button, ints, (x,y) format
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

	def checkForInput(self, position):
		"""
			Checks if the Button is clicked
			screen: Current Screen
			position: Current Mouse Position to compare if it overlaps with Button
		"""
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		"""
			Changes the Buttons Color when the mouse cursor overlaps its position
			screen: Current Screen
			position: Current Mouse Position to compare if it overlaps with Button
		"""
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hover_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)
