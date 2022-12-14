from pygame.draw import *
import pygame as __pg
import numpy as __np


__circle_cache = {}
def __circlepoints(r):
    r = int(round(r))
    if r in __circle_cache:
        return __circle_cache[r]

    x, y, e = r, 0, 1 - r
    __circle_cache[r] = points = []
    while x >= y:
        points.append((x, y))
        y += 1
        if e < 0:
            e += 2 * y - 1
        else:
            x -= 1
            e += 2 * (y - x) - 1

    points += [(y, x) for x, y in points if x > y]
    points += [(-x, y) for x, y in points if x]
    points += [(x, -y) for x, y in points if y]
    points.sort()
    return points


def __render_outline(text, font, font_color):
    o_color = (255-font_color[0], 255-font_color[1], 255-font_color[2])
    opx = 1
    
    text_surface = font.render(text, True, font_color).convert_alpha()
    w = text_surface.get_width() + 2*opx
    h = font.get_height()
    o_surf = __pg.Surface((w, h+2*opx)).convert_alpha()
    o_surf.fill((0, 0, 0, 0))
    surf = o_surf.copy()
    o_surf.blit(font.render(text, True, o_color).convert_alpha(), (0, 0))
    for dx, dy in __circlepoints(opx):
        surf.blit(o_surf, (dx+opx, dy+opx))

    surf.blit(text_surface, (opx, opx))
    return surf


class __TextRectException:
    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        return self.message


def multiline_text_surface(text, font_size=25, font_color=(0, 0, 0), rect_size=(40, 40), align='center'):
    rect = __pg.rect.Rect(0, 0, rect_size[0], rect_size[1])
    font = __pg.font.Font('freesansbold.ttf', font_size)
    final_lines = []
    requested_lines = text.splitlines()
    for requested_line in requested_lines:
        if font.size(requested_line)[0] > rect.width:
            words = requested_line.split(' ')
            for word in words:
                if font.size(word)[0] >= rect.width:
                    raise __TextRectException(
                        "The word " + word + " is too long to fit in the rect passed.")

            accumulated_line = ""
            for word in words:
                test_line = accumulated_line + word + " "
                # Build the line while the words fit.
                if font.size(test_line)[0] < rect.width:
                    accumulated_line = test_line
                else:
                    final_lines.append(accumulated_line)
                    accumulated_line = word + " "

            final_lines.append(accumulated_line)
        else:
            final_lines.append(requested_line)

    surface = __pg.Surface(rect.size, __pg.SRCALPHA, 32)
    surface = surface.convert_alpha()
    accumulated_height = 0
    for line in final_lines:
        if accumulated_height + font.size(line)[1] >= rect.height:
            raise __TextRectException(
                "Once word-wrapped, the text string was too tall to fit in the rect.")
        if line != "":
            temp_surface = __render_outline(line, font, font_color)
        if align == 'left':
            surface.blit(temp_surface, (0, accumulated_height))
        elif align == 'center':
            surface.blit(
                temp_surface, ((rect.width - temp_surface.get_width()) / 2, accumulated_height))
        elif align == 'right':
            surface.blit(temp_surface, (rect.width -
                         temp_surface.get_width(), accumulated_height))
        else:
            raise __TextRectException("Invalid align argument: " + str(align))

        accumulated_height += font.size(line)[1]

    return surface


def __dashed_line(surf, start_pos, end_pos, color=(0, 0, 0), width=1, dash_length=3, exclude_corners = False):
    start_pos = __np.array(start_pos)
    end_pos = __np.array(end_pos)

    length = __np.linalg.norm(end_pos - start_pos)
    dash_amount = int(length / dash_length)

    dash_knots = __np.array([__np.linspace(start_pos[i], end_pos[i], dash_amount) for i in range(2)]).transpose()
    for n in range(int(exclude_corners), dash_amount - int(exclude_corners), 2):
        if n < dash_amount - 1:
            line(surf, color, tuple(dash_knots[n]), tuple(dash_knots[n+1]), width)


def dashed_rectangle(surf, rect, color=(0, 0, 0), width=1, dash_length=3, exclude_corners = False):
    __dashed_line(surf, rect.topleft, rect.topright, color, width, dash_length, exclude_corners)
    __dashed_line(surf, rect.topright, rect.bottomright, color, width, dash_length, exclude_corners)
    __dashed_line(surf, rect.bottomright, rect.bottomleft, color, width, dash_length, exclude_corners)
    __dashed_line(surf, rect.bottomleft, rect.topleft, color, width, dash_length, exclude_corners)
