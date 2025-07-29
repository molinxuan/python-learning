# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Chinese-language Python learning curriculum designed for beginners. The repository contains structured lessons, exercises, and projects to teach Python programming from basics to practical applications.

## Repository Structure

```
python-learning/
├── basics/                    # Core lesson modules (6 lessons total)
│   ├── 01-variables-types/    # Variables and data types
│   ├── 02-control-flow/       # Control flow (if/for/while)
│   ├── 03-functions/          # Functions and parameters
│   ├── 04-data-structures/    # Lists, dictionaries, tuples, sets
│   ├── 05-file-io/           # File operations and error handling
│   └── 06-oop/               # Object-oriented programming
├── exercises/                 # Practice problems by difficulty
│   ├── beginner/             # Beginner exercises
│   ├── intermediate/         # Intermediate exercises
│   └── advanced/             # Advanced exercises
├── projects/                  # Hands-on projects by complexity
│   ├── simple/               # Simple projects (like personal_info_card.py)
│   ├── intermediate/         # Intermediate projects
│   └── advanced/             # Advanced projects
├── resources/                # Additional learning materials
├── test/                     # Test files for experimentation
├── Python学习指南.md         # Main learning guide (Chinese)
└── 学习进度跟踪.md            # Progress tracking template (Chinese)
```

## Learning Progression

The curriculum follows a structured 6-lesson progression:

1. **Lesson 1**: Variables and data types (int, float, str, bool)
2. **Lesson 2**: Control flow statements (if-else, loops)
3. **Lesson 3**: Functions and scope
4. **Lesson 4**: Data structures (lists, dicts, tuples, sets)
5. **Lesson 5**: File I/O and exception handling
6. **Lesson 6**: Object-oriented programming

Each lesson includes:
- Teaching file in `basics/XX-topic/`
- Corresponding exercises in `exercises/beginner/`
- Practical project in `projects/simple/`

## Common Development Commands

### Running Python Files
```bash
# Method 1: Direct execution
python filename.py

# Method 2: Using python3 (recommended)
python3 filename.py

# Method 3: Make executable and run
chmod +x filename.py
./filename.py
```

### Testing Code
Since this is an educational repository without formal test framework:
- Run individual lesson files to see educational content
- Run exercise files to check solutions
- Run project files to see completed examples

### Environment Check
```bash
# Verify Python installation
python --version
# or
python3 --version
```

## Content Guidelines

- All content is in Chinese (中文)
- Teaching files use extensive comments and print statements for learning
- Exercise files include TODO markers for student completion
- Project files demonstrate real-world application of concepts
- Code follows educational best practices with clear variable names and abundant comments

## File Naming Conventions

- Teaching files: descriptive names like `variables_and_types.py`
- Exercise files: `lesson[XX]_exercises.py` format
- Project files: descriptive names like `personal_info_card.py`
- All Python files include UTF-8 encoding declaration and shebang

## Working with This Repository

When making changes:
1. Maintain the educational structure and Chinese language content
2. Ensure all code includes helpful comments for learners
3. Keep examples simple and focused on the lesson objectives
4. Test code by running files to verify educational output works correctly
5. Maintain consistency with existing naming and formatting conventions

## Educational Focus

This repository prioritizes:
- Clear, beginner-friendly explanations
- Practical, relatable examples
- Progressive skill building
- Hands-on practice through exercises and projects
- Chinese language accessibility for native speakers