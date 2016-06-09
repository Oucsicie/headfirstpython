#! /usr/local/bin/python2.7
# -*- coding: utf-8 -*-


import json
import yate
import athletemodel


names= athletemodel.get_namesID_from_store()

print(yate.start_response('application/json'))
print(json.dumps(sorted(names)))


