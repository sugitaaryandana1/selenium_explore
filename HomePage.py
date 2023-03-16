from selenium import webdriver
import time


# Main Function
if __name__ == '__main__':

	options = webdriver.ChromeOptions()
	options.add_argument("--start-maximized")
	options.add_argument('--log-level=3')

	# Provide the path of chromedriver present on your system.
	driver = webdriver.Chrome(executable_path="chromedriver",
							chrome_options=options)
	driver.set_window_size(2560,1600)
	driver.maximize_window()
	# Send a get request to the url
	driver.get('https://qa-interview.srcli.xyz/')
	time.sleep(10)

	#Login
	# Send a get request to the url
	driver.get('https://qa-interview.srcli.xyz/login')
	time.sleep(10)
	#inputUsername
	username = driver.find_element_by_xpath(".//*[@name='username']")
	username.send_keys('root')
	time.sleep(10)

	username = driver.find_element_by_xpath(".//*[@name='password']")
	username.send_keys('root123')
	time.sleep(10)

	driver.find_element_by_xpath("//input[@type='submit' and @value='Login']").click()
	time.sleep(10)
	

	#ListData
	# Send a get request to the url
	driver.get('https://qa-interview.srcli.xyz/data')
	time.sleep(10)

	start = driver.find_element_by_xpath(".//*[@name='start']")
	start.send_keys('2018-07-07')
	time.sleep(10)

	end = driver.find_element_by_xpath(".//*[@name='end']")
	end.send_keys('2018-07-07')
	time.sleep(10)

	driver.find_element_by_xpath("//input[@type='submit' and @value='Filter']").click()
	time.sleep(10)

	driver.get('https://qa-interview.srcli.xyz/logout')
	time.sleep(10)

	driver.get('https://qa-interview.srcli.xyz/test')
	time.sleep(10)
	#driver.quit()
	print("Done")
