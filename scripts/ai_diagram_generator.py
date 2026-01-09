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

    def generate_worksheet_content(self, problem_text: str, problem_title: str) -> str:
        """
        Generate educational worksheet content with scaffolding.
        """
        # Extract Macedonian problem text (placeholder)
        adapted_text = problem_text  # In real implementation, translate/adapt

        # Generate scaffolding
        scaffolding = []

        if "триаголник" in problem_text.lower():
            scaffolding.extend([
                "* **Потребни Формули:** Питагорова теорема $c^2 = a^2 + b^2$",
                "* **Совет:** Нацртај ги аглите и означете ги познатите страни",
                "* **Клучен чекор:** Одреди кој агол е прав"
            ])

        worksheet = f"""### 2. СОДРЖИНА ЗА РАБОТНИОТ ЛИСТ (За Ученикот)

**Наслов на лекцијата/темата: {problem_title}**

**Текст на задачата:**
{adapted_text}

**Паткази и Стратегија (Scaffolding):**
{chr(10).join(f'* {item}' for item in scaffolding)}

*(Крај на задачата - Нема решение)*
"""
        return worksheet

    def process_problem(self, problem_text: str, problem_id: str, problem_title: str) -> str:
        """
        Main processing function following the system instruction structure.
        """
        # Generate Asymptote code
        asy_code = self.generate_asymptote_code(problem_text, problem_id)

        # Generate Nano Banana prompt
        nb_prompt = self.generate_nano_banana_prompt(problem_text)

        # Generate worksheet content
        worksheet = self.generate_worksheet_content(problem_text, problem_title)

        # Combine into final output
        output = f"""### 1. ВИЗУЕЛНИ РЕСУРСИ (За Дизајнерот)
> **Asymptote Code (Recreation):**
> ```asy
{asy_code}
> ```

> **Nano Banana Prompt (Context):**
> {nb_prompt}

---

{worksheet}
"""

        return output

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

    # Extract and save components
    lines = result.split('\n')

    # Find Asymptote code
    asy_start = None
    asy_end = None
    for i, line in enumerate(lines):
        if "```asy" in line:
            asy_start = i + 1
        elif asy_start and "```" in line and i > asy_start:
            asy_end = i
            break

    if asy_start and asy_end:
        asy_code = '\n'.join(lines[asy_start:asy_end])
        visualizer.save_diagram(args.problem_id, asy_code)

    # Find worksheet content
    worksheet_start = None
    for i, line in enumerate(lines):
        if "### 2. СОДРЖИНА ЗА РАБОТНИОТ ЛИСТ" in line:
            worksheet_start = i
            break

    if worksheet_start:
        worksheet_content = '\n'.join(lines[worksheet_start:])
        visualizer.save_worksheet(args.problem_id, worksheet_content)

    print("✓ Processing complete!")
    print(result)

if __name__ == "__main__":
    main()