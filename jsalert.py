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
	driver.get('https://the-internet.herokuapp.com/javascript_alerts')
	time.sleep(5)
	
	#ClicforJSAlert
	driver.find_element_by_xpath("//button[text()='Click for JS Alert']").click()
	driver.switch_to.alert.accept()
	time.sleep(5)

	#ClickforJSConfirmOK
	driver.find_element_by_xpath("//button[text()='Click for JS Confirm']").click()
	driver.switch_to.alert.accept()
	time.sleep(5)

	#ClickforJSConfirmCANCEL
	driver.find_element_by_xpath("//button[text()='Click for JS Confirm']").click()
	driver.switch_to.alert.dismiss()
	time.sleep(5)


	#ClickforJSPrompt
	driver.find_element_by_xpath("//button[text()='Click for JS Prompt']").click()
	time.sleep(3)
	driver.switch_to.alert.send_keys("Testing")
	time.sleep(3)
	driver.switch_to.alert.accept()
	time.sleep(3)
	

	#driver.quit()
	print("Done")