from env import *

perfile = np.array([[0.]])

def test(state, perfile):
    actions = getValidActions(state)
    list_action = np.where(actions==1)[0]
    idx = np.random.randint(0, len(list_action))
    return list_action[idx], perfile
