


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

def find_specific_pdf(folder_path, target_filename):
    """Find a specific PDF file in the given folder."""
    target_path = os.path.join(folder_path, target_filename)
    if os.path.exists(target_path):
        return target_path
    return None

def crop_pdf(input_pdf, output_pdf, crop_percentage):
    """Crop odd pages after page 4 based on a percentage of the page width and remove metadata."""
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for i, page in enumerate(reader.pages):
        # Check if page is odd and after page 4
        if i > 3 and (i + 1) % 2 != 0:
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
folder_path = r" C:\Users\ "
target_filename = "pdf.pdf"
input_pdf = find_specific_pdf(folder_path, target_filename)

if input_pdf:
    print(f"Found PDF file: {input_pdf}")
    output_pdf = os.path.join(folder_path, f"cropped_{target_filename}")
    crop_pdf(input_pdf, output_pdf, crop_percentage=28)
    print(f"Processed and saved as {output_pdf}")
else:
    print(f"No PDF file found with the name {target_filename} in {folder_path}.")
# ------------------------------------------------------------
