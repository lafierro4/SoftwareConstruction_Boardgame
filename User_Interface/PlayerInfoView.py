# PlayerInfoView
# Displays player-specific information, including names, financial status, and property ownership. Ensures player’s data is accurately presented to the user.
 
# Show Property Details
# Communicates with any Property to display its information when a player selects it. (Owned by them, someone else, Or no one)
# Pre-Condition: \@requires self.is_property_owned() or not self.is_property_owned()
# Post-Condition: \@ensures self.ui.display_property_selected()
# Method Signature: display_property(self) ->None

FPS = 60 
import  tkinter as tk
import pygame, os
from Game_Engine.Player import Player
from User_Interface.util import *

 
class PlayerSelectBox:
    def __init__(self, x, y, width, height, font):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = font
        self.input_text = ""
        self.active = False
        self.character_limit = 10

        button_size = height
        space_buffer = button_size * 2

        self.back_button = ImageButton(((x + width) + space_buffer, y + (button_size / 2)),
                                       pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "images", "previous_arrow.png")), (button_size, button_size)))
        self.forward_button = ImageButton(((x + width) + space_buffer * 3, y + (button_size / 2)),
                                          pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "images", "next_arrow.png")), (button_size, button_size)))

        self.token_images = token_image_surface(button_size)
        self.active_token = 0

    def handle_event(self, event):
        for button in [self.back_button, self.forward_button]:
            if event.type == pygame.MOUSEBUTTONDOWN and button.check_clicked(event.pos):
                self.active_token = (self.active_token - 1) if button == self.back_button else (self.active_token + 1)
                self.active_token %= len(self.token_images)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                # Do something with the entered text if needed
                print("Player Name:", self.input_text)
                self.input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]
            else:
                if len(self.input_text) < self.character_limit:
                    self.input_text += event.unicode

    def update(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
        if self.active:
            pygame.draw.rect(screen, (0, 255, 0), self.rect, 2)
        else:
            pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)  

        input_surface = self.font.render(self.input_text, True, (0, 0, 0))
        screen.blit(input_surface, (self.rect.x + 5, self.rect.y + 5))

        self.back_button.rect.topleft = ((self.rect.x + self.rect.width) + 2 * self.rect.height, self.rect.y + 5)
        self.forward_button.rect.topleft = ((self.rect.x + self.rect.width) + 4 * self.rect.height, self.rect.y + 5)

        token_image_x = (self.rect.x + self.rect.width) + 3 * self.rect.height
        token_image_y = self.rect.y + 5
        screen.blit(self.token_images[self.active_token], (token_image_x, token_image_y))

        self.back_button.image = pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "images", "previous_arrow.png")), (self.rect.height, self.rect.height))
        self.forward_button.image = pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "images", "next_arrow.png")), (self.rect.height, self.rect.height))
        screen.blit(self.back_button.image, self.back_button.rect.topleft) 
        screen.blit(self.forward_button.image, self.forward_button.rect.topleft)


def player_select_screen(screen:pygame.Surface,number_of_players):
    input_font = pygame.font.Font(os.path.join("assets", "images", "Minecraft.ttf"), 50)
    title_font = pygame.font.Font(os.path.join("assets", "images", "Minecraft.ttf"), 45)
    bg_image = pygame.transform.smoothscale(pygame.image.load(os.path.join("assets","images","bg_settings.png")), (screen.get_width(), screen.get_height()) )
    bg_image.set_alpha(128)

    # Making the Player Selection Box
    player_boxes = []
    box_width = 200
    box_height = 50
    space_between_boxes = 20
    total_height = len(range(3)) * (box_height + space_between_boxes) - space_between_boxes
    starting_y = (screen.get_height() - total_height) // 2
    for i in range(number_of_players): 
        player_box = PlayerSelectBox((screen.get_width() - box_width) // 4,starting_y + i * (box_height + space_between_boxes), screen.get_width() // 2, 50, input_font)
        player_boxes.append(player_box)

    title_text = title_font.render("Insert Players Name and Choose a Token.", True, hex_to_rgb("#ffffff"))
    title_text_rect = title_text.get_rect(center= (screen.get_width()/2, screen.get_height()/5))
    box_width = title_text.get_width() + 20
    box_height = title_text.get_height() + 20
    box_rect = pygame.Rect(title_text_rect.centerx - box_width / 2, title_text_rect.centery - box_height / 2, box_width, box_height)

    submit_button = Button(pos=(screen.get_width() / 2, screen.get_height() - 100),text_input="Start Game",font= title_font, base_color="#000000",hover_color="#0a18f3",
                            image= pygame.transform.smoothscale(pygame.image.load(os.path.join("assets","images","button_background.png")), 
                                                         ((screen.get_width()/2.5),(screen.get_height()/5))))
    run = True
    clock = pygame.time.Clock()
    while run:
        if (bg_image.get_width(), bg_image.get_height()) != (screen.get_width(), screen.get_height()):
            bg_image = pygame.transform.smoothscale(bg_image, (screen.get_width(), screen.get_height()))
        screen.blit(bg_image,(0,0))
        pygame.draw.rect(screen, hex_to_rgb("#ff2323"), box_rect)
        pygame.draw.rect(screen, hex_to_rgb("#000000"), box_rect, 5)  
        screen.blit(title_text,title_text_rect)

        submit_button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            for player_box in player_boxes:
                player_box.handle_event(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if submit_button.check_clicked(event.pos):
                    player_data = (player_names, player_tokens) = [], []
                    for player_box in player_boxes:
                        player_names.append( player_box.input_text)
                        player_tokens.append( player_box.active_token)
                        
                    return player_data

        for player_box in player_boxes:
            player_box.update(screen)

        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()

def display_player_info(player:Player):
    root = tk.Tk()
    root.title(f"{player.name}'s Infomation")
    root.geometry("640x360")
    label_name = tk.Label(root, text=f"Player Name: {player.name}")
    label_name.pack()
 
    label_financial_status = tk.Label(root, text=f"Player Balance: ${player.balance}")
    label_financial_status.pack()
 
    label_property_ownership = tk.Label(root, text="Property Ownership:")
    label_property_ownership.pack()

    listbox_assets = tk.Listbox(root)
    listbox_assets.pack()

    if player.assets != None:
        for asset in player.assets:
            listbox_assets.insert(tk.END, asset.name)

    # Run the Tkinter main loop
    root.mainloop()