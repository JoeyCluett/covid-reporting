
from WebAccessor import *
web_accessor = WebAccessor()

info_list = [
    web_accessor.get_info_by_state('ND'), # use state abbreviation
    web_accessor.get_info_by_state('IL'),
    web_accessor.get_info_by_state('MN'),
]

def sort_key(o):
    return o.state_name
info_list = sorted(info_list, key=sort_key)



print('State   Tests      Positive   Negative')
for i in info_list:
    print('%s      %-10d %-10d %-10d' % ( i.state_name, i.total_tested, i.positive_results, i.negative_results ))
