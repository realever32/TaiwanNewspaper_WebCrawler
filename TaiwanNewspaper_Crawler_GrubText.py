#-------------------------------------------------------------------------------
# Name:        TaiwanNewspaper_Crawler_GrubText.py
# Date:        2015/10/30
# Author:      k1tten
# E-mail:      realever15@gmail.com
# Github:      https://github.com/realever32/TaiwanNewspaper_WebCrawler
# Purpose:     This Is Use To Practice How To Use Python To Create A WebCrawler.
#-------------------------------------------------------------------------------
def main():
    import time
    import requests
    import random
   
    #WebSite's URL.
    url = "http://www.twtimes.com.tw/index.php?page=news&ntype=4"
    
    #Get Web's Response Resources. 
    response = requests.get(url)

    #Import Lxml Etree.
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
        urlLt.append(i.get('href'))      #Put The Values Of 'href' Into urlLt
    
    #Declare a Variable to Control The Name Of File That We Created. 
    x = 0

    #Loop Of Grub The Response Of Web and Create File Put That
    for i in urlLt:                                                 #Loop's Range
        nextUrl = "http://www.twtimes.com.tw/index.php" + i         #Put href's Value Behind The index.php
        response = requests.get(nextUrl)                            #Get Web's Response
        print "Download : " + nextUrl                               #Print downloading's Website.
        tree = etree.HTML(response.text)                            #Get Response from Context's Website.

        #Set Web Context Path
        searchResult = tree.xpath('//span/table/tr[3]/td/text()')           
        
        #Create a Loop To Grub Web Context.
        for i in searchResult:                            
            #Try-Except Statement , Exception Handling.
            try:                                                
                file = open( '%s.txt' %(nameLt[x]),'a' )            #Create a File To Put Web Context.
                file.write( unicode(i).encode('utf-8') + '\n' )     #Use UTF-8 To Put Web Context Into File.
                file.close()                                        #Save And Close FIle.
            except UnicodeError:                                    #If UnicodeError Happen , Pass that.
                pass
            else:                                                   #If Any Else Error Happen , Pass that.
                pass
            time.sleep( random.randint(1,3) )                       #To Avoid Web DDOS.
        x += 1                                                      #Do The Next !

    #Create a If Statement To Run The main() Function
    #Please Check This Website : http://pydoing.blogspot.tw/2012/12/Python-Module-and-Script.html
if __name__ == '__main__':
    main()
