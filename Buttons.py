import pygame as pyg
import Verification

pyg.init()

WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)


class ButtonC:
    def __init__(self, txt, surface, location, bg=WHITE, fg=BLACK, size=(80, 30), font_name=None, font_size=16):
        self.color = bg  # the static (normal) color
        self.bg = bg  # actual background color, can change on mouse_over
        self.fg = fg  # text color
        self.size = size

        self.font = pyg.font.SysFont(font_name, font_size)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in self.size])

        self.surface = surface
        self.rect = self.surface.get_rect(center=location)

        self.call_back_ = Verification.reset()

    def event_handle(self, event):
        if event.type == pyg.MOUSEBUTTONDOWN:
            self.call_back()

    def draw(self):
        self.mouse_over()

        self.surface.fill(self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)
        self.surface.blit(self.surface, self.rect)

    def mouse_over(self):
        self.bg = self.color
        pos = pyg.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.bg = GREY  # mouse_over color

    def call_back(self):
        self.call_back_()


class ButtonS:
    def __init__(self, txt, surface, location, answer=0, parameter=0, bg=WHITE, fg=BLACK, size=(80, 30), font_name=None,
                 font_size=16):
        self.color = bg  # the static (normal) color
        self.bg = bg  # actual background color, can change on mouse_over
        self.fg = fg  # text color
        self.size = size

        self.font = pyg.font.SysFont(font_name, font_size)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in self.size])

        self.surface = surface
        self.rect = self.surface.get_rect(center=location)
        self.answer = answer
        self.parameter = parameter

    def event_handle(self, event):
        if event.type == pyg.MOUSEBUTTONDOWN:
            self.call_back()

    def draw(self):
        self.mouse_over()

        self.surface.fill(self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)
        self.surface.blit(self.surface, self.rect)

    def mouse_over(self):
        self.bg = self.color
        pos = pyg.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.bg = GREY  # mouse_over color

    def call_back(self):
        Verification.verification(self.answer, self.parameter)
