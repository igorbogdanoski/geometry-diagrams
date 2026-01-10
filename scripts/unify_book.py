import os
import re
import subprocess
import shutil
from datetime import datetime
from pathlib import Path

# Конфигурација
ASY_EXE = r"C:\Progra~1\Asymptote\asy.exe"
PROJECT_ROOT = Path(r"c:\Users\pc4all\Documents\matholimpiad\geometry-diagrams\projects\geometrija_kniga")
HEADER_PATH = Path(r"c:\Users\pc4all\Documents\matholimpiad\geometry-diagrams\templates\pro_header.asy")
ARCHIVE_ROOT = PROJECT_ROOT / "archive"

def get_next_worksheet_number():
    """Наоѓа кој е следниот број за работен лист во архивата."""
    ARCHIVE_ROOT.mkdir(exist_ok=True)
    existing = list(ARCHIVE_ROOT.glob("worksheet_*"))
    if not existing:
        return 1
    
    nums = []
    for p in existing:
        match = re.search(r'worksheet_(\d+)', p.name)
        if match:
            nums.append(int(match.group(1)))
    
    return max(nums) + 1 if nums else 1

def verify_and_fix_code(code):
    """Ги поправа вообичаените грешки според Професионалниот водич."""
    code = code.replace('point O = (0,0);', 'point O = origin;')
    code = re.sub(r'\bsize\(.*?\);', '// size removed', code)
    code = code.replace('dot(O, dotfactor=4)', 'dot(O)')
    code = code.replace('dotfactor=4', '')
    
    # Fix Label rotation: Label(..., rotate(90)) -> rotate(90)*Label(...)
    code = re.sub(r'Label\((.*?),\s*(rotate\(\d+\))\)', r'\2*Label(\1)', code)
    
    # Fix draw(guide, Arrow, pen) -> draw(guide, pen, Arrow)
    code = re.sub(r'draw\((.*?),\s*(Arrows?\(.*?\)),\s*([a-z. ]+)\)', r'draw(\1, \3, \2)', code)

    # Escape single braces in labels for LaTeX
    code = code.replace('Label("{",', 'Label("\{",')
    code = code.replace('Label("}",', 'Label("\}",')

    if 'Label' in code or 'label' in code:
        if 'filltype' not in code:
            code = code.replace('align=', 'filltype=UnFill(1mm), align=')

    if 'Arrow' in code and 'TeXHead' not in code:
        code = code.replace('Arrow', 'Arrow(TeXHead)')
        
    return code

def unify():
    ws_num = get_next_worksheet_number()
    ws_name = f"worksheet_{ws_num}"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    
    print(f"--- Processing {ws_name} ---")

    # 1. Processing Code
    input_code_path = PROJECT_ROOT / "input_code.md"
    if not input_code_path.exists() or input_code_path.stat().st_size == 0:
        print("Error: input_code.md is empty.")
        return

    with open(input_code_path, "r", encoding="utf-8") as f:
        code_content = f.read()

    with open(HEADER_PATH, "r", encoding="utf-8") as f:
        header = f.read()

    asy_blocks = re.findall(r'```asy\s*(.*?)\s*```', code_content, re.DOTALL)
    image_paths = []

    for block in asy_blocks:
        match = re.search(r'//\s*PROBLEM:\s*([^\n]+)', block)
        file_id = match.group(1).strip() if match else f"img_{len(image_paths)}"
        
        clean_code = verify_and_fix_code(block)
        src_path = PROJECT_ROOT / "src" / f"{file_id}.asy"
        src_path.parent.mkdir(exist_ok=True)
        
        with open(src_path, "w", encoding="utf-8") as f:
            f.write(header + "\n" + clean_code)
        
        svg_out = PROJECT_ROOT / "svg" / file_id
        svg_out.parent.mkdir(exist_ok=True)
        print(f"Generating: {file_id}.svg")
        subprocess.run(
            [ASY_EXE, "-f", "svg", "-o", str(svg_out), src_path.name],
            cwd=str(src_path.parent)
        )
        image_paths.append(f"svg/{file_id}.svg")

    # 2. Merging with Tasks
    input_tasks_path = PROJECT_ROOT / "input_tasks.md"
    with open(input_tasks_path, "r", encoding="utf-8") as f:
        tasks_content = f.read()

    final_md = tasks_content
    
    # Fix answer formatting (put inside $ for \quad)
    final_md = re.sub(r'\*\*Одговори:\*\*\s*(A\).*)', r'**Одговори:** $\1$', final_md)

    used_images = 0
    while "[СЛИКА ОД ОРИГИНАЛ]" in final_md and used_images < len(image_paths):
        final_md = final_md.replace("[СЛИКА ОД ОРИГИНАЛ]", f"\n![Diagram]({image_paths[used_images]})\n", 1)
        used_images += 1
    
    # Append leftover images
    if used_images < len(image_paths):
        final_md += "\n\n### Дополнителни дијаграми:\n"
        for i in range(used_images, len(image_paths)):
            final_md += f"![Diagram]({image_paths[i]})\n"

    output_file = PROJECT_ROOT / f"FINAL_{ws_name}.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(final_md)

    # 3. ARCHIVING & CLEANUP
    archive_dir = ARCHIVE_ROOT / f"{ws_name}_{timestamp}"
    archive_dir.mkdir(parents=True)
    
    shutil.move(str(input_tasks_path), str(archive_dir / "input_tasks.md"))
    shutil.move(str(input_code_path), str(archive_dir / "input_code.md"))
    
    open(input_tasks_path, 'w', encoding='utf-8').close()
    open(input_code_path, 'w', encoding='utf-8').close()

    print(f"\n[SUCCESS] {ws_name} completed.")
    print(f"Final file: {output_file}")
    print(f"Inputs archived to: {archive_dir}")
    print("Ready for next input!")

if __name__ == "__main__":
    unify()
