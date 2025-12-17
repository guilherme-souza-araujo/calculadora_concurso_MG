import argparse

from calculo import save_csv
from redacao import convert_redacao
from titulos import convert_titulos
from totais import convert_totais

parser = argparse.ArgumentParser(description="Calcular nota concurso")

parser.add_argument("--ping", type=int, help="Pagina inicial nota geral")
parser.add_argument("--pfng", type=int, help="Pagina final nota geral")
parser.add_argument("--pir", type=int, help="Pagina inicial redação")
parser.add_argument("--pfr", type=int, help="Pagina final redação")
parser.add_argument("--pit", type=int, help="Pagina inicial titulos")
parser.add_argument("--pft", type=int, help="Pagina final titulos")
parser.add_argument("--path_nota_geral", type=str, help="Caminho do arquivo nota geral")
parser.add_argument("--path_nota_redacao", type=str, help="Caminho do arquivo nota das redações")
parser.add_argument("--path_nota_titulo", type=str, help="Caminho do arquivo nota titulos")
parser.add_argument("--path_resultado", type=str, help="Caminho do arquivo CSV a ser gerado com o resultado")


args = parser.parse_args()

totais_path = args.path_nota_geral
redacao_path = args.path_nota_redacao
titulo_path = args.path_nota_titulo
path_resultado = args.path_resultado

totais = convert_totais(totais_path, args.ping, args.pfng)
redacao = convert_redacao(redacao_path, args.pir, args.pfr)
titulos = convert_titulos(titulo_path, args.pit, args.pft)

save_csv(totais, redacao, titulos, path_resultado)