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

	#clickButtonNewComputer
	button = driver.find_element_by_id("add")
	button.click()
	time.sleep(5)

	#InputValueComputerName
	computername = driver.find_element_by_id("name")
	computername.send_keys("Test Sugita")

	#InputValueIntroduced
	introduced = driver.find_element_by_id("introduced")
	introduced.send_keys("2021-10-10")

	#InputValueDiscontinued
	discontinued = driver.find_element_by_id("discontinued")
	discontinued.send_keys("2022-10-10")

	#InputValueCompany
	driver.find_element_by_xpath("//select[@name='company']/option[text()='RCA']").click()
	time.sleep(3)

	driver.find_element_by_xpath("//input[@type='submit' and @value='Create this computer']").click()

	time.sleep(3)

	#driver.quit()
	print("Done")
