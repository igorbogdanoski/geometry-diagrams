#!/usr/bin/env python3
"""
AI-Powered Geometry Diagram Generator

This script implements the Educational Content Architect & Geometry Visualizer system
for automated generation of Asymptote diagrams and worksheets from geometry problems.

Based on the system instruction for Macedonian Olympiad mathematics education.
"""

import os
import json
import re
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Tuple

class GeometryVisualizer:
    """
    Educational Content Architect & Geometry Visualizer

    Processes geometry problems to generate:
    1. Asymptote code for precise diagrams
    2. Educational worksheets with scaffolding
    3. Nano Banana prompts for illustrations
    """

    def __init__(self):
        self.templates_dir = Path(__file__).parent.parent / "templates"
        self.diagrams_dir = Path(__file__).parent.parent / "diagrams"
        self.worksheets_dir = Path(__file__).parent.parent / "worksheets"

        # Ensure directories exist
        self.diagrams_dir.mkdir(exist_ok=True)
        self.worksheets_dir.mkdir(exist_ok=True)

        # Asymptote code templates
        self.asy_templates = {
            "basic_triangle": """
settings.outformat = "pdf";
size(200);
defaultpen(linewidth(1pt));

// Triangle vertices
pair A = (0, 0);
pair B = (4, 0);
pair C = (2, 3);

// Draw triangle
draw(A--B--C--cycle, black);

// Labels
label("$A$", A, SW);
label("$B$", B, SE);
label("$C$", C, N);

// Optional: right angle marker at B
draw((B.x, B.y)--(B.x+0.3, B.y)--(B.x+0.3, B.y+0.3), black);
""",
            "parallel_lines": """
settings.outformat = "pdf";
size(200);
defaultpen(linewidth(1pt));

// Parallel lines
pair A1 = (0, 2);
pair B1 = (6, 2);
pair A2 = (0, 0);
pair B2 = (6, 0);

// Draw parallels
draw(A1--B1, black);
draw(A2--B2, black);

// Transversal
pair P1 = (1, 2);
pair P2 = (3, 0);
draw(P1--P2, blue);

// Labels
label("$a$", B1, E);
label("$b$", B2, E);
""",
            "circle": """
settings.outformat = "pdf";
size(200);
defaultpen(linewidth(1pt));

// Circle
pair center = (0, 0);
real radius = 2;

// Draw circle
draw(circle(center, radius), black);

// Center and labels
dot(center);
label("$O$", center, S);
label("$r$", center + (1.5, 0.5));
"""
        }

    def extract_geometric_elements(self, problem_text: str) -> Dict:
        """
        Extract geometric elements from problem text.

        Returns:
            Dict with keys: shapes, points, angles, measurements
        """
        elements = {
            "shapes": [],
            "points": [],
            "angles": [],
            "measurements": [],
            "properties": []
        }

        # Extract points (A, B, C, etc.)
        points = re.findall(r'\b[A-Z]\b', problem_text)
        elements["points"] = list(set(points))

        # Extract shapes
        if "триаголник" in problem_text.lower():
            elements["shapes"].append("triangle")
        if "круг" in problem_text.lower() or "кружница" in problem_text.lower():
            elements["shapes"].append("circle")
        if "правоаголник" in problem_text.lower():
            elements["shapes"].append("rectangle")
        if "квадрат" in problem_text.lower():
            elements["shapes"].append("square")

        # Extract angles
        angles = re.findall(r'(\d+)\s*°', problem_text)
        elements["angles"] = [int(angle) for angle in angles]

        # Extract measurements
        measurements = re.findall(r'(\d+(?:,\d+)?)\s*(cm|mm|m)', problem_text)
        elements["measurements"] = measurements

        return elements

    def generate_asymptote_code(self, problem_text: str, problem_id: str) -> str:
        """
        Generate Asymptote code based on problem analysis.
        """
        elements = self.extract_geometric_elements(problem_text)

        # Choose appropriate template
        if "триаголник" in problem_text.lower():
            base_code = self.asy_templates["basic_triangle"]
        elif "паралелни" in problem_text.lower():
            base_code = self.asy_templates["parallel_lines"]
        elif "круг" in problem_text.lower():
            base_code = self.asy_templates["circle"]
        else:
            base_code = self.asy_templates["basic_triangle"]  # fallback

        # Customize based on extracted elements
        code_lines = base_code.strip().split('\n')

        # Add points if specified
        if elements["points"]:
            points_code = []
            for i, point in enumerate(elements["points"][:3]):  # Limit to 3 points for basic shapes
                x, y = [0, 2, 4][i], [0, 0, 3][i]  # Simple positioning
                points_code.append(f"pair {point} = ({x}, {y});")
            points_code.append("")

            # Insert after settings
            insert_pos = 3
            code_lines[insert_pos:insert_pos] = points_code

        # Add angle markers if angles specified
        if elements["angles"]:
            angle_code = []
            for angle in elements["angles"][:2]:  # Limit to 2 angles
                angle_code.append(f"// Angle marker for {angle}°")
                angle_code.append("draw(arc((0,0), 0.5, 0, 45), red);")
                angle_code.append(f'label("${angle}^\\circ$", (0.3, 0.2));')
            angle_code.append("")

            code_lines.extend(angle_code)

        return '\n'.join(code_lines)

    def generate_nano_banana_prompt(self, problem_text: str) -> str:
        """
        Generate Nano Banana prompt for illustration context.
        """
        if "триаголник" in problem_text.lower():
            return "Geometric triangle pattern on mathematical graph paper, clean minimal design, educational mathematics style, no text."
        elif "круг" in problem_text.lower():
            return "Circular geometric pattern with compass and ruler, technical drawing style, educational mathematics, no text."
        elif "паралелни" in problem_text.lower():
            return "Parallel lines construction on engineering blueprint, technical precision, educational geometry, no text."
        else:
            return "Geometric shapes on coordinate plane, clean mathematical illustration, educational style, no text."

    def process_problem(self, problem_text: str, problem_id: str, problem_title: str) -> Dict:
        """
        Main processing function - generates complete educational package.

        Returns:
            Dict with keys: asy_code, worksheet_md, image_path, compiled_success
        """
        result = {
            'asy_code': '',
            'worksheet_md': '',
            'image_path': '',
            'compiled_success': False
        }

        # Generate Asymptote code
        asy_code = self.generate_asymptote_code(problem_text, problem_id)

        # Save Asymptote code
        self.save_diagram(problem_id, asy_code)
        result['asy_code'] = asy_code

        # Attempt compilation
        compiled_path = self.compile_diagram(problem_id)
        result['image_path'] = compiled_path
        result['compiled_success'] = compiled_path is not None

        # Generate worksheet content with embedded image
        worksheet = self.generate_worksheet_content_with_image(problem_text, problem_title, compiled_path)
        self.save_worksheet(problem_id, worksheet)
        result['worksheet_md'] = worksheet

        return result

    def compile_diagram(self, problem_id: str) -> Optional[str]:
        """Compile Asymptote diagram and return path to generated PDF."""
        asy_file = self.diagrams_dir / f"{problem_id}.asy"
        pdf_file = self.diagrams_dir / f"{problem_id}.pdf"

        if not asy_file.exists():
            print(f"✗ Asymptote file not found: {asy_file}")
            return None

        try:
            # Run asy compilation
            result = subprocess.run(
                ["asy", "-f", "pdf", str(asy_file)],
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.returncode == 0 and pdf_file.exists():
                print(f"✓ Compiled diagram: {pdf_file}")
                return str(pdf_file)
            else:
                print(f"✗ Compilation failed: {result.stderr}")
                return None

        except Exception as e:
            print(f"✗ Compilation error: {e}")
            return None

    def generate_worksheet_content_with_image(self, problem_text: str, problem_title: str, image_path: Optional[str]) -> str:
        """
        Generate worksheet content with embedded image reference.
        Optimized for SimpleTex and Word/InDesign export.
        """
        # Adapted problem text (placeholder for translation)
        adapted_text = self.adapt_to_macedonian(problem_text)

        # Generate scaffolding
        scaffolding = self.generate_scaffolding(problem_text)

        # Image reference for Markdown
        image_ref = ""
        if image_path:
            image_ref = f'\n![Геометриска конструкција]({image_path})\n'

        worksheet = f"""# {problem_title}

## 📐 Геометриска Конструкција
{image_ref}

## 📝 Текст на Задачата
{adapted_text}

## 🧠 Стратегија и Насоки
{chr(10).join(f'* {item}' for item in scaffolding)}

## 💡 Практични Совети
* Користи геометриски инструменти за прецизно цртање
* Означи ги сите познати и непознати елементи
* Провери ги конструкциите со мерење

---
*Работен лист генериран со AI - Educational Content Architect & Geometry Visualizer*
"""

        return worksheet

    def adapt_to_macedonian(self, problem_text: str) -> str:
        """
        Adapt problem text to Macedonian educational standards.
        Placeholder - in real implementation, use translation AI.
        """
        # Basic adaptations
        adapted = problem_text

        # Localize names (example)
        adapted = adapted.replace("triangle", "триаголник")
        adapted = adapted.replace("circle", "кружница")
        adapted = adapted.replace("parallel", "паралелни")

        # Add Macedonian LaTeX formatting
        adapted = re.sub(r'(\w+)\s*\^\s*(\w+)', r'$\1^{\circ}$', adapted)  # 30^o -> 30°
        adapted = re.sub(r'(\d+)\s*degrees?', r'$\1^{\circ}$', adapted)

        return adapted

    def generate_scaffolding(self, problem_text: str) -> List[str]:
        """Generate educational scaffolding hints."""
        hints = []

        if "триаголник" in problem_text.lower():
            hints.extend([
                "**Потребни Формули:** Питагорова теорема $c^2 = a^2 + b^2$",
                "**Совет:** Нацртај ги аглите и означете ги познатите страни",
                "**Клучен чекор:** Одреди кој агол е прав"
            ])

        if "круг" in problem_text.lower():
            hints.extend([
                "**Формула:** Плоштина $P = \\pi r^2$, Периметар $O = 2\\pi r$",
                "**Совет:** Центарот е клучна точка за симетрии",
                "**Клучен чекор:** Повлечи радиуси до пресечните точки"
            ])

        if "паралелни" in problem_text.lower():
            hints.extend([
                "**Својство:** Наизменични агли се еднакви",
                "**Совет:** Користи транспарентна хартија за проверка",
                "**Клучен чекор:** Повлечи трансверзала"
            ])

        return hints

    def save_diagram(self, problem_id: str, asy_code: str):
        """Save Asymptote code to diagrams directory."""
        filename = f"{problem_id}.asy"
        filepath = self.diagrams_dir / filename

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(asy_code)

        print(f"✓ Saved diagram: {filepath}")

    def save_worksheet(self, problem_id: str, worksheet_content: str):
        """Save worksheet content to worksheets directory."""
        filename = f"{problem_id}_worksheet.md"
        filepath = self.worksheets_dir / filename

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(worksheet_content)

        print(f"✓ Saved worksheet: {filepath}")

def main():
    """Command-line interface for the geometry visualizer."""
    import argparse

    parser = argparse.ArgumentParser(description="AI-Powered Geometry Diagram Generator")
    parser.add_argument("--problem-id", required=True, help="Unique problem identifier")
    parser.add_argument("--title", required=True, help="Problem title")
    parser.add_argument("--input", required=True, help="Path to problem text file")

    args = parser.parse_args()

    # Read problem text
    with open(args.input, 'r', encoding='utf-8') as f:
        problem_text = f.read()

    # Initialize visualizer
    visualizer = GeometryVisualizer()

    # Process problem
    result = visualizer.process_problem(problem_text, args.problem_id, args.title)

    print("✓ Processing complete!")
    print(f"Asymptote code saved to diagrams/{args.problem_id}.asy")
    print(f"Worksheet saved to worksheets/{args.problem_id}_worksheet.md")
    if result['compiled_success']:
        print(f"PDF compiled: {result['image_path']}")
    else:
        print("PDF compilation failed")

if __name__ == "__main__":
    main()