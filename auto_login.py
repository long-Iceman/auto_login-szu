import requests
import time

class INST(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        request = self._get_page()
        
        for i in range(5):
            if request.status_code != 200:
                time.sleep(2)
                request = self._get_page()
        if request.status_code == 200:
            self._login(request)
    
    def _get_page(self):
        login_page = 'https://drcom.szu.edu.cn/a70.htm'
        
        header = {
            'Referer' : 'https://drcom.szu.edu.cn/a70.htm',
            'User-Agent' : self.UA
        }
        self.session_requests = requests.Session()
        result = self.session_requests.get(login_page, headers = header)
        return result
        
    def _login(self, request):
        login_url = 'https://drcom.szu.edu.cn/a70.htm'
        header = {
            'Host': 'drcom.szu.edu.cn',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
            'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language' : 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding' : 'gzip, deflate, br',
            'DNT' : '1',
            'Connection' : 'keep-alive',
            'Upgrade-Insecure-Requests' : '1'
        }
        
        post_data = {
            'DDDDD': self.username,
            'upass': self.password,
            '0MKKey' : '%B5%C7%A1%A1%C2%BC'
        }
        
        result = self.session_requests.post(login_url, data = post_data, headers = header)
        
def main():
    name = '******' # campus card number
    pwd = '********' # query number for campus card
    INST(name, pwd)
    
if __name__ == '__main__':
    main()
