from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains as chains

from Locators import Locators
from TestData import TestData


class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).send_keys(text)

    def get_text(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).text

    def is_visible(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return bool(element)
        except TimeoutException:
            return False


class LandingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def beranda(self):
        self.click(Locators.BERANDA)
        self.is_visible(Locators.PELAYANAN_TERBAIK)

    def kalkulator(self):
        self.click(Locators.KALKULATOR)
        self.enter_text(Locators.UMUR_SAAT_INI, TestData.UMUR_SAAT_INI)
        self.enter_text(Locators.PENGHASILAN_PERBULAN, TestData.PENGHASILAN_BULAN)
        self.enter_text(Locators.CICILAN_LAINNYA, TestData.CICILAN_LAINNYA)
        self.click(Locators.HITUNG)
        self.is_visible(Locators.HASIL_KALKULATOR)

    def tabungan(self):
        self.click(Locators.TABUNGAN)
        self.is_visible(Locators.TABUNGAN_DP_HUNIAN)

    def kpr(self):
        self.click(Locators.KPR)
        self.is_visible(Locators.KEMUDAHAN_PENGAJUAN)

    def download(self):
        self.click(Locators.DOWNLOAD)
        self.is_visible(Locators.WE_HELP_YOU)

    def tentang(self):
        self.click(Locators.TENTANG)
        self.is_visible(Locators.ZENIA_FOOTER)

    def googleplay(self):
        self.click(Locators.BUTTON_GOOGLE_PLAY)
        self.is_visible(Locators.HASIL_GOOGLE_PLAY)

    def facebook(self):
        self.click(Locators.FACEBOOK)
        self.is_visible(Locators.HASIL_FACEBOOK)

    def instagram(self):
        self.click(Locators.INSTAGRAM)
        self.is_visible(Locators.HASIL_INSTAGRAM)

    def twitter(self):
        self.click(Locators.TWITTER)
        self.is_visible(Locators.HASIL_TWITTER)
