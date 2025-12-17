import pdfplumber
import re


rows = []

def is_number(prova_redacao: str):
    try:
        float(prova_redacao)
        return True
    except ValueError:
        return False

def convert_totais(pdf_path: str, pag_inicial: int, pag_final: int) -> list[dict]:
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            if page.page_number < pag_inicial:
                continue

            if page.page_number > pag_final:
                break

            text_lines = page.extract_text_lines()
            if not text_lines:
                continue

            should_process = False
            for line in text_lines:
                line_text = line['text'].strip()

                # Skip headers and separators
                if "Inscrição" in line_text or "Nome" in line_text:
                    should_process = True
                    continue

                if "----" in line_text:
                    continue

                if not should_process:
                    continue

                # Split by 2 or more spaces
                parts = re.split(" ", line_text)

                if len(parts) < 10:
                    should_process = False
                    continue

                if parts[0] == "*Os":
                    continue

                if "PcD" in line_text:
                    parts[len(parts) - 2] = parts[len(parts) - 2] + " " + parts[len(parts) - 1]
                    parts.pop(len(parts) - 1)

                while len(parts) > 10:
                    parts[1] = " ".join(parts[1:3])
                    parts.pop(2)

                pt = parts[3].replace(",", ".")
                mat = parts[4].replace(",", ".")
                dh = parts[5].replace(",", ".")
                le = parts[6].replace(",", ".")
                ce = parts[7].replace(",", ".")
                no = parts[8].replace(",", ".")

                row = {
                    "inscricao": parts[0],
                    "Nome": parts[1],
                    "Nascimento": parts[2],
                    "Lingua_Portuguesa": float(pt) if is_number(pt) else pt,
                    "Matematica_Aplicada": float(mat) if is_number(mat) else mat,
                    "Direitos_Humanos": float(dh) if is_number(dh) else dh,
                    "Legislacao_Educacional": float(le) if is_number(le) else le,
                    "Conhecimentos_Especificos": float(ce) if is_number(ce) else ce,
                    "Nota_Objetiva": float(no) if is_number(no) else no,
                    "Situacao": parts[9],
                }
                rows.append(row)

    return rows
