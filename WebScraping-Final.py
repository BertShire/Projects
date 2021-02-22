#!/usr/bin/env python
# coding: utf-8

# In[1]:


import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from selenium import webdriver
import time
PATH = "C:\Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(PATH)
i=1
Filename = "PBAPlayersdata.csv"
f=open(Filename,"w")
header="Name, Age, Years, Earnings, Style, Events,2020_Average\n"
f.write(header)
while i < 5:
    driver.get("https://www.pba.com/players")
    time.sleep(2)
    if i >1:
        driver.find_element_by_xpath('//button[contains(text(), '+str(i)+')]').click()
    time.sleep(2)
    page = driver.page_source
    #Parser
    page_soup=soup(page,"html.parser")
    #Grabs each player
    players=page_soup.findAll("div",{"class":"players-list"})
    i = i + 1
    for player in players:    
        #Goes through each player on the page to get their name
        Name = player.a["href"]
        print(Name[9:])
        #Grabs new url with players data
        url1='https://www.pba.com'+Name
        uClient = uReq(url1)
        page=uClient.read()
        uClient.close()
        page_soup=soup(page,"html.parser")
        #This code only shows up if a player has no data and has just joined the PBA tour
        Stats=page_soup.find("div",{"class":"view-empty"})
        if Stats is not  None:
            print("No Stats found")
            continue
        #If Stats shows up as not None then the player has no data so we skip this player
        else:
            Ages=page_soup.find("div",{"class":"field field--name-field-date-of-birth field--type-datetime field--label-inline clearfix"})
            Age = Ages.text
            Age1= Age.replace('\n','')[3:]
            print(Age.replace('\n','')[3:])
            Stats=page_soup.find("div",{"class":"view-empty"})
            Time = page_soup.find("time",{"class":"datetime"})
            if Time is None:
                print("Data unavailable")
                continue
            else:
                Years=2020-int(Time.text)
                print("Years on tour:",Years)
            Earnings=page_soup.find("td",{"class":"views-field views-field-winnings"}) 
            Earned = Earnings.text
            print("Earnings:",Earned.replace(',',''))
            Style = page_soup.find("div",{"class":"field field--name-field-bowls field--type-list-string field--label-inline clearfix"})
            if Style is None:
                print("Style: Data Unavailable")
                continue
            else:
                Style = Style.text
                Style1= Style.replace('\n','')[5:]
                print("Style:",Style.replace('\n','')[5:])
            Events=page_soup.find("td",{"class":"views-field views-field-events"})
            Event = Events.text
            print("Events played:",Event)
            Averages=page_soup.findAll("td",{"class":"views-field views-field-average"})
            Average=Averages[1].text
            print("Most recent Average:",Average)
            f.write(Name[9:] + "," + Age.replace('\n','')[3:] + "," + str(Years) + "," + str(Earned.replace(',','')[1:]) + "," + Style.replace('\n','')[5:] +","+Event.replace(',','')+","+ str(Average)+"\n")
driver.close()
f.close()


# In[ ]:




