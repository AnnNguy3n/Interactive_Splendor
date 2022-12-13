import numpy as np

normal_cards_infor = np.array([[0, 2, 2, 2, 0, 0, 0], [0, 2, 3, 0, 0, 0, 0], [0, 2, 1, 1, 0, 2, 1], [0, 2, 0, 1, 0, 0, 2], [0, 2, 0, 3, 1, 0, 1], [0, 2, 1, 1, 0, 1, 1], [1, 2, 0, 0, 0, 4, 0], [0, 2, 2, 1, 0, 2, 0], [0, 1, 2, 0, 2, 0, 1], [0, 1, 0, 0, 2, 2, 0], [0, 1, 1, 0, 1, 1, 1], [0, 1, 2, 0, 1, 1, 1], [0, 1, 1, 1, 3, 0, 0], [0, 1, 0, 0, 0, 2, 1], [0, 1, 0, 0, 0, 3, 0], [1, 1, 4, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 4], [0, 0, 0, 0, 0, 0, 3], [0, 0, 0, 1, 1, 1, 2], [0, 0, 0, 0, 1, 2, 2], [0, 0, 1, 0, 0, 3, 1], [0, 0, 2, 0, 0, 0, 2], [0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 2, 1, 0, 0], [0, 4, 0, 2, 2, 1, 0], [0, 4, 1, 1, 2, 1, 0], [0, 4, 0, 1, 0, 1, 3], [1, 4, 0, 0, 4, 0, 0], [0, 4, 0, 2, 0, 2, 0], [0, 4, 2, 0, 0, 1, 0], [0, 4, 1, 1, 1, 1, 0], [0, 4, 0, 3, 0, 0, 0], [0, 3, 1, 0, 2, 0, 0], [0, 3, 1, 1, 1, 0, 1], [1, 3, 0, 4, 0, 0, 0], [0, 3, 1, 2, 0, 0, 2], [0, 3, 0, 0, 3, 0, 0], [0, 3, 0, 0, 2, 0, 2], [0, 3, 3, 0, 1, 1, 0], [0, 3, 1, 2, 1, 0, 1], [1, 2, 0, 3, 0, 2, 2], [2, 2, 0, 2, 0, 1, 4], [1, 2, 3, 0, 2, 0, 3], [2, 2, 0, 5, 3, 0, 0], [2, 2, 0, 0, 5, 0, 0], [3, 2, 0, 0, 6, 0, 0], [3, 1, 0, 6, 0, 0, 0], [2, 1, 1, 0, 0, 4, 2], [2, 1, 0, 5, 0, 0, 0], [2, 1, 0, 3, 0, 0, 5], [1, 1, 0, 2, 3, 3, 0], [1, 1, 3, 2, 2, 0, 0], [3, 0, 6, 0, 0, 0, 0], [2, 0, 0, 0, 0, 5, 3], [2, 0, 0, 0, 0, 5, 0], [2, 0, 0, 4, 2, 0, 1], [1, 0, 2, 3, 0, 3, 0], [1, 0, 2, 0, 0, 3, 2], [3, 4, 0, 0, 0, 0, 6], [2, 4, 5, 0, 0, 3, 0], [2, 4, 5, 0, 0, 0, 0], [1, 4, 3, 3, 0, 0, 2], [1, 4, 2, 0, 3, 2, 0], [2, 4, 4, 0, 1, 2, 0], [1, 3, 0, 2, 2, 0, 3], [1, 3, 0, 0, 3, 2, 3], [2, 3, 2, 1, 4, 0, 0], [2, 3, 3, 0, 5, 0, 0], [2, 3, 0, 0, 0, 0, 5], [3, 3, 0, 0, 0, 6, 0], [4, 2, 0, 7, 0, 0, 0], [4, 2, 0, 6, 3, 0, 3], [5, 2, 0, 7, 3, 0, 0], [3, 2, 3, 3, 0, 3, 5], [3, 1, 3, 0, 3, 5, 3], [4, 1, 0, 0, 0, 0, 7], [5, 1, 0, 3, 0, 0, 7], [4, 1, 0, 3, 0, 3, 6], [3, 0, 0, 5, 3, 3, 3], [4, 0, 0, 0, 7, 0, 0], [5, 0, 3, 0, 7, 0, 0], [4, 0, 3, 3, 6, 0, 0], [5, 4, 0, 0, 0, 7, 3], [3, 4, 5, 3, 3, 3, 0], [4, 4, 0, 0, 0, 7, 0], [4, 4, 3, 0, 0, 6, 3], [3, 3, 3, 3, 5, 0, 3], [5, 3, 7, 0, 0, 3, 0], [4, 3, 6, 0, 3, 3, 0], [4, 3, 7, 0, 0, 0, 0]])
noble_cards_infor = np.array([[0, 4, 4, 0, 0], [3, 0, 3, 3, 0], [3, 3, 3, 0, 0], [3, 0, 0, 3, 3], [0, 3, 0, 3, 3], [4, 0, 4, 0, 0], [4, 0, 0, 4, 0], [0, 3, 3, 0, 3], [0, 4, 0, 0, 4], [0, 0, 0, 4, 4]])

