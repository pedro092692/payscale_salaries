import requests

class Web:

    @staticmethod
    def download_web_page(url):
        response = requests.get(url)
        return response.text
