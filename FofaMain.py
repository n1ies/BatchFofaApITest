# -*- coding: utf-8 -*-
import requests

r = requests.get('https://fofa.info/api/v1/search/all?email=your_email&key=your_key&qbase64=aXA9IjEwMy4zNS4xNjguMzgi')
status = r.status_code
content = r.content
print(content)