import subprocess

def overlay_images(blurred_image_path, bg_removed_image_path):
    final_image_path = "final_image.png"
    subprocess.run([
        "convert", blurred_image_path, bg_removed_image_path,
        "-gravity", "center", "-composite", final_image_path
    ])
    return final_image_path
