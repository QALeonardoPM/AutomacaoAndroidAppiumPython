#Trata-se de um script exemplo de portfólio, sem intenções de execução real

# Importação de bibliotecas padrão do Python e de terceiros

# Bibliotecas padrão do Python
from time import sleep

# Bibliotecas de terceiros
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import ElementNotVisibleException, NoSuchElementException, ElementNotSelectableException
from selenium.webdriver.support.wait import WebDriverWait

# Definição da função para criar WebDriverWait
def create_wait(driver, timeout=35):
    return WebDriverWait(driver, timeout, poll_frequency=1, ignored_exceptions=[
        ElementNotVisibleException,
        ElementNotSelectableException,
        NoSuchElementException
   ])
    
# Desired_caps semelhante as informações presentes no Json do Appium 
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'Pixel 6 API 30'
desired_caps['app'] = ('caminho/do/app.apk')
desired_caps['appPackage'] = 'appPackage.testeanonimizado'
desired_caps['appActivity'] = 'appActivity.testeanonimizado'
desired_caps['autoGrantPermissions'] = True

# Caminho ao appium server conforme Appium 
driver = webdriver.Remote('http://caminho/servidor/teste/anonimizado', desired_caps)

###############
# Início dos passos realizados no emulador Android
# Versão do app utilizada v1.4.10
###############

# Espera
wait = create_wait(driver)
print("App aberto")

# Inclusão de CPF para login
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID,
    "com.exemplo.app:id/input_cpf"
))
ele.send_keys("000.000.000-00")

# Realização do login no aplicativo
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID,
    "com.exemplo.app:id/button_login"
))
ele.click()

# Espera
wait = create_wait(driver)
print("Login OK")

# Selecionando no Menu Principal a opção de Sincronia
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID,
    "com.exemplo.app:id/txt_title_sincronia"
))
ele.click()

# Espera
wait = create_wait(driver)

# Desmarcando sincronia de envio de dados
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID,
    "com.exemplo.app:id/cb_enviar_dados"
))
ele.click()

# Botão Conectar para iniciar a sincronia
print("Iniciando Sincronia")
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID,
    "com.exemplo.app:id/button_sincronizar"
))
ele.click()
sleep(50)

# Espera
wait = create_wait(driver)

ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID,
    "com.exemplo.app:id/topo"
))
ele.click()
print("Clicando para não dar timeout na sincronia")
sleep(50)

# Espera
wait = create_wait(driver)
print("Sincronia OK")

# Volta para a tela anterior de Menu
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ACCESSIBILITY_ID, "Navigate up"
))
ele.click()

# Espera
wait = create_wait(driver)

# Clicando no botão que abre o Menu Lateral
ele = wait.until(lambda x: x.find_element(
    AppiumBy.XPATH,
    "//android.widget.ImageButton[@content-desc='Open']"
))
ele.click()

# Clicando no botão de Preferências no Menu Lateral
print("Acessando Preferências para criação das Faixas")
ele = wait.until(lambda x: x.find_element(
    AppiumBy.XPATH, "//android.widget.*[@content-desc='ElementoGenerico']"
))
ele.click()
sleep(2)

# Clicando no OK da mensagem se aparecer no emulador
try:
    ele = driver.find_element(AppiumBy.ID, "com.exemplo.app:id/button_ok")
    sleep(1)
    ele.click()
    print("Mensagem apresentada na tela OK")
    wait = WebDriverWait(
        driver, 25, poll_frequency=1,
        ignored_exceptions=[
            ElementNotVisibleException,
            ElementNotSelectableException,
            NoSuchElementException
        ]
    )
except NoSuchElementException:
    print("Botão de OK não está presente na tela")
    wait = WebDriverWait(
        driver, 25, poll_frequency=1,
        ignored_exceptions=[
            ElementNotVisibleException,
            ElementNotSelectableException,
            NoSuchElementException
        ]
    )

# Voltando para o Menu Principal
ele = wait.until(lambda x: x.find_element(AppiumBy.ACCESSIBILITY_ID, "Navigate up"))
ele.click()

# Espera
wait = create_wait(driver)

# Selecionando no Menu Principal a opção de acao
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID,
    "com.exemplo.app:id/txt_title_acao"
))
ele.click()
sleep(1)

