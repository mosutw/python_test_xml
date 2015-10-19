# -*- coding: utf8 -*-
import requests

content = "helloworld"
#postdic = {
#    "ToUserName":"qianxun",
#    "FromUserName":"xiaowang",
#    "MsgType":"text",
#    "Content":content
#}
#
#r = requests.post("http://127.0.0.1:5000",params=postdic)
#r = requests.get("http://127.0.0.1:5000",params=postdic)
#print r.text     #此处返回flask框对应return的数据

#向后台发送xml格式的数据
postdic = u"""
<xml>
<ToUserName>wang</ToUserName>
<FromUserName>xiao</FromUserName>
<MsgType>text</MsgType>
<Content>hello</Content>
</xml>
"""
r = requests.post("http://127.0.0.1:5000",postdic)
print dir(r)
print r.text
