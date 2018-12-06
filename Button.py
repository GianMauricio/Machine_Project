import pygame as pyg


class Button:

    def __init__(self, x, y, w, h, surface, image_active, image_inactive, validity=False, state=False):
        self.rect = pyg.Rect(x, y, w, h)
        self.return_value = validity
        self.active_state = image_active
        self.inactive_state = image_inactive
        self.screen = surface
        self.state = state

    def handle_event(self, event):
        print("Checking for event")
        if event.type == pyg.MOUSEBUTTONDOWN:
            print("Event received")
            if self.rect.collidepoint(pyg.mouse.get_pos()[0], pyg.mouse.get_pos()[1]):
                print("Changing state")
                self.state = True
        if event.type == pyg.MOUSEBUTTONUP:
            self.state = False
            self.shift_validity()

    def shift_validity(self):
        print("Command acknowledged")
        self.return_value = True

    def draw_button(self):
        if self.state:
            self.screen.blit(self.inactive_state, self.rect)
        else:
            self.screen.blit(self.active_state, self.rect)
