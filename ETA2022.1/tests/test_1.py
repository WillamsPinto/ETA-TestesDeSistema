

class Test1:

    def test_click_login_btn(self, open_login):
        open_login.click_login_btn()
        assert open_login.is_url_login(), "Pagina alterada!"
        assert open_login.has_login_message_error(), 'Mensagem erro não encontrada!'
