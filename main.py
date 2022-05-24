from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

driver = webdriver.Chrome()
driver.get('https://www.crackthemes.com/page/59/')
driver1 = webdriver.Chrome()





def carawl(link):

    driver1.get(link)
    time.sleep(4)

    download_link = driver1.find_element_by_class_name("quote").text
    
    
    # open file in write mode quotez
    name=random.randrange(20, 5000, 3)
    f = open(str(name)+".txt", "a")
    
    f.write("%s\n" % download_link)
    f.close()
    
    
    print('Done')




while True:
    try:
        links = driver.find_elements_by_class_name("post-title")
        for i in links:
            try:
                carawl(i.find_element_by_tag_name('a').get_attribute("href"))
                time.sleep(5)
            except:
                print(i.find_element_by_tag_name('a').get_attribute("href"))
    except:
        pass



    driver.get(driver.find_element_by_class_name("nextpostslink").get_attribute("href"))
    time.sleep(5)

