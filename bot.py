from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

class BotWpp:

    def __init__(self):
        self.driver = webdriver.Chrome('C:\\Users\\Pedro\\Desktop\\chromedriver.exe')
        self.driver.get('https://web.whatsapp.com/')
        self.corrente_1 = '''Quer saber Mais ? Entre em https://www.nytimes.com/2020/02/21/us/politics/bernie-sanders-russia.html'''
        self.corrente_2 = '''Entre tambem em nosso grupo NY: https://chat.whatsapp.com/blablabla'''
        self.groups = ['Grupo - 1', 'Grupo - 2', 'Grupo - 3'] # Insert the groups that you want
        
    
    def sleep_time(self):
        time.sleep(4)

    def message(self):
       
        for grupo in self.groups:
            self.sleep_time()
            varible_group = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']") # Will find all spans who is related to the groups at the list
            self.sleep_time()

            varible_group.click() #Click on the group
            chat = self.driver.find_element_by_class_name("_13mgZ") # Look for Text box (The biggest one)
            self.sleep_time()
            
            chat.click() # Click again to enter on that
            chat.send_keys(self.corrente_1) #Use this func to send the text that you want to
            ActionChains(self.driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
           
            chat.send_keys(self.corrente_2) # Second part of the text
            button = self.driver.find_element_by_xpath("//span[@data-icon='send']") # Find the button          
            self.sleep_time()
            
            button.click()
            self.sleep_time()


if __name__ == '__main__':
    bot_object = BotWpp()
    time.sleep(30) # I'm doing like this, because we need time to scan the QR Code
    bot_object.message()