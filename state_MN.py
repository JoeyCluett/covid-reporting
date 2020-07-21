# Minnesota

import requests as req
from bs4 import BeautifulSoup
from info import *
import re

def state_MN(web_accessor):

    r = req.get('https://www.health.state.mn.us/diseases/coronavirus/situation.html')
    pg = BeautifulSoup(r.text, 'lxml')

    item = pg.find('span', text='Total positive cases (cumulative)')
    pos_case_nums = None
    for tag in item.previous_siblings:
        if tag.name == 'strong':
            pos_case_nums = int(re.sub('[^\d]+', '', tag.get_text()))
            break

    item = pg.find('strong', text='Total approximate number of completed tests:')
    total_tests = None
    for tag in item.next_siblings:
        total_tests = int(re.sub('[^\d]+', '', str(tag)))
        break # only want first iteration

    return StateInfo('MN', total_tests, total_tests - pos_case_nums, pos_case_nums)
