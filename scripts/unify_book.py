import os
import re
import subprocess
from pathlib import Path

# Конфигурација
ASY_EXE = r"C:\Progra~1\Asymptote\asy.exe"
PROJECT_ROOT = Path(r"c:\Users\pc4all\Documents\matholimpiad\geometry-diagrams\projects\geometrija_kniga")
HEADER_PATH = Path(r"c:\Users\pc4all\Documents\matholimpiad\geometry-diagrams\templates\pro_header.asy")

def verify_and_fix_code(code):
    """Ги поправа вообичаените грешки според Професионалниот водич."""
    # 1. Отстрани size() ако постои (Водичот налага unitsize)
    code = re.sub(r'size\(.*?\);', '// size removed', code)
    
    # 2. Поправи ја грешката со dotfactor во функцијата dot
    code = code.replace('dot(O, dotfactor=4)', 'dot(O)')
    code = code.replace('dotfactor=4', '')
    
    # 3. Обезбеди UnFill(1mm) за сите ознаки (Labels) ако моделот заборавил
    if 'Label' in code or 'label' in code:
        if 'filltype' not in code:
            code = code.replace('align=', 'filltype=UnFill(1mm), align=')

    # 4. Провери за TeXHead кај стрелките
    if 'Arrow' in code and 'TeXHead' not in code:
        code = code.replace('Arrow', 'Arrow(TeXHead)')
        
    return code

def unify():
    print("--- 1. Processing Asymptote Codes ---")
    with open(PROJECT_ROOT / "input_code.md", "r", encoding="utf-8") as f:
        code_content = f.read()

    with open(HEADER_PATH, "r", encoding="utf-8") as f:
        header = f.read()

    asy_blocks = re.findall(r'```asy\s*(.*?)\s*```', code_content, re.DOTALL)
    image_paths = []

    for block in asy_blocks:
        match = re.search(r'//\s*PROBLEM:\s*([^\n]+)', block)
        file_id = match.group(1).strip() if match else f"img_{len(image_paths)}"
        
        # ВЕРИФИКАЦИЈА И КОРЕКЦИЈА
        clean_code = verify_and_fix_code(block)
        
        src_path = PROJECT_ROOT / "src" / f"{file_id}.asy"
        src_path.parent.mkdir(exist_ok=True)
        
        with open(src_path, "w", encoding="utf-8") as f:
            # Комбинирање на заглавието со поправениот код
            f.write(header + "\n" + clean_code)
        
        # Компајлирање во SVG за приказ во Markdown
        svg_out = PROJECT_ROOT / "svg" / f"{file_id}.svg"
        svg_out.parent.mkdir(exist_ok=True)
        print(f"Generating: {file_id}.svg")
        subprocess.run([ASY_EXE, "-f", "svg", "-o", str(svg_out), str(src_path)])
        
        image_paths.append(f"svg/{file_id}.svg")

    print("\n--- 2. Merging with Tasks ---")
    with open(PROJECT_ROOT / "input_tasks.md", "r", encoding="utf-8") as f:
        tasks_content = f.read()

    # Замена на [СЛИКА ОД ОРИГИНАЛ] со генерираните слики по редослед
    final_md = tasks_content
    for img_url in image_paths:
        final_md = final_md.replace("[СЛИКА ОД ОРИГИНАЛ]", f"![Diagram]({img_url})", 1)

    with open(PROJECT_ROOT / "final_worksheet.md", "w", encoding="utf-8") as f:
        f.write(final_md)

    print(f"\n[DONE] Final worksheet created: {PROJECT_ROOT / 'final_worksheet.md'}")

if __name__ == "__main__":
    unify()
