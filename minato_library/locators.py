"""module docstring"""
# -*- coding: utf-8 -*-
from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class HomePageLocator:
    """_summary_"""

    BUTTON_LOGIN = (By.ID, "login")


@dataclass
class LoginPageLocator:
    """_summary_"""

    INPUT_CARD_NUMBER = (
        By.ID,
        "usrcardnumber",
    )
    INPUT_PASSWORD = (
        By.ID,
        "password",
    )
    BUTTON_LOGIN = (
        By.CSS_SELECTOR,
        "#body > form > div > div.ex-navi > input.button.exec.large",
    )


@dataclass
class PortalPageLocator:
    """_summary_"""

    MENU_LENT_STATUS = (By.ID, "stat-lent")

    MENU_RESERVATION_STATUS = (By.ID, "stat-resv")


@dataclass
class LentStatusPageLocator:
    """_summary_"""

    TABLE = (By.CSS_SELECTOR, "#body > form > div > div.main > table")
    TR_TAGS = (By.TAG_NAME, "tr")
    TD_TAGS = (By.TAG_NAME, "td")


@dataclass
class ReservationStatusPageLocator:
    """_summary_"""

    TABLE = (By.CSS_SELECTOR, "#ItemDetaTable")
    TR_TAGS = (By.TAG_NAME, "tr")
    TD_TAGS = (By.TAG_NAME, "td")
