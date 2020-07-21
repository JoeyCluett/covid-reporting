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
    


