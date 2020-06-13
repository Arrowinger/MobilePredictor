# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 21:57:08 2019

@author: K P
"""
from selenium import webdriver
import re

driver = webdriver.Chrome('chromedriver.exe')

#driver.get('https://www.flipkart.com/redmi-note-6-pro-black-64-gb/product-reviews/itmfayzxqnzjhtbh?pid=MOBFAJB4CWKAZGPZ')

#print(page.text)
#page = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div/div/div[2]/div["+str(7)+"]/div/div/div/div[2]/div")
#page = driver.find_elements_by_css_selector("html.fonts-loaded body div#container div div.t-0M7P.NzPlEE._2doH3V div._3e7xtJ div div._1HmYoV.hCUpcT.col-12-12 div._1HmYoV._35HD7C.col-9-12 div.bhgxx2.col-12-12 div._1PBCrt div.col div.col._390CkK._1gY8H- div.row div.qwjRop")
#for data in page:
 #   print(data.text)
#print(type(page))


#for the last page

#last_page = driver.find_element_by_css_selector("html.fonts-loaded body div#container div div.t-0M7P.NzPlEE._2doH3V div._3e7xtJ div div._1HmYoV.hCUpcT.col-12-12 div._1HmYoV._35HD7C.col-9-12 div.bhgxx2.col-12-12 div div._2zg3yZ._3KSYCY span")
#value_last = last_page.text
#print(value_last)
#letters = value_last.split(' ')
#print(letters[-1])
#la = (letters[-1])
#la = la.replace(',','')
#print(la)
#las = int(la)

#st = 'hii,hello'

# when the searched string is found it returns -1
#if la.find(',') != -1:
 #   print(la)
#else:
 #   print("found")

#i = 2,555
#type(i)
#for x in range(1,las):
#   print("hi")

#driver.quit()


def scrapy(value):

    website = value
    driver.get(website)
    title = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[1]/h1/span").text
    price = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]").text
    description = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[8]/div[3]/div/div[2]/div[1]").text
    image = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[2]/img")
    image = image.get_attribute('src')
    pid = re.search('p/(.*?)&', value).group(1)
    product_name = re.search('com/(.*?)/p', value).group(1)


# collecting the reviews for multiple pages
    try:
        list_review = []
        #driver.get('https://www.flipkart.com/' + product_name + '/product-reviews/' + pid + '&page=' + str(1))
        #last_page = driver.find_element_by_css_selector("html.fonts-loaded body div#container div div.t-0M7P.NzPlEE._2doH3V div._3e7xtJ div div._1HmYoV.hCUpcT.col-12-12 div._1HmYoV._35HD7C.col-9-12 div.bhgxx2.col-12-12 div div._2zg3yZ._3KSYCY span")
        #value_last = last_page.text
        #letters = value_last.split(' ')
        #la = (letters[-1])
        #if la.find(',') == -1:
         #   la = la.replace(',', '')
        #las = int(la)
        for i in range(1,200):

            driver.get('https://www.flipkart.com/'+product_name+'/product-reviews/'+pid+'&page='+str(i))
    
            for j in range(3,12):
                driver.implicitly_wait(10)
                name = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div/div/div[2]/div["+str(j)+"]/div/div/div/div[2]/div")

                list_review.append(name.text)
        #driver.implicitly_wait(10)
    #driver.quit()
    except Exception:
        pass


#positive review
    try:
        positive_review = []
        for i in range(1,2):

            driver.get('https://www.flipkart.com/' + product_name + '/product-reviews/' + pid +'&aid=overall&certifiedBuyer=false&sortOrder=POSITIVE_FIRST'+ '&page=' + str(i))

            for j in range(3, 12):
                driver.implicitly_wait(10)
                name = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div/div/div[2]/div[" + str(j) + "]/div/div/div/div[2]/div")

                positive_review.append(name.text)
        # driver.implicitly_wait(10)
    # driver.quit()
    except Exception:
        pass

#negative review
    try:
        negative_review = []
        for i in range(1,2):

            driver.get('https://www.flipkart.com/' + product_name + '/product-reviews/' + pid +'&aid=overall&certifiedBuyer=false&sortOrder=NEGATIVE_FIRST'+ '&page=' + str(i))

            for j in range(3, 12):
                driver.implicitly_wait(10)
                name = driver.find_element_by_xpath(
                    "/html/body/div[1]/div/div[3]/div[2]/div/div/div[2]/div[" + str(j) + "]/div/div/div/div[2]/div")

                negative_review.append(name.text)
        # driver.implicitly_wait(10)
    # driver.quit()
    except Exception:
        pass
    
    return list_review, positive_review, negative_review, title, price, description,image,




#name = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div/div/div[2]/div["+str(j)+"]/div/div/div/div[2]/div")
#print(name.text)



#/html/body/div[1]/div/div[3]/div[2]/div/div/div[2]/div[12]/div/div/div/div[2]/div
#/html/body/div[1]/div/div[3]/div[2]/div/div/div[2]/div[12]/div/div/div/div[2]/div

#/html/body/div[1]/div/div[3]/div[2]/div/div/div[2]/div[3]/div/div/div/div[2]/div


























    
