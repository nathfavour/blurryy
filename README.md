
# 📸 Blurryy

Welcome to **Blurryy**! 🎉 This is a powerful CLI tool that intelligently blurs the background of your images, giving them a professional portrait mode effect. Perfect for enhancing your photos with just a few simple commands! 🚀

## Features ✨

- **Background Removal**: Automatically removes the background from your images using `rembg` CLI.
- **Customizable Blur**: Apply a customizable blur effect to the background using ImageMagick.
- **Seamless Overlay**: Combines the blurred background with the original foreground for a stunning portrait effect.
- **Configurable**: Easily configure settings via a JSON file or CLI arguments.

## Installation 🛠️

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/blurryy.git
   ```

2. Navigate to the project directory:
   ```sh
   cd blurryy
   ```

3. Install the package in editable mode:
   ```sh
   pip install -e .
   ```

4. Ensure you have `rembg` and `ImageMagick` installed:
   ```sh
   pip install rembg
   sudo apt-get install imagemagick
   ```

## Usage 🚀

### Basic Usage

To blur the background of an image, simply run:
```sh
blurryy path/to/your/image.jpg
```

### Advanced Options

- **Specify Output Path**: Save the final image to a specific location.
  ```sh
  blurryy path/to/your/image.jpg --output-path path/to/save/final_image.png
  ```

- **Temporary Save**: Save intermediate images temporarily.
  ```sh
  blurryy path/to/your/image.jpg --temp-save
  ```

- **Custom Blur Value**: Adjust the blur intensity (0-100).
  ```sh
  blurryy path/to/your/image.jpg --blur-value 20
  ```

## Configuration ⚙️

Blurryy uses a configuration file located at `~/.blurryyconfig.json`. This file is automatically created and updated with default values if it doesn't exist. You can customize the settings by editing this file.

### Default Configuration
```json
{
    "save_temp": false,
    "blur_value": 10
}
```

## Contributing 🤝

We welcome contributions! Feel free to open issues or submit pull requests. Let's make Blurryy even better together! 💪

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements 🙏

- [rembg](https://github.com/danielgatis/rembg) for background removal.
- [ImageMagick](https://imagemagick.org/) for image processing.

---

Made with ❤️ by [Your Name](https://github.com/yourusername)
