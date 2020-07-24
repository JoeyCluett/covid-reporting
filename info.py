class StateInfo:
    def __init__(self, state_name, total_tested, negative_results, positive_results):
        self.state_name = state_name
        self.total_tested = total_tested
        self.negative_results = negative_results
        self.positive_results = positive_results

    def __str__(self):
        return self.state_name + ":" + \
            "\n    Total Tests :    " + str(self.total_tested) + \
            "\n    Negative Cases : " + str(self.negative_results) + \
            "\n    Positive Cases : " + str(self.positive_results)

def generate_html_table(info_list):

    f = open('index.html', 'w+')

    _ = f.write('<!DOCTYPE html><html><head>')
    _ = f.write('<title>COVID-19 Testing Results</title>')
    _ = f.write('<style>table, th, td { border: 1px solid black; border-collapse:collapse; }</style>')
    _ = f.write('</head><body>')


    _ = f.write('<table>')
    _ = f.write('<tr><th>State</th><th>Total Tests</th><th>Positive Cases</th><th>Negative Cases</th></tr>')

    for info in info_list:
        _ = f.write('<tr>')

        _ = f.write('<td>%s</td><td>%d</td><td>%d</td><td>%d</td>' % ( \
            info.state_name, info.total_tested, info.positive_results, info.negative_results ))

        _ = f.write('</tr>')

    _ = f.write('</table>')

    _ = f.write('<br>this site does not use cookies or store any kind of user data whatsoever. happy trails.')

    _ = f.write('</body></html>')

    f.close()

# idk why, but re does not handle all cases of numbers 
# with commas. this function is a fallback
def strip_commas(input_str):

    output_str = ''

    for c in input_str:
        if ord(c) >= ord('0') and ord(c) <= ord('9'):
            output_str = output_str + c # i hate this... so much

    return output_str
