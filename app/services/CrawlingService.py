from selenium import webdriver
from selenium.webdriver.common.by import By
from ..model import Bankrupt
import os

PERSON_TEXT = 'חייב יחיד'
NO_INFO = 'אין מידע'


def get_chrome_driver():
    # Local
    # return webdriver.Chrome(
    #     executable_path="/Users/idzipris/workspace/Projects/Java/BankruptcyCrawler/chromedriver/chromedriver 4")

    # Heroku
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    return webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)


def get_bankrupts(ids):
    browser = get_chrome_driver()
    bankrupts = []
    for id in ids:
        bankrupt = Bankrupt.Bankrupt(id)
        if not id.isnumeric() or len(id) < 1:
            bankrupt.set_type(NO_INFO)
            bankrupts.append(bankrupt)
            continue
        browser.get('https://insolvency.justice.gov.il/poshtim/Main/Tikim/wfrmListTikim.aspx')
        browser.find_element_by_xpath("//input[@id='rngListTikim_txtPoshetID']").send_keys(id)
        browser.find_element_by_xpath("//input[@id='btnSearch']").click()

        details_elements = browser.find_elements(By.LINK_TEXT, 'פרטים')
        if len(details_elements) == 0:
            bankrupt.set_type(NO_INFO)
            bankrupts.append(bankrupt)
            continue
        details_elements[-1].click()
        bankrupt_type = browser.find_element(By.ID, 'bnrTikTopInfo_grdInfo_Label4_0').text
        bankrupt.set_type(bankrupt_type)
        if PERSON_TEXT in bankrupt_type:
            construct_person(browser, bankrupt)
        else:
            construct_company(browser, bankrupt)
        bankrupts.append(bankrupt)
    return bankrupts


def construct_person(browser, person):
    person.set_case_id(browser.find_element_by_id('bnrTikTopInfo_grdInfo_lblTikNoKanar_0').text)
    person.set_cancel_reason(browser.find_element_by_id('lstTikGeneralDetails_txtCancelReason').get_attribute('value'))
    person.set_case_status(browser.find_element_by_id('lstTikGeneralDetails_txtTikStatus').get_attribute('value'))
    person.set_authority(browser.find_element_by_id('lstTikGeneralDetails_txtRashutMetapelet').get_attribute('value'))
    person.set_cancel_date(
        browser.find_element_by_id('lstTikGeneralDetails_txtTzavCancellationDate').get_attribute('value'))
    person.set_bankruptcy_date(
        browser.find_element_by_id('lstTikGeneralDetails_txtTzavPshitaDate').get_attribute('value'))
    person.set_concentration_date(
        browser.find_element_by_id('lstTikGeneralDetails_txtTzavKinusDate').get_attribute('value'))


def construct_company(browser, company):
    company.set_case_id(browser.find_element_by_id('bnrTikTopInfo_grdInfo_lblTikNoKanar_0').text)
    company.set_case_status(browser.find_element_by_id('lstTikGeneralDetails_txtTikStatus').get_attribute('value'))
    company.set_authority(browser.find_element_by_id('lstTikGeneralDetails_txtRashutMetapelet').get_attribute('value'))
    company.set_destruction_date(
        browser.find_element_by_id('lstTikGeneralDetails_txtTzavPshitaDate').get_attribute('value'))
    company.set_delay_date(
        browser.find_element_by_id('lstTikGeneralDetails_txtTzavCancellationDate').get_attribute('value'))
