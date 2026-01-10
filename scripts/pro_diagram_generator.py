import os
import re
import subprocess
from pathlib import Path

class ProAsyGenerator:
    def __init__(self):
        self.root = Path(__file__).parent.parent
        self.header_path = self.root / "templates" / "pro_header.asy"
        self.output_dir = self.root / "diagrams"
        
    def read_header(self):
        with open(self.header_path, 'r', encoding='utf-8') as f:
            return f.read()

    def generate_problem_code(self, problem_data):
        header = self.read_header()
        
        # Example of high-precision construction logic (Group 1-3 from Guide)
        construction = f"""
// --- Construction: {problem_data['title']} ---
point O = (0,0);
{problem_data['construction']}

// --- Drawing ---
{problem_data['drawing']}

// --- Labels ---
{problem_data['labels']}
"""
        return header + construction

    def compile(self, filename):
        try:
            asy_cmd = r"C:\Program Files\Asymptote\asy.exe"
            # Compile to PDF
            subprocess.run(
                [asy_cmd, "-f", "pdf", f"{filename}.asy"],
                capture_output=True,
                text=True,
                cwd=str(self.output_dir)
            )
            # Compile to SVG (High Quality)
            subprocess.run(
                [asy_cmd, "-f", "svg", f"{filename}.asy"],
                capture_output=True,
                text=True,
                cwd=str(self.output_dir)
            )
            print(f"[OK] {filename} generated in PDF and SVG.")
            return True
        except Exception as e:
            print(f"[ERR] Compilation failed: {e}")
            return False

    def _compile_no_tex(self, asy_path):
        # Create a temp copy without TeX
        with open(asy_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        temp_path = asy_path.with_name(f"{asy_path.stem}_notex.asy")
        with open(temp_path, 'w', encoding='utf-8') as f:
            f.write('settings.tex="none";\n' + content)
            
        asy_cmd = r"C:\Program Files\Asymptote\asy.exe"
        subprocess.run([asy_cmd, "-f", "pdf", f"diagrams/{temp_path.name}"], cwd=self.root)

# Example usage for a real geometry problem
if __name__ == "__main__":
    generator = ProAsyGenerator()
    
    # Data for Problem 4 from Olympiad Archive
    problem4 = {
        "title": "Задача 4 - Агли помеѓу четири полуправи",
        "construction": """
// Пресметка: 3x + 90 - 3x + 7x = 180 (бидејќи OA perp OB и OC perp OD)
// Резултат: x = 18
real x = 18;
real angleA = 0;
real angleB = 90;
real angleC = 3*x; // 54 degrees
real angleD = angleC - 90; // -36 degrees (или 324)

pair A = dir(angleA) * 3;
pair B = dir(angleB) * 3;
pair C = dir(angleC) * 3;
pair D = dir(angleD) * 3;
""",
        "drawing": r"""
draw(O--A, black + linewidth(1pt));
draw(O--B, black + linewidth(1pt));
draw(O--C, black + linewidth(1pt));
draw(O--D, black + linewidth(1pt));

markrightangle(A, O, B, size=0.3cm);
markrightangle(C, O, D, size=0.3cm);

markangle("$3x^\circ$", A, O, C, radius=0.7cm, p=red);
markangle("$7x^\circ$", B, O, D, radius=1cm, p=blue);
""",
        "labels": r"""
dot(O); label("$O$", O, SW, label_mask);
label("$A$", A, E, label_mask);
label("$B$", B, N, label_mask);
label("$C$", C, NE, label_mask);
label("$D$", D, SE, label_mask);
"""
    }
    
    code = generator.generate_problem_code(problem4)
    with open(generator.output_dir / "zadacha_4_pure.asy", "w", encoding='utf-8') as f:
        f.write(code)
    
    generator.compile("zadacha_4_pure")
