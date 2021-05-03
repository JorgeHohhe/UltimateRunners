import pygame
from ...graphics.images_loader import *
import source.audio.audio_loader as al

WIN_WIDTH = 1000
WIN_HEIGHT = 680
class Menu():
    def __init__(self, checkinputs):
        self.checkinputs = checkinputs
        self.mid_width = WIN_WIDTH/2
        self.mid_height = WIN_HEIGHT/2
        self.run_display = True
        self.display = pygame.Surface((WIN_WIDTH,WIN_HEIGHT))
        self.window = pygame.display.set_mode(((WIN_WIDTH,WIN_HEIGHT)))
        self.cursor_rect = pygame.Rect(0,0,50,50)
        self.offset = -120 #cursor
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        self.YELLOW = (255,255,0)
        self.font_name = 'freesansbold.ttf'
        self.chooselvl = 1
    
    def draw_text(self, text, size, x, y, color):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.window.blit(text_surface, text_rect)
        

    def draw_cursor(self):
        self.draw_text('>', 40, self.cursor_rect.x, self.cursor_rect.y, self.WHITE)


class MainMenu(Menu):
    def __init__(self, checkinputs):
        Menu.__init__(self, checkinputs)
        self.state = "Start"
        self.startx, self.starty = self.mid_width, self.mid_height + 50
        #Help
        self.volumex, self.volumey = self.mid_width, self.mid_height + 100
        #Choose Map
        self.mapx, self.mapy = self.mid_width, self.mid_height + 150
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.checkinputs.check_events()
            self.check_input()
            self.window.blit(BG, (0,0))
            self.draw_text('Main Menu', 40, WIN_WIDTH/2, WIN_HEIGHT/2 - 20, self.WHITE)
            self.draw_text("Start Game", 40, self.startx, self.starty, self.WHITE)
            self.draw_text("Help", 40, self.volumex, self.volumey, self.WHITE)
            self.draw_text("Choose Map", 40, self.mapx, self.mapy, self.WHITE)
            self.draw_cursor()
            pygame.display.update()
            self.checkinputs.reset_keys()
            pygame.display.flip()

    def move_cursor(self):
        if self.checkinputs.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.volumex + self.offset, self.volumey)
                self.state = 'Volume'
            elif self.state == 'Volume':
                self.cursor_rect.midtop = (self.mapx + self.offset, self.mapy)
                self.state = 'Choose Map'
            elif self.state == 'Choose Map':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.checkinputs.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.mapx + self.offset, self.mapy)
                self.state = 'Choose Map'
            elif self.state == 'Choose Map':
                self.cursor_rect.midtop = (self.volumex + self.offset, self.volumey)
                self.state = 'Volume'
            elif self.state == 'Volume':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
    
    def check_input(self):
        self.move_cursor()
        if self.checkinputs.START_KEY:
            if self.state == 'Start':
                self.checkinputs.playing = True
            elif self.state == 'Volume':
                self.checkinputs.curr_menu = self.checkinputs.helpmenu
            elif self.state == 'Choose Map':
                self.checkinputs.curr_menu = self.checkinputs.choose_map
            self.run_display = False

class ChooseMapMenu(Menu):
    def __init__(self, checkinputs):
        Menu.__init__(self, checkinputs)
        self.state = 'Level 1'
        self.map1x, self.map1y = self.mid_width, self.mid_height + 50
        self.map2x, self.map2y = self.mid_width, self.mid_height + 100
        self.map3x, self.map3y = self.mid_width, self.mid_height + 150
        self.cursor_rect.midtop = (self.map1x + self.offset, self.map1y)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.checkinputs.check_events()
            self.check_input2()
            self.window.blit(BG, (0,0))
            self.draw_text('Choose Level', 40, WIN_WIDTH/2, WIN_HEIGHT/2 - 20, self.WHITE)
            self.draw_text("Level 1", 40, self.map1x, self.map1y, self.WHITE)
            self.draw_text("Level 2", 40, self.map2x, self.map2y, self.WHITE)
            self.draw_text("Level 3", 40, self.map3x, self.map3y, self.WHITE)
            self.draw_cursor()
            pygame.display.update()
            self.checkinputs.reset_keys()
            pygame.display.flip()

    def move_cursor2(self):
        if self.checkinputs.BACK_KEY:
            self.checkinputs.curr_menu = self.checkinputs.main_menu
            self.run_display = False
        elif self.checkinputs.DOWN_KEY:
            if self.state == 'Level 1':
                self.cursor_rect.midtop = (self.map2x + self.offset, self.map2y)
                self.state = 'Level 2'
            elif self.state == 'Level 2':
                self.cursor_rect.midtop = (self.map3x + self.offset, self.map3y)
                self.state = 'Level 3'
            elif self.state == 'Level 3':
                self.cursor_rect.midtop = (self.map1x + self.offset, self.map1y)
                self.state = 'Level 1'
        elif self.checkinputs.UP_KEY:
            if self.state == 'Level 1':
                self.cursor_rect.midtop = (self.map3x + self.offset, self.map3y)
                self.state = 'Level 3'
            elif self.state == 'Level 3':
                self.cursor_rect.midtop = (self.map2x + self.offset, self.map2y)
                self.state = 'Level 2'
            elif self.state == 'Level 2':
                self.cursor_rect.midtop = (self.map1x + self.offset, self.map1y)
                self.state = 'Level 1'
        
    
    def check_input2(self):
        self.move_cursor2()
        if self.checkinputs.START_KEY:
            if self.state == 'Level 1':
                self.chooselvl = 1
                self.checkinputs.playing = True
            elif self.state == 'Level 2':
                self.chooselvl = 2
                self.checkinputs.playing = True
            elif self.state == 'Level 3':
                self.chooselvl = 3
                self.checkinputs.playing = True
            self.run_display = False


