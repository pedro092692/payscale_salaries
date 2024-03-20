from bs4 import BeautifulSoup

class Scrapper:

    def __init__(self):
        self.major_data = {
            "Major":[],
            "Degree Type":[],
            "Early Career Pay":[],
            "Mid Career Pay":[]
        }

    @staticmethod
    def payscale_data(content) -> list:
        data = BeautifulSoup(content, 'html.parser')
        table = data.find(name="table", class_="data-table")
        data = table.findAll(name="span", class_="data-table__value")
        return data

    @staticmethod
    def extract_data(dataset) -> list:
        row_data = []
        for i in range(len(dataset)):
            if i == 0:
                index_s = 0
                index_f = 6
                row_data.append(dataset[index_s:index_f])

            if index_f < len(dataset):
                index_s = index_f
                index_f += 6
                row_data.append(dataset[index_s:index_f])

        return row_data


    def data_dict(self, data):

        for i in range(len(data)):
            self.major_data["Major"].append(data[i][1].text)
            self.major_data["Degree Type"].append(data[i][2].text)
            self.major_data["Early Career Pay"].append(int(data[i][3].text[1:].replace(',','')))
            self.major_data["Mid Career Pay"].append(int(data[i][4].text[1:].replace(',','')))

    def get_data(self, url_content):
        table_list = self.payscale_data(url_content)
        row_data = self.extract_data(table_list)
        self.data_dict(row_data)



