#-------------------------------------------------------------------------------
# Name:        TaiwanNewspaper_Crawler.py
# Author:      k1tten
# Email:       realever15@gmail.com
# Created:     2015/10/29
# Purpose:     To Practice How To Use Python Create A WebCrawler.
#-------------------------------------------------------------------------------
def main():
    import time
    import requests
    import random
   
    #WebSite's URL
    url = "http://www.twtimes.com.tw/index.php?page=news&ntype=4"
    
    #Get Web's Response Resources. 
    response = requests.get(url)

    #導入lxml
    from lxml import etree

    #Use Etree Function To Get Response Of Website
    tree = etree.HTML(response.text)
    
    #The Path Of Target
    #Use FireFox Web Developer
    searchResult = tree.xpath('//div[@class="newsli"]/ul/li/a')
   
    #Declare URL And Title Variable
    urlLt = []
    nameLt = []

    #Loop For Getting The Value Of 'href'
    for i in searchResult:               #Loop's Range Is Path Of Target 
        nameLt.append(i.text)            #Put Title's Words Into nameLt
        print i.text                     #Print Title
        urlLt.append(i.get('href'))      #Put The Values Of 'href' Into urlLt
        print i.get('href')              #Print The Values Of 'href'
    
    #Declare a Variable to Control The Name Of File That We Created. 
    x = 0

    #Loop Of Grub The Response Of Web and Create File Put That
    for i in urlLt:                                            #Loop's Range
        nextUrl = "http://www.twtimes.com.tw/index.php" + i    #Put href's Value Behind The index.php
        response = requests.get(nextUrl)                       #Get Web's response
        print "download: " + nextUrl                           #Print Downloading's Website
        file = open('%s.txt' %(nameLt[x]),'a')                 #Create a Title named File
        file.write( response.content + '\n')                   #Puts All Response Into The File
        file.close()                                           #Save And Close The File
        time.sleep(random.randint(1,3))                        #Avoid To DDOS The Website
        x += 1                                                 #Do The Next!

    #Create a If Statement To Run The main() Function
    #Please Check This Website : http://pydoing.blogspot.tw/2012/12/Python-Module-and-Script.html
if __name__ == '__main__':
    main()
