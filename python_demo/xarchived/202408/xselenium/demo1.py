import time
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

url = 'https://www.baidu.com/'

chrome_option = ChromeOptions()
chrome_option.headless = True   # 后续应该用 --headless option
for option in [
    # 截图仍然无法获取devtools的内容
    # '--auto-open-devtools-for-tabs',
    '--dns-prefetch-disable',
    '--disable-translate',
    '--disable-extensions',
    '--disable-background-networking',
    '--safebrowsing-disable-auto-update',
    '--disable-sync',
    '--metrics-recording-only',
    '--disable-default-apps',
    '--no-first-run',
    '--disable-setuid-sandbox',
    '--hide-scrollbars',
    '--no-sandbox',
    '--no-zygote',
    '--autoplay-policy=no-user-gesture-required',
    '--disable-notifications',
    '--disable-permissions-api',
    '--ignore-certificate-errors',
    '--single-process',
    '--disable-gpu',
    '--disable-dev-shm-usage',
    '--use-fake-ui-for-media-stream',
    '--use-fake-device-for-media-stream',
    '--allow-file-access-from-files',
    f'--use-file-for-fake-video-capture=path/to/video',
    f'--use-file-for-fake-audio-capture=path/to/audio',
]:
    chrome_option.add_argument(option)
chrome_option.add_experimental_option('w3c', False)
chrome_option.add_experimental_option('perfLoggingPrefs', {'enableNetwork': True, 'enablePage': False})
chrome_option.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])

caps = DesiredCapabilities.CHROME.copy()
caps['loggingPrefs'] = {
    'browser': 'ALL',
    'performance': 'ALL',
}
caps['perfLoggingPrefs'] = {
    'enableNetwork': True,
    'enablePage': False,
    'enableTimeline': False
}

driver = Chrome(options=chrome_option, desired_capabilities=caps)

driver.get(url)
time.sleep(3)
driver.get_screenshot_as_file('test1.png')
driver.quit()