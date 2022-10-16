import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display

email = 'logjefferson6@gmail.com'
password = 'xonB23Y5'
path='/content/loot/chromedriver.exe'


if __name__ == '__main__':
    # destroy display
    display = Display(visible=0, size=(800, 600))
    display.start()
    ## install stuff
    chrome_options = Options()
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_extension('tamper.crx')
    driver = webdriver.Chrome(executable_path=path,options=chrome_options)

    ## install focus
    # go to install page
    time.sleep(10)
    print('installed tampermonkey')
    driver.get("https://greasyfork.org/en/scripts/429635-always-on-focus")
    driver.execute_script("document.querySelector('.install-link').click()")
    for i in range(3):
        print(i)
        time.sleep(1)

    # problem starts here. cannot find element although there is. cannot navigate to this window
    # fixed by switching to the "userscript installation" window
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(by='id', value='input_SW5zdGFsbF91bmRlZmluZWQ_bu').click()
    print('installed script')

    # close everything and reopen
    
    #-1  = tampermonkey home
    #0 = always on focus
    #1 = userscript installation
    driver.switch_to.window(driver.window_handles[0])
    driver.close()
    driver.switch_to.window(driver.window_handles[-1])
    driver.get('https://loot.tv/account/login')

    #login
    driver.find_element(by='xpath',value='//*[@id="__next"]/div/div[2]/div[2]/div/div/div[2]/div[1]/input').send_keys(email)
    driver.find_element(by='xpath',value='//*[@id="__next"]/div/div[2]/div[2]/div/div/div[2]/div[2]/input').send_keys(password)
    driver.find_element(by='xpath',value='//*[@id="__next"]/div/div[2]/div[2]/div/div/div[3]/button').click()
    print('logged in')
    time.sleep(5)

    # navigate to first video
    driver.execute_script('''window.open("https://loot.tv/video/671788","_blank");''')
    print('started watching')

    while True:
        points=driver.find_element(by='xpath',value='//*[@id="__next"]/div/div[1]/div[5]/div/a[1]/div/span').text
        print(points)
        time.sleep(300)


    
