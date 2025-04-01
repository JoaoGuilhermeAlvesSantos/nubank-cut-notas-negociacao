import argparse
import os
import pdfplumber


def process_pdfs(directory):
    # Listar todos os arquivos PDF no diretório
    pdf_files = [f for f in os.listdir(directory) if f.lower().endswith('.pdf')]
    
    if not pdf_files:
        print("Nenhum arquivo PDF encontrado no diretório.")
        return

    for pdf_file in pdf_files:
        pdf_path = os.path.join(directory, pdf_file)
        print(f"Abrindo: {pdf_path}")

        # Abrir e processar o PDF
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                print(f"\n--- Página {i+1} de {pdf_file} ---\n")
                print(text if text else "[Nenhum texto encontrado]")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process all pdf files in a dir")
    parser.add_argument("directory", type=str, help="Target path (usually 'target')")
    args = parser.parse_args()
    
    if os.path.isdir(args.directory):
        process_pdfs(args.directory)
    else:
        print("Error: Not a valid dir path.")