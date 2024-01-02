from selenium.webdriver.common.by import By


class AmazonLocators:
    SEARCH_BAR = (By.XPATH, "//*[@placeholder='Search Amazon.in']")
    SEARCH_BUTTON = (By.XPATH, "//*[@id='nav-search-submit-button']")
    SELECT_ITEM = (By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
    ADD_CART = (By.XPATH, "//input[@id='add-to-cart-button']")
    PRICE_OF_SELECTED_ITEM = (By.XPATH, "(//span[normalize-space()='74,900'])[1]")

    VIEW_CART_BUTTON = (By.XPATH, "//input[@aria-labelledby='attach-sidesheet-view-cart-button-announce']")

    PRICE_OF_CART_ITEM = (By.XPATH, "(//span[@class='a-size-medium a-color-base sc-price sc-white-space-nowrap sc-product-price a-text-bold'])[1]")