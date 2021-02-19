from tools.sms import YunTongXin
from kindergarten_be.celery import app


@app.task
def send_sms(phone, code):
    config = {
        'accountSid': '8aaf0708762cb1cf01772441bc5657d5',
        'accountToken': '6a07a9fe6c5c49899d9b29e53d430773',
        'appId': '8aaf0708762cb1cf01772441bd3a57dc',
        'templateId': '1',
    }
    yun = YunTongXin(**config)
    res = yun.run(phone, code)
    return res

