from selenium.webdriver.common.by import By

class Locators():

    # Navbar
    BERANDA = (By.XPATH, '//*[@id="responsive-navbar-nav"]/div/a[1]')
    KALKULATOR = (By.XPATH, '//*[@id="responsive-navbar-nav"]/div/a[2]')
    TABUNGAN = (By.XPATH, '//*[@id="responsive-navbar-nav"]/div/a[3]')
    KPR = (By.XPATH, '//*[@id="responsive-navbar-nav"]/div/a[4]')
    DOWNLOAD = (By.XPATH, '//*[@id="responsive-navbar-nav"]/div/a[5]')
    TENTANG = (By.XPATH, '//*[@id="responsive-navbar-nav"]/div/a[6]')

    # Landing Page Locators
    PELAYANAN_TERBAIK = (By.CSS_SELECTOR, "#__next > div.serviceProgram > div > div:nth-child(1) > div > h3")
    CARI_TAHU = (By.CSS_SELECTOR, "000")
    TABUNGAN_DP_HUNIAN = (By.CSS_SELECTOR, "#tabungan > div > div.col-md-auto > h3")
    KEMUDAHAN_PENGAJUAN = (By.CSS_SELECTOR, "#kpr > div:nth-child(1) > div.my-auto.col > h3")
    WE_HELP_YOU = (By.CSS_SELECTOR, "#download > div > div > div.leftContent.col > div:nth-child(1) > h3")
    ZENIA_FOOTER = (By.CSS_SELECTOR, "#footer > div > div:nth-child(3) > div.rightFooter1.row")

    # Kalkulator Locators
    UMUR_SAAT_INI = (By.CSS_SELECTOR, "000")
    PENGHASILAN_PERBULAN = (By.CSS_SELECTOR, "000")
    CICILAN_LAINNYA = (By.CSS_SELECTOR, "000")
    HITUNG = (By.CSS_SELECTOR, "000")
    HASIL_KALKULATOR = (By.CSS_SELECTOR, "000")

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