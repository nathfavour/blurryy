import os
import subprocess
from .combine import overlay_images

def process_image(image_path, output_path, temp_save, blur_value, config):
    # Remove the background using rembg CLI
    temp_bg_removed_path = "temp_bg_removed.png"
    subprocess.run(["rembg", "i", image_path, temp_bg_removed_path])
    
    # Blur the original image using ImageMagick
    blur_value = blur_value or config['blur_value']
    temp_blurred_path = "temp_blurred.png"
    subprocess.run(["convert", image_path, "-blur", f"0x{blur_value}", temp_blurred_path])
    
    # Overlay the images
    final_image_path = overlay_images(temp_blurred_path, temp_bg_removed_path)
    
    # Save the final image
    if not output_path:
        output_path = os.path.splitext(image_path)[0] + "_blur.png"
    os.rename(final_image_path, output_path)
    
    # Clean up temporary files if not saving them
    if not temp_save and not config['save_temp']:
        os.remove(temp_bg_removed_path)
        os.remove(temp_blurred_path)
