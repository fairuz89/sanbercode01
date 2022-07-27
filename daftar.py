import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestDaftar(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_success_daftar(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("fairuz04")
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("fairuz04@gmail.com")
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("123456")
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('berhasil', response_data)
        self.assertEqual(response_message, 'created user!')

    def test_a_failed_daftar_dengan_email_sama(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("fairuz02")
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("fairuz02@gmail.com")
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("123456")
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Email sudah terdaftar, gunakan Email lain', response_data)
        self.assertEqual(response_message, 'Gagal Registrasi')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()