import argparse
import os
import pdfplumber


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process all pdf files in a dir")
    parser.add_argument("directory", type=str, help="Target path (usually 'target')")
    args = parser.parse_args()
    
    if os.path.isdir(args.directory):
        process_pdfs(args.directory)
    else:
        print("Error: Not a valid dir path.")