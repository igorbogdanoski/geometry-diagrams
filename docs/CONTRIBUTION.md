# Contribution Guide for Geometry Diagrams

## Overview

This repository maintains high-quality Asymptote diagrams for geometry problems in the Olympiad Math Archive. Contributions should focus on accuracy, educational value, and consistency.

## Getting Started

1. **Familiarize with Asymptote**: Read the [Asymptote documentation](https://asymptote.sourceforge.io/)
2. **Study Examples**: Review existing diagrams in `diagrams/`
3. **Follow Standards**: Use the established coding conventions

## Diagram Standards

### Technical Requirements
- **Output Format**: PDF (vector format for scalability)
- **Size**: 200-300 units for optimal readability
- **Colors**: Black for main elements, blue for secondary, red for emphasis
- **Labels**: LaTeX math mode for symbols, plain text for values

### Educational Standards
- **Clarity**: Diagrams should be immediately understandable
- **Accuracy**: Exact geometric constructions matching problem descriptions
- **Completeness**: Include all referenced points, lines, and angles
- **Localization**: Use Macedonian labels where appropriate

### Code Standards
```asy
// Header comment with problem reference
// settings.outformat = "pdf";
// size(200);

// Clear variable naming
pair A = (0, 0);
pair B = (4, 0);

// Consistent styling
draw(A--B, black);
label("$A$", A, SW);
```

## Workflow

### 1. Problem Analysis
- Identify the geometry problem from the main archive
- Note all geometric elements (points, lines, circles, angles)
- Determine optimal diagram layout

### 2. Asymptote Implementation
- Create `.asy` file in `diagrams/` with `problem_id.asy` naming
- Implement geometric constructions
- Add appropriate labels and annotations
- Test compilation: `asy problem_id.asy`

### 3. Quality Assurance
- Verify diagram matches problem description
- Check label positioning and readability
- Ensure no compilation errors
- Test at different scales

### 4. Documentation
- Update README if adding new functionality
- Add comments for complex constructions

## AI-Assisted Generation

This repository supports AI-generated diagrams following the system instruction:

```
Educational Content Architect & Geometry Visualizer
[Full system instruction here]
```

### Using AI Generation
1. Provide problem text and visual description
2. Review generated Asymptote code
3. Test and refine the diagram
4. Commit with reference to AI tool used

## File Organization

```
diagrams/
├── problem_1234.asy    # Individual problem diagrams
├── theorem_pythagoras.asy  # General theorem illustrations
└── constructions/      # Subfolder for complex constructions

worksheets/
├── generated/          # AI-generated worksheets
└── templates/          # Worksheet templates
```

## Testing

### Local Testing
```bash
# Compile single diagram
asy diagrams/problem_1234.asy

# Batch compile all
python scripts/batch_compile.py

# Check for errors
python scripts/validate_diagrams.py
```

### CI/CD
- GitHub Actions automatically compiles all diagrams
- Failed compilations block merges
- PDF outputs are archived as artifacts

## Common Issues

### Compilation Errors
- Check for undefined variables
- Verify pair/triple definitions
- Ensure proper bracket matching

### Geometric Accuracy
- Double-check angle measurements
- Verify parallel/perpendicular relationships
- Confirm point positions match problem

### Label Positioning
- Use relative positioning (N, S, E, W, NE, etc.)
- Avoid overlapping labels
- Test at different zoom levels

## Advanced Topics

### Parametric Diagrams
```asy
// Variable parameters for multiple problem instances
real side = 5;
pair A = (0,0);
pair B = (side, 0);
// ... rest of construction
```

### Reusable Components
```asy
// Define reusable functions
void draw_triangle(pair A, pair B, pair C) {
    draw(A--B--C--cycle);
    label("$A$", A, SW);
    label("$B$", B, SE);
    label("$C$", C, N);
}
```

## Getting Help

- **Issues**: Use GitHub Issues for bugs and feature requests
- **Discussions**: Use GitHub Discussions for questions
- **Code Review**: All PRs require review before merge

## Recognition

Contributors will be acknowledged in the main Olympiad Math Archive credits and this repository's README.