from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException as EI
import unittest
import time

class Instahrye(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Edge()
        #self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
    def test_apply(self):
        driver = self.driver
        try:
            fwait = WebDriverWait(driver, 140, poll_frequency=3, ignored_exceptions=[EI])
            driver.maximize_window()
            driver.get("https://www.instahyre.com/")
            driver.implicitly_wait(5)
            loginelement = driver.find_element(By.XPATH, '//*[@id="nav-user-login"]')
            loginelement.click()
            time.sleep(1)
            driver.implicitly_wait(50)
            emailelement = fwait.until(
                EC.presence_of_element_located((By.XPATH,'//*[@id="email"]'))
            )
            emailelement.send_keys("hariprasad2691997@gmail.com")

            passwordelement = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
            )
            passwordelement.send_keys("Ghp@1234567890")

            submitelement = driver.find_element(By.XPATH, '//*[@id="login-form"]/button')
            submitelement.click()
            time.sleep(2)
            driver.implicitly_wait(10)
            time.sleep(1)

            tabelement_allsoftware = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="search-allsoftware"]'))
            )
            time.sleep(3)
            tabelement_allsoftware.click()
            tabelement_wfh = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="search-wfh"]'))
            )
            time.sleep(3)
            #tabelement_wfh.click()
            print("wfh ended")
            tabelement_test = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="search-test"]'))
            )
            time.sleep(1)
            #tabelement_test.click()
            time.sleep(1)

            viewelement = fwait.until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="interested-btn"]'))
            )  
            viewelement.click()
            driver.implicitly_wait(10)
            print("View element found and clicked")
            time.sleep(2)
            driver.implicitly_wait(20)

            applyelement = fwait.until(
                EC.element_to_be_clickable((By.XPATH,'//*[@id="candidate-suggested-employers"]/div/div[3]/div/div/div[2]/div[3]/div[2]/div[2]/button'))
            )                                  
            applyelement.click()
            if not applyelement.is_displayed:
                driver.close()
            #errorelement = driver.find_element(By.XPATH, '//*[@id="messages"]/div/div/div/div/div')
            else:
                count=0
                while applyelement.is_displayed:
                    driver.implicitly_wait(5)
                    time.sleep(5)
                    applyelement.click()
                    count +=1   
                    if count % 50 == 0:
                        print("applied 50 jobswe are at break will take 5 sec to continue")
                        time.sleep(10)
                    if count % 500 == 0:
                        time.sleep(3)
                        driver.back()
                        print("Successfully applied for 500 jobs as per requirement")
                        logoutelement = driver.find_element(By.XPATH,'//*[@id="nav-candidates-logout"]')
                        logoutelement.click()
        except Exception as e:
            driver.back()
            logoutelement = driver.find_element(By.XPATH,'//*[@id="nav-candidates-logout"]')
            logoutelement.click()
            driver.quit()
        finally:
            #driver.implicitly_wait(40)
            driver.quit()
    def tearDown(self):
        #self.driver.implicitly_wait(40)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()






    