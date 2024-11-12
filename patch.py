import os
import shutil
import sys

# Define paths
venv_path = os.getenv("VIRTUAL_ENV")

if not venv_path:
    print("Error: Virtual environment is not activated.")
    sys.exit(1)

# Paths to the files
original_file_path = os.path.join(venv_path, "lib/python3.11/site-packages/llama_index/core/indices/property_graph/base.py")
backup_file_path = os.path.join(venv_path, "lib/python3.11/site-packages/llama_index/core/indices/property_graph/base_backup.py")
patched_file_path = "patch_files/property_graph_base.py"

# Check if the original file exists
if not os.path.exists(original_file_path):
    print(f"Error: Original file not found at {original_file_path}")
    sys.exit(1)

# Check if the patched file exists
if not os.path.exists(patched_file_path):
    print(f"Error: Patched file not found at {patched_file_path}")
    sys.exit(1)

try:
    # Backup the original file
    print("Backing up the original file...")
    shutil.copy2(original_file_path, backup_file_path)
    print(f"Backup created at {backup_file_path}")

    # Replace the original file with the patched file
    print("Applying the patch...")
    shutil.copy2(patched_file_path, original_file_path)
    print("Patch applied successfully!")

except Exception as e:
    print(f"Error during patching: {e}")
    sys.exit(1)
