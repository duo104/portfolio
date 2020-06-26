from selenium import webdriver
from time import sleep
import requests

class InstaBot:
  def __init__(self, username, pw):
    self.username = username
    self.pw       = pw     
    self.driver = webdriver.Chrome()
    self.driver.get("https://instagram.com")
    sleep(2)

  def login(self):
    driver = self.driver      
    driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(self.username)
    driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(self.pw)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    sleep(2)

  def closeBrowser(self):
    self.driver.close()

  def follow_back_tag_follow(self):
          driver = self.driver
          driver.get('https://www.instagram.com/explore/tags/%E3%83%95%E3%82%A9%E3%83%AD%E3%83%90%E7%B5%B6%E5%AF%BE/')

          href_list = []
          for i in range(1, 7):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(2)  
                a_tag = tag = driver.find_elements_by_tag_name('a')        
                for elem in a_tag:
                        target = elem.get_attribute('href')
                        if '.com/p/' in target:
                                href_list.append(target)
                print(href_list)

          for href in href_list:
                  driver.get(href)
                  driver.find_element_by_xpath("//button[contains(text(), 'フォローする')]").click()



  def auto_suggested_users_follow(self):
           driver = self.driver
           driver.get('https://www.instagram.com/explore/people/suggested/')
           
           name_list = []
           for i in range(1, 7):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(2)
                tag = driver.find_elements_by_tag_name('img')
                for elem in tag:
                        alt = elem.get_attribute('alt')
                        alt = alt.strip('のプロフィール写真')
                        name_list.append(alt)
           print(name_list)

           for name in name_list:
                   driver.get('https://www.instagram.com/' + name + '/')
                   self.driver.find_element_by_xpath("//button[contains(text(), 'フォローする')]").click()  

  def auto_like(self, hashtag):
    driver = self.driver      
    self.hashtag = hashtag      
    driver.get("https://www.instagram.com/explore/tags/{}".format(hashtag))
    sleep(2)

    pic_hrefs = []
    for i in range(1, 7):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(2)    
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                if '.com/p/' in elem.get_attribute('href')]
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]        
            except Exception:
                    continue
     
    print(pic_hrefs)               
 
    unique_photos = len(pic_hrefs)
    for pic_href in pic_hrefs:
            driver.get(pic_href)
            sleep(2)

            try:
                sleep(2)
                like_button = driver.find_element_by_xpath('//button[@class="wpO6b "]').click()
                like_button().click()
            except Exception as e:
                sleep(2)
            unique_photos -= 1

   
