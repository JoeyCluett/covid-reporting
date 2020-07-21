# North Dakota

import requests as req
from bs4 import BeautifulSoup
from info import *

def state_ND(web_accessor_unused):

    r = req.get('https://www.health.nd.gov/diseases-conditions/coronavirus/north-dakota-coronavirus-cases')
    pg = BeautifulSoup(r.text, 'lxml')

    # this is just how health.nd.gov is organized

    pos_cases = pg.find('p', text='Positive Cases') # only one <p> tag with the text 'Positive Cases'
    pos_case_nums = None
    for tag in pos_cases.previous_siblings: # 'siblings' are counterintuitive in BeautifulSoup
        if tag.name == 'h2':
            pos_case_nums = int(tag.get_text())
            break # only need the one <h2> tag

    neg_cases = pg.find('p', text='Negative')
    neg_case_nums = None
    for tag in neg_cases.previous_siblings:
        if tag.name == 'h2':
            neg_case_nums = int(tag.get_text())
            break

    total_test = pg.find('p', text='Total Unique Individuals Tested')
    total_test_nums = None
    for tag in total_test.previous_siblings:
        if tag.name == 'h2':
            total_test_nums = int(tag.get_text())
            break

    return StateInfo("ND", total_test_nums, neg_case_nums, pos_case_nums)

    #class="main-container container js-quickedit-main-content"
    #print(div_list[1])


