import pygame as __pg


SCREEN_SIZE = (1440, 810)

background = __pg.image.load("Extended_module/Imgs/background.png")
logo = __pg.image.load("Extended_module/Imgs/logo.jpg")

normal_card = [__pg.image.load("Extended_module/Imgs/Cards"+f"/{i}.png") for i in range(90)]
normal_card_size = normal_card[0].get_size()

noble_card = [__pg.image.load("Extended_module/Imgs/Cards"+f"/{i+90}.png") for i in range(10)]
noble_card_size = noble_card[0].get_size()

hidden_card = {
    i: __pg.image.load("Extended_module/Imgs/Cards"+f"/hide_card_{i}.png") for i in range(1, 4)
}

stock = {
    key: __pg.image.load("Extended_module/Imgs"+f"/{key}.png") for key in ["red", "blue", "green", "black", "white", "gold"]
}

def scale(name, size):
    global background
    global normal_card_size
    global noble_card_size

    if name == "background":
        background = __pg.transform.smoothscale(background, size)
    elif name == "normal_card":
        for i in range(len(normal_card)):
            normal_card[i] = __pg.transform.smoothscale(normal_card[i], size)
        for key in hidden_card.keys():
            hidden_card[key] = __pg.transform.smoothscale(hidden_card[key], size)
        normal_card_size = normal_card[0].get_size()
    elif name == "noble_card":
        for i in range(len(noble_card)):
            noble_card[i] = __pg.transform.smoothscale(noble_card[i], size)
        noble_card_size = noble_card[0].get_size()
    elif name == "stock":
        for key in stock.keys():
            stock[key] = __pg.transform.smoothscale(stock[key], size)
    else:
        raise Exception(".")
