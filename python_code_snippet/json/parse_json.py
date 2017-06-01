# coding=utf-8
import json
import hashlib


a = {"b":{"a":[{"n1":"WIFI","lo":116.30744414106923,"t2":"1387873418.195T+08:00","t3":"target_首页-海报视频点击","p1":"com.tudou.ui.activity.HomeActivity","n2":840,"la":39.98049465154441,"l":False},{"n1":"WIFI","lo":116.30744414106923,"t2":"1387873415.880T+08:00","t1":"A1005","s1":"5da19f89080af666bc2cb8d8775706df","p1":"com.tudou.ui.activity.HomeActivity"}]},"h":{"i":{"o2":"4.3","o1":"Android","b2":"Nexus 7","m":"10:bf:48:c2:81:f5","h":1205,"w":800,"u":"f835c7f8-c331-4b47-a6a3-772021544aa9","b1":"google"}}}


def parse_json(input_json):
    if isinstance(input_json, dict):
        for key in input_json.keys():
            key_value = input_json.get(key)
            if isinstance(key_value, dict):
                parse_json(key_value)
            elif isinstance(key_value, list):
                for json_array in key_value:
                    parse_json(json_array)
            else:
                print(str(key) + " = " + str(key_value))
    elif isinstance(input_json, list):
        for input_json_array in input_json:
            parse_json(input_json_array)


def run(t):
    for k,v in t.iteritems():
        if isinstance(v, list):
            for element in v:
                run(element)
        elif isinstance(v, dict):
            run(v)
        else: print(k,v)

if __name__ == '__main__':
    run(a)