import os
import re
from datetime import datetime

# Define constants for modifications
REPLACEMENTS = {
    r'iliyaqdrwalqu/SiGtRiP': '66666677777/Argos',
    r'ghcr.io/iliyaqdrwalqu/argoss': 'ghcr.io/66666677777/argos',
    r'argos-universalsigtrip': 'argos-universal',
    r'argos@sigtrip.dev': 'argos@66666677777.dev'
}

# File types to search
FILE_TYPES = ('.md', '.yml', '.toml', '.dockerfile', '.py')

# Function to perform replacements in a file
def migrate_file(file_path):
    changed = False
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    for pattern, replacement in REPLACEMENTS.items():
        new_content = re.sub(pattern, replacement, content)
        if new_content != content:
            changed = True
            content = new_content

    if changed:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

    return changed

# Main migration function
def migrate_repository(root_dir):
    report = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(FILE_TYPES):
                file_path = os.path.join(dirpath, filename)
                if migrate_file(file_path):
                    report.append(file_path)

    return report

# Generate migration report
def generate_report(report):
    report_file = 'migration_report.txt'
    with open(report_file, 'w', encoding='utf-8') as file:
        file.write(f"Migration Report - {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC\n")
        file.write("=" * 50 + "\n")
        for changed_file in report:
            file.write(f"Modified: {changed_file}\n")
        file.write(f"\nTotal files modified: {len(report)}\n")

# Summary statistics
def print_summary(report):
    print(f"Total files modified: {len(report)}")

# Script execution
if __name__ == "__main__":
    root_directory = '.'  # Set the root directory to current location
    report = migrate_repository(root_directory)
    generate_report(report)
    print_summary(report)