# Espera
wait = create_wait(driver)

# Incluindo valor aleatório para pesquisa no campo de Nome/Razão Social
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID,
    "com.exemplo.app:id/edt_razao_social"
))
ele.send_keys("Nome")

# Espera
wait = create_wait(driver)

# Realizando pesquisa utilizando o valor incluído nos filtros
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID,
    "com.exemplo.app:id/btn_pesquisar"
))
ele.click()

print('Pesquisa cliente OK')

# Espera
wait = create_wait(driver)

# Clicando em Cadastrar para cadastro de um novo cliente
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID,
    "com.exemplo.app:id/btn_novo_prop"
))
ele.click()

# Espera
wait = create_wait(driver)

# Preenchimento dos dados do cadastro de cliente
# Seleção de tipo de Pessoa Física
print('Iniciando cadastro de cliente')
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID,
    "com.exemplo.app:id/rd_pessoa_fisica"
))
ele.click()

# Valor de CPF aleatório no campo de CPF
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID,
    "com.exemplo.app:id/edt_cpf"
))
ele.send_keys("000.000.000-00") #dado anonimizado

# Valor de código de área para telefone
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID,
    "com.exemplo.app:id/edt_ddd_telefone"
))
ele.send_keys("99")

# Inclusão de valor de telefone celular
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID,
    "com.exemplo.app:id/edt_telefone"
))
ele.send_keys("12345-1234")

# Inclusão de valor no campo de nome do cliente
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID,
    "com.exemplo.app:id/edt_nome"
))
ele.send_keys("Nome cliente PF Teste") #dado anonimizado

# Inclusão de valor no campo de data de nascimento
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID,
    "com.exemplo.app:id/edt_datanascimento"
))
ele.send_keys("11/11/2011")

# Inclusão de valor no campo de tipo de estabelecimento
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID,
    "com.exemplo.app:id/aut_tipo_estabelecimento"
))
ele.send_keys("DISTRIBUIDOR")

# Inclusão de valor no campo de email do cliente
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID,
    "com.exemplo.app:id/edt_email"
))
ele.send_keys("teste@email.com")

# Inclusão de informações de Endereço Principal
# Clicando no botão de CADASTRO
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID,
    "com.exemplo.app:id/btn_end_principal"
))
ele.click()
print("Iniciando cadastro de endereço Principal")

# Espera
wait = create_wait(driver)

# Incluindo valor aleatório para pesquisa de CEP
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID,
    "com.exemplo.app:id/txt_busca"
))
ele.send_keys("00000000") #dado anonimizado

# Clicando no botão PESQUISAR
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID,
    "com.exemplo.app:id/btn_pesquisar_cep"
))
ele.click()

# Clicando na opção de CEP Geral
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID,
    "com.exemplo.app:id/btn_cep_geral"
))
ele.click()

# Clicando na lista de Municípios
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID,
    "com.exemplo.app:id/spn_mun_cep_geral"
))
ele.click()

# Clicando em município da lista
ele = wait.until(lambda x: x.find_element(
    AppiumBy.XPATH, "//android.widget.*[@content-desc='ElementoGenerico']"
))
ele.click()

# Clicando no CONFIRMAR do CEP Geral
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID,
    "com.exemplo.app:id/btn_confirma_cep_geral"
))
ele.click()

# Clicando no campo de Divisão para informar valor
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID,
    "com.exemplo.app:id/txt_divisao"
))
ele.click()

# Incluindo valor de Divisão
ele.send_keys("1 DISTRITO")

# Incluindo valor de Bairro
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID,
    "com.exemplo.app:id/txt_bairro"
))
ele.send_keys("Bairro TESTE PF")

# Incluindo valor de número endereço
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID,
    "com.exemplo.app:id/txt_numero"
))
ele.send_keys("999999")

# Incluindo valor de complemento
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID,
    "com.exemplo.app:id/txt_complemento"
))
ele.send_keys("Complemento TESTE Pessoa Física")

# Salvando cadastro de endereço principal
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID,
    "com.exemplo.app:id/btn_salvar"
))
ele.click()

# Espera
wait = create_wait(driver)

# Clicando no OK da mensagem de confirmação do endereço salvo
print("Endereço Principal OK")
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID,
    "com.exemplo.app:id/button_ok"
))
ele.click()

