# Illinois

from info import *
import re

def state_IL(web_accessor):

    print('IL...', end='', flush=True)

    web_accessor.chrome.get('https://dph.illinois.gov/covid19')

    t = web_accessor.chrome.find_element_by_id(id_='covid19positive')

    # non-digits need to be stripped out. ill use a regex
    positive_cases = int(re.sub('[^\d]+', '', t.text))

    t = web_accessor.chrome.find_element_by_id(id_='covid19totaltest')
    total_tests = int(re.sub('[^\d]+', '', t.text))

    print('DONE', flush=True)

    return StateInfo('IL', total_tests, total_tests-positive_cases, positive_cases)

    # failed attempts:

    """    
    driver = webdriver.PhantomJS()
    driver.get('https://dph.illinois.gov/covid19')

    t = driver.find_element_by_id(id_='covid19positive')
    print(t.text)
    """

    """
    r = req.get('https://dph.illinois.gov/covid19')
    pg = BeautifulSoup(r.text, 'lxml')
    t = pg.find("h3", { "id" : "covid19positive" })
    print(t)
    cases_positive = int(t.get_text())
    return cases_positive
    """