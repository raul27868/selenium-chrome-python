


#Identifica donde esta el driver de chrome
EXECUTABLE_PATH = '/usr/bin/chromedriver'

#Opciones del navegador 
#https://stackoverflow.com/questions/62889739/selenium-gives-timed-out-receiving-message-from-renderer-for-all-websites-afte
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
chrome_options.headless = True
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
chrome_options.add_argument('disable-infobars')
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument('--disable-gpu')

#chrome_prefs = {}
#chrome_options.experimental_options["prefs"] = chrome_prefs
#chrome_prefs["profile.default_content_settings"] = {"images": 2}
#chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}

 
 
 # options to prevent TIMEOUTS
chrome_options.add_argument("start-maximized"); #https://stackoverflow.com/a/26283818/1689770
chrome_options.add_argument("enable-automation"); #https://stackoverflow.com/a/43840128/1689770
chrome_options.add_argument("--no-sandbox"); #https://stackoverflow.com/a/50725918/1689770
chrome_options.add_argument("--disable-infobars"); #https://stackoverflow.com/a/43840128/1689770
chrome_options.add_argument("--disable-dev-shm-usage"); #https://stackoverflow.com/a/50725918/1689770
chrome_options.add_argument("--disable-browser-side-navigation"); #https://stackoverflow.com/a/49123152/1689770
chrome_options.add_argument("--disable-gpu"); #https://stackoverflow.com/questions/51959986/how-to-solve-selenium-chromedriver-timed-out-receiving-message-from-renderer-exc
chrome_options.add_argument("--disable-features=VizDisplayCompositor"); #https://stackoverflow.com/questions/55373625/getting-timed-out-receiving-message-from-renderer-600-000-when-we-execute-selen
chrome_options.add_argument("--force-device-scale-factor=1")

chrome_options.add_argument("--window-size=1920,10536")
 
def save_screenshot(driver , path )  :
    # Ref: https://stackoverflow.com/a/52572919/

    #Si la pagina es muy grande se pruduce un errror de timeout . Se puede solventar eliminando contenido de la pagina
    # En el ejemplo se borran los <li data-stid="property-listing">
    #     body = driver.find_element_by_tag_name('body')
    #     driver.execute_script("[...document.querySelectorAll('li[data-stid=\"property-listing\"]')].map(el => el.parentNode.removeChild(el))")

    try:
      original_size = driver.get_window_size()
      required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
      required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
      driver.set_window_size(required_width, required_height)
      # driver.save_screenshot(path)  # has scrollbar
      driver.find_element_by_tag_name('body').screenshot(path)  # avoids scrollbar
      driver.set_window_size(original_size['width'], original_size['height'])
    except Exception as e:
      print("No es posible grabar")
      print("\tError:" ,e)


#Determina si un objeto del navegador es "clickeable"
def is_clickable( webelement):
    return webelement.is_displayed() and webelement.is_enabled()

 
 