# Espera
wait = create_wait(driver)

# Clicando no SIM na mensagem de Atenção/Confirmação
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID,
    "com.exemplo.app:id/button_yes"
))
ele.click()

# Espera
wait = create_wait(driver)

# Clicando no OK da mensagem de confirmação de cliente salvo
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/button_ok"
))
ele.click()
print("Cliente salvo OK")

# Espera
wait = create_wait(driver)

# Scroll na tela para mostrar o endereço de correspondência
user_action = TouchAction(driver)
user_action.tap(x=1, y=1000).perform()
driver.find_element(AppiumBy.ID, "com.exemplo.app:id/txt_input_email").click()
user_action.press(x=550, y=2500).move_to(x=578, y=480).release().perform()

# Inclusão de Endereço de Correspondência
# Clicando no botão CADASTRAR do endereço de correspondência
print("Iniciando cadastro de endereço de correspondência")
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/btn_end_corresp"
))
ele.click()

# Espera
wait = create_wait(driver)

# Clicando botão CEP DE OUTRA UF
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/btn_cep_outra_uf"
))
ele.click()

# Espera
wait = create_wait(driver)

# Preenchendo informações do Endereço
# Município
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/txt_municipio"
))
ele.send_keys("ACRELÂNDIA")

# Tipo de Logradouro
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/txt_tp_logradouro"
))
ele.send_keys("Avenida")

# Endereço
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/txt_endereco"
))
ele.send_keys("ABEL SCUISSIATO")

# CEP
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/txt_cep"
))
ele.send_keys("99999999")

# Bairro
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/txt_bairro"
))
ele.send_keys("Bairro Teste Appium sistema PF")

# Número
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/txt_numero"
))
ele.send_keys("123456")

# Complemento
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/txt_complemento"
))
ele.send_keys("Complemento Teste PF 12345")

# Salvando endereço de correspondência
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/btn_salvar"
))
ele.click()

# Espera
wait = create_wait(driver)

# Clicando OK na mensagem de confirmação
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/button_ok"
))
ele.click()

# Espera
wait = create_wait(driver)
print("Cadastro de endereço de correspondência OK")

# Confirmação de alteração no cadastro do cliente
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/button_yes"
))
ele.click()

# Botão OK na mensagem de confirmação de cliente salvo
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/button_ok"
))
ele.click()

# Scroll na tela para mostrar o campo de observações
user_action = TouchAction(driver)
user_action.tap(x=1, y=1000).perform()
driver.find_element(AppiumBy.ID, "com.exemplo.app:id/txt_input_email").click()
user_action.press(x=550, y=1290).move_to(x=578, y=514).release().perform()

# Inclusão de Valor no campo de observações do cliente
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/edt_observacoes"
))
ele.send_keys("Texto de observações TESTE PF")

# Acessando a aba de instrumentos
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ACCESSIBILITY_ID, "Instrumentos"
))
ele.click()
# Preenchendo a Aba Dados 
print("Iniciando preenchimento da aba DADOS")

# Ano de Fabricação
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/edt_ano_fabricacao"
))
ele.send_keys("2000")

# Número do Bloco
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/'ElementoGenerico'"
))
ele.send_keys("9999999999")

# Distribuidor
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/'ElementoGenerico'"
))
ele.send_keys("ACELUB")

# Identificador
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/'ElementoGenerico'"
))
ele.send_keys("99999999999999999999999999999999999999999999999999")

print("Concluído preenchimento da aba DADOS")

# Clicando no botão SALVAR da aba Dados
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/btnSalvar_dados"
))
ele.click()

# Clicando OK na mensagem sobre necessidade de inclusão de irregularidade
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/button_ok"
))
ele.click()

# Cadastro de irregularidades para o instrumento
# Acessando a aba de Irregularidades
ele = wait.until(lambda x: x.find_element(
    AppiumBy.XPATH, "//android.widget.*[@content-desc='ElementoGenerico']"
))
ele.click()

# Espera
wait = create_wait(driver)

# Inclusão irregularidade 999 observações
print("Iniciando preenchimento de Irregularidade")

ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/'ElementoGenerico'"
))
ele.send_keys("999")

# Observação da Irregularidade
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/edt_observacao"
))
ele.send_keys("Irregularidade Teste Android Appium Python")

