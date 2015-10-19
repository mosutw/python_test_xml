#/usr/bin/env python
from flask import Flask,request,jsonify
from dicttoxml import dicttoxml
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

app = Flask(__name__)
app.debug = True

@app.route('/',methods=['POST','GET']) 
def xml_convert_dic():
#     request_data = request.data
    print request.data
    root = ET.fromstring(request.data)
    msg = {}
    for child in root:
        msg[child.tag] = child.text
    print "msg:" 
    print  msg
    return dicttoxml(msg)

#def get_data():
#    print request
#    touser = request.args.get("ToUserName","") 
#    print touser
#    return touser  

if __name__ == "__main__":
    app.run()
