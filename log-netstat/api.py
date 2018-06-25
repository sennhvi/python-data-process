#!/usr/bin/python
# -*- coding: utf-8 -*-
#python3
import httplib2, urllib
params = urllib.urlencode({'ip':'9.8.8.8','datatype':'jsonp','callback':'find'})
url = 'http://api.ip138.com/query/?'+params
headers = {"token":"141a68cb4fa6bf162a7603a8db5f21da"}#token为示例
http = httplib2.Http()
response, content = http.request(url,'GET',headers=headers)
print(content)
