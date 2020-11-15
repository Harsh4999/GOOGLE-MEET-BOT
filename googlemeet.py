from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import speech_recognition as sr
options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")
options.add_argument("--window-size=800,600")
options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,     # 1:allow, 2:block
    "profile.default_content_setting_values.media_stream_camera": 1,
     "profile.default_content_setting_values.notifications": 2
  })
tab_url = ['https://meet.google.com/frk-dsyh-jby' , 'https://meet.google.com/kmq-qppj-kdc' , 'https://meet.google.com/iig-euva-bxv']  

j=0
p=5 #ENTER TIME BETWEEN 2 CLASSES
while j<=3:
	driver = webdriver.Chrome(chrome_options=options)
	driver.get('https://gmail.com/')
	search = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
	search.send_keys('') #ENTER YOUR GMAIL ADDRESS
	button = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]')
	button.click()
	driver.implicitly_wait(5)
	driver.find_element_by_name('password').send_keys('') #ENTER YOUR GMAIL PASSWORD
	driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()
	driver.implicitly_wait(15)


	driver.execute_script("window.open('');")
	driver.switch_to.window(driver.window_handles[1])
	driver.get(tab_url[j])
	driver.implicitly_wait(3)
	driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span').click()
	#driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[6]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span').click()
	#Turning Audio & Video off.
	driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[3]/div/div/span/span').click()
	#driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[6]/div[3]/div[9]/div[2]/div[3]/div/div/span').click()
	#driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[6]/div[3]/div[9]/div[2]/div[1]/div/div/div/span/span').click()
	
	#driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[6]/div[3]/div[6]/div[3]/div/div[2]/div[1]/span/span/div').click()
	#q = driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[6]/div[3]/div[3]/div/div[2]/div[2]/div[1]/div[1]')
	#print(q)
	
	n = 18 #ENETER CLASS TIME IN SECONDS 
	t=n/3
	st=time.time()

	driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[6]/div[3]/div/div[2]/div[3]/span/span/div/div').click()
	#driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[6]/div[3]/div[6]/div[3]/div/div[2]/div[3]/span/span/div').click()
	while True:
		ct=time.time()
		et=ct-st
		if(et<n):

			r = sr.Recognizer()
			with sr.Microphone() as source:
				print('BOLO : ')
				audio = r.listen(source)

				try:
					text = r.recognize_google(audio)
					print('Said : {}'.format(text))
					if(text.find('Harsh') != -1 or text.find('harsh') != -1 or text.find('161') != -1): #Enter your name when sir/mam calls your name 
						#now enter your response to the name call I have written 7161 you can replace it with your response
						driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[1]/div[1]/div[2]/textarea').send_keys('7161')
						driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[2]/span').click()
						continue
					else:
						print('NOT FOUND')
						continue


					#driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[6]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[2]/span').click()
				except:
					print('Sorry')
		else:
			break			
		
		#	time.sleep(t)
		#driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[1]/div[1]/div[2]/textarea').click().send_keys('7161')
		#driver.implicitly_wait(3)
		#time.sleep(2)
		#driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[6]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[2]/span/span/span/svg').click()
		#	i+=1


	#time.sleep(n) 
	driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div').click()
	#driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[6]/div[3]/div[9]/div[2]/div[2]/div').click()
	driver.quit()
	time.sleep(p)
	j+=1

