from calculo import save_csv
from redacao import convert_redacao
from titulos import convert_titulos
from totais import convert_totais


totais_path = input("Informe o caminho do arquivo de nota geral:")
ping = int(input("Informe a pagina inicial a ser processada da nota geral:"))
pfng = int(input("Informe a pagina final a ser processada da nota geral:"))

redacao_path = input("Informe o caminho do arquivo de nota de redação:")
pir = int(input("Informe a pagina inicial a ser processada da nota de redação:"))
pfr = int(input("Informe a pagina final a ser processada da nota de redação:"))

titulo_path = input("Informe o caminho do arquivo de nota de titulos:")
pit = int(input("Informe a pagina inicial a ser processada da nota de titulos:"))
pft = int(input("Informe a pagina final a ser processada da nota de titulos:"))

path_resultado = input("Informe o caminho do arquivo CSV a ser gerado com o resultado:")

totais = convert_totais(totais_path, ping, pfng)
redacao = convert_redacao(redacao_path, pir, pfr)
titulos = convert_titulos(titulo_path, pit, pft)

save_csv(totais, redacao, titulos, path_resultado)