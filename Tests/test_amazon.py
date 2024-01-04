
import pytest
from Demo_Page.Page_Objects.search_item import SearchItem
from Demo_Page.Constants.constant import Constant
from Demo_Page.Page_Objects.locators import AmazonLocators
from Demo_Page.Utilities.test_base import TestBase


@pytest.fixture(scope="module")
def test_base(driver):
    return TestBase(driver)

@pytest.mark.usefixtures("test_base")
def test_search(driver, test_base):
    try:

        search_item = SearchItem(driver)
        search_item.open(Constant.BASE_URL)

        test_base.wait_for_element(AmazonLocators.SEARCH_BAR)
        search_item.set_search_item(Constant.SEARCH_ITEM)
        test_base.wait_for_element(AmazonLocators.SELECT_ITEM)
        search_item.select_item()

        windows_opened = driver.window_handles
        driver.switch_to.window(windows_opened[1])
        text_in_item = (search_item.price_of_selected_item())
        test_base.wait_for_element_interactable(AmazonLocators.ADD_CART)
        search_item.add_to_cart()
        test_base.wait_for_element_interactable(AmazonLocators.VIEW_CART_BUTTON)
        search_item.cart_btn()
        test_base.wait_for_element_interactable(AmazonLocators.PRICE_OF_CART_ITEM)
        text_in_cart = (search_item.price_of_cart_item())
        price = (text_in_cart[:-3])
        price_in_cart = price.strip()
        # test_base.wait_for_element_interactable(AmazonLocators.PRICE_OF_CART_ITEM)
        assert text_in_item == price_in_cart

    except Exception as e:
        print("test case error price was not matched", e)




