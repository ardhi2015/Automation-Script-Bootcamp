from selenium import webdriver
import unittest

from Locators import Locators
from TestData import TestData
from Pages import LandingPage


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=TestData.CHROME_PATH)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

class Landingpage(BaseTest):
    def test_landingpagee(self):
        self.landingpage = LandingPage(self.driver)

        self.landingpage.beranda()
        with self.subTest(msg="beranda"):
            element_text_pelayanan = self.landingpage.get_text(Locators.PELAYANAN_TERBAIK)
            self.assertEqual("Pelayanan Terbaik Dari Kami", element_text_pelayanan)

        self.landingpage.tabungan()
        with self.subTest(msg="tabungan"):
            element_text_tabungan = self.landingpage.get_text(Locators.TABUNGAN_DP_HUNIAN)
            self.assertEqual("Tabungan DP Hunian", element_text_tabungan)

        self.landingpage.kpr()
        with self.subTest(msg="kpr"):
            element_text_kpr = self.landingpage.get_text(Locators.KEMUDAHAN_PENGAJUAN)
            self.assertEqual("Kemudahan\nPengajuan KPR", element_text_kpr)

        self.landingpage.download()
        with self.subTest(msg="download"):
            element_text_download = self.landingpage.get_text(Locators.WE_HELP_YOU)
            self.assertEqual("We Help YouMake Your Dream\nCome Ture", element_text_download)

        self.landingpage.tentang()
        with self.subTest(msg="tentang"):
            element_text_tentang = self.landingpage.get_text(Locators.ZENIA_FOOTER)
            self.assertEqual("Follow Sosial Media Kami", element_text_tentang)

# belum ada isine

        # self.landingpage.google_play()
        # with self.subTest(msg="google_play"):
        #     element_text_google_play = self.landingpage.get_text(Locators.HASIL_GOOGLE_PLAY)
        #     self.assertEqual("Tabungan DP Hunian", element_text_google_play)
        #
        # self.landingpage.facebook()
        # with self.subTest(msg="facebook"):
        #     element_text_facebook = self.landingpage.get_text(Locators.HASIL_FACEBOOK)
        #     self.assertEqual("Tabungan DP Hunian", element_text_facebook)
        #
        # self.landingpage.instagram()
        # with self.subTest(msg="facebook"):
        #     element_text_instagram = self.landingpage.get_text(Locators.HASIL_INSTAGRAM)
        #     self.assertEqual("Tabungan DP Hunian", element_text_instagram)
        #
        # self.landingpage.twitter()
        # with self.subTest(msg="facebook"):
        #     element_text_twitter = self.landingpage.get_text(Locators.HASIL_TWITTER)
        #     self.assertEqual("Tabungan DP Hunian", element_text_twitter)

if __name__ == "__main__":
    unittest.main()