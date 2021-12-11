from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os 
import time
#import ait
#import autoit
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException



class youtube(object):
	# global driver
	global scroll_bar
	scroll_bar = 0
	"""docstring for youtube"""
	def __init__(self, arg):
		super(youtube, self).__init__()
		self.arg = arg
		print('youtube driver initiated')
		scroll_bar = 0
		
	def open(self):
		global driver
		driver = webdriver.Chrome(executable_path=os.getcwd() + r'/tools/chromedriver.exe')  
		driver.get("https://www.youtube.com")
		scroll_bar = 0
		print("open")

	def download_video(self):
		print('downloading: ' + driver.current_url)
		path = os.getenv('USERPROFILE') + r'/Videos/%(title)s'
		os.system('"' + os.getcwd() + '/tools/youtube-dl.exe" -f best -o ' + path +  ' ' + driver.current_url);
		#youtube-dl2 -f best -o "C:\Users\ICTMS\Videos\%(title)s" https://www.youtube.com/watch?v=mp_piRVzx7Y

	def search(self,criteria):
		print("searching...")
		search = driver.find_element_by_name("search_query")
		try:
	 		
	 		search.send_keys(criteria)
	 		search.send_keys(Keys.RETURN)
	 		scroll_bar = 0
	 		
	 		return True
		except:
			return False

	def scroll_down(self):
		try:
			driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN) 
		except:
			return 0

	def scroll_up(self):
		try:
			driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_UP) 
		except:
			return 0

	def link_click(self,link_string):

		try:
			link = driver.find_element_by_partial_link_text(link_string)
			link.click()
			scroll_bar = 0
			print("link clicked")
			return True
		except:
			print("Unable to locate link!")
			return False

	def close(self):
		try:
			driver.close()
			print("closed")
			return True
		except:
			return False
	
	def getResultCount(self):
		try:
			results = driver.find_elements_by_class_name("style-scope ytd-video-renderer")
			return len(results)
		except:
			return 0

	def waitForSearchResult(self):
		print("Waiting for page to load completely!")
		try:
		    myElem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME , 'style-scope ytd-topbar-menu-button-renderer')))
		    print("Page is ready!")
		    time.sleep(1)
		    return True
		except TimeoutException:
		    print("Loading took too much time!")
		    return False


# youtube = youtube('none')
# youtube.open()
# youtube.scroll_down(400)
# time.sleep(1)
# youtube.scroll_down(400)
# time.sleep(1)
# youtube.scroll_down(400)
# time.sleep(1)
# youtube.scroll_down(400)
# youtube.close()



# youtube = youtube('none')
# youtube.open()
# if youtube.search('funny'):
# 	if youtube.waitForSearchResult():
# 		youtube.link_click('TRY NOT TO LAUGH')
		
# 		time.sleep(5)
# 		youtube.download_video()

# 		time.sleep(5000)
# 		youtube.close()

