# Trata-se de um script exemplo de portfólio, sem intenções de execução real

# Importação de bibliotecas padrão do Python e de terceiros

# Bibliotecas padrão do Python
from time import sleep

# Bibliotecas de terceiros
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementNotVisibleException,
    ElementNotSelectableException,
    NoSuchElementException
)

# Definição da função para criar WebDriverWait
def create_wait(driver, timeout=25):
    return WebDriverWait(driver, timeout, poll_frequency=1, ignored_exceptions=[
        ElementNotVisibleException,
        ElementNotSelectableException,
        NoSuchElementException
    ])    

# Desired_caps semelhante às informações presentes no JSON do Appium
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'Pixel 6 API 30'
desired_caps['app'] = 'caminho/do/app.apk'
desired_caps['appPackage'] = 'appPackage.testeanonimizado'
desired_caps['appActivity'] = 'appActivity.testeanonimizado'
desired_caps['autoGrantPermissions'] = True

# Caminho ao Appium server conforme Appium
driver = webdriver.Remote('http://caminho/servidor/teste/anonimizado', desired_caps)

###############
# Início dos passos realizados no emulador Android
###############

# Espera
wait = create_wait(driver)
print("App aberto")
# Inclusão de CPF de um usuário para login
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.send_keys("111.111.111-11")  # CPF fictício/anonimizado

# Realização do login no aplicativo
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()

# Espera
wait = create_wait(driver)
print("Login OK")

# Selecionando no Menu Principal a opção de Sincronia
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()

# Espera
wait = create_wait(driver)

# Desmarcando sincronia de envio de dados
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()

# Botão Conectar para iniciar a sincronia
print("Iniciando Sincronia completa")
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()
sleep(30)

# Espera
wait = create_wait(driver)

ele = wait.until(
    lambda x: x.find_element(AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'")
)
ele.click()
print("Clicando para não dar timeout na sincronia")
sleep(30)


# Espera
wait = create_wait(driver)
print("Sincronia OK")

# Volta para a tela anterior de Menu
ele = wait.until(lambda x: x.find_element(AppiumBy.ACCESSIBILITY_ID, "Navigate up"))
ele.click()

# Espera
wait = create_wait(driver)

# Clicando no botão que abre o Menu Lateral
ele = wait.until(
    lambda x: x.find_element(AppiumBy.XPATH, "//android.widget.ImageButton['ElementoGenerico']")
)
ele.click()

# Clicando no botão de Preferências no Menu Lateral
print("Acessando Preferências para criação das Faixas")
ele = wait.until(
    lambda x: x.find_element(AppiumBy.XPATH, "//android.widget.*['ElementoGenerico']")
)
ele.click()
sleep(3)

# Clicando no OK da mensagem se aparecer no emulador
try:
    ele = driver.find_element(AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:id/button_ok")
    sleep(1)
    ele.click()
    print("Mensagem apresentada na tela OK")
    wait = create_wait(driver)

except NoSuchElementException:
    print("Botão de OK não está presente na tela")
    wait = create_wait(driver)

# Voltando para o Menu Principal
ele = wait.until(lambda x: x.find_element(AppiumBy.ACCESSIBILITY_ID, "Navigate up"))
ele.click()

# Espera
wait = create_wait(driver)

# Selecionando no Menu Principal a opção de ação
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()
sleep(1)

# Espera
wait = create_wait(driver)

# Incluindo valor aleatório para pesquisa no campo de CPF/CNPJ
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.send_keys("11111111111")

# Espera
wait = create_wait(driver)

print("Pesquisa Proprietário OK")

# Realizando pesquisa utilizando o valor incluído nos filtros
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()

# Espera
wait = create_wait(driver)

# Clicando em Cadastrar para cadastro de um novo proprietário
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()

# Espera
wait = create_wait(driver)

# Preenchimento dos dados do cadastro de proprietário pessoa física
# Seleção de tipo de Pessoa Física
print("Iniciando cadastro de proprietário")
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()

# Valor de CPF aleatório no campo de CPF
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.send_keys("111.111.111-11")  # CPF fictício/anonimizado

# Valor de código de área para telefone
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.send_keys("99")

# Inclusão de valor de telefone celular
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.send_keys("99999-9999")

# Inclusão de valor no campo de nome do proprietário
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.send_keys("Nome Proprietário Teste")

# Inclusão de valor no campo de data de nascimento
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.send_keys("11/11/2011")

# Inclusão de valor no campo de tipo de estabelecimento
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:id/'ElementoGenerico'"
    )
)
ele.send_keys("DISTRIBUIDOR")

