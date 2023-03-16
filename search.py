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
	driver.get('http://computer-database.gatling.io/computers')
	#SearchColumnComputer

	search = driver.find_element_by_id("searchbox")

	#InputValue
	search.send_keys("ARRA")

	time.sleep(15)
	
	button = driver.find_element_by_id("searchsubmit")
	
	button.click()

	time.sleep(15)

	#driver.quit()
	print("Done")
