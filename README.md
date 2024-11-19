


# PDF Cropper and Metadata Cleaner

This Python script processes a specific PDF file by cropping odd pages after the fourth page and removing metadata for compliance. It is designed to search for a target PDF within a specified folder, process it, and save the cropped version with a new filename.

---

## Features
- **PDF Search**: Locates a specific PDF file in a given folder.
- **Page Cropping**: Crops odd-numbered pages after the fourth page by a percentage of the page width.
- **Metadata Removal**: Clears all metadata from the processed PDF for compliance.

---

## Requirements
- Python 3.x
- PyPDF2 (`pip install pypdf2`)

---

## How to Use
1. Clone or download this repository.
2. Modify the `folder_path` and `target_filename` variables to specify the folder path and filename of the PDF you want to process.
3. Run the script:
   ```bash
   python script_name.py
