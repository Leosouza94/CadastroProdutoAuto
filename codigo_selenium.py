import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas

# Inicializa o driver do Chrome
driver = webdriver.Chrome()

# PASSO 1 - Entra no sistema onde o cadastro dos produtos vai ser realizado
driver.get("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

# PASSO 2 - Fazer login
time.sleep(5)  # Aguarda o carregamento da página por 5 seg
driver.find_element(By.ID,"email").send_keys("leosouza94@hotmail.com") #Procura pela ID email e insere um email
driver.find_element(By.ID,"password").send_keys("minha senha") #Procura pela id password e insere uma senha
driver.find_element(By.ID,"pgtpy-botao").click() #Procura pela id pgtpy-botao e clica
time.sleep(5)

# PASSO 3 - Importar tabela (base de dados)
tabela = pandas.read_csv('produtos.csv') #importa a tabela onde os produtos estão listados

# PASSO 4 - Cadastrar produtos
for linha in tabela.index: #para cada linha, dentro das linhas da tabela:
    #ele procura cada elemento da página por ID(são campos de digitação) e insere nestes campos as informações da tabela
    #uso tabela.loc[linha,coluna], passadas para string, para escrever nos campos
    driver.find_element(By.ID,"codigo").send_keys(str(tabela.loc[linha, 'codigo']))
    driver.find_element(By.ID,"marca").send_keys(str(tabela.loc[linha, 'marca']))
    driver.find_element(By.ID,"tipo").send_keys(str(tabela.loc[linha, 'tipo']))
    driver.find_element(By.ID,"categoria").send_keys(str(tabela.loc[linha, 'categoria']))
    driver.find_element(By.ID,"preco_unitario").send_keys(str(tabela.loc[linha, 'preco_unitario']))
    driver.find_element(By.ID,"custo").send_keys(str(tabela.loc[linha, 'custo']))
    
    #A coluna OBS nem sempre é preenchida, então, se ela não for nula, ele preenche o que está escrito nela.
    #Se não, ele preenche 'Sem observação'
    if not pandas.isna(tabela.loc[linha,'obs']):
        driver.find_element(By.ID,"obs").send_keys(str(tabela.loc[linha, 'obs']))
    else:
        driver.find_element(By.ID,"obs").send_keys('Sem observação')
        
    #Procura pelo ID pgtpy-botao, que é o botão de enviar, e dá um click
    driver.find_element(By.ID,"pgtpy-botao").click()

# Fechar o navegador ao final (opcional)
##driver.quit()

