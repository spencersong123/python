# coding=utf-8
__author__ = 'bingzheng song'
import requests
import itchat
key = 'f2e3aa61e2794db5ba192160cd07d824'
def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': key,
        'info':msg,
        'userid':'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    reply = get_response(msg['Text'])
    return reply
itchat.auto_login(hotReload=True)
itchat.run()