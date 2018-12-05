import pygame as pyg
import BoxerUnboxer
# Box for inputting

spin_put_box = pyg.image.load("Resources/Assets/box_center.png")

# Spawning the box

# Input box with text

pyg.init()
screen = pyg.display.set_mode((640, 480))
COLOR_INACTIVE = pyg.Color('lightskyblue3')
COLOR_ACTIVE = pyg.Color('dodgerblue2')
FONT = pyg.font.Font(None, 32)


class InputBox:

    def __init__(self, x, y, w, h, place, text=''):
        self.rect = pyg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.place = place

    def handle_event(self, event):
        if event.type == pyg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos[0], event.pos[1]):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE

        if event.type == pyg.KEYDOWN:
            if self.active:
                if event.key == pyg.K_RETURN:
                    BoxerUnboxer.boxer(self.text, self.place)
                    self.text = ''

                elif event.key == pyg.K_BACKSPACE:
                    self.text = self.text[:-1]

                else:
                    if len(str(self.text)) < 1:
                        self.text += event.unicode

                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(22, 22)
        self.rect.w = width

    def draw(self, text_screen):
        # Blit the text.
        text_screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pyg.draw.rect(text_screen, self.color, self.rect, 2)
