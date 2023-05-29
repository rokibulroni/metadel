import sys
from PIL import Image, ImageDraw

def remove_metadata(image_path):
    try:
        image = Image.open(image_path)
        image_without_metadata = Image.new(image.mode, image.size)
        image_without_metadata.paste(image)
        image_without_metadata.save(image_path)
        print("All metadata removed successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python metadata_remover.py <image_path>")
    else:
        image_path = sys.argv[1]
        remove_metadata(image_path)