# Inclusão de valor no campo de email do proprietário
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.send_keys("teste@mail.com.br")

# Inclusão de seleção na check de envio de informações por email
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()

# Inclusão de informações de Endereço Principal
# Clicando no botão de CADASTRO
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()

print("Iniciando cadastro de endereço Principal")

# Espera
wait = create_wait(driver)

# Incluindo valor aleatório para pesquisa de CEP
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.send_keys("{{cep}}")

# Clicando no botão PESQUISAR
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()

# Clicando na opção de CEP Geral
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()

# Clicando na lista de Municípios
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()

# Clicando em município da lista
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.XPATH, "//android.widget.*[@content-desc='ElementoGenerico']"
    )
)
ele.click()

# Clicando no CONFIRMAR do CEP Geral
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()

# Clicando no campo de Divisão para informar valor
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()
ele.send_keys("1 DISTRITO")

# Incluindo valor de Bairro
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.send_keys("Bairro TESTE")

# Incluindo valor de número endereço
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.send_keys("999999")

# Incluindo valor de complemento
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.send_keys("Complemento TESTE 123")

# Salvando cadastro de endereço principal
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()

# Espera
wait = create_wait(driver)

# Clicando no OK da mensagem de confirmação do endereço salvo
print("Endereço Principal OK")
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()

# Espera
wait = create_wait(driver)

# Clicando no SIM na mensagem de Atenção/Confirmação
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()

# Espera
wait = create_wait(driver)

# Clicando no OK da mensagem de confirmação de proprietário salvo
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()
print("Proprietário Salvo OK")

# Espera
wait = create_wait(driver)

# Scroll na tela para mostrar o endereço de correspondência
user_action = TouchAction(driver)
user_action.tap(x=1, y=1000).perform()

driver.find_element(
    AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
).click()

user_action.press(x=550, y=2500).move_to(x=578, y=480).release().perform()
# Inclusão de Endereço de Correspondência
# Clicando no botão CADASTRAR do endereço de correspondência
print("Iniciando cadastro de endereço de correspondência")
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()

# Espera
wait = create_wait(driver)

# Clicando botão CEP DE OUTRA UF
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()

# Espera
wait = create_wait(driver)

# Preenchendo informações do Endereço
# Município
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.send_keys("ACRELÂNDIA")

# Tipo de Logradouro
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.send_keys("Avenida")

# Endereço
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.send_keys("ABEL SCUISSIATO")

# CEP
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.send_keys("99999999")

# Bairro
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.send_keys("Bairro Teste Appium sistema")

# Número
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.send_keys("123456")

# Complemento
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.send_keys("Complemento Teste APPIUM sistema Móvel")

# Salvando endereço de correspondência
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()

# Aguarda até que o processo de salvamento finalize
wait = create_wait(driver)

print("Endereço de correspondência salvo com sucesso!")

# Clicando OK na mensagem de confirmação
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()

# Espera
wait = create_wait(driver)

print("Cadastro de endereço de correspondência OK")
# Clicando OK na confirmação de instrumento incluído
print("Instrumento incluído OK")
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()

# Incluindo valor de resultado para o serviço
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.XPATH, "//android.widget.*[@content-desc='ElementoGenerico']"
    )
)
ele.click()

# Incluindo valor de Dígito da Marca de Verificação
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.send_keys("4")

# Salvando o serviço do instrumento
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()

# Clicando OK na mensagem de Dados do Instrumento
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()
print("Instrumento Salvo com Resultado")

# Clicando no título de aba DADOS
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ACCESSIBILITY_ID, "Dados"
    )
)
ele.click()

# Preenchendo a Aba Dados
print("Iniciando preenchimento da aba DADOS")
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.send_keys("2000")

# Número do Bloco Medidor
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.send_keys("9999999999")

# Distribuidor
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.send_keys("anonimizado")

# Identificador 
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.send_keys("99999999999999999999999999999999999999999999999999")
print("Concluído preenchimento da aba DADOS")

# Cadastro de irregularidades para o instrumento
# Acessando a aba de Irregularidades
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.XPATH, "//android.widget.*[@content-desc='ElementoGenerico']"
    )
)
ele.click()

