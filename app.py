from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as condicao_esperada
from selenium.common.exceptions import *
from time import sleep
import random
import schedule

    


def like_instagram():
    def iniciar_driver():

        chrome_options = Options()

        arguments = ['--lang=en-US', '--start-maximized']

        for argument in arguments:
            chrome_options.add_argument(argument)

        chrome_options.add_experimental_option('prefs', {
            'download.prompt_for_download': False,
            'profile.default_content_setting_values.notifications': 2,
            'profile.default_content_setting_values.automatic_downloads': 1

        })

        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()), options=chrome_options)
        wait = WebDriverWait(
            driver,
            10,
            poll_frequency=1,
            ignored_exceptions=[
                NoSuchElementException,
                ElementNotVisibleException,
                ElementNotSelectableException,
            ]
        )
        return driver, wait

    driver, wait = iniciar_driver()
    driver.implicitly_wait(4)

    #informações da conta e dos sites
    instagram = 'https://www.instagram.com/'
    email = 'email'
    senha = 'senha'
    pagina_curtir = 'https://www.instagram.com/devaprender/'
    driver.get(instagram)


    #logar na conta
    digitar_email = driver.find_element(By.XPATH, "//input[@aria-label='Phone number, username, or email']")
    digitar_email.send_keys(email)
    sleep(random.uniform(1,3))
    digitar_senha = driver.find_element(By.XPATH, "//input[@aria-label='Password']")
    digitar_senha.send_keys(senha)
    sleep(random.uniform(1,3))
    negar = driver.find_element(By.XPATH, "//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1xmf6yo x1e56ztr x540dpk x1m39q7l x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1']")
    negar.click()
    sleep(random.uniform(3,5))

    #escolher perfil
    driver.get(pagina_curtir)
    sleep(random.uniform(4,5))


    #escolher postagem e dar Like nos que ainda está sem Like
    sleep(random.uniform(2,3))
    postagens = driver.find_elements(By.XPATH, "//div[@class='_aagw']")
    for postagem in postagens[:5]:
        postagem.click()
        sleep(random.uniform(2,3))

        like = driver.find_element(By.XPATH, "//span[@class='_aamw']/div")
        texto = like.get_attribute('textContent')
        if texto == 'Like':
            like.click()

        sleep(random.uniform(1,2))
        botao_fechar = driver.find_element(By.XPATH, "//div[@class='x160vmok x10l6tqk x1eu8d0j x1vjfegm']")
        botao_fechar.click()
        sleep(random.uniform(2,3))



schedule.every().day.at("06:00").do(like_instagram)

while True:
    # Executar tarefas agendadas
    schedule.run_pending()

    # Aguardar um curto período de tempo para evitar uso excessivo da CPU
    sleep(1)
