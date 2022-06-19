# -*- coding: utf-8 -*-
import argparse
import base64
import json
import os
from shlex import join

import requests


# 解析参数
def parse_commond():
    parse = argparse.ArgumentParser()
    target = parse.add_argument_group('target')
    target.add_argument('-e', dest='EMAIL', type=str, help=_OPTIONS_HELP_['EMAIL'])
    target.add_argument('-k', dest='KEY', type=str, help=_OPTIONS_HELP_['KEY'])
    target.add_argument('-q', dest='QUERY', type=str, help=_OPTIONS_HELP_['QUERY'])
    return parse.parse_args()


# 解析传入的fofaInfo配置、拼接Url请求、返回Json结果
def jointUrl(email, key, base64Content, size):
    r = requests.get(
        'https://fofa.info/api/v1/search/all?email={0}&key={1}&qbase64={2}&size={3}'
            .format(email, key, base64Content, size))
    url = r.url
    print(url)
    content = r.content
    return content


# 对传入的请求语法进行加密 b'' 为bytes字节流 需转回Str使用
def query(email, key, query):
    return jointUrl("{}".format(email), "{}".format(key),
                    bytes.decode(base64.b64encode(query.encode(encoding='utf-8'))), 10000)


def parse_json(args):
    str1 = args.QUERY
    print(str1)
    str = query(args.EMAIL, args.KEY, args.QUERY).decode(encoding='utf-8')
    print(str)
    dicts = json.loads(str)
    path = os.getcwd() + '/output'
    if not os.path.exists(path):
        os.mkdir(os.getcwd() + '/output')
    f = open(os.getcwd() + '/output/test.txt', 'w')
    for i in dicts['results']:
        f.write(join(i))
        f.write("\r\n")

    f.close()


# 帮助选项
_OPTIONS_HELP_ = {
    'EMAIL': 'fofa账户email邮箱 ',
    'KEY': 'fofa账户的key值',
    'QUERY': r"输入将要查询的语法规则 (如 host=\"baidu.com\")"
}

if __name__ == '__main__':
    print(parse_commond())
    parse_json(parse_commond())
