from pages.CheckoutInformationPage import CheckoutInformationPage
from pages.YourCart import YourCart


class Test_4:

    def test_error_msg_checkout(self, add_product_to_cart):
        products_page = add_product_to_cart
        products_page.open_cart()

        your_cart = YourCart(driver=products_page.driver)
        assert your_cart.is_your_cart_page(), "Your Cart page not found!"
        your_cart.click_checkout()

        checkout_page = CheckoutInformationPage(driver=your_cart.driver)
        assert checkout_page.is_checkout_information_page(), "Checkout: Your Information page not found!"
        checkout_page.click_continue()

        assert checkout_page.has_first_name_error(), "First name error message not found!"



