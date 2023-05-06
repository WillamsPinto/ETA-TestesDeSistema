
from pages.ProductsPage import ProductsPage


class Test2:

    def test_efetuar_login(self, open_login):
        open_login.efetuar_login()
        products_page = ProductsPage(open_login.driver)
        assert products_page.is_products_page(), "Pagina de produtos não encontrada!"
        assert products_page.count_products_page() == 6, 'Quantidade de produtos inválida!'
        assert products_page.has_menu_btn(), 'Botão de menu não encontrado!'