# Espera
wait = create_wait(driver)

# Inclusão irregularidade 999 observações
print("Iniciando preenchimento de Irregularidade")
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:id/'ElementoGenerico'"
    )
)
ele.send_keys("999")

# Observação da Irregularidade
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.send_keys("Irregularidade Teste Android Appium Python")

# Quadro Demonstrativo = Sim
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()

# Adicionando Irregularidade
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()
print("Irregularidade de instrumento incluída")

# Validação da regra que não permite repetir irregularidade
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.send_keys("999")
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()
print("Validação regra de não repetir irregularidade de instrumento concluída com sucesso!")

# Salvando instrumento com irregularidade
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()
print("Salvando instrumento com irregularidade")

# OK na Confirmação de serviço salvo com sucesso
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()

# Espera
wait = create_wait(driver)

# Processo de cobrança - Acessando a aba de Relatórios
print("Acessando aba Relatórios")
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ACCESSIBILITY_ID, "Relatórios"
    )
)
ele.click()

# Espera
wait = create_wait(driver)

# Clicando no botão que abre o Menu Lateral
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.XPATH, "//android.widget.ImageButton['ElementoGenerico']"
    )
)
ele.click()

# Processo para deixar RD salvo
# Clicando no Botão de Relatório
print("Abrindo Relatório")
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.XPATH, "//android.widget.*['ElementoGenerico']"
    )
)
ele.click()
sleep(1)

# Espera
wait = create_wait(driver)

# Clicando no botão para salvar o RD
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()
sleep(1)

# Clicando OK na mensagem de Atenção
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()
sleep(1)

# Abrindo lista de datas disponíveis
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()
sleep(1)

# Selecionando a data mais alta na lista
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.XPATH, "//android.widget.*['ElementoGenerico']"
    )
)
ele.click()
sleep(1)

# Clicando no botão para salvar o RD
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()

# Clicando OK na mensagem de RD Salvo com sucesso
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()
print("RD salvo com sucesso")

# Volta para a tela de Menu Principal
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ACCESSIBILITY_ID, "Navigate up"
    )
)
ele.click()

# Clicando no botão que abre o Menu Lateral novamente
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.XPATH, "//android.widget.ImageButton['ElementoGenerico']"
    )
)
ele.click()

# Iniciando processo de Backup
# Clicando no botão de Backup no Menu Lateral
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.XPATH, "//android.widget.*['ElementoGenerico']"
    )
)
ele.click()

# Espera
wait = create_wait(driver)

print("Iniciando backup")
# Clicando no botão que realiza o Backup
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()

# Espera
wait = create_wait(driver)
print("Finalizando backup")

# Volta para a tela anterior de Menu Principal
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ACCESSIBILITY_ID, "Navigate up"
    )
)
ele.click()

# Espera
wait = create_wait(driver)

# Abrindo a sincronia pelo Menu Principal
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()

# Espera
wait = create_wait(driver)

# Processo de sincronia envio de dados
print("Iniciada sincronia de envio de dados")

# Desmarcando sincronia de envio de dados
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()

# Desmarcando sincronia de recebimento de escalas
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()

# Desmarcando sincronia de atualização de endereços
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()

# Clicando no botão para iniciar a sincronia
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()

sleep(20)
print("Realizada sincronia de envio de dados")

# Espera
wait = create_wait(driver)
print("Sincronia de Envio OK")

# Volta para a tela anterior de Menu
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ACCESSIBILITY_ID, "Navigate up"
    )
)
ele.click()
# Espera
wait = create_wait(driver)

# Saindo do aplicativo
# Clicando no botão que abre o Menu Lateral
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.XPATH, "//android.widget.ImageButton['ElementoGenerico']"
    )
)
ele.click()

# Clicando no botão Sair no Menu Lateral
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.XPATH, "//android.widget.*['ElementoGenerico']"
    )
)
ele.click()

# Clicando no botão SAIR na mensagem de confirmação
ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID, "com.minhaempresa.com.br.appminhaempresa:'ElementoGenerico'"
    )
)
ele.click()
print("Feito Logoff")

# Espera
wait = create_wait(driver)

# Saindo do aplicativo
print("Saindo do aplicativo")
driver.terminate_app("com.minhaempresa.com.br.appminhaempresa")

finally:
    driver.quit()
    print("Driver encerrado.")