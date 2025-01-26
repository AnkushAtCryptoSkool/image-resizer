# pip install pillow
from PIL import Image
import os


def resize_image(input_path, output_path, new_size):
    try:
        # Check if the input file exists
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"The file {input_path} does not exist.")

        # Open the image file
        image = Image.open(input_path)

        # Resize the image
        resized_image = image.resize(new_size)

        # Check if the output directory exists, if not, create it
        output_dir = os.path.dirname(output_path)
        if not os.path.exists(output_dir) and output_dir != '':
            os.makedirs(output_dir)

        # Save the resized image as PNG to preserve transparency
        resized_image.save(output_path, format='PNG')

        print("Image has been resized and saved successfully!")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except IOError as e:
        print(f"IOError: The file could not be opened or saved. Details: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Define paths and new size
input_image_path = r"C:\Users\ankus\OneDrive\Pictures\Screenshots\Screenshot 2024-10-19 061106.png"  # Replace with your image path
output_image_path = r"C:\Users\ankus\OneDrive\Pictures\Screenshots\resized_image.png"  # Save as PNG to preserve transparency
new_size = (100, 400)  # Specify the new size (width, height)

# Call the function to resize the image
resize_image(input_image_path, output_image_path, new_size)
