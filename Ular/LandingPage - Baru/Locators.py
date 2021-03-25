from selenium.webdriver.common.by import By

class Locators():

    # Navbar
    BERANDA = (By.XPATH, '/html/body/div/div[1]/nav/div/ul/li[1]/a/a')
    KALKULATOR = (By.XPATH, '/html/body/div/div[1]/nav/div/ul/li[2]/a/a')
    TABUNGAN = (By.XPATH, '/html/body/div/div[1]/nav/div/ul/li[3]/a/a')
    KPR = (By.XPATH, '/html/body/div/div[1]/nav/div/ul/li[4]/a/a')
    DOWNLOAD = (By.XPATH, '/html/body/div/div[1]/nav/div/ul/li[6]/a/button')
    TENTANG = (By.XPATH, '/html/body/div/div[1]/nav/div/ul/li[5]/a/a')

    # Landing Page Locators
    PELAYANAN_TERBAIK = (By.CSS_SELECTOR, "#root > div.home > div.service__section > div > h1")
    CARI_TAHU = (By.CSS_SELECTOR, "#kalkulator > div > div > div.col-kalkulator > div > div.top-line-kalkulator")
    TABUNGAN_DP_HUNIAN = (By.CSS_SELECTOR, "#tabungan > div > div > div:nth-child(1) > div > div.top-line1")
    KEMUDAHAN_PENGAJUAN = (By.CSS_SELECTOR, "#kpr > div > div > div:nth-child(1) > div > div.top-line2")
    WE_HELP_YOU = (By.CSS_SELECTOR, "#download > div > div > div:nth-child(1) > div > div.top-line2")
    ZENIA_FOOTER = (By.CSS_SELECTOR, "#root > div:nth-child(4) > section > p")

    # Kalkulator Locators
    UMUR_SAAT_INI = (By.CSS_SELECTOR, "#kalkulator > form > div:nth-child(2) > input")
    PENGHASILAN_PERBULAN = (By.CSS_SELECTOR, "#kalkulator > form > div:nth-child(4) > input")
    CICILAN_LAINNYA = (By.CSS_SELECTOR, "#kalkulator > form > div:nth-child(6) > input")
    HITUNG = (By.CSS_SELECTOR, "#kalkulator > form > button")
    HASIL_KALKULATOR = (By.CSS_SELECTOR, "#kalkulator > div > div > div.kalkulator > div > div > div.card-body > h6")

    # Button Slider
    BUTTON_KIRI = (By.CSS_SELECTOR, "#__next > div:nth-child(2) > div > a.carousel-control-prev")
    BUTTON_KANAN = (By.CSS_SELECTOR, "#__next > div:nth-child(2) > div > a.carousel-control-next")

    # Google Play
    BUTTON_GOOGLE_PLAY = (By.CSS_SELECTOR, "000")
    HASIL_GOOGLE_PLAY = (By.CSS_SELECTOR, "000")

    # Social Media Kami
    FACEBOOK = (By.CSS_SELECTOR, "000")
    INSTAGRAM = (By.CSS_SELECTOR, "000")
    TWITTER = (By.CSS_SELECTOR, "000")
    HASIL_FACEBOOK = (By.CSS_SELECTOR, "000")
    HASIL_INSTAGRAM = (By.CSS_SELECTOR, "000")
    HASIL_TWITTER = (By.CSS_SELECTOR, "000")