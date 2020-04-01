# 1. Desenvolva um script em Python, que tem como objetivo realizar o
# download de um aplicativo na PlayStore. E.g.: Instagram

import unittest
from time import sleep
from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey

class TesteGooglePlay(unittest.TestCase):
    def setUp(self):
        print('Configurando teste...')
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['deviceName'] = 'Android'
        desired_caps['appPackage'] = 'com.android.vending' # Play Store
        desired_caps['appActivity'] = 'com.android.vending.AssetBrowserActivity'
        desired_caps['noReset'] = 'true' # Impede limpeza dos dados

        # Conecta driver de automação
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_instalacao(self):
        print('Iniciando teste...')

        # Dados da pesquisa
        nome_app = 'Instagram'
        pacote_app = 'com.instagram.android'

        print('Clicando na barra de busca')
        elem_barra = self.driver.find_element_by_id('com.android.vending:id/search_bar')
        elem_barra.click()

        print('Digitando texto')
        elem_campo = self.driver.find_element_by_id('com.android.vending:id/search_bar_text_input')
        elem_campo.send_keys(nome_app) # Digita texto ("Instagram")
        self.driver.press_keycode(AndroidKey.ENTER) # Pressiona ENTER

        print('Clicar instalar')
        elem_instalar = self.driver.find_element_by_id('com.android.vending:id/right_button')
        elem_instalar.click()

        print('Esperando...')
        # Verifica de 10 em 10 segundos se o app está instalado
        for x in range(1, 12): # No maximo 12x de 10 segundos
            print('Verificando instalacao... Tentativa: ', x,'/ 12')
            if(self.driver.is_app_installed(pacote_app)):
                break
            else:
                sleep(10)
        
        is_instalado = self.driver.is_app_installed(pacote_app)

        # Verifica se o app está instalado
        self.assertTrue(is_instalado, "Aplicativo não foi instalado com sucesso")

if __name__ == '__main__':
    unittest.main()
