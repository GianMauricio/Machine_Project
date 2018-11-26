import pygame as pyg
import BoxerUnboxer as BU
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
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE

        if event.type == pyg.KEYDOWN:

            if self.active:
                if event.key == pyg.K_RETURN:
                    BU.boxer(self.text, self.place)
                    self.text = ''

                elif event.key == pyg.K_BACKSPACE:
                    self.text = self.text[:-1]

                else:
                    if len(str(self.text)) < 1:
                        self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def return_string_var(self):
        return self.text

    def update(self):
        # Resize the box if the text is too long.
        width = max(22, 22)
        self.rect.w = width

    def draw(self, text_screen):
        # Blit the text.
        text_screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pyg.draw.rect(text_screen, self.color, self.rect, 2)


def main():
    clock = pyg.time.Clock()
    input_box1 = InputBox(100, 100, 140, 32)
    input_box2 = InputBox(125, 100, 140, 32)
    input_box3 = InputBox(150, 100, 140, 32)
    input_box4 = InputBox(175, 100, 140, 32)
    input_boxes = [input_box1, input_box2, input_box3, input_box4]
    done = False

    while not done:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()

        screen.fill((30, 30, 30))
        for box in input_boxes:
            box.draw(screen)

        pyg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pyg.quit()

