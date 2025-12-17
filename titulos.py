import pdfplumber
import re

NUM_PARTS = 7

rows = []

def convert_titulos(pdf_path: str, pag_inicial: int, pag_final: int) -> list[dict]:
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
                if "Inscrição" in line_text or "Nome" in line_text or "----" in line_text:
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

                while len(parts) > NUM_PARTS:
                    parts[1] = " ".join(parts[1:3])
                    parts.pop(2)

                row = {
                    "inscricao": parts[0],
                    "Nome": parts[1],
                    "Doutorado": float(parts[2].replace(",", ".")),
                    "Mestrado": float(parts[3].replace(",", ".")),
                    "Especializacao": float(parts[4].replace(",", ".")),
                    "Tempo_de_Servico": float(parts[5].replace(",", ".")),
                    "Avaliacao_de_Titulos": float(parts[6].replace(",", ".")),
                }
                rows.append(row)

    return rows
