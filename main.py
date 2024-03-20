from web import Web
from scrapper import Scrapper
from manage_data import Data

web = Web()
scrapper = Scrapper()


# 1 Download all pages
url = 'https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/'

for i in range(1, 33):
    content = web.download_web_page(f'{url}{i}')
    # scrape data from data
    scrapper.get_data(url_content=content)

#save data to csv file
data = Data(scrapper.major_data)
