# CODEALPHA
# Task#4: Task Automation with Python Scripts
# Objective: Identify a repetitive task in your workflow and create Python scripts to automate it. This could include tasks like file organization, data cleaning, or system maintenance.

import os
import shutil

def organize_files(folder_path):
    """
    Organizes files in the specified folder by their types.
    """
    # Define categories and their corresponding file extensions
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov"],
        "Audio": [".mp3", ".wav", ".aac"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Others": []  # For files that don't match the above categories
    }

    # Ensure the folder exists
    if not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return

    # Create directories for each category
    for category in categories:
        category_path = os.path.join(folder_path, category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)

    # Move files to their respective category folders
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Check the file extension and move to the appropriate folder
        _, file_extension = os.path.splitext(file_name)
        moved = False
        for category, extensions in categories.items():
            if file_extension.lower() in extensions:
                shutil.move(file_path, os.path.join(folder_path, category, file_name))
                moved = True
                break

        # If no matching category, move to "Others"
        if not moved:
            shutil.move(file_path, os.path.join(folder_path, "Others", file_name))

    print("Files organized successfully!")

# Replace this with the path of the folder you want to organize
folder_to_organize = input("Enter the folder path to organize: ").strip()
organize_files(folder_to_organize)
