import random
from datetime import datetime


def get_ticket():
    s='sdsadsadfhdfefefh1234567890jjhhjjjhfd'
    ticket=''
    for i in range(25):
        ticket+=random.choice(s)
    return ticket


def get_order_num():
    num = ''
    s = '1234567890abcdefghijklmnopqefdf'
    for i in range(8):
        num += random.choice(s)
    order_time = datetime.now().strftime('%Y%m%d%H%M%S')
    return order_time + num