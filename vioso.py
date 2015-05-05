#References
#http://stackoverflow.com/questions/5419888/reading-from-a-frequently-updated-file

import time
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("thefile",  help="input file to check")

    driver = webdriver.Chrome()
    driver.get("http://touchpianist.com")


    args = parser.parse_args()
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "pixi-canvas")))
        loglines = follow(open(args.thefile, 'r'))
        for line in loglines:
            element.click()
    finally:
        driver.quit()
