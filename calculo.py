class Calculo:
    Inscricao: str
    Nome: str
    LinguaPortuguesa: any = ""
    MatematicaAplicada: any = ""
    DireitosHumanos: any = ""
    LegislacaoEducacional: any = ""
    ConhecimentosEspecificos: any = ""
    ProvaRedacao: any = ""
    Mestrado: any = "0"
    Doutorado: any = "0"
    Especializacao: any = "0"
    TempoServico: any = "0"
    AvaliacaoTitulos: any = "0"
    NotaFinal: float
    Situacao: str


def is_number(value: str):
    try:
        float(value)
        return True
    except ValueError:
        return False

def save_csv(totais: list[dict], redacao: list[dict], titulos: list[dict], output_path: str):
    try:
        ranking = ["Inscricao,"
                   "Nome,"
                   "Lingua Portuguesa,"
                   "Matematica Aplicada,"
                   "Direitos Humanos,"
                   "Legislacao Educacional,"
                   "Conhecimentos Especificos,"
                   "Prova_de_Redacao,"
                   "Mestrado,"
                   "Doutorado,"
                   "Especializacao,"
                   "Tempo de Servico,"
                   "Avaliacao de Titulos,"
                   "Nota Final,"
                   "Situação"]

        for pessoa in totais:
            calculo = Calculo()
            calculo.Inscricao = pessoa["inscricao"]
            calculo.Nome = pessoa["Nome"]
            calculo.LinguaPortuguesa = pessoa["Lingua_Portuguesa"]
            calculo.MatematicaAplicada = pessoa["Matematica_Aplicada"]
            calculo.DireitosHumanos = pessoa["Direitos_Humanos"]
            calculo.LegislacaoEducacional = pessoa["Legislacao_Educacional"]
            calculo.ConhecimentosEspecificos = pessoa["Conhecimentos_Especificos"]
            calculo.NotaFinal = pessoa["Nota_Objetiva"]
            calculo.Situacao = pessoa["Situacao"]

            calculo.ProvaRedacao = 0
            for rd in redacao:
                if rd["inscricao"] == calculo.Inscricao:
                    red = rd["Prova_de_Redacao"]
                    if is_number(red):
                        calculo.NotaFinal += red
                    else:
                        calculo.NotaFinal += 20

                    calculo.ProvaRedacao = rd["Prova_de_Redacao"]

            for tt in titulos:
                if tt["inscricao"] == calculo.Inscricao:
                    at = tt["Avaliacao_de_Titulos"]
                    if is_number(at):
                        calculo.NotaFinal += at

                    calculo.Mestrado = tt["Mestrado"]
                    calculo.Doutorado = tt["Doutorado"]
                    calculo.Especializacao = tt["Especializacao"]
                    calculo.TempoServico = tt["Tempo_de_Servico"]
                    calculo.AvaliacaoTitulos = tt["Avaliacao_de_Titulos"]

            ranking.append(f"{calculo.Inscricao},"
                           f"{calculo.Nome},"
                           f"{calculo.LinguaPortuguesa},"
                           f"{calculo.MatematicaAplicada},"
                           f"{calculo.DireitosHumanos},"
                           f"{calculo.LegislacaoEducacional},"
                           f"{calculo.ConhecimentosEspecificos},"
                           f"{calculo.ProvaRedacao},"
                           f"{calculo.Mestrado},"
                           f"{calculo.Doutorado},"
                           f"{calculo.Especializacao},"
                           f"{calculo.TempoServico},"
                           f"{calculo.AvaliacaoTitulos},"
                           f"{calculo.NotaFinal:.2f},"
                           f"{calculo.Situacao}")

        #ranking.sort(key=lambda x: x["nota_final"], reverse=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(ranking))

    except Exception as e:
        print(f"Error: Failed to decode JSON from the file. Details: {e}")