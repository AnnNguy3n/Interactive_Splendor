# code if else v_2
bias = np.zeros(getActionSize())
bias[12] = 42
bias[11] = 42
bias[10] = 42
bias[9] = 42
bias[8] = 38
bias[7] = 38
bias[6] = 38
bias[5] = 38
bias[4] = 34
bias[3] = 34
bias[2] = 34
bias[1] = 34
bias[13] = 30
bias[14] = 30
bias[15] = 30
for nllay in range(31,36):
    bias[nllay] = 27
for theup in range(16,28):
    bias[theup] = 22
for nltra in range(36,42):
    bias[nltra] = 10
for thean in range(28,31):
    bias[thean] = 4

@njit()
def ifelse(state,per):
    actions = getValidActions(state)
    output = actions * per[0] + actions
    action = np.random.choice(np.where(output == np.max(output))[0])
    win = getReward(state)
    if win == 1:
        per[1][0] += 1
    if win != -1:
        per[1][1] += 1
    return action, per

per = [bias,np.zeros(2)]