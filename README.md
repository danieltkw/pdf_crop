

# PDF Cropper and Metadata Cleaner

This Python script processes a PDF file by cropping pages based on user input and removing metadata for compliance. It allows the user to dynamically set cropping preferences, including the starting page, whether to crop odd/even pages and the cropping percentage.

---

## Features

- **Dynamic Folder and File Selection**:
  - Specify a folder and PDF filename or let the script automatically detect a `.pdf` file in the script's folder.
  - Handles missing files, invalid inputs, and non-existent folders.

- **Cropping Options**:
  - Start cropping from a specific page or the first page by default.
  - Choose to crop odd pages, even pages, or both.
  - Set the cropping percentage (e.g., 28%).

- **Metadata Removal**:
  - Strips metadata from the PDF for compliance.

---

## Requirements

- Python 3.x
- PyPDF2
- 
---

## How to Use

1. Clone or download this repository.
2. Install the required library:
   ```bash
   pip install pypdf2
