# 2. Desenvolva um script em Python, que tem como objetivo realizar o login
# no aplicativo “Instagram”, utilizando uma conta de email.

import unittest
from time import sleep
from appium import webdriver

class TesteInstagram(unittest.TestCase):
    def setUp(self):
        print('Configurando teste...')
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['deviceName'] = 'Android'
        desired_caps['appPackage'] = 'com.instagram.android' # Instagram
        desired_caps['appActivity'] = 'com.instagram.android.activity.MainTabActivity'
        desired_caps['noReset'] = 'false' # Permite limpeza dos dados

        # Conecta driver de automação
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_instalacao(self):
        print('Iniciando teste...')

        # Credenciais
        dados_login = 'fulano@beltrano.com'
        dados_senha = 'minhasenha'

        # Aguarda tempo de inicialização
        sleep(3)

        print('Clicando no botao login')
        bt_login = self.driver.find_element_by_id('com.instagram.android:id/log_in_button')
        bt_login.click()

        print('Preenchendo login')
        campo_usuario = self.driver.find_element_by_id('com.instagram.android:id/login_username')
        campo_usuario.send_keys(dados_login) # Digita o texto "fulano@beltrano.com"

        print('Preenchendo senha')
        campo_senha = self.driver.find_element_by_id('com.instagram.android:id/password')
        campo_senha.send_keys(dados_senha) # Digita o texto "minhasenha"

        print('Clicando no botao efetuar login')
        bt_login = self.driver.find_element_by_id('com.instagram.android:id/next_button')
        bt_login.click()

        # Aguarda tempo de login
        sleep(5)

        # Verifica se chegou à tela principal
        self.assertEqual(self.driver.current_activity, 'com.instagram.mainactivity.MainActivity', 'Login falhou')

if __name__ == '__main__':
    unittest.main()
