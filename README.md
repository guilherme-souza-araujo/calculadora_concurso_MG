# Calculadora de Nota

Este projeto é uma ferramenta em Python projetada para calcular as notas do concurso da educação do estado de MG.
A ferramenta extrai dados dos 3 arquivos diferentes e exporta a soma das notas para um arquivo CSV.

## 🚀 Estrutura do Projeto

O projeto está organizado da seguinte forma:

- **`main.py`**: Ponto de entrada principal da aplicação.
- **`main_interactive.py`**: Versão interativa do programa para uso via terminal.
- **`calculo.py`**: Contém a lógica principal de processamento das notas.
- **`redacao.py`**: Módulo específico para o cálculo da pontuação de redação.
- **`titulos.py`**: Gerencia a pontuação referente a títulos ou certificados.
- **`totais.py`**: Responsável por consolidar os resultados e gerar os totais finais.
- **`requirements.txt`**: Lista de dependências do projeto.
- **`files/`**: Diretório destinado ao armazenamento de arquivos de dados ou logs.

## 🛠️ Pré-requisitos

Certifique-se de ter o Python 3.13+ instalado. O projeto utiliza `virtualenv` para gerenciamento de pacotes.

## 📦 Instalação

1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   cd calculadora_nota
   ```

2. Crie e ative o ambiente virtual:
   ```bash
   python -m venv venv
   # No Windows:
   .\venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Como Usar

### Modo interativo

Para iniciar a aplicação em modo interativo, execute:

```bash
python main_interactive.py
```

### Modo bash

#### Parâmetros do main.py

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `--ping` | `int` | Página inicial da nota geral |
| `--pfng` | `int` | Página final da nota geral |
| `--pir` | `int` | Página inicial da redação |
| `--pfr` | `int` | Página final da redação |
| `--pit` | `int` | Página inicial dos títulos |
| `--pft` | `int` | Página final dos títulos |
| `--path_nota_geral` | `str` | Caminho do arquivo PDF com as notas gerais |
| `--path_nota_redacao` | `str` | Caminho do arquivo PDF com as notas das redações |
| `--path_nota_titulo` | `str` | Caminho do arquivo PDF com as notas dos títulos |
| `--path_resultado` | `str` | Caminho do arquivo CSV a ser gerado com o resultado |

**Exemplo de uso:**

```bash
python main.py --ping 1 --pfng 10 --pir 1 --pfr 5 --pit 1 --pft 3 \
  --path_nota_geral "files/_163_29288764.pdf" \
  --path_nota_redacao "files/_166_12972708.pdf" \
  --path_nota_titulo "files/_168_10815577.pdf" \
  --path_resultado "resultado.csv"
```