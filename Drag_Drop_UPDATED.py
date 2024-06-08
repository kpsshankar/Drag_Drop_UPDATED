from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver import ActionChains







class DragAndDrop:


   def __init__(self,url):
       self.url = url
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       self.action = ActionChains(self.driver)


   def boot(self):
       self.driver.get(self.url)
       sleep(3)
       self.driver.maximize_window()


   def quit(self):
       self.driver.quit()


  
   def dragAndDrop(self):
       actions = ActionChains(webdriver)
       fullXPath1 = "/html/body/div/div[2]/div/div[2]/aside[1]/ul/li[1]/a"
       fullXPath2 = "/html/body/div/div[2]/div/div[2]/aside[1]/ul/li[2]/a"
       #actions.drag_and_drop(self.driver.find_element(by=By.XPATH, value=fullXPath1)),(self.driver.find_element(by=By.XPATH, value=fullXPath2)).(start, destination).perform()
       start=self.driver.find_element(by=By.XPATH, value=fullXPath1)
       destination =self.driver.find_element(by=By.XPATH, value=fullXPath2)
       self.action.drag_and_drop(start, destination).perform()
       sleep(3)
       #fullXPath ="/html/body/div[2]/p"
       #droptext = self.driver.find_element(by=By.XPATH, value=fullXPath)
       #if droptext == "Dropped!":
            #print("Success")
       #else:
            #print("Error")
#except NoSuchElementException as e:


obj = DragAndDrop("https://jqueryui.com/droppable/")
obj.boot()
obj.dragAndDrop()


