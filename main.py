from Extended_module import pg
import sys
import env
import numpy as np
import agent


pg.init()
pg.display.set_icon(pg.image.Splendor.logo)
pg.display.set_caption("VIS - Splendor")

pg.image.Splendor.scale("background", pg.image.Splendor.SCREEN_SIZE)
pg.image.Splendor.scale("normal_card", (100, 140))
pg.image.Splendor.scale("noble_card", (100, 100))
pg.image.Splendor.scale("stock", (50, 50))

screen = pg.display.set_mode(pg.image.Splendor.SCREEN_SIZE)
clock = pg.time.Clock()

list_stock_name = ["red", "blue", "green", "black", "white", "gold"]
[pg.image.Splendor.background.blit(pg.image.Splendor.stock[name], (830+106*list_stock_name.index(name), 30)) for name in list_stock_name]

pg.image.Splendor.scale("stock", (40, 40))
[pg.image.Splendor.background.blit(pg.image.Splendor.stock[name], (340+60*list_stock_name.index(name), 160)) for name in list_stock_name if name != "gold"]
[pg.image.Splendor.background.blit(pg.image.Splendor.stock[name], (340+60*list_stock_name.index(name), 300)) for name in list_stock_name]
[pg.image.Splendor.background.blit(pg.image.Splendor.stock[name], (340+60*list_stock_name.index(name), 440)) for name in list_stock_name if name != "gold"]

pg.image.Splendor.background.blit(pg.draw.multiline_text_surface("Player scores", rect_size=(300, 100),  font_size=30), (30, 40))
pg.image.Splendor.background.blit(pg.draw.multiline_text_surface("Tokens got", rect_size=(300, 100),  font_size=30), (30, 180))
pg.image.Splendor.background.blit(pg.draw.multiline_text_surface("Tokens", rect_size=(300, 100),  font_size=30), (30, 320))
pg.image.Splendor.background.blit(pg.draw.multiline_text_surface("Discount tokens", rect_size=(300, 100),  font_size=30), (30, 460))
pg.image.Splendor.background.blit(pg.draw.multiline_text_surface("Reserved cards", rect_size=(300, 100),  font_size=30), (30, 670))


# Class
class Sprite(pg.sprite.Sprite):
    def __init__(self, img, pos, align='center'):
        super().__init__()
        self.pos = pos
        self.align = align
        self.set_image(img)

    def set_image(self, img):
        self.image = img
        self.rect = img.get_rect()
        setattr(self.rect, self.align, self.pos)

    def set_value(self, new):
        rect_size = self.image.get_size()
        font_size = 30 if rect_size[0] == 40 else 35
        self.set_image(pg.draw.multiline_text_surface(str(new), rect_size=rect_size, font_size=font_size))


# Data
data = {}

"Thẻ thường"
for lv in range(1, 4):
    key = f"lv_{lv}.hide"
    data[key] = {
        "card_id": -1.0,
        "sprite": Sprite(pg.Surface(pg.image.Splendor.normal_card_size), (880, 210+160*(4-lv)))
    }

    for i in range(4):
        key = f"lv_{lv}.{i}"
        data[key] = {
            "card_id": -1.0,
            "sprite": Sprite(pg.Surface(pg.image.Splendor.normal_card_size), (1000+120*i, 210+160*(4-lv)))
        }

"3 Thẻ úp"
for i in range(3):
    key = f"reserved.{i}"
    data[key] = {
        "card_id": -1.0,
        "sprite": Sprite(pg.Surface(pg.image.Splendor.normal_card_size), (390+120*i, 690))
    }

"Thẻ noble"
for i in range(5):
    key = f"noble.{i}"
    data[key] = {
        "card_id": -1.0,
        "sprite": Sprite(pg.Surface(pg.image.Splendor.noble_card_size), (880+120*i, 210))
    }

"Nguyên liệu trên bàn chơi"
for name in list_stock_name:
    key = f"board_token.{name}"
    data[key] = {
        "num": 0,
        "sprite": Sprite(pg.Surface((50, 50)), (855+106*list_stock_name.index(name), 105), "center")
    }

"Nguyên liệu của người chơi"
for name in list_stock_name:
    key = f"player_token.{name}"
    data[key] = {
        "num": 0,
        "sprite": Sprite(pg.Surface((40, 40)), (360+60*list_stock_name.index(name), 360), "center")
    }

"Nguyên liệu vĩnh viễn của người chơi"
for name in list_stock_name:
    if name != "gold":
        key = f"discount.{name}"
        data[key] = {
        "num": 0,
        "sprite": Sprite(pg.Surface((40, 40)), (360+60*list_stock_name.index(name), 500), "center")
    }

"Nguyên liệu đã lấy trong turn của người chơi"
for name in list_stock_name:
    if name != "gold":
        key = f"got.{name}"
        data[key] = {
        "num": 0,
        "sprite": Sprite(pg.Surface((40, 40)), (360+60*list_stock_name.index(name), 220), "center")
    }

"Điểm của 4 người chơi"
for i in range(4):
    key = f"score.{i}"
    data[key] = {
        "num": 0,
        "sprite": Sprite(pg.Surface((50, 50)), (340+96*i, 40), "topleft")
    }


#
def draw_dashed_rectangles(screen, data, exclude_keys):
    for key in data.keys():
        if key not in exclude_keys:
            if key.startswith("lv_") or key.startswith("noble") or key.startswith("reserved"):
                if type(data[key]["card_id"]) == float:
                    pg.draw.dashed_rectangle(screen, data[key]["sprite"].rect)

            elif key.startswith("board_token") or key.startswith("got") or key.startswith("player_token") or key.startswith("discount") or key.startswith("score"):
                pg.draw.dashed_rectangle(screen, data[key]["sprite"].rect)


#
layer = pg.sprite.Group()
for key in data.keys():
    if key.startswith("board_token") or key.startswith("player_token") or key.startswith("got") or key.startswith("discount") or key.startswith("score"):
        layer.add(data[key]["sprite"])
        data[key]["sprite"].set_value(0)

#
screen.blit(pg.image.Splendor.background, (0, 0))
draw_dashed_rectangles(screen, data, [])
layer.draw(screen)
pg.display.flip()


