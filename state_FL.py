# Florida

import requests as req
from bs4 import BeautifulSoup
from info import *
import re

def state_FL(web_accessor):

    print('FL...', end='', flush=True)

    web_accessor.chrome.get('https://floridahealthcovid19.gov/')
    tag_pos = web_accessor.chrome.find_element_by_id(id_='tested-positive-stat')
    tag_neg = web_accessor.chrome.find_element_by_id(id_='tested-negative-stat')

    cases_neg = int(strip_commas(tag_neg.text))
    cases_pos = int(strip_commas(tag_pos.text))

    print('DONE', flush=True)

    return StateInfo('FL', cases_pos + cases_neg, cases_neg, cases_pos)



    # failed earlier attempts

    """
    r = req.get('https://floridahealthcovid19.gov/')
    pg = BeautifulSoup(r.text, 'lxml')

    tag_pos_cases = pg.find('div', id='tested-positive-stat')
    print(tag_pos_cases)
    #pos_cases = int(re.sub('[^\d]+', '', tag_pos_cases.get_text()))

    tag_neg_cases = pg.find(id='tested-negative-stat')
    print(tag_neg_cases)
    #neg_cases = int(re.sub('[^\d]+', '', tag_neg_cass.get_text()))

    #return StateInfo('FL', pos_cases + neg_cases, neg_cases, pos_cases)
    """

    """
    r = req.get('http://www.floridahealth.gov/newsroom/2020/07/071820-1245-covid19.pr.html')
    pg = BeautifulSoup(r.text, 'lxml')

    t = pg.find('p', text='Confirmed Cases in Florida Residents')
    tag_pos_cases = t.find_parent('td').find_next_sibling('td').p.get_text()
    pos_cases = int(re.sub('[^\d]+', '', tag_pos_cases))

    return StateInfo('FL', -1, -1, pos_cases)
    """

