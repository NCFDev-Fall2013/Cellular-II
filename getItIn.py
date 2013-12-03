import pygame, sys, threading
from pygame.locals import *

class Innie(object):

    def __init__(self, x, y, surface, maxChars, font):
        self.x = x
        self.y = y
        self.surf = surface
        rect = pygame.Rect(int(surface.get_width()/2), int(surface.get_height()/2), int(surface.get_width()/2), int(surface.get_height()/5))
        self.bound = rect
        self.scribe = self.bound.copy()
        #self.scribe.inflate_ip(x+0.1, y-0.1)
        self.stop = maxChars
        self.font = font
        self.value = ''
        self.boogie = pygame.Surface((self.scribe.width,self.scribe.height))
        self.shifted = False
        self.restricted = ('1','2','3','4','5','6','7','8','9','0')
        self.updateBool = False
        
    def upSelf(self,event):
        print "value is " + self.value
        pygame.draw.rect(self.surf,(0,0,255),self.bound, 5)
        #pygame.draw.rect(self.surf,(0,0,0),self.scribe, 0)
        self.surf.blit(self.font.render(self.value, True, (255,0,0)),(self.x,self.y))
        self.upText(event)

    def selfUpped(self, event):
        print "value is " + self.value
        oldVal = self.value
        self.upText(event)
        boo = pygame.Surface((int(self.bound.width),int(self.bound.height)))
        boo.fill((0,0,0))
        boo2 = self.font.render(self.value, True, (255,0,0))
        #boo2 = pygame.Surface((int(self.bound.width),int(self.bound.height)))
        #boo2.fill((0,0,255))
        #boo3 = pygame.Surface((int(self.scribe.width),int(self.scribe.height)))
        #boo3.fill((0,0,0))
        boo.blit(boo2,(0,0))
        #boo.blit(boo3,(int(self.surf.get_width()/2), int(self.surf.get_height()/2)))
        #pygame.draw.rect(self.surf,(0,0,255),self.scribe, 5)
        #pygame.draw.rect(self.surf,(0,0,0),self.bound, 0)
        if oldVal != self.value:
            self.updateBool = True
        return boo
 
    def upText(self,event):
        """ Update the input based on passed events """
        print "event is ", event
        if event.type == KEYUP:
            if event.key == K_LSHIFT or event.key == K_RSHIFT: self.shifted = False
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE: self.value = self.value[:-1]
            elif event.key == K_LSHIFT or event.key == K_RSHIFT: self.shifted = True
            elif event.key == K_SPACE: self.value += ' '
            if not self.shifted:
                if event.key == K_a and 'a' in self.restricted: self.value += 'a'
                elif event.key == K_b and 'b' in self.restricted: self.value += 'b'
                elif event.key == K_c and 'c' in self.restricted: self.value += 'c'
                elif event.key == K_d and 'd' in self.restricted: self.value += 'd'
                elif event.key == K_e and 'e' in self.restricted: self.value += 'e'
                elif event.key == K_f and 'f' in self.restricted: self.value += 'f'
                elif event.key == K_g and 'g' in self.restricted: self.value += 'g'
                elif event.key == K_h and 'h' in self.restricted: self.value += 'h'
                elif event.key == K_i and 'i' in self.restricted: self.value += 'i'
                elif event.key == K_j and 'j' in self.restricted: self.value += 'j'
                elif event.key == K_k and 'k' in self.restricted: self.value += 'k'
                elif event.key == K_l and 'l' in self.restricted: self.value += 'l'
                elif event.key == K_m and 'm' in self.restricted: self.value += 'm'
                elif event.key == K_n and 'n' in self.restricted: self.value += 'n'
                elif event.key == K_o and 'o' in self.restricted: self.value += 'o'
                elif event.key == K_p and 'p' in self.restricted: self.value += 'p'
                elif event.key == K_q and 'q' in self.restricted: self.value += 'q'
                elif event.key == K_r and 'r' in self.restricted: self.value += 'r'
                elif event.key == K_s and 's' in self.restricted: self.value += 's'
                elif event.key == K_t and 't' in self.restricted: self.value += 't'
                elif event.key == K_u and 'u' in self.restricted: self.value += 'u'
                elif event.key == K_v and 'v' in self.restricted: self.value += 'v'
                elif event.key == K_w and 'w' in self.restricted: self.value += 'w'
                elif event.key == K_x and 'x' in self.restricted: self.value += 'x'
                elif event.key == K_y and 'y' in self.restricted: self.value += 'y'
                elif event.key == K_z and 'z' in self.restricted: self.value += 'z'
                elif event.key == K_0 and '0' in self.restricted: self.value += '0'
                elif event.key == K_1 and '1' in self.restricted: self.value += '1'
                elif event.key == K_2 and '2' in self.restricted: self.value += '2'
                elif event.key == K_3 and '3' in self.restricted: self.value += '3'
                elif event.key == K_4 and '4' in self.restricted: self.value += '4'
                elif event.key == K_5 and '5' in self.restricted: self.value += '5'
                elif event.key == K_6 and '6' in self.restricted: self.value += '6'
                elif event.key == K_7 and '7' in self.restricted: self.value += '7'
                elif event.key == K_8 and '8' in self.restricted: self.value += '8'
                elif event.key == K_9 and '9' in self.restricted: self.value += '9'
                elif event.key == K_BACKQUOTE and '`' in self.restricted: self.value += '`'
                elif event.key == K_MINUS and '-' in self.restricted: self.value += '-'
                elif event.key == K_EQUALS and '=' in self.restricted: self.value += '='
                elif event.key == K_LEFTBRACKET and '[' in self.restricted: self.value += '['
                elif event.key == K_RIGHTBRACKET and ']' in self.restricted: self.value += ']'
                elif event.key == K_BACKSLASH and '\\' in self.restricted: self.value += '\\'
                elif event.key == K_SEMICOLON and ';' in self.restricted: self.value += ';'
                elif event.key == K_QUOTE and '\'' in self.restricted: self.value += '\''
                elif event.key == K_COMMA and ',' in self.restricted: self.value += ','
                elif event.key == K_PERIOD and '.' in self.restricted: self.value += '.'
                elif event.key == K_SLASH and '/' in self.restricted: self.value += '/'
            elif self.shifted:
                if event.key == K_a and 'A' in self.restricted: self.value += 'A'
                elif event.key == K_b and 'B' in self.restricted: self.value += 'B'
                elif event.key == K_c and 'C' in self.restricted: self.value += 'C'
                elif event.key == K_d and 'D' in self.restricted: self.value += 'D'
                elif event.key == K_e and 'E' in self.restricted: self.value += 'E'
                elif event.key == K_f and 'F' in self.restricted: self.value += 'F'
                elif event.key == K_g and 'G' in self.restricted: self.value += 'G'
                elif event.key == K_h and 'H' in self.restricted: self.value += 'H'
                elif event.key == K_i and 'I' in self.restricted: self.value += 'I'
                elif event.key == K_j and 'J' in self.restricted: self.value += 'J'
                elif event.key == K_k and 'K' in self.restricted: self.value += 'K'
                elif event.key == K_l and 'L' in self.restricted: self.value += 'L'
                elif event.key == K_m and 'M' in self.restricted: self.value += 'M'
                elif event.key == K_n and 'N' in self.restricted: self.value += 'N'
                elif event.key == K_o and 'O' in self.restricted: self.value += 'O'
                elif event.key == K_p and 'P' in self.restricted: self.value += 'P'
                elif event.key == K_q and 'Q' in self.restricted: self.value += 'Q'
                elif event.key == K_r and 'R' in self.restricted: self.value += 'R'
                elif event.key == K_s and 'S' in self.restricted: self.value += 'S'
                elif event.key == K_t and 'T' in self.restricted: self.value += 'T'
                elif event.key == K_u and 'U' in self.restricted: self.value += 'U'
                elif event.key == K_v and 'V' in self.restricted: self.value += 'V'
                elif event.key == K_w and 'W' in self.restricted: self.value += 'W'
                elif event.key == K_x and 'X' in self.restricted: self.value += 'X'
                elif event.key == K_y and 'Y' in self.restricted: self.value += 'Y'
                elif event.key == K_z and 'Z' in self.restricted: self.value += 'Z'
                elif event.key == K_0 and ')' in self.restricted: self.value += ')'
                elif event.key == K_1 and '!' in self.restricted: self.value += '!'
                elif event.key == K_2 and '@' in self.restricted: self.value += '@'
                elif event.key == K_3 and '#' in self.restricted: self.value += '#'
                elif event.key == K_4 and '$' in self.restricted: self.value += '$'
                elif event.key == K_5 and '%' in self.restricted: self.value += '%'
                elif event.key == K_6 and '^' in self.restricted: self.value += '^'
                elif event.key == K_7 and '&' in self.restricted: self.value += '&'
                elif event.key == K_8 and '*' in self.restricted: self.value += '*'
                elif event.key == K_9 and '(' in self.restricted: self.value += '('
                elif event.key == K_BACKQUOTE and '~' in self.restricted: self.value += '~'
                elif event.key == K_MINUS and '_' in self.restricted: self.value += '_'
                elif event.key == K_EQUALS and '+' in self.restricted: self.value += '+'
                elif event.key == K_LEFTBRACKET and '{' in self.restricted: self.value += '{'
                elif event.key == K_RIGHTBRACKET and '}' in self.restricted: self.value += '}'
                elif event.key == K_BACKSLASH and '|' in self.restricted: self.value += '|'
                elif event.key == K_SEMICOLON and ':' in self.restricted: self.value += ':'
                elif event.key == K_QUOTE and '"' in self.restricted: self.value += '"'
                elif event.key == K_COMMA and '<' in self.restricted: self.value += '<'
                elif event.key == K_PERIOD and '>' in self.restricted: self.value += '>'
                elif event.key == K_SLASH and '?' in self.restricted: self.value += '?'

        if len(self.value) > self.stop and self.stop >= 0: self.value = self.value[:-1]
        