#
def get_user_input(key, data, screen, layer):
    def sub_0():
        if len(user_txt) > 0:
            data[key]["num"] = int(user_txt)
            data[key]["sprite"].set_value(int(user_txt))
        layer.add(data[key]["sprite"])
        screen.blit(pg.image.Splendor.background, (0, 0))
        layer.draw(screen)
        draw_dashed_rectangles(screen, data, [])
        pg.display.flip()

    def sub_1():
        screen.blit(pg.image.Splendor.background, (0, 0))
        layer.draw(screen)
        draw_dashed_rectangles(screen, data, [key])
        pg.draw.rect(screen, (0, 0, 0), input_rect, 2)
        screen.blit(pg.draw.multiline_text_surface(user_txt, user_font_size, rect_size=(input_rect.width, input_rect.height)), input_rect.topleft)
        pg.display.flip()

    if key.startswith("board_token") or key.startswith("player_token") or key.startswith("got") or key.startswith("discount") or key.startswith("score"):
        layer.remove(data[key]["sprite"])
        input_rect = data[key]["sprite"].rect.copy()
        input_rect.left -= 10
        input_rect.width += 20
        user_txt = ""
        user_font_size = 30 if data[key]["sprite"].image.get_size()[0] == 40 else 35
        max_len = 2 if key.startswith("score") else 1

        screen.blit(pg.image.Splendor.background, (0, 0))
        layer.draw(screen)
        draw_dashed_rectangles(screen, data, [key])
        pg.draw.rect(screen, (0, 0, 0), input_rect, 2)
        pg.display.flip()

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_BACKSPACE:
                        if len(user_txt) > 0:
                            user_txt = user_txt[:-1]
                            sub_1()
                    elif event.key in [getattr(pg, f"K_{i}") for i in range(10)] + [getattr(pg, f"K_KP{i}") for i in range(10)]:
                        if len(user_txt) < max_len:
                            user_txt += event.unicode
                            sub_1()
                            if len(user_txt) == max_len:
                                sub_0()
                                return
                    elif event.key == pg.K_KP_ENTER or event.key == pg.K_RETURN:
                        sub_0()
                        return
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        sub_0()
                        return

    elif key.startswith("noble"):
        layer.remove(data[key]["sprite"])
        input_rect = pg.Surface((700, 790))
        list_pos = []
        for i in range(10):
            a = i // 5
            b = i % 5
            list_pos.append((30+140*b, 30+140*a))

        screen.blit(pg.image.Splendor.background, (0, 0))
        layer.draw(screen)
        draw_dashed_rectangles(screen, data, [key])
        screen.blit(input_rect, (10, 10))
        for i in range(10):
            screen.blit(pg.image.Splendor.noble_card[i], list_pos[i])
        pg.display.flip()

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_pos = pg.mouse.get_pos()
                        pick = -1.0
                        for i in range(10):
                            pos = list_pos[i]
                            if pg.Rect(pos[0], pos[1], 100, 100).collidepoint(mouse_pos):
                                pick = i
                                break

                        data[key]["card_id"] = pick

                        if pick == -1.0:
                            data[key]["sprite"].image.fill((0, 0, 0))
                            layer.remove(data[key]["sprite"])
                        else:
                            data[key]["sprite"].set_image(pg.image.Splendor.noble_card[pick].copy())
                            layer.add(data[key]["sprite"])

                        screen.blit(pg.image.Splendor.background, (0, 0))
                        layer.draw(screen)
                        draw_dashed_rectangles(screen, data, [])
                        pg.display.flip()
                        return

    elif key.startswith("lv_"):
        if key.endswith(".hide"):
            if data[key]["card_id"] == -1.0:
                data[key]["card_id"] = 1
                data[key]["sprite"].set_image(pg.image.Splendor.hidden_card[int(key[3])].copy())
                layer.add(data[key]["sprite"])
            else:
                data[key]["card_id"] = -1.0
                data[key]["sprite"].image.fill((0, 0, 0))
                layer.remove(data[key]["sprite"])

            screen.blit(pg.image.Splendor.background, (0, 0))
            layer.draw(screen)
            draw_dashed_rectangles(screen, data, [])
            pg.display.flip()

        else:
            layer.remove(data[key]["sprite"])
            if key.startswith("lv_1"):
                input_rect = pg.Surface((935, 790))
                k = 8
                num_card = 40
                start = 0
                _start = 25
            elif key.startswith("lv_2"):
                input_rect = pg.Surface((705, 790))
                k = 6
                num_card = 30
                start = 40
                _start = 255
            elif key.startswith("lv_3"):
                input_rect = pg.Surface((475, 790))
                k = 4
                num_card = 20
                start = 70
                _start = 485

            list_pos = []
            for i in range(num_card):
                a = i // k
                b = i % k
                list_pos.append((_start+115*b, 25+155*a))

            screen.blit(pg.image.Splendor.background, (0, 0))
            layer.draw(screen)
            draw_dashed_rectangles(screen, data, [key])
            screen.blit(input_rect, (_start-15, 10))
            for i in range(num_card):
                screen.blit(pg.image.Splendor.normal_card[i+start], list_pos[i])
            pg.display.flip()

            while True:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        sys.exit()

                    if event.type == pg.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            mouse_pos = pg.mouse.get_pos()
                            pick = -1.0
                            for i in range(num_card):
                                pos = list_pos[i]
                                if pg.Rect(pos[0], pos[1], 100, 140).collidepoint(mouse_pos):
                                    pick = i
                                    break

                            data[key]["card_id"] = pick + start

                            if pick == -1.0:
                                data[key]["card_id"] = -1.0
                                data[key]["sprite"].image.fill((0, 0, 0))
                                layer.remove(data[key]["sprite"])
                            else:
                                data[key]["sprite"].set_image(pg.image.Splendor.normal_card[pick+start].copy())
                                layer.add(data[key]["sprite"])

                            screen.blit(pg.image.Splendor.background, (0, 0))
                            layer.draw(screen)
                            draw_dashed_rectangles(screen, data, [])
                            pg.display.flip()
                            return

    elif key.startswith("reserved"):
        layer.remove(data[key]["sprite"])
        input_rect = pg.Surface((500, 240))
        input_rect.fill((255, 255, 255))
        list_pos = []
        for i in range(3):
            list_pos.append((310+150*i, 410))

        screen.blit(pg.image.Splendor.background, (0, 0))
        layer.draw(screen)
        draw_dashed_rectangles(screen, data, [key])
        screen.blit(input_rect, (260, 360))
        for i in range(3):
            screen.blit(pg.image.Splendor.hidden_card[i+1], list_pos[i])
        pg.display.flip()

        is_running = True
        while is_running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_pos = pg.mouse.get_pos()
                        lv_pick = 0
                        for i in range(3):
                            pos = list_pos[i]
                            if pg.Rect(pos[0], pos[1], 100, 140).collidepoint(mouse_pos):
                                lv_pick = i + 1
                                break
                        
                        is_running = False
        
        if lv_pick != 0:
            if lv_pick == 1:
                input_rect = pg.Surface((935, 790))
                k = 8
                num_card = 40
                start = 0
                _start = 25
            elif lv_pick == 2:
                input_rect = pg.Surface((705, 790))
                k = 6
                num_card = 30
                start = 40
                _start = 255
            elif lv_pick == 3:
                input_rect = pg.Surface((475, 790))
                k = 4
                num_card = 20
                start = 70
                _start = 485
            
            list_pos = []
            for i in range(num_card):
                a = i // k
                b = i % k
                list_pos.append((_start+115*b, 25+155*a))
            
            screen.blit(pg.image.Splendor.background, (0, 0))
            layer.draw(screen)
            draw_dashed_rectangles(screen, data, [key])
            screen.blit(input_rect, (_start-15, 10))
            for i in range(num_card):
                screen.blit(pg.image.Splendor.normal_card[i+start], list_pos[i])
            pg.display.flip()

            while True:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        sys.exit()
                    
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            mouse_pos = pg.mouse.get_pos()
                            pick = -1.0
                            for i in range(num_card):
                                pos = list_pos[i]
                                if pg.Rect(pos[0], pos[1], 100, 140).collidepoint(mouse_pos):
                                    pick = i
                                    break
                            
                            data[key]["card_id"] = pick + start

                            if pick == -1.0:
                                data[key]["card_id"] = -1.0
                                data[key]["sprite"].image.fill((0, 0, 0))
                                layer.remove(data[key]["sprite"])
                            else:
                                data[key]["sprite"].set_image(pg.image.Splendor.normal_card[pick+start].copy())
                                layer.add(data[key]["sprite"])
                            
                            screen.blit(pg.image.Splendor.background, (0, 0))
                            layer.draw(screen)
                            draw_dashed_rectangles(screen, data, [])
                            pg.display.flip()
                            return
        
        else:
            data[key]["card_id"] = -1.0
            data[key]["sprite"].image.fill((0, 0, 0))
            layer.remove(data[key]["sprite"])
            screen.blit(pg.image.Splendor.background, (0, 0))
            layer.draw(screen)
            draw_dashed_rectangles(screen, data, [])
            pg.display.flip()
            return


