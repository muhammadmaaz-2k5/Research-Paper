import os
import subprocess
import shutil
import pymupdf

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
WORKSPACE = os.path.dirname(DIR_PATH)
OUTPUT_PDF = os.path.join(WORKSPACE, "LiveArena_Research_Paper.pdf")
SYNC_PDF = os.path.join(DIR_PATH, "LiveArena_Research_Paper.pdf")

def run_latex():
    print(f"Working directory: {DIR_PATH}")
    
    # 1. First pdflatex pass
    print("Running pdflatex pass 1...")
    p1 = subprocess.run(["pdflatex", "-interaction=nonstopmode", "main.tex"], cwd=DIR_PATH, capture_output=True, text=True)
    if p1.returncode != 0:
        print("Error in pdflatex pass 1:")
        print(p1.stdout[-800:])
        return False
        
    # 2. Bibtex pass
    print("Running bibtex...")
    b = subprocess.run(["bibtex", "main"], cwd=DIR_PATH, capture_output=True, text=True)
    if b.returncode != 0:
        print("Warning/Error in bibtex:")
        print(b.stdout[-400:])
        
    # 3. Second pdflatex pass
    print("Running pdflatex pass 2...")
    subprocess.run(["pdflatex", "-interaction=nonstopmode", "main.tex"], cwd=DIR_PATH, capture_output=True, text=True)
    
    # 4. Third pdflatex pass (resolve all references)
    print("Running pdflatex pass 3...")
    subprocess.run(["pdflatex", "-interaction=nonstopmode", "main.tex"], cwd=DIR_PATH, capture_output=True, text=True)
    
    generated_pdf = os.path.join(DIR_PATH, "main.pdf")
    if not os.path.exists(generated_pdf):
        print("Failed: main.pdf not found.")
        return False
        
    shutil.copy2(generated_pdf, OUTPUT_PDF)
    shutil.copy2(generated_pdf, SYNC_PDF)
    print(f"SUCCESS: Compiled and saved PDF to {OUTPUT_PDF} ({os.path.getsize(OUTPUT_PDF):,} bytes)")
    
    # Inspect PDF using PyMuPDF
    doc = pymupdf.open(OUTPUT_PDF)
    print(f"Total Pages in final IEEE paper: {len(doc)}")
    doc.close()
    return True

if __name__ == "__main__":
    run_latex()
