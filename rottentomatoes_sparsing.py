from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
import pandas as pd
import time,re,os

#make browser
ua=UserAgent()# import UserAgent
dcap = dict(DesiredCapabilities.PHANTOMJS)# import DesiredCapabilities
dcap["phantomjs.page.settings.userAgent"] = (ua.random)
service_args=['--ssl-protocol=any','--ignore-ssl-errors=true']
driver = webdriver.Chrome('chromedriver',desired_capabilities=dcap,service_args=service_args)

# test
# urlList= ['https://www.rottentomatoes.com/m/justice_league_2017','https://www.rottentomatoes.com/m/geostorm','https://www.rottentomatoes.com/m/star_wars_the_last_jedi',
# 'https://www.rottentomatoes.com/m/thor_ragnarok_2017','https://www.rottentomatoes.com/m/jumanji_welcome_to_the_jungle','https://www.rottentomatoes.com/m/the_star_2017',
# 'https://www.rottentomatoes.com/m/coco_2017','https://www.rottentomatoes.com/m/sleeping_giant','https://www.rottentomatoes.com/m/blade_runner_2049','https://www.rottentomatoes.com/m/just_getting_started'
# ]  

file = '5.txt'

def urllist(file):
	urlList = []
	with open(file) as f:
		lines = f.readlines()
		for line in lines:
			urlList.append(line.strip())
	return urlList


columns = ['movie_title','meter_score','audience_score','meter_avg_rating',
'meter_review_count','user_avg_rating','user_rating_count','rating','genre',
'directed_by','writen_by','in_theaters','on_disc','box_office','runtime','studio','synopsis','url']


def parsing_score(urlList):
    
    records = []
    
    for url in urlList:

        driver.get(url)
        
        # movie title
        try:
            movie_title = driver.find_element_by_css_selector('h1,title hidden-xs').text
        except:
        	pass
        #print(movie_title)
            
        # target value
        try:
            meter_score = driver.find_element_by_xpath('//*[@id="tomato_meter_link"]/span[2]').text
        except:
        	pass
        #print(meter_score)
        
        try:
            audience_score = driver.find_element_by_xpath('//*[@id="scorePanel"]/div[2]/div[1]/a/div/div[2]/div[1]/span').text
        except:
        	pass
        #print(audience_score)
        
        # Meter Rating and count
        try:
            meter_avg_rating = driver.find_element_by_xpath("//*[@id='scoreStats']/div[1]").text.replace('Average Rating: ', "")
        except:
        	pass
        #print(meter_avg_rating)
        try:
            meter_review_count = driver.find_element_by_xpath('//*[@id="scoreStats"]/div[2]/span[2]').text
        except:
            pass
        #print(meter_review_count)                                        
        # User Rating and count
        try:
            user_avg_rating = driver.find_element_by_xpath('//*[@id="scorePanel"]//div[2]/div[2]/div[1]').text.replace('Average Rating: ', "")   
        except:
        	pass
        #print(user_avg_rating)
        try:
            user_rating_count = driver.find_element_by_xpath('//*[@id="scorePanel"]/div[2]/div[2]/div[2]').text .replace('User Ratings: ', "")
        except:
        	pass                
        #print(user_rating_count)
        
        # movie info
        try:
            rating = driver.find_element_by_xpath("//*[@class='content-meta info']//*[contains(text(),'Rating: ')]//following::div").text
        except:
            pass    
        #print(rating)

        try:
            genre = driver.find_element_by_xpath("//*[contains(text(),'Genre: ')]//following::div").text
        except:
            pass
        #print(genre)

        try:
            directed_by = driver.find_element_by_xpath("//*[contains(text(),'Directed By: ')]//following::div").text
        except:
            pass
        #print(directed_by)
        
        try:
            writen_by = driver.find_element_by_xpath("//*[contains(text(),'Written By: ')]//following::div").text
        except:
            pass
        #print(writen_by)

        try:
            in_theaters = driver.find_element_by_xpath("//*[contains(text(),'In Theaters: ')]//following::div").text

        except:
            pass
        #print(in_theaters)

        try:
            on_disc = driver.find_element_by_xpath("//*[contains(text(),'On Disc/Streaming: ')]//following::div").text
        except:
            pass
        #print(on_disc)

        try:
        #   box_office = driver.find_element_by_xpath('//*[@id="mainColumn"]/section[3]/div/div[2]/ul/li[7]/div[2]').text 
            box_office = driver.find_element_by_xpath("//*[contains(text(),'Box Office: ')]//following::div").text
        except:
            pass
        #print(box_office)

        try:
            runtime = driver.find_element_by_xpath("//*[contains(text(),'Runtime: ')]//following::div").text
        except:
            pass
        #print(runtime)

        try:
            studio = driver.find_element_by_xpath("//*[contains(text(),'Studio: ')]//following::div").text 
        except:
            pass

        try:
            synopsis = driver.find_element_by_xpath('//*[@id="movieSynopsis"]').text
        except:
            pass

        records.append((movie_title,meter_score,audience_score,str(meter_avg_rating),meter_review_count,
            str(user_avg_rating),user_rating_count,rating,genre,directed_by,writen_by,in_theaters,
            on_disc,box_office,runtime,studio,synopsis,url))
    return records



def tocsv(records):

    data = pd.DataFrame(records,columns=columns)
    #print(data.head())
    data.to_csv('rottentomatoes5.csv',index = None)

if __name__ == '__main__':
	tocsv(parsing_score(urllist(file)))





