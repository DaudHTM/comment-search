from selenium import webdriver
from selenium.webdriver.edge.service import Service

from bs4 import BeautifulSoup
import selenium.webdriver.edge.options
import time
from msedge.selenium_tools import EdgeOptions, Edge




oldId='Y0tV7XDxjOg' #my old id


#beast old id ----

#oldId='dZklZVaU4AI'

videoId=''
x=3

youtube_url ="https://www.youtube.com/channel/UCe1RPSNh2et_iEFijRL_klA/featured" # my channel url

#mr beast url 
#youtube_url="https://www.youtube.com/results?search_query=Mrbeast6000"

driver = Edge(executable_path=r'D:\\EdgeDriver\\msedgedriver.exe')

vid=True
actId=''
def get_youtube_stats():
    
    content = driver.page_source.encode("utf-8").strip()
    print(type(content))
    youtube_soup = BeautifulSoup(content, "lxml")
    title = youtube_soup.find("a", id='video-title')
    if title!=None:
        print(title)
        videoIdAA=title['href']
        print(videoIdAA)
        if 'shorts' in videoIdAA:
            videoIda=videoIdAA.split("s/")
            videoId=videoIda[1]
        else:
            videoIdAA=videoIdAA.split("=")
            videoId=videoIdAA[1]
       
            
            
        return videoId


        

while True:
    

    time.sleep(.05)
    driver.get(youtube_url)
    
    time.sleep(.05)
    driver.implicitly_wait(100)
    driver.delete_all_cookies()
    videoId=get_youtube_stats()
    print(videoId)
    if videoId!=oldId and videoId!=None:
        break
    



print(actId)
driver.close()