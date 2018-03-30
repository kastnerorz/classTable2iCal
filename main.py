import requests
from icalendar import Calendar, Event
from datetime import datetime
import pytz
import json
import re

cal = Calendar()
cal.add('prodid', '-//My calendar product//mxm.dk//')
cal.add('version', '2.0')

url = ['xk.shu.edu.cn:8080', 'xk.shu.edu.cn']
url_index = url[0]
username = '16122038'
password = 'Dicos.123'

def login(session):
    url_captcha = url_index + '/Login/GetValidateCode?%20%20+%20GetTimestamp()'
    captcha_bin = session.get(url_captcha).content
    captcha_post_data = {'captcha': ('captcha.jpg', captcha_bin, 'image/jpeg')}
    captcha_session = requests.session()
    try:
        captcha_req_result = captcha_session.post('http://114.115.217.207:5000/jwc-xuanke', files=cj, timeout=10)
        captcha_text = captcha_req_result.json()['result']
    except:
        print(u'获取验证码失败')
        captcha_session.keep_alive = False
        print(u'close captcha session...')
        return False
    LoginData = {
        'txtUserName': username,
        'txtPassword': password,
        'txtValiCode': captcha_text
    }
    print
    u'正在登录...'
    ReqLogin = session.post(url_index, LoginData)
    Result = re.findall(u'divLoginAlert">\r\n\s*(.*?)\r\n', ReqLogin.text)
    if not Result:
        try:
            Semester = re.findall(u'<font color="red">(.*?)<', ReqLogin.content)[0]
            LoginInfo = re.findall(u'23px;">\r\n\s*(.*?)：(.*?)\r\n', ReqLogin.text)
        except:
            print
            u'[get semester info error]'
            return False
        print
        '%s' % Semester
        for info in LoginInfo:
            print
            '%s:%s' % info
        print
        u'登录成功!'
        return True
    else:
        print
        u'[登录失败]', Result[0]
        return False

def main():
    headers = {'user-agent',
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

    req = requests.Session()
    login(req)

if __name__ == '__main__':
    main()