#!/usr/bin/env python3
"""
Batch compilation script for Asymptote diagrams.

This script compiles all .asy files in the diagrams/ directory to PDF format.
"""

import os
import subprocess
import glob
from pathlib import Path

def compile_diagram(asy_file, output_dir="diagrams"):
    """Compile a single Asymptote file to PDF."""
    try:
        # Run asy command
        result = subprocess.run(
            ["asy", "-f", "pdf", asy_file],
            capture_output=True,
            text=True,
            cwd=output_dir
        )

        if result.returncode == 0:
            print(f"✓ Compiled {asy_file}")
            return True
        else:
            print(f"✗ Failed {asy_file}: {result.stderr}")
            return False

    except FileNotFoundError:
        print("Error: Asymptote (asy) not found. Please install Asymptote.")
        return False
    except Exception as e:
        print(f"Error compiling {asy_file}: {e}")
        return False

def main():
    """Compile all .asy files in the diagrams directory."""
    diagrams_dir = Path(__file__).parent.parent / "diagrams"

    if not diagrams_dir.exists():
        print(f"Diagrams directory not found: {diagrams_dir}")
        return

    asy_files = list(diagrams_dir.glob("*.asy"))

    if not asy_files:
        print("No .asy files found in diagrams directory")
        return

    print(f"Found {len(asy_files)} Asymptote files")

    success_count = 0
    for asy_file in asy_files:
        if compile_diagram(asy_file.name, str(diagrams_dir)):
            success_count += 1

    print(f"\nCompilation complete: {success_count}/{len(asy_files)} successful")

if __name__ == "__main__":
    main()