from lib2to3.pgen2 import driver
import unittest
import time
from urllib import response
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAdmin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_addUser(self):
        driver=self.driver
        driver.maximize_window()
        #Open Web
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        time.sleep(3)

        #Proses Login
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(2)

        #Proses Add Data
        driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a/b").click()
        time.sleep(2)
        driver.find_element(By.ID,"btnAdd").click()
        time.sleep(1)

        select = Select(driver.find_element(By.ID,"systemUser_userType"))
        select.select_by_visible_text('Admin')

        role = driver.find_element(By.ID,"systemUser_employeeName_empName")
        role.send_keys("Fion")
        role.send_keys(Keys.ARROW_DOWN)
        role.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.find_element(By.ID,"systemUser_userName").send_keys("fairuz01")

        select = Select(driver.find_element(By.ID,"systemUser_status"))
        select.select_by_visible_text('Enabled')

        driver.find_element(By.ID,"systemUser_password").send_keys("admin123")
        driver.find_element(By.ID,"systemUser_confirmPassword").send_keys("admin123")

        driver.find_element(By.ID,"btnSave").click()
        time.sleep(5)

        #Filter Data
        driver.find_element(By.ID,"searchSystemUser_userName").send_keys("admin123")
        driver.find_element(By.ID,"searchBtn").click()
        time.sleep(2)

        # Verifikasi Data
        response_data_username = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr/td[2]").text
        response_data_userRole = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr[1]/td[3]").text
        response_data_employeeName = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr[1]/td[4]").text
        response_data_status = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr[1]/td[5]").text

        self.assertEqual(response_data_username,"fairuz01")
        self.assertEqual(response_data_userRole,"Admin")
        self.assertEqual(response_data_employeeName,"Fiona Grace")
        self.assertEqual(response_data_status,"Enabled")

    def test_b_userAdd_Negative_Scenario(self):
        driver=self.driver
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        time.sleep(3)

        driver.find_element(By.ID,"txtUsername").send_keys("Admin")
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(2)

        driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a/b").click()
        time.sleep(2)
        driver.find_element(By.ID,"btnAdd").click()
        time.sleep(1)

        select = Select(driver.find_element(By.ID,"systemUser_userType"))
        select.select_by_visible_text('Admin')

        role = driver.find_element(By.ID,"systemUser_employeeName_empName")
        role.send_keys("Fion")
        role.send_keys(Keys.ARROW_DOWN)
        role.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.find_element(By.ID,"systemUser_userName").send_keys("fairuz01")

        select = Select(driver.find_element(By.ID,"systemUser_status"))
        select.select_by_visible_text('Enabled')

        driver.find_element(By.ID,"systemUser_password").send_keys("testing123")
        driver.find_element(By.ID,"systemUser_confirmPassword").send_keys("testing123")

        driver.find_element(By.ID,"btnSave").click()
        time.sleep(1)

        response_data_validationError = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[3]/span").text

        self.assertEqual(response_data_validationError,"Already exists")


    def test_c_editUser(self):
        driver=self.driver
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(2)

        driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a/b").click()
        time.sleep(2)

        driver.find_element(By.ID,"searchSystemUser_userName").send_keys("fairuz01")
        driver.find_element(By.ID,"searchBtn").click()
        time.sleep(2)

        driver.find_element(By.LINK_TEXT,"fairuz01").click()
        time.sleep(2)

        driver.find_element(By.ID,"btnSave").click()
        time.sleep(1)

        select = Select(driver.find_element(By.ID,"systemUser_userType"))
        select.select_by_visible_text("ESS")
        
        driver.find_element(By.ID,"btnSave").click()
        time.sleep(5)

        driver.find_element(By.ID,"searchSystemUser_userName").send_keys("fairuz01")
        driver.find_element(By.ID,"searchBtn").click()
        time.sleep(2)
        
        response_data_role = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr[1]/td[3]").text

        self.assertEqual(response_data_role,"ESS")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
