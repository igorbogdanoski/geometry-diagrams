# Geometry Diagrams Repository

This repository contains Asymptote-generated diagrams for the Olympiad Math Archive geometry problems.

## Purpose

Provide precise, scalable vector diagrams for mathematical education, specifically tailored for Macedonian Olympiad-level geometry problems.

## Structure

- `diagrams/` - Asymptote source files (.asy)
- `worksheets/` - Generated educational worksheets
- `scripts/` - Automation tools for diagram generation
- `docs/` - Documentation and contribution guides

## Getting Started

### Prerequisites
- Asymptote (asy) compiler
- Python 3.8+
- LaTeX distribution (for Asymptote)

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/geometry-diagrams.git
cd geometry-diagrams

# Install Python dependencies
pip install -r requirements.txt
```

### Usage
```bash
# Compile a single diagram
asy diagrams/example.asy

# Generate all diagrams
python scripts/batch_compile.py

# Create worksheet from problem
python scripts/generate_worksheet.py --problem-id 1234
```

## AI-Powered Generation

This repository uses an AI system to automatically generate Asymptote code from geometry problem descriptions. The system follows these principles:

1. **Technical Recreation**: Exact geometric construction matching the original problem
2. **Educational Adaptation**: Clear labeling and scaffolding for student learning
3. **Macedonian Localization**: Culturally appropriate naming and units

## Contributing

See [CONTRIBUTION.md](docs/CONTRIBUTION.md) for detailed guidelines.

## License

Same as the main Olympiad Math Archive - Educational use permitted.

## Integration with Main Archive

This repository complements [olympiad-math-archive](https://github.com/yourusername/olympiad-math-archive) by providing:

- High-quality vector diagrams
- Automated diagram generation
- Consistent visual styling
- Reusable geometric components