FPS = 60 
import tkinter as tk
from tkinter import font, ttk
import pygame, os
from Game_Engine.Player import Player
from User_Interface.util import *

 
class PlayerSelectBox:
    def __init__(self, x, y, width, height, font):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = font
        self.input_text = ""
        self.active = False
        self.character_limit = 8

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
            if event.key == pygame.K_BACKSPACE:
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


def player_select_screen(screen:pygame.Surface,number_of_players, vs_ai_mode):
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
        if vs_ai_mode:
            player_box = PlayerSelectBox((screen.get_width() - box_width) // 4,starting_y + i * (box_height + space_between_boxes), screen.get_width() // 2, 50, input_font)
            player_boxes.append(player_box)
            break
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
                        if vs_ai_mode and player_box.active_token > 0:
                            player_box.input_text = player_box.input_text.split()[0]
                    if vs_ai_mode:
                        ai_players = number_of_players - 1
                        for i in range(ai_players):
                            player_names.append(f"AI {i+1}")
                            player_tokens.append(i + 1)
                        
                    return player_data

        for player_box in player_boxes:
            player_box.update(screen)

        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()


def display_player_info(player: Player):
    def on_select(event):
        selected_index = treeview_assets.selection()
        if selected_index:
            add_house_button.pack(pady=5)

    def buy_house():
        selected_item = treeview_assets.focus()
        if selected_item:
            selected_index = treeview_assets.index(selected_item)
            if player.assets != None:
                selected_asset = player.assets[selected_index]
                if selected_asset.space_type == "property":
                    if selected_asset.num_houses <= 4:
                        result = selected_asset.build_house()
                    else:
                        result = f"Maximum Houses Purchased for {selected_asset.name}"
                else:
                    result = f"{selected_asset.name} is Not a Property\nUnable to Purchase Houses"
                result_label.config(text=result)
                balance_var.set(f"Player Balance: ${player.balance}")
            update_treeview()

    def update_treeview():
        treeview_assets.delete(*treeview_assets.get_children())
        if player.assets is not None:
            for asset in player.assets:
                if asset.space_type == "property":
                    treeview_assets.insert("", "end",values=(asset.name, asset.num_houses, asset.current_rent, asset.house_price))
                else:
                    treeview_assets.insert("", "end",values=(asset.name, "N/A", "N/A", "N/A"))
        root.update()

    root = tk.Tk()
    root.title(f"{player.name}'s Information")
    root.geometry("825x550")

    label_name = tk.Label(root, text=f"Player Name: {player.name}")
    label_name.pack()

    balance_var = tk.StringVar()
    balance_var.set(f"Player Balance: ${player.balance}")
    label_financial_status = tk.Label(root, textvariable=balance_var)
    label_financial_status.pack()

    label_property_ownership = tk.Label(root, text="Property Ownership:")
    label_property_ownership.pack()

    treeview_assets = ttk.Treeview(root, columns=("Name", "Num Houses", "Current Rent", "House Price"), show="headings")
    treeview_assets.heading("Name", text="Property Name")
    treeview_assets.heading("Num Houses", text="Number of Houses")
    treeview_assets.heading("Current Rent", text="Current Rent")
    treeview_assets.heading("House Price", text="House Price")
    treeview_assets.pack()

    if player.assets is not None:
        update_treeview()

    add_house_button = tk.Button(root, font=("", 12), text="Buy House", command=buy_house)
    treeview_assets.bind('<<TreeviewSelect>>', on_select)
    add_house_button.pack()

    result_label = tk.Label(root, text="")
    result_label.pack(pady=10)

    root.mainloop()


    root.mainloop()