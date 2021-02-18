import datetime
import hashlib
import base64
import json

import requests


class YunTongXin():
    base_url = 'https://app.cloopen.com:8883'

    def __init__(self, accountSid, accountToken, appId, templateId):
        self.accountSid = accountSid
        self.accountToken = accountToken
        self.appId = appId
        self.templateId = templateId

    def get_request_url(self, sig):
        self.url = self.base_url + '/2013-12-26/Accounts/%s/SMS/TemplateSMS?sig=%s' % (self.accountSid, sig)
        return self.url

    def get_timestamp(self):
        return datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    def get_sig(self, timestamp):
        s = self.accountSid + self.accountToken + timestamp
        m = hashlib.md5()
        m.update(s.encode())
        return m.hexdigest().upper()

    def get_request_header(self, timestamp):
        s = self.accountSid + ':' + timestamp
        auth = base64.b64encode(s.encode()).decode()
        return {
            'Accept': 'application/json',
            'Content-Type': 'application/json;charset=utf-8',
            'Authorization': auth
        }

    def get_request_body(self, phone, code):
        return {
            'to': phone,
            'appId': self.appId,
            'templateId': self.templateId,
            'datas': [code, '3']
        }

    def request_api(self, url, header, body):
        res = requests.post(url, headers=header, data=body)
        return res.text

    def run(self, phone, code):
        timestamp = self.get_timestamp()
        sig = self.get_sig(timestamp)
        url = self.get_request_url(sig)
        header = self.get_request_header(timestamp)
        body = self.get_request_body(phone, code)
        data = self.request_api(url, header, json.dumps(body))
        return data


if __name__ == '__main__':
    config = {
        'accountSid': '8aaf0708762cb1cf01772441bc5657d5',
        'accountToken': '6a07a9fe6c5c49899d9b29e53d430773',
        'appId': '8aaf0708762cb1cf01772441bd3a57dc',
        'templateId': '1',

    }

    yun = YunTongXin(**config)
    res = yun.run('18813618139', '881227')
    print(res)