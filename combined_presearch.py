import time
import random

for z in range(1,36):
	import webbrowser
	url = f'https://engine.presearch.org/search?q=gordon+ramsay+show+season+{random.randint(1,5)}+episode+{random.randint(1,20)}'
	
	webbrowser.register('edge',
		None,
		webbrowser.BackgroundBrowser("C://Program Files (x86)//Microsoft//Edge//Application//msedge.exe"))
	webbrowser.get('edge').open(url)

	webbrowser.register('chrome',
		None,
		webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
	webbrowser.get('chrome').open(url)
	
	webbrowser.register('firefox',
		None,
		webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
	webbrowser.get('firefox').open(url)

	time.sleep(15)
	print (z)     
	
	if z%5 == 0:
		import os
		while 1 :
			os.system("TASKKILL /F /IM msedge.exe")
			time.sleep(5)
			break

	if z%5 == 0:
		import os
		while 1 :
			os.system("TASKKILL /F /IM chrome.exe")
			time.sleep(5)
			break
	
	if z%5 == 0:
		import os
		while 1 :
			os.system("TASKKILL /F /IM firefox.exe")
			time.sleep(5)
			break 
