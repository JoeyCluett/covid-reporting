from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

from state_ND import *
from state_IL import *
#from state_AZ import *
from state_MN import *
from state_FL import *

class WebAccessor():

    def __init__(self):
        # create headless Chrome instance

        opts = Options()
        opts.add_argument("--headless")
        opts.add_argument("--window-size=1920x1080")
        CHROME_DRIVER = webdriver.Chrome( \
            chrome_options=opts, \
            executable_path=os.getenv('HOME') + '/chromedriver/chromedriver')

        self.chrome = CHROME_DRIVER

    def get_info_by_state(self, state_abbr):
        if   state_abbr == 'ND': return state_ND(self)
        elif state_abbr == 'IL': return state_IL(self)
        elif state_abbr == 'MN': return state_MN(self)
        elif state_abbr == 'FL': return state_FL(self)
        else:
            return StateInfo(state_abbr, -1, -1, -1)
