import os
import sys
from WebAccessor import *
web_accessor = WebAccessor()

from state_AZ import *

state_AZ(web_accessor)

try:
    info_list = [
        web_accessor.get_info_by_state('ND'), # use state abbreviation
        web_accessor.get_info_by_state('IL'),
        web_accessor.get_info_by_state('MN'),
        web_accessor.get_info_by_state('FL'),
        web_accessor.get_info_by_state('AZ'),
    ]
except Exception:
    web_accessor.chrome.quit() # cant let this guy keep going
    raise # re-throw the exception, it contains some useful information

def sort_key(o):
    return o.state_name
info_list = sorted(info_list, key=sort_key)


print('State   Tests      Positive   Negative')
for i in info_list:
    print('%s      %-10d %-10d %-10d' % ( i.state_name, i.total_tested, i.positive_results, i.negative_results ))


# destroy the running background Chrome instance.
# for some reason, this is not done automagically
web_accessor.chrome.quit()
