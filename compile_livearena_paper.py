import os
import subprocess
import shutil
import pypdf

DIR_PATH = r"C:\Users\RYZEN 7\Desktop\Thesis\FYP-Sports-Events\ieee_research_paper"
WORKSPACE_1 = r"C:\Users\RYZEN 7\Desktop\Thesis\FYP-Sports-Events"
WORKSPACE_2 = r"c:\Users\RYZEN 7\Desktop\Thesis\RsearchPaper"

OUTPUT_PDF_1 = os.path.join(WORKSPACE_1, "LiveArena_Research_Paper.pdf")
OUTPUT_PDF_2 = os.path.join(WORKSPACE_2, "LiveArena_Research_Paper.pdf")
SYNC_PDF = os.path.join(DIR_PATH, "LiveArena_Research_Paper.pdf")

def run_latex():
    print(f"Working directory: {DIR_PATH}")
    
    # 1. First pdflatex pass
    print("Running pdflatex pass 1...")
    p1 = subprocess.run(["pdflatex", "-interaction=nonstopmode", "main.tex"], cwd=DIR_PATH, capture_output=True, text=True)
    if p1.returncode != 0:
        print("Error in pdflatex pass 1:")
        print(p1.stdout[-1000:])
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
        
    shutil.copy2(generated_pdf, OUTPUT_PDF_1)
    shutil.copy2(generated_pdf, OUTPUT_PDF_2)
    shutil.copy2(generated_pdf, SYNC_PDF)
    print(f"SUCCESS: Compiled and saved PDF to:")
    print(f"  - {OUTPUT_PDF_1} ({os.path.getsize(OUTPUT_PDF_1):,} bytes)")
    print(f"  - {OUTPUT_PDF_2} ({os.path.getsize(OUTPUT_PDF_2):,} bytes)")
    print(f"  - {SYNC_PDF} ({os.path.getsize(SYNC_PDF):,} bytes)")
    
    # Inspect PDF using pypdf
    reader = pypdf.PdfReader(OUTPUT_PDF_2)
    print(f"Total Pages in final IEEE paper: {len(reader.pages)}")
    for i, p in enumerate(reader.pages):
        lines = p.extract_text().splitlines()
        first = lines[0] if lines else ''
        print(f"  Page {i+1}: {first[:60]}")
    return True

if __name__ == "__main__":
    run_latex()
