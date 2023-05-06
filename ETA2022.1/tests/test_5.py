from pages.CheckoutCompletePage import CheckoutCompletePage
from pages.CheckoutInformationPage import CheckoutInformationPage
from pages.CheckoutOverviewPage import CheckoutOverviewPage
from pages.YourCart import YourCart


class Test_5:

    def test_finalizar_compra(self, add_product_to_cart):
        products_page = add_product_to_cart
        products_page.open_cart()

        your_cart = YourCart(driver=products_page.driver)
        assert your_cart.is_your_cart_page(), "Your Cart page not found!"
        item_price = your_cart.get_item_price()
        your_cart.click_checkout()

        checkout_page = CheckoutInformationPage(driver=your_cart.driver)
        assert checkout_page.is_checkout_information_page(), "Checkout: Your Information page not found!"
        checkout_page.insert_first_name()
        checkout_page.insert_last_name()
        checkout_page.insert_postal_code()
        checkout_page.click_continue()

        checkout_overview_page = CheckoutOverviewPage(driver=checkout_page.driver)
        assert checkout_overview_page.has_same_price(item_price), "O valor do item não corresponde ao do carrinho!"
        assert checkout_overview_page.has_a_payment_information_title(), "titulo das informações de pagamanetos não encontrado!"
        assert checkout_overview_page.has_a_shipping_information_title(), "titulo das informações de envio não encontrado!"
        assert checkout_overview_page.has_a_price_total_title(), "titulo do preço total não encontrado!"
        assert checkout_overview_page.total_value_is_correct(), "Valor total não condiz com a soma do sub item e a taxa!"
        checkout_overview_page.click_finish_btn()

        checkout_complete_page = CheckoutCompletePage(driver=checkout_overview_page.driver)
        assert checkout_complete_page.has_header_complete_msg(), 'Titulo incorreto'
        assert checkout_complete_page.has_txt_complete_msg(), 'Mensagem de texto incorreto'



