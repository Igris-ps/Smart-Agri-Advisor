from PIL import Image

def analyze_image(image_file):
    try:
        image = Image.open(image_file)
        # Placeholder logic for now
        # Real model can be plugged in later
        return "disease"
    except:
        return "unknown"
