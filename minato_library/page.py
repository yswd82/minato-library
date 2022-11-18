"""module docstring"""
# -*- coding: utf-8 -*-
from dataclasses import dataclass
from .locators import (
    HomePageLocator,
    LoginPageLocator,
    PortalPageLocator,
    LentStatusPageLocator,
    ReservationStatusPageLocator,
)


class BasePage:
    """class docstring"""

    locator = None

    def __init__(self, driver) -> None:
        self.driver = driver


class HomePage(BasePage):
    """_summary_

    Args:
        BasePage (_type_): _description_
    """

    locator = HomePageLocator

    def click_login(self):
        """_summary_"""
        element = self.driver.find_element(*self.locator.BUTTON_LOGIN)
        element.click()
        return LoginPage(self.driver)


class LoginPage(BasePage):
    """class docstring"""

    locator = LoginPageLocator

    def input_card_number(self, card_number):
        """_summary_

        Args:
            card_number (_type_): _description_
        """
        element = self.driver.find_element(*self.locator.INPUT_CARD_NUMBER)
        element.send_keys(card_number)

    def input_password(self, password):
        """_summary_

        Args:
            password (_type_): _description_
        """
        element = self.driver.find_element(*self.locator.INPUT_PASSWORD)
        element.send_keys(password)

    def click_login(self):
        """_summary_"""
        element = self.driver.find_element(*self.locator.BUTTON_LOGIN)
        element.click()
        return PortalPage(self.driver)


class PortalPage(BasePage):
    """_summary_

    Args:
        BasePage (_type_): _description_
    """

    locator = PortalPageLocator

    def click_lent_status(self):
        """_summary_"""
        element = self.driver.find_element(*self.locator.MENU_LENT_STATUS)
        element.click()
        return LentStatusPage(self.driver)

    def click_reservation_status(self):
        """_summary_"""
        element = self.driver.find_element(*self.locator.MENU_RESERVATION_STATUS)
        element.click()


class LentStatusPage(BasePage):
    """_summary_

    Args:
        BasePage (_type_): _description_
    """

    locator = LentStatusPageLocator

    INDEX = {
        0: "item_name",
        1: "item_category",
        2: "lent_branch",
        3: "lent_date",
        4: "expire_date",
        5: "reservation_count",
        6: "extend_count",
        7: "lent_extend",
    }

    def get_lent_status(self) -> list:
        """_summary_

        Returns:
            _type_: _description_
        """
        element = self.driver.find_element(*self.locator.TABLE)
        tr_tags = element.find_elements(*self.locator.TR_TAGS)

        items = []
        for tr_tag in tr_tags:
            td_tags = tr_tag.find_elements(*self.locator.TD_TAGS)

            if td_tags:
                item = {}
                for key, value in self.INDEX.items():
                    item.update({value: td_tags[key].text})

                item = LentItem(**item)
                items.append(item)

        return items


from datetime import date, datetime


@dataclass
class LentItem:
    """_summary_"""

    item_name: str
    item_category: str
    lent_branch: str
    lent_date: str
    expire_date: str
    reservation_count: int
    extend_count: int
    lent_extend: str

    def has_expired(self) -> bool:
        """_summary_

        Returns:
            bool: _description_
        """
        return datetime.today() > datetime.strptime(self.expire_date, "%Y/%m/%d")

    def has_extended(self) -> bool:
        """_summary_

        Returns:
            bool: _description_
        """
        return self.extend_count > 0