# QD = Sim
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/'ElementoGenerico'"
))
ele.click()

# Adicionando Irregularidade
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/btn_adicionar_nc"
))
ele.click()

print("Irregularidade incluída")

# Clicando botão SALVAR da aba de irregularidades
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/'ElementoGenerico'"
))
ele.click()

print("Salvando com irregularidade")

# OK na Confirmação de serviço salvo com sucesso
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/button_ok"
))
ele.click()

# Espera
wait = create_wait(driver)

# Inclusão de segundo instrumento 
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/btn_novo_instrumento"
))
ele.click()

print("Iniciando cadastro do 2° instrumento")

# Espera
wait = create_wait(driver)

# Inclusão irregularidade 999 observações
print("Iniciando preenchimento de Irregularidade")
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/'ElementoGenerico'"
))
ele.send_keys("999")

# Observação da Irregularidade
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/edt_observacao"
))
ele.send_keys("Irregularidade Teste Android Appium Python")

# QD = Sim
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/rb_qd_sim"
))
ele.click()

# Adicionando Irregularidade
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/btn_adicionar_nc"
))
ele.click()
print("Irregularidade incluída")

# Clicando botão SALVAR da aba de irregularidades
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/'ElementoGenerico'"
))
ele.click()
print("Salvando com irregularidade")

# OK na Confirmação de serviço salvo com sucesso
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/button_ok"
))
ele.click()

# Espera
wait = create_wait(driver)

# Pesquisas Instrumento por número minhaempresa
print("Pesquisando instrumento")

# Pesquisando com valor que não tem resultado
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/'ElementoGenerico'"
))
ele.send_keys("555")

ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/'ElementoGenerico'"
))
ele.click()
print("Pesquisa sem retorno de instrumento")
sleep(1)

# Limpando valor utilizado no campo
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/'ElementoGenerico'"
))
ele.clear()
sleep(1)

ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/'ElementoGenerico'"
))

# Pesquisando com valor que tem resultado
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/'ElementoGenerico'"
))
ele.send_keys("8888888")

ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/'ElementoGenerico'"
))
ele.click()
sleep(1)
print("Pesquisa com retorno de instrumento")

# Acessando cadastro de instrumento filtrado
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/'ElementoGenerico'"
))
ele.click()
print("Acessando edição de instrumento")
sleep(1)

print("Registrando assinatura")
# Marcando assinatura
user_action = TouchAction(driver)
user_action.tap(x=1, y=1000).perform()
driver.find_element(AppiumBy.ID, "com.exemplo.app:id/'ElementoGenerico'").click()
user_action.press(x=1200, y=800).move_to(x=200, y=800).release().perform()

# Incluindo nome do responsável
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/'ElementoGenerico'"
))
ele.send_keys("Nome responsável teste assinatura")

ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/'ElementoGenerico'"
))
ele.send_keys("Função Responsável testes assinatura")

# Clicando no botão de confirmação
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/'ElementoGenerico'"
))
ele.click()

# Espera
wait = create_wait(driver)
print("Cobrança com assinatura")

# Voltando para cadastro do cliente
ele = wait.until(lambda x: x.find_element(AppiumBy.ACCESSIBILITY_ID, "Navigate up"))
ele.click()

# Espera
wait = create_wait(driver)

# Clicando para voltar para a aba clientes
ele = wait.until(lambda x: x.find_element(AppiumBy.ACCESSIBILITY_ID, "cliente"))
ele.click()
print("Voltando para a aba cliente")

# Salvando o cadastro do cliente
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/btn_salvar"
))
ele.click()

# Confirmando a alteração no cadastro
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/button_yes"
))
ele.click()

# Confirmando que o cliente foi salvo
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/button_ok"
))
ele.click()
print("Cadastro de cliente salvo")

# Voltando para a tela de Pesquisa de clientes
ele = wait.until(lambda x: x.find_element(AppiumBy.ACCESSIBILITY_ID, "Navigate up"))
ele.click()
print("Saindo do cadastro do cliente")

ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/button_yes"
))
ele.click()
# Clicando no botão para salvar o RD
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/btn_salvar_rd"
))
ele.click()
sleep(1)

# Clicando OK na mensagem de Atenção
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/button_ok"
))
ele.click()
sleep(1)