def getValidActions(player_state_origin:np.int64):
    list_action_return = np.zeros(42)
    p_state = player_state_origin.copy()
    p_state = p_state.astype(np.int64)
    b_stocks = p_state[:6] #Các nguyên liệu trên bàn chơi
    p_st = p_state[6:11] #Các nguyên liệu của bản thân đang có
    yellow_count = p_state[11] #Số thẻ vàng đang có
    normal_cards = p_state[18:102] #Thông tin 12 thẻ đang mở
    p_upside_down_card =  p_state[127:148] #thông tin 3 thẻ đang úp
    taken = p_state[148: 153] #các nguyên liệu đã lấy trong turn
    p_count_st = p_state[12:17] #Nguyên liệu mặc định của người chơi
    list_action_return[0] = 1
    check_action_0 = False
    #Trả nguyên liệu
    p_st_have_auto = p_state[6:12]
    sum_p_st_have_auto = sum(p_st_have_auto)
    if sum_p_st_have_auto > 10:
        list_action_return_stock = [i_+36 for i_ in range(6) if p_st_have_auto[i_] != 0]
        # list_action = np.array(list_action_return_stock)
        list_action_return[0] = 0
        list_action_return[np.array(list_action_return_stock)] = 1
        return list_action_return

    #Lấy nguyên liệu
    s_taken = np.sum(taken)
    temp_ = [i_ + 31 for i_ in range(5) if b_stocks[i_] != 0]
    if s_taken == 1:
        s_ = np.where(taken==1)[0][0]
        if b_stocks[s_] < 3: # Có thể lấy double
            if (s_+ 31) in temp_:
                temp_.remove(s_ + 31) #Xóa action đã lấy ở file temp nếu nguyên liệu không trên 4
        list_action_return[np.array(temp_)] = 1
        check_action_0 = True
    elif s_taken == 2:
        lst_s_ = np.where(taken==1)[0]
        for s_ in lst_s_:
            if (s_+31) in temp_:
                temp_.remove(s_+31)
        list_action_return[np.array(temp_)] = 1
        check_action_0 = True
    elif s_taken == 0:
        if len(temp_) > 0:
            # list_action_return[0] = 0
            list_action_return[np.array(temp_)] = 1   
    if s_taken > 0:
        return list_action_return

    # Kiểm tra 15 thẻ có thể mở, action từ [1:16]
    for id_card in range(12):
        card = normal_cards[7*id_card: 7+7*id_card]
        if sum(card) > 0:
            card_need = p_st + p_count_st - card[-5:]
            if -sum(card_need[np.where(card_need < 0)]) <= yellow_count: #(x*x>0)
                list_action_return[id_card+1] = 1
    for id_card in range(3):
        card = p_upside_down_card[7*id_card: 7+7*id_card]
        if sum(card) > 0:
            card_need = p_st + p_count_st -card[-5:]
            if -sum(card_need[np.where(card_need < 0)]) <= yellow_count:
                list_action_return[id_card+13] = 1
    count_upside_down = 0
    for id_card in range(3):
        card_upside_down = p_upside_down_card[7*id_card:7+7*id_card]
        if sum(card_upside_down) > 0:
            count_upside_down += 1
        else:
            break
    if count_upside_down < 3: # Nếu chưa có đủ 3 thẻ úp thì có thể úp thêm một thẻ
        list_action_upside_down = np.array([i+16 for i in range(0, p_state[159])])
        list_action_return[list_action_upside_down] = 1
        list_card_hide = np.where(p_state[156:159] == 1)[0] + 28
        list_action_return[list_card_hide] = 1
        
    if check_action_0 == False and np.sum(list_action_return) > 1:
        list_action_return[0] = 0

    return list_action_return


