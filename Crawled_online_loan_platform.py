#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 11:02:09 2018

@author: jinxing
"""
#第一步First Step
from selenium import webdriver
executable_path = '/Users/jinxing/Desktop/chromedriver'
driver = webdriver.Chrome(executable_path=executable_path)
driver.get("https://shuju.wdzj.com/platdata-1.html")

base1 = "//*[@id=\"platTableTmpl\"]/table[1]/tbody/tr["
base2 = "]/td[2]/div/a"

txt = open('out.txt','w')


for i in range(464):
    i += 1
    path = base1+str(i)+base2
    elem = driver.find_element_by_xpath(path)
    print(elem.get_attribute('href'),file=txt)

txt.close()


#第二步 Second Step
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 12:27:43 2018

@author: jinxing
"""
from selenium import webdriver
executable_path = '/Users/jinxing/Desktop/chromedriver'
driver = webdriver.Chrome(executable_path=executable_path)
#driver.get("https://shuju.wdzj.com/plat-info-59.html")

#base1 = "/html/body/div[2]/div[2]/div[2]/div[2]/a[4]"
#path = base1
#elem = driver.find_element_by_xpath(path)
#print(elem.get_attribute('href'))
file = 'out.txt'
txt = open('gongshangout.txt','w')

urlList = []
with open(file) as f:
    lines = f.readlines()
    for line in lines:
        urlList.append(line.strip())

for url in urlList:
        driver.get(url)
        path = "/html/body/div[2]/div[2]/div[2]/div[2]/a[4]"
        elem = driver.find_element_by_xpath(path)
        print(elem.get_attribute('href'),file=txt)
txt.close()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 13:44:52 2018

@author: jinxing
"""
#第三步 Third step
from selenium import webdriver
executable_path = '/Users/jinxing/Desktop/chromedriver'
driver = webdriver.Chrome(executable_path=executable_path)
"""
driver.get("https://www.wdzj.com/dangan/ljf2/gongshang/")

base1 = "/html/body/div[10]/div/div/div[1]/div[1]/div[2]/table/tbody/tr[1]/td[2]"
path = base1
elem = driver.find_element_by_xpath(path).text
print(elem)
"""
file = 'gongshangout.txt'
txt = open('name.txt','w')

urlList = []
with open(file) as f:
    lines = f.readlines()
    for line in lines:
        urlList.append(line.strip())

for url in urlList:
        driver.get(url)
        path = "/html/body/div[10]/div/div/div[1]/div[1]/div[2]/table/tbody/tr[1]/td[2]"
        elem = driver.find_element_by_xpath(path).text
        print(elem,file=txt)
txt.close()
