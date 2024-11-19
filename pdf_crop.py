



# // Daniel T. K. W. - github.com/danieltkw - danielkopolo95@gmail.com
# ------------------------------------------------------------
import os
import platform
from PyPDF2 import PdfReader, PdfWriter

# Clear the screen at the start (Windows and Unix support)
if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear")

def find_any_pdf(folder_path):
    """Find any PDF file in the given folder if a specific file is not provided."""
    for file in os.listdir(folder_path):
        if file.lower().endswith(".pdf"):  # Case-insensitive check for .pdf
            return os.path.join(folder_path, file)
    return None

def crop_pdf(input_pdf, output_pdf, crop_percentage, start_page, alter_odd, alter_even):
    """Crop selected pages of a PDF based on user choices."""
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for i, page in enumerate(reader.pages):
        # Skip pages before the start page
        if i < start_page - 1:
            writer.add_page(page)
            continue

        # Determine if the page should be cropped
        page_number = i + 1
        should_crop = (
            (alter_odd and page_number % 2 != 0) or
            (alter_even and page_number % 2 == 0)
        )

        if should_crop:
            media_box = page.mediabox
            page_width = float(media_box.width)
            
            # Define new crop box dimensions
            crop_width = page_width * crop_percentage / 100
            page.mediabox.lower_left = (crop_width, media_box.lower_left[1])
            page.mediabox.lower_right = (media_box.lower_right[0], media_box.lower_right[1])
        
        # Add the (cropped or unchanged) page to the writer
        writer.add_page(page)

    # Replace metadata with an empty dictionary for compliance
    writer.add_metadata({})

    # Save the new PDF
    with open(output_pdf, "wb") as f:
        writer.write(f)

# Main execution
folder_path = input("Enter folder path (leave empty to use the script's folder): ").strip()
if not folder_path:
    folder_path = os.path.dirname(os.path.abspath(__file__))  # Use script's folder

if not os.path.exists(folder_path):
    print(f"The specified folder path does not exist: {folder_path}")
    exit()

print(f"Using folder path: {folder_path}")
print("Contents of the folder:", os.listdir(folder_path))

target_filename = input("Enter the PDF filename (leave empty to find any PDF): ").strip()
if not target_filename:
    input_pdf = find_any_pdf(folder_path)
    if not input_pdf:
        print("No PDF file found in the specified folder.")
        exit()
else:
    input_pdf = os.path.join(folder_path, target_filename)
    if not os.path.exists(input_pdf):
        print(f"No PDF file found with the name {target_filename} in {folder_path}.")
        exit()

start_page_input = input("Enter the page to start cropping (e.g., 5, leave empty to start from the first page): ").strip()
start_page = int(start_page_input) if start_page_input.isdigit() else 1

alter_odd = input("Crop odd pages? (yes/no): ").strip().lower() == "yes"
alter_even = input("Crop even pages? (yes/no): ").strip().lower() == "yes"
crop_percentage = float(input("Enter crop percentage (e.g., 28): "))

output_pdf = os.path.join(folder_path, f"cropped_{os.path.basename(input_pdf)}")
crop_pdf(input_pdf, output_pdf, crop_percentage, start_page, alter_odd, alter_even)
print(f"Processed and saved as {output_pdf}")
# ------------------------------------------------------------