#
def convert_data_to_state(data):
    b_infor = np.zeros(6)
    for i in range(6):
        name = list_stock_name[i]
        b_infor[i] = data[f"board_token.{name}"]["num"]
    
    p_infor = np.zeros(12)
    "Tokens"
    for i in range(6):
        name = list_stock_name[i]
        p_infor[i] = data[f"player_token.{name}"]["num"]
    
    "Discount"
    for i in range(5):
        name = list_stock_name[i]
        p_infor[i+6] = data[f"discount.{name}"]["num"]
    
    "Score"
    p_infor[11] = data["score.0"]["num"]

    # Thẻ mở trên bàn
    list_open_card = []
    for lv in range(1, 4):
        for i in range(4):
            key = f"lv_{lv}.{i}"
            if data[key]["card_id"] != -1.0:
                list_open_card.append(data[key]["card_id"])
    
    state_normal_card = np.zeros(84)
    list_open_card.sort()
    temp = env.normal_cards_infor[list_open_card].flatten()
    state_normal_card[:len(temp)] = temp

    # Thẻ noble
    list_open_noble = []
    for i in range(5):
        key = f"noble.{i}"
        if data[key]["card_id"] != -1.0:
            list_open_noble.append(data[key]["card_id"])
    
    state_noble_card = np.zeros(25)
    list_open_noble.sort()
    temp = env.noble_cards_infor[list_open_noble].flatten()
    state_noble_card[:len(temp)] = temp

    # Thẻ úp
    list_reserved = []
    for i in range(3):
        key = f"reserved.{i}"
        if data[key]["card_id"] != -1.0:
            list_reserved.append(data[key]["card_id"])
    
    state_reserved_card = np.zeros(21)
    list_reserved.sort()
    temp = env.normal_cards_infor[list_reserved].flatten()
    state_reserved_card[:len(temp)] = temp

    # Nguyên liệu đã lấy trong turn
    token_got = np.zeros(5)
    for i in range(5):
        name = list_stock_name[i]
        token_got[i] = data[f"got.{name}"]["num"]
    
    # Điểm của người chơi khác
    other_p_score = np.zeros(3)
    for i in range(1, 4):
        other_p_score[i-1] = data[f"score.{i}"]["num"]
    
    # Thẻ ẩn có thể úp
    hidden_card = np.zeros(3)
    for i in range(1, 4):
        if data[f"lv_{i}.hide"]["card_id"] != -1:
            hidden_card[i-1] = 1
    
    #
    p_state = np.append(b_infor, p_infor)
    p_state = np.append(p_state, state_normal_card)
    p_state = np.append(p_state, state_noble_card)
    p_state = np.append(p_state, state_reserved_card)

    p_state = np.append(p_state, token_got)
    p_state = np.append(p_state, other_p_score)
    p_state = np.append(p_state, hidden_card)
    p_state = np.append(p_state, [len(list_open_card)])

    p_state = np.append(p_state, [0])
    
    return p_state