# Abrindo lista de datas disponíveis
print("Iniciando preenchimento do RD")
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/spn_dt_rd"
))
ele.click()
sleep(1)

# Selecionando a data mais alta na lista
ele = wait.until(lambda x: x.find_element(
    AppiumBy.XPATH, "//android.widget.*[@content-desc='ElementoGenerico']"
))
ele.click()
sleep(1)

# Incluindo Dados do veículo
# Placa do veículo
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/aut_veiculo"
))
ele.send_keys("{{placa_veiculo}}")

# Salvando viatura como padrão
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/switch_placa_veiculo"
))
ele.click()

# Incluindo informações de quilometragem
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/edt_km_inicial"
))
ele.send_keys("3500")

ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/edt_km_final"
))
ele.send_keys("3800")

# Incluindo informações de horários
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/edt_hora_inicial"
))
ele.send_keys("09:00")

ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/edt_hora_final"
))
ele.send_keys("16:00")

# Incluindo funcionário auxiliar e salvando como padrão
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/aut_funcionario_auxiliar"
))
ele.send_keys("TESTE")

ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/switch_funcionario_auxiliar"
))
ele.click()

# Selecionando valor para lista de Diária
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/spn_diaria"
))
ele.click()

ele = wait.until(lambda x: x.find_element(
    AppiumBy.XPATH, "//android.widget.TextView[contains('ElementoGenerico')]"
))
ele.click()

# Selecionando número de cópias
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/spn_nro_copias"
))
ele.click()

ele = wait.until(lambda x: x.find_element(
    AppiumBy.XPATH, "//android.widget.*[@content-desc='ElementoGenerico'"
))
ele.click()

# Incluindo valor no campo de Observações
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/edt_observacoes"
))
ele.send_keys("Exemplo observações teste RD")

# Clicando no botão para salvar o RD
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/btn_salvar_rd"
))
ele.click()

# Clicando OK na mensagem de RD Salvo com sucesso
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/button_ok"
))
ele.click()
print("RD salvo com sucesso")
sleep(1)

# Voltando para a tela de Menu Principal
ele = wait.until(lambda x: x.find_element(AppiumBy.ACCESSIBILITY_ID, "Navigate up"))
ele.click()

# Clicando no botão que abre o Menu Lateral
ele = wait.until(lambda x: x.find_element(
    AppiumBy.XPATH, "//android.widget.ImageButton['ElementoGenerico']"
))
ele.click()
# Abrindo a sincronia pelo Menu Principal
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/txt_title_'ElementoGenerico'"
))
ele.click()

# Espera
wait = create_wait(driver)

# Processo de sincronia envio de dados
# Desmarcando sincronia de envio de dados
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/cb_'ElementoGenerico'"
))
ele.click()

# Desmarcando sincronia de recebimento
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/cb_'ElementoGenerico'"
))
ele.click()

# Desmarcando sincronia de atualização
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/cb_'ElementoGenerico'"
))
ele.click()

# Clicando no botão para iniciar a sincronia
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/'ElementoGenerico'"
))
ele.click()
print("Iniciada sincronia de envio de dados")

sleep(20)
print("Realizada sincronia de envio de dados")

# Espera
wait = create_wait(driver)
print("Sincronia de Envio OK")

# Volta para a tela anterior de Menu
ele = wait.until(lambda x: x.find_element(AppiumBy.ACCESSIBILITY_ID, "Navigate up"))
ele.click()

# Espera
wait = create_wait(driver)

# Saindo do aplicativo
# Clicando no botão que abre o Menu Lateral
ele = wait.until(lambda x: x.find_element(
    AppiumBy.XPATH, "//android.widget.ImageButton['ElementoGenerico']"
))
ele.click()

# Clicando no botão Sair no Menu Lateral
ele = wait.until(lambda x: x.find_element(
    AppiumBy.XPATH, "//android.widget.*[@content-desc='ElementoGenerico']"
))
ele.click()

# Clicando no botão SAIR na mensagem de confirmação
ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID, "com.exemplo.app:id/button_yes"
))
ele.click()
print("Feito Logoff")

# Espera
wait = create_wait(driver)

# Saindo do aplicativo
print("Saindo do aplicativo")
driver.terminate_app('com.exemplo.app')

finally:
    driver.quit()
    print("Driver encerrado.")
