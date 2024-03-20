import pandas

class Data:

    def __init__(self, data: dict):
        self.data = data
        self.save_data()


    def data_to_dataframe(self) -> pandas.DataFrame:
        data = self.data = pandas.DataFrame(self.data)
        return data

    def save_data(self):
        data = self.data_to_dataframe()
        data.to_csv('major_data_salary.csv', index=False)