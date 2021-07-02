import time,random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://gabrielecirulli.github.io/2048/')

browser.implicitly_wait(10)
htmlElem = browser.find_element_by_tag_name('html')
game_massage = browser.find_element_by_class_name("game-message")
keys_list = [Keys.ARROW_UP,Keys.ARROW_DOWN,Keys.ARROW_RIGHT,Keys.ARROW_LEFT]

while game_massage.text == '':
    htmlElem.send_keys(random.choice(keys_list))

your_score = browser.find_element_by_class_name('score-container').text
best_score = browser.find_element_by_class_name('best-container').text

print(f"""
==========================
you score is: {your_score}
==========================
""")

browser.quit()
time.sleep(1)
