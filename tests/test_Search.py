import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from pages.homePage import HomePage
from pages.searchPage import SearchPage

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
        
    def test_search(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_searchbox("HP")
        time.sleep(2)
        search_Page = SearchPage(self.driver)
        assert search_Page.display_status_verify()

    def test_search_invalid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_searchbox("Honda")
        time.sleep(2)
        search_Page = SearchPage(self.driver)
        assert search_Page.retrieve_no_product_found.__eq__("There is no product that matches the search criteria.")

    def test_search_without_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_searchbox("")
        time.sleep(2)
        search_Page = SearchPage(self.driver)
        assert search_Page.retrieve_no_product_found.__eq__("There is no product that matches the search criteria.")
        