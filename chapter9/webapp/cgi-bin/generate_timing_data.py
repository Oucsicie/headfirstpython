#! /usr/local/bin/python2.7
# -*- coding: utf-8 -*-


import cgitb

import cgi


import athletemodel
import yate


form_data=cgi.FieldStorage()
athlete_id=form_data['which_athlete'].value
athlete= athletemodel.get_athlete_from_id(athlete_id)


print(yate.start_response())
print(yate.include_header("Coach Kelly's Timing Data"))
print(yate.header("Athlete:" + athlete['Name'] + ",DOB:" + athlete['DOB']\
                   + "."))
print(yate.para("the top times for this athlete are:"))
print(yate.u_list(athlete['top3']))
print(yate.para("The entire set of timing data is: " + str(str(athlete['data']))
                 + " (duplicates removed)."))
print(yate.include_footer ({"Home" :"/index.html", \
                            "Select another athlete": "generate_list.py"})) 
