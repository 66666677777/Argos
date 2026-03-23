import os
import glob
import re

# List of critical files to scan
critical_files = [
    'pyproject.toml',
    'Dockerfile',
    'README.md',
    'INSTALL.md',
    '.github/workflows/*'
]

# Patterns to replace
replacements = {
    'iliyaqdrwalqu/SiGtRiP': '66666677777/Argos',
    'argoss': 'Argos'
}

# Function to replace patterns in a file
def replace_in_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    for old, new in replacements.items():
        content = re.sub(old, new, content)

    with open(file_path, 'w') as file:
        file.write(content)

# Main batch update function
def main():
    for pattern in critical_files:
        for file_path in glob.glob(pattern):
            replace_in_file(file_path)

if __name__ == '__main__':
    main()