#
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pg.mouse.get_pos()
                for key in data.keys():
                    if data[key]["sprite"].rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                        get_user_input(key, data, screen, layer)
                        print(key, data[key])
                        break
                else:
                    print(mouse_pos)
        
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_KP_ENTER or event.key == pg.K_RETURN:
                p_state = convert_data_to_state(data)
                try:
                    action, agent.perfile = agent.test(p_state, agent.perfile)
                    print(f"Action: {action}: ", end="")
                    if action == 0:
                        print("Bỏ lượt")
                    elif action >= 1 and action <= 12:
                        print("Mở thẻ trên bàn có thông tin như sau:", p_state[11+7*action:18+7*action].astype(int))
                    elif action >= 13 and action <= 15:
                        print("Mở thẻ đang giữ có thông tin như sau:", p_state[127+7*(action-13):134+7*(action-13)].astype(int))
                    elif action >= 16 and action <= 27:
                        print("Úp thẻ trên bàn có thông tin như sau:", p_state[18+7*(action-16):25+7*(action-16)].astype(int))
                    elif action >= 28 and action <= 30:
                        print("Úp thẻ ẩn cấp ", action-27)
                    elif action >= 31 and action <= 35:
                        print("Lấy nguyên liệu", list_stock_name[action-31])
                    elif action >= 36 and action <= 41:
                        print("Trả nguyên liệu", list_stock_name[action-36])
                    else:
                        raise Exception("Action không hợp lệ.")
                except:
                    print("\nCó vẻ như state không hợp lệ, hàm getValidActions đang không thẻ render ra action nào.\n")
    clock.tick(60)
