from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")
options.add_argument("--window-size=800,600")
options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,     # 1:allow, 2:block
    "profile.default_content_setting_values.media_stream_camera": 1,
     "profile.default_content_setting_values.notifications": 2
  })
tab_url = ['' ,'' ,''] #ENTER ALL CLASS URL IN ORDER  
j=0
p=5 #ENTER TIME BETWEEN 2 CLASSES
while j<=3: #J SHOULD BE LESS THAN THE NUMBER OF URL TO ATTEND HERE PUT NUMBER OF URL INSTEAD OF 3
	driver = webdriver.Chrome(chrome_options=options)
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
	driver.get(tab_url[j])
	driver.implicitly_wait(15)
	driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[6]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span').click()

	driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[6]/div[3]/div[9]/div[2]/div[3]/div/div/span').click()
	driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[6]/div[3]/div[9]/div[2]/div[1]/div/div/div/span/span').click()
	n = 18 #ENETER CLASS TIME IN SECONDS 
	i=0
	t=n/3
	while i<3:
		time.sleep(t)
		if i==0:
			driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[6]/div[3]/div[6]/div[3]/div/div[2]/div[3]/span/span/div').click()
            #ENTER YOUR MESSAGE TO BE GIVEN IN CHAT-BOX AT BEGINING , MIDDLE & END OF CLASS eg = roll number, yes sir etc.WRITE WHERE I HAVE WRITTEN 7161
			driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[6]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[1]/div[1]/div[2]/textarea').send_keys('7161')
			time.sleep(2)
			#driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[6]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[2]/span/span/span/svg').click()
			driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[6]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[2]/span').click()
			i+=1

		else :
			driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[6]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[1]/div[1]/div[2]/textarea').send_keys('7161')
			time.sleep(2)
			driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[6]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[2]/span').click()
			#driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[6]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[2]/span/span/span/svg').click()
			i+=1
		if i==3:
			break


	time.sleep(n) 
	driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[6]/div[3]/div[9]/div[2]/div[2]/div').click()
	driver.quit()
	time.sleep(p)
	j+=1

