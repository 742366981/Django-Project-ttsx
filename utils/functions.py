import random


def get_ticket():
    s='sdsadsadfhdfefefh1234567890jjhhjjjhfd'
    ticket=''
    for i in range(25):
        ticket+=random.choice(s)
    return ticket