#! /usr/local/bin/python3


import cgi
import os
import time
import sys
import yate



print(yate.start_response('text/plant'))
addr=os.environ.get('REMOTE_ADDR')
host=os.environ.get('REMOTE_HOST')
method=os.environ.get('REQUEST_METHOD')
cur_time=time.asctime(time.localtime())
print>>sys.stderr,str(host)+","+str(addr)+","+str(cur_time)+":"+str(method)+":"
form=cgi.FieldStorage()
for each_form_item in form.keys():
    print>>sys.stderr,each_form_item+ '->'+ form[each_form_item].value
print>>sys.stderr
print('OK')