class HelpMenu(Menu):
    def __init__(self, checkinputs):
        Menu.__init__(self, checkinputs)
        self.map1x, self.map1y = self.mid_width, self.mid_height - 50
        self.map2x, self.map2y = self.mid_width, self.mid_height 
        self.map3x, self.map3y = self.mid_width, self.mid_height + 50

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.checkinputs.check_events()
            self.check_input3()
            self.window.blit(BG, (0,0))
            self.window.blit(CUBE, (WIN_WIDTH/2-450, self.map1y - 20))
            self.window.blit(DRAGON, (WIN_WIDTH/2-480, self.map1y +60))
            self.window.blit(ORB, (WIN_WIDTH/2-450, self.map1y +140))
            self.window.blit(LASER, (WIN_WIDTH/2-435, self.map1y +220))
            self.draw_text('Help', 50, WIN_WIDTH/2, WIN_HEIGHT/2 - 280, self.YELLOW)
            self.draw_text("Ultimate Runners é um jogo de plataforma com interação por meio de toque/clique",20, self.map1x, self.map1y -160, self.WHITE)
            self.draw_text("para controlar diferentes personagens, que reagem deformas únicas quando ",20, self.map1x, self.map1y -140, self.WHITE)
            self.draw_text("pressionada a tecla ESPAÇO no teclado.",20,self.map1x, self.map1y -120, self.WHITE)
            self.draw_text("Você deve utilizar constantemente essa tecla para desviar dos obstáculos no decorrer de cada nível.", 20, self.map1x, self.map1y - 100,  self.WHITE)
            self.draw_text("Pressione BACKSPACE para retornar ao menu principal.",20,self.map1x, self.map1y -80, self.WHITE)
            self.draw_text("CUBO", 20, self.map1x, self.map1y, self.YELLOW)
            self.draw_text("pode realizar pequenos saltos, quando em contato com a superfície;", 20, self.map1x, self.map1y + 20,  self.WHITE)
            self.draw_text("após o salto, ele cai pela ação da gravidade.", 20, self.map1x, self.map1y + 40, self.WHITE)
            self.draw_text("DRAGÃO", 20, self.map1x, self.map1y + 80, self.YELLOW)
            self.draw_text("pode ser impulsionado para cima de forma gradativa,", 20, self.map1x, self.map1y + 100, self.WHITE)
            self.draw_text("caindo lentamente pela ação da gravidade.", 20, self.map1x, self.map1y + 120, self.WHITE)
            self.draw_text("ORBE", 20, self.map1x, self.map1y + 160, self.YELLOW)
            self.draw_text("pode se mover abruptamente por alternância da gravidade,", 20, self.map1x, self.map1y + 180, self.WHITE)
            self.draw_text("quando em contato com a superfície.", 20, self.map1x, self.map1y + 200, self.WHITE)
            self.draw_text("LASER", 20, self.map1x, self.map1y + 240, self.YELLOW)
            self.draw_text("pode subir e descer rapidamente em ângulos mais", 20, self.map1x, self.map1y + 260, self.WHITE)
            self.draw_text("íngremes.", 20, self.map1x, self.map1y + 280, self.WHITE)
            pygame.display.update()
            self.checkinputs.reset_keys()
            pygame.display.flip()
    
    def check_input3(self):
        if self.checkinputs.BACK_KEY:
            self.checkinputs.curr_menu = self.checkinputs.main_menu
            self.run_display = False
