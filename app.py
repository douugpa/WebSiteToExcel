from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

# acessar o site https://www.novaliderinformatica.com.br/computadores-gamers
driver = webdriver.Chrome()
driver.get('https://www.novaliderinformatica.com.br/computadores-gamers')

# extrair todos os nomes
nomes = driver.find_elements(By.XPATH, "//a[@class='nome-produto']")

# extrair todos os preços
precos = driver.find_elements(By.XPATH, "//strong[@class='preco-promocional']")

# Criar Planilha
workbook = openpyxl.Workbook()
# Criando a pagina Produtos na planilha
workbook.create_sheet('Produtos')
sheet_produtos = workbook['Produtos']
# Criando as colunas na pagina Produtos da planilha
sheet_produtos['A1'].value = "Nome"
sheet_produtos['B1'].value = "Preços"

# inserir os nomes e preços na planilha
for nome, preco in zip(nomes, precos):
   sheet_produtos.append([nome.text, preco.text]) 

   workbook.save('produtos.xlsx')