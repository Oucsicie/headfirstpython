#! /usr/local/bin/python3
# -*- coding:utf-8 -*-


import cgi
import json
import yate
import athletemodel


form_data= cgi.FieldStorage()
athlete_name= form_data['which_athlete'].value
athlete= athletemodle.get_athlete_from_id(athlete_id)


print(yate.start_response('application/json'))
print (json.dumps(athletes[athlete_name].to_dict))
