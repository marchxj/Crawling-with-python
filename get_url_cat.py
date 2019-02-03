from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import time


RT = 'https://www.rottentomatoes.com/browse/dvd-streaming-all'
min_max = '?minTomato=0&maxTomato=100&'
services = 'services=amazon;hbo_go;itunes;netflix_iw;vudu;amazon_prime;fandango_now'
genres = '&genres={}&sortBy=release'

def get_url(pagenum):
    executable_path = '/usr/local/bin/chromedriver'
    driver = webdriver.Chrome(executable_path=executable_path)
    driver.wait = WebDriverWait(driver, 5) # Wait to let webdriver complete the initialization
    driver.get(RT+min_max+services+genres.format(pagenum))
    
    fw = open('URL_cat14.txt','w')
    while True:
        try:
            showMoreButton = driver.find_element_by_xpath('//*[@id="show-more-btn"]/button')
            time.sleep(1)
            showMoreButton.click()
            time.sleep(1)# 
        except Exception as e:
            print(e)
            break
    print ("Complete")
    time.sleep(10)
    movie_info = driver.find_elements_by_css_selector("div.movie_info")
    for movie in movie_info:          
            movie_url = movie.find_element_by_css_selector('a').get_attribute('href')        
            fw.write(movie_url +'\n')
    fw.close()



get_url(14)

f = open('URL_cat14.txt').readlines()
print(len(f))


# pagenum = [1,2,4,5,6,8,9,10,11,13,18,14]
# pagename = {'Action':1,'Animation':2,'Art & Foreign':4
#            'Classics':5,'Comedy':6,'Documentary':8
#            'Drama':9,'Horror':10,'Kids & Family':11
#            'Mystery':13,'Romance':18,'Sci-fi & Fantasy':14}
# pagename = {'1':'Action','2':'Animation','4':'Art & Foreign'
#            '5':'Classics','6':'Comedy','8':'Documentary'
#            '9':'Drama','10':'Horror','11':'Kids & Family'
#            '13':'Mystery','18':'Romance','14':'Sci-fi & Fantasy'}



