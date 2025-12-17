import pdfplumber
import re

NUM_PARTS = 4

rows = []

def is_number(prova_redacao: str):
    try:
        float(prova_redacao)
        return True
    except ValueError:
        return False


def convert_redacao(pdf_path: str, pag_inicial: int, pag_final: int) -> list[dict]:
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

                if not should_process:
                    continue

                # Split by 2 or more spaces
                parts = re.split(" ", line_text)

                if len(parts) < NUM_PARTS:
                    should_process = False
                    continue

                if parts[0] == "*Os":
                    continue

                if "PcD" in line_text:
                    parts[len(parts) - 2] = parts[len(parts) - 2] + " " + parts[len(parts) - 1]
                    parts.pop(len(parts) - 1)

                while len(parts) > NUM_PARTS:
                    parts[1] = " ".join(parts[1:3])
                    parts.pop(2)

                prova_redacao = parts[2].replace(",", ".")

                row = {
                    "inscricao": parts[0],
                    "Nome": parts[1],
                    "Prova_de_Redacao": float(prova_redacao) if is_number(prova_redacao) else prova_redacao,
                    "Situação": parts[3],
                }
                rows.append(row)
    return rows
