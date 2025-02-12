import click
import json
import os
from .config import load_config, DEFAULT_CONFIG
from .processing import process_image

def ensure_config():
    config_path = os.path.expanduser("~/.blurryyconfig.json")
    if not os.path.exists(config_path):
        with open(config_path, 'w') as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)
    else:
        with open(config_path, 'r+') as f:
            user_config = json.load(f)
            updated_config = {**DEFAULT_CONFIG, **user_config}
            f.seek(0)
            json.dump(updated_config, f, indent=4)
            f.truncate()

@click.command()
@click.argument('image_path', required=False)
@click.option('--output-path', default=None, help='Path to save the final image.')
@click.option('--temp-save', is_flag=True, help='Save intermediate images temporarily.')
@click.option('--blur-value', default=None, type=int, help='Blur intensity value (0-100).')
def cli(image_path, output_path, temp_save, blur_value):
    ensure_config()
    if image_path:
        config = load_config()
        if blur_value is not None:
            blur_value = max(0, min(blur_value, 100))  # Ensure blur value is within range 0-100
        process_image(image_path, output_path, temp_save, blur_value, config)
    else:
        click.echo("Error: Missing argument 'IMAGE_PATH'.", err=True)
        click.echo(cli.get_help(click.Context(cli)))

if __name__ == "__main__":
    cli()
