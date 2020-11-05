from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")
options.add_argument("--window-size=800,600")
options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2,     # 1:allow, 2:block
    "profile.default_content_setting_values.media_stream_camera": 2,
     "profile.default_content_setting_values.notifications": 2
  })
driver = webdriver.Chrome(chrome_options=options)
tab_url = 'https://meet.google.com/frk-dsyh-jby' #ENTER GOOGLE MEET URL
driver.get('https://gmail.com/')
search = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
search.send_keys('harsh.trivedi109881@marwadiuniversity.ac.in') #ENTER YOUR GMAIL ADDRESS
button = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]')
button.click()
driver.implicitly_wait(5)
driver.find_element_by_name('password').send_keys('Aupu@362') #ENTER YOUR GMAIL PASSWORD
driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()
driver.implicitly_wait(15)
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get(tab_url)
driver.implicitly_wait(15)
driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span').click()
driver.implicitly_wait(15)
driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[6]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span').click()
time.sleep(10) #ENETER CLASS TIME IN SECONDS 
driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[6]/div[3]/div[9]/div[2]/div[2]/div').click()

#time.sleep(40)
#driver.find_element_by_jsname('Qx7uuf').click()
#Qx7uuf
#driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[6]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span').click()
#chrome_options = Options()
#chrome_options.add_experimental_option("prefs", { "profile.default_content_setting_values.camera": 1})
#chrome_options.add_experimental_option("prefs", { "profile.default_content_setting_values.microphone": 1})
#desired_cap = chrome_options.to_capabilities()
#desired_cap.update({
#  'browser_version': '75.0',
#  'os': 'Windows',
#  'os_version': '10'
#})
#C:\\Users\\Infiniti\\Downloads\\chromedriver_win32\\chromedriver.exe


#C:\\chromedriver_win32\\chromedriver.exe