import json
import re
import codecs

#https://stackoverflow.com/questions/45218234/converting-log-file-to-json

'''
output = {'IP': {}, 'ts': {} }

o = codecs.open('o.json',"w",encoding='utf-8')
with open("access.log", "r") as file:
    data = file.readlines()
    for i in data:
        s = str(i).split()
        output['IP']['Host'] = s[0].replace("['","")
        o.write(json.dumps(output))
'''
##############################################################################
'code to format json object'

import json
import re
import codecs

json_file = codecs.open('formatted.json','w',encoding='utf-8')

with open('unformatted.json', 'r', encoding='utf-8') as content_file:
    c = content_file.read()
    c = json.loads(c)
    formatted_json = json.dumps(c, indent=4)
    json_file.write(formatted_json)

################################################################################

log_file = codecs.open('access.log','r',encoding='utf-8')
o_file = codecs.open('heap.json','w',encoding='utf-8')

head = chr(9) + "[" + chr(10)
o_file.write(head)

lines = log_file.readlines()
last_line = lines[-1]

for l in lines:
    arr = l.strip(chr(10)).split(',')
    if len(arr) == 14 and l != last_line:
        f_0 = chr(9) + chr(9) + "{" + chr(10)
        f_1 = '"metricName": "' + arr[0] + '",'  + chr(10)
        f_2 = '"metricId": ' + arr[1] + ','  + chr(10)
        f_3 = '"metricPath": "' + arr[2] + '",'  + chr(10)
        f_4 = '"frequency": "' + arr[3] + '",'  + chr(10)
        f_5 = '"metricValues": [{' + \
             '"occurences": ' + arr[4] + ',' + '"current": ' + arr[5] + ','\
             '"min": ' + arr[6] + ',' + '"max": ' + arr[7] + ','\
             '"startTimeInMills": ' + arr[8] + ',' + '"usedRange": ' + arr[9] + ','\
             '"count": ' + arr[10] + ',' + '"sum": ' + arr[11] + ','\
             '"value": ' + arr[12] + ',' + '"standardDeviation": ' + arr[13] + '}]' + chr(10) + '},' + chr(10)
        gen_str = f_0 + f_1 + f_2 + f_3 + f_4 + f_5
        o_file.write(gen_str)
    if len(arr) == 14 and l == last_line:
        f_0 = chr(9) + chr(9) + "{" + chr(10)
        f_1 = '"metricName": "' + arr[0] + '",'  + chr(10)
        f_2 = '"metricId": ' + arr[1] + ','  + chr(10)
        f_3 = '"metricPath": "' + arr[2] + '",'  + chr(10)
        f_4 = '"frequency": "' + arr[3] + '",'  + chr(10)
        f_5 = '"metricValues": [{' + \
             '"occurences": ' + arr[4] + ',' + '"current": ' + arr[5] + ','\
             '"min": ' + arr[6] + ',' + '"max": ' + arr[7] + ','\
             '"startTimeInMills": ' + arr[8] + ',' + '"usedRange": ' + arr[9] + ','\
             '"count": ' + arr[10] + ',' + '"sum": ' + arr[11] + ','\
             '"value": ' + arr[12] + ',' + '"standardDeviation": ' + arr[13] + '}]' + chr(10) + '}' + chr(10)
        gen_str = f_0 + f_1 + f_2 + f_3 + f_4 + f_5
        o_file.write(gen_str)
    if len(arr) < 14 and l != last_line:
        f_0 = chr(9) + chr(9) + "{" + chr(10)
        f_1 = '"metricName": "' + arr[0] + '",'  + chr(10)
        f_2 = '"metricId": ' + arr[1] + ','  + chr(10)
        f_3 = '"metricPath": "' + arr[2] + '",'  + chr(10)
        f_4 = '"frequency": "' + arr[3] + '",'  + chr(10)
        f_5 = '"metricValues": ['  + ']' + chr(10) + '},' + chr(10)
        gen_str = f_0 + f_1 + f_2 + f_3 + f_4 + f_5
        o_file.write(gen_str)
    if len(arr) < 14 and l == last_line:
        f_0 = chr(9) + chr(9) + "{" + chr(10)
        f_1 = '"metricName": "' + arr[0] + '",'  + chr(10)
        f_2 = '"metricId": ' + arr[1] + ','  + chr(10)
        f_3 = '"metricPath": "' + arr[2] + '",'  + chr(10)
        f_4 = '"frequency": "' + arr[3] + '",'  + chr(10)
        f_5 = '"metricValues": ['  + ']' + chr(10) + '}' + chr(10)
        gen_str = f_0 + f_1 + f_2 + f_3 + f_4 + f_5
        o_file.write(gen_str)

tail = "]"
o_file.write(tail)
