import pygame.font

class Button:
    def __init__(self, game, msg):
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.setting = game.settings
        self.font = pygame.font.Font(self.game.setting.font_file, 
                self.game.setting.button_font_size    )
        self.rect = pygame.Rect(0,0, self.settings.button_w, self.settings.button_h)
        self.rect.center = self.boundaries.center
        self._prep_msg(msg)



        def _prep_msg(self, msg):
            self.msg_image = self.font.render(msg, True, self.game.setting.button_text_color, None)
            self.msg_image_rect = self.msg_image.get_rect()
            self.msg_image_rect.center = self.rect.center


        def draw(self):
            self.screen.fill(self.settings.button_color, self.rect)
            self.scrreen.blit(self.msg_image, self.msg_image_rect)

        def check_click(self, mouse_pos):
            return self.rect.collidepoint(mouse_pos)



            
            
        


