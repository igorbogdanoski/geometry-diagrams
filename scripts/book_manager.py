import os
import re
import subprocess
from pathlib import Path

# Конфигурација
ASY_EXE = r"C:\Progra~1\Asymptote\asy.exe"
PROJECT_ROOT = Path(r"c:\Users\pc4all\Documents\matholimpiad\geometry-diagrams\projects\geometrija_kniga")
HEADER_PATH = Path(r"c:\Users\pc4all\Documents\matholimpiad\geometry-diagrams\templates\pro_header.asy")

def process_ai_output(raw_input):
    # 1. Екстракција на задачи (текст)
    tasks = re.findall(r'\*\*Задача\s*(\d+):\*\*(.*?)(?=\*\*Задача|\/\/|$)', raw_input, re.DOTALL)
    for num, content in tasks:
        task_file = PROJECT_ROOT / "tasks" / f"zadaca_{num}.md"
        task_file.parent.mkdir(exist_ok=True)
        with open(task_file, 'w', encoding='utf-8') as f:
            f.write(f"**Задача {num}:**{content.strip()}")
        print(f"[TXT] Зачуван текст за задача {num}")

    # 2. Екстракција на Asymptote код
    asy_blocks = re.findall(r'```asy\s*(.*?)\s*```', raw_input, re.DOTALL)
    
    with open(HEADER_PATH, 'r', encoding='utf-8') as f:
        header = f.read()

    for block in asy_blocks:
        # Наоѓање на името преку // PROBLEM: маркер
        match = re.search(r'//\s*PROBLEM:\s*([^\n]+)', block)
        if match:
            file_name = match.group(1).strip().replace(' ', '_')
            clean_code = block.replace(match.group(0), "").strip()
            
            asy_file = PROJECT_ROOT / "src" / f"{file_name}.asy"
            asy_file.parent.mkdir(exist_ok=True)
            
            # Додавање на про заглавието ако веќе го нема во блокот
            final_code = clean_code if "settings" in clean_code else header + "\n" + clean_code
            
            with open(asy_file, 'w', encoding='utf-8') as f:
                f.write(final_code)
            
            print(f"[ASY] Компајлирање: {file_name}")
            
            # PDF Експорт
            subprocess.run([ASY_EXE, "-f", "pdf", "-o", str(PROJECT_ROOT / "pdf" / f"{file_name}.pdf"), str(asy_file)])
            # SVG Експорт
            subprocess.run([ASY_EXE, "-f", "svg", "-o", str(PROJECT_ROOT / "svg" / f"{file_name}.svg"), str(asy_file)])
            
            print(f"[DONE] Генериран дијаграм за {file_name}")

if __name__ == "__main__":
    input_file = PROJECT_ROOT / "input_batch.txt"
    if input_file.exists():
        with open(input_file, 'r', encoding='utf-8') as f:
            process_ai_output(f.read())
    else:
        print(f"Ставете го излезот од AI во {input_file}")
