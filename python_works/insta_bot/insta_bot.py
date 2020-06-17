from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests

username = input("usernameを入力してください > ")
pw       = input("passwordを入力してください > ")

class InstaBot:
  def __init__(self, username, pw):
    self.driver = webdriver.Chrome()
    self.driver.get("https://instagram.com")
    sleep(2)
    self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
    self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
    self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
    sleep(4)
    self.driver.find_element_by_xpath("//button[contains(text(), '後で')]")\
            .click()
    sleep(2)
    self.driver.find_element_by_xpath("//button[contains(text(), '後で')]")\
            .click()                 
    sleep(2)

  def soup_initialize():
    tag = input("検索するタグを入力して下さい > ")
    r   = requests.get("https://www.instagram.com/explore/tags/{}".format(tag))
    soup = BeautifulSoup(r.text, "html.parser")
    soup.find_all("a")

  def auto_like(self):
    self.bot.soup_initialize
    sleep(2)
    self.driver.get("https://www.instagram.com/explore/tags/{}".format(tag))
    sleep(2)
    self.driver.findElement(By.className("wp06b")).click();
    sleep(2)
    




bot = InstaBot(username=username, pw=pw)
bot.auto_like()