
class RegionalPlot:
    def __init__(self):
        self.dates = []
        self.cases = []
        self.acc_cases = 0

    def insert_data_point(self, date, case):
        self.dates.append(date)
        self.cases.append(str(self.acc_cases + int(case)))
        self.acc_cases += int(case)

    def format_x(self):
        assert len(self.dates) == len(self.cases)
        return "[" + ", ".join(self.dates) + "]"

    def format_y(self):
        assert len(self.dates) == len(self.cases)
        return "[" + ", ".join(self.cases) + "]"
