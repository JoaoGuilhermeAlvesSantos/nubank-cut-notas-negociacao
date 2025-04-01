import argparse
import os, re
import pdfplumber


def aggregate(list_of_dicts):
    items = set([d["item"] for d in list_of_dicts])
    aggregated = []
    for item in items:
        total = 0
        quantity = 0
        for d in list_of_dicts:
            if d["item"] == item:
                total += d["total"]
                quantity += d["quantity"]
        aggregated.append(
            {
                "item": item,
                "quantity": quantity,
                "avgprice": f"{total/quantity:.2f}",
                "total": f"{total:.2f}",
            }
        )
    return aggregated


def process_pdfs(directory):
    # Listar todos os arquivos PDF no diretório
    pdf_files = [f for f in os.listdir(directory) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print("There's no pdf files in the target directory.")
        return

    transactions = []
    for pdf_file in pdf_files:
        pdf_path = os.path.join(directory, pdf_file)

        # Abrir e processar o PDF
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                pattern = r"\b\d{2}/\d{2}/\d{4}\b"
                date = re.findall(pattern, text)[0]
                for j in page.extract_text_lines():
                    txline = j["text"]
                    if txline.startswith("BOVESPA"):
                        terms = txline.split()
                        dictt = {
                            "date": date,
                            "market": terms[0],
                            "type": terms[1],
                            "item": terms[3],
                            "quantity": int(terms[-4]),
                            "price": float(
                                terms[-3].replace(".", "").replace(",", ".")
                            ),
                            "total": float(
                                terms[-2].replace(".", "").replace(",", ".")
                            ),
                        }
                        transactions.append(dictt)
    return transactions


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process all pdf files in a dir")
    parser.add_argument("directory", type=str, help="Target path (usually 'target')")
    args = parser.parse_args()

    if os.path.isdir(args.directory):
        listing = process_pdfs(args.directory)
        aggregated = aggregate(listing)
        print("item;quantidade;preçomedio;total")
        for i in aggregated:
            print(f"{i['item']};{i['quantity']};{i['avgprice']};{i['total']}")
    else:
        print("Error: Not a valid dir path.")
