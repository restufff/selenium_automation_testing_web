from telnetlib import XASCII
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import Select


@pytest.yield_fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("http://old-demo.securehr.net/")
    yield driver


def test_login(driver):
    # Admin Login
    username = driver.find_element_by_xpath(
        '//div[@class="form-bottom"]//input[@name="nip"]')
    username.send_keys("Q04570")
    password = driver.find_element_by_xpath(
        '//div[@class="form-bottom"]//input[@name="password"]')
    password.send_keys("phiR0@2016")
    password.send_keys(Keys.ENTER)
    driver.implicitly_wait(2)

    # Add Category
    pengaturan = driver.find_element_by_xpath(
        '//ul[@id="side-menu"]/li[3]')
    pengaturan.click()
    management = driver.find_element_by_xpath(
        '//*[@id="side-menu"]/li[3]/ul/li/a')
    management.click()
    category = driver.find_element_by_xpath(
        '//*[@id="side-menu"]/li[3]/ul/li/ul/li[1]/a')
    category.click()

    # Click Button Tambah in new Frame
    driver.switch_to.frame(
        driver.find_element_by_xpath('//iframe[@id="title"]'))
    tambah = driver.find_element_by_xpath(
        '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/a[1]')
    tambah.click()

    # Choose Referensi
    referensi = driver.find_element_by_xpath('//*[@id="ctrRef"]')
    optionSelect = Select(referensi)
    optionSelect.select_by_value('RCA-000129')
    driver.implicitly_wait(2)

    # Input judul kategori
    driver.find_element(
        By.XPATH, '/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td[2]/input').send_keys('Mesin Foto Copy')
    driver.implicitly_wait(3)
    driver.find_element(
        By.XPATH, '//*[@id="cd"]'
    ).send_keys('Ini Untuk Keperluan Testing Aja Ko' + Keys.ENTER)

    # Navigate IFRAME to first page
    driver.switch_to.default_content()
    driver.find_element(
        By.XPATH, '//*[@id="tt"]/div[1]/div[3]/ul/li[2]/a[2]').click()

    # Adding Item with Item's that already input in RESOURCE CATEGORY
    ResourceItem = driver.find_element(
        By.XPATH, '//*[@id="side-menu"]/li[3]/ul/li/ul/li[2]/a'
    )

    # Close Frame
    ResourceItem.click()

    # Change Frame Add Items
    driver.switch_to.frame(
        driver.find_element_by_xpath('//iframe[@id="title"]'))
    driver.find_element_by_xpath(
        '//a[@href="/resources/item.php?act=add&display=&"]').click()

    # Choose Items
    # Fill Kategori
    ItemsOption = driver.find_element(
        By.XPATH, '//*[@id="rca_id"]')
    ItemsOptionSelect = Select(ItemsOption)
    ItemsOptionSelect.select_by_value('RCA-000133')

    # Fill Nama Aset
    driver.find_element(
        By.XPATH, '//*[@id="rsc_name"]').send_keys('Mesin Foto Copy Versi Super')

    # Fill in Keterangan
    driver.find_element(
        By. XPATH, '//*[@id="desc"]').send_keys('Ini Testing Penting')

    # Check satuan waktu
    driver.find_element(
        By. XPATH, '//form[@id="forem"]//input[@value="daily"]').click()

    # Choose Tipe Penggunaan
    driver.find_element(
        By. XPATH, '//*[@id="forem"]/table[1]/tbody/tr[6]/td[2]/input[1]'
    ).click()

    # Fill in Atribut
    tahun = driver.find_element(By.XPATH, '//*[@id="item_manufactured[]"]')
    tahunOption = Select(tahun)
    tahunOption.select_by_value('50')
    driver.find_element(
        By.XPATH, '//*[@id="items"]/tbody/tr[2]/td[1]/input[1]').send_keys('Judul Testing Aja')

    # Upload FIle
    upload = driver.find_element(
        By.XPATH, '//*[@id="items"]/tbody/tr[2]/td[1]/input[3]'
    )
    upload.send_keys('F:\QA Automation\Selenium\image\koin.jpeg')
    driver.find_element(
        By.XPATH, '//*[@id="items"]/tbody/tr[2]/td[2]/input[1]').send_keys('10.01.50')
    driver.find_element(
        By.XPATH, '//*[@id="items"]/tbody/tr[2]/td[2]/input[2]').send_keys('FCMACH-01')
    lokasi = driver.find_element(By.XPATH, '//*[@id="item_location[]"]')
    lokasiOption = Select(lokasi)
    lokasiOption.select_by_value('5591')
    driver.find_element(
        By.XPATH, '//*[@id="items"]/tbody/tr[2]/td[4]/input[3]').send_keys('Rudi')
    driver.implicitly_wait(20)
    driver.find_element(
        By.XPATH, '//*[@id="nm_peg__autocomplete_list"]/li[1]'
    ).click()
    driver.find_element(
        By.XPATH, '//*[@id="forem"]/table[3]/tbody/tr/td/input[2]'
    ).click()
