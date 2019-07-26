# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver import FirefoxOptions
import unittest, time, re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.contrib.auth.models import User
# from bookkeeping.models import Book, BookChargeSheet
from django.test import TestCase
# from django.db.migrations.executor import MigrationExecutor
# from django.db.migrations import executor


class SetUpModelTest(TestCase):

    def test_string_representation(self):
        u = self.create_user()
        self.assertTrue(isinstance(u, User))
        self.assertEqual(str(u), u.username)

    def create_user(self):
        return User.objects.create(username='testadmin', password='admin@123', is_superuser=True, is_staff=True)


class AppDynamicsAdminLoginJob(unittest.TestCase):
    def setUp(self):
        # opts = FirefoxOptions()
        # opts.add_argument("-headless")
        # self.driver = webdriver.Firefox(firefox_options=opts)

        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='All'])[1]/following::a[1]").click()
        driver.find_element_by_link_text("Sign In / Register").click()
        driver.find_element_by_id("login_username").click()
        driver.find_element_by_id("login_username").clear()
        driver.find_element_by_id("login_username").send_keys("admin")
        driver.find_element_by_id("login_password").clear()
        driver.find_element_by_id("login_password").send_keys("admin@123")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='*'])[2]/following::button[1]").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)


class AppDynamicsLogOutJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='All'])[1]/following::a[1]").click()
        driver.find_element_by_link_text("Sign In / Register").click()
        driver.find_element_by_id("login_username").click()
        driver.find_element_by_id("login_username").clear()
        driver.find_element_by_id("login_username").send_keys("admin")
        driver.find_element_by_id("login_password").clear()
        driver.find_element_by_id("login_password").send_keys("admin@123")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='*'])[2]/following::button[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='admin'])[1]/following::a[1]").click()
        driver.find_element_by_link_text("Sign Out").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
