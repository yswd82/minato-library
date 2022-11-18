"""module docstring"""
# -*- coding: utf-8 -*-
from selenium.webdriver.common.alert import Alert
from .page import HomePage, LoginPage, PortalPage, LentStatusPage



class LibraryBase:
    pass


class MinatoLibrary(LibraryBase):
    """_summary_

    Args:
        LibraryBase (_type_): _description_

    Returns:
        _type_: _description_
    """
    home_url = "https://www.lib.city.minato.tokyo.jp/licsxp-opac/OpacInitLoginAction.do?subSystemFlag=0&yoycartflg=undefined"

    def __init__(self, driver):
        """_summary_

        Args:
            driver (_type_): _description_
        """

        self.driver = driver
        self.driver.get(self.home_url)

        self.current_page = HomePage(driver)

        self.current_page = self.current_page.click_login()

    def login(self, card_number:str, password:str):
        """_summary_

        Args:
            card_number (_type_): _description_
            password (_type_): _description_
        """
        if isinstance(self.current_page, LoginPage):

            self.current_page.input_card_number(card_number)
            self.current_page.input_password(password)
            self.current_page = self.current_page.click_login()

            # 予約資料か延滞があった場合のダイアログを抑止
            Alert(self.driver).accept()

    def lent_status(self) -> list:
        res = []
        if isinstance(self.current_page, PortalPage):
            self.current_page = self.current_page.click_lent_status()

        if isinstance(self.current_page, LentStatusPage):
            res = self.current_page.get_lent_status()

        return res
