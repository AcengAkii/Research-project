import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image, ImageDraw  # Added missing import
import io

# Function to generate an image (for demonstration purposes)
def generate_image(value):
    # Create an image with some text
    img = Image.new('RGB', (100, 100), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    d.text((10, 40), str(value), fill=(0, 0, 0))
    return img

# Generate images for the table
image_data = [generate_image(i) for i in range(1, 10)]  # Generate images for values 1-9

# Create a DataFrame to hold the image data
df = pd.DataFrame({
    'Value': range(1, 10),
    'Image': image_data
})

# Plotting the images along with the values
fig, axs = plt.subplots(3, 3, figsize=(8, 8))  # Create a 3x3 grid for images
axs = axs.ravel()  # Flatten the 2D array of axes to iterate over it

for i, ax in enumerate(axs):
    ax.imshow(df['Image'][i])  # Display the image
    ax.set_title(f"Value: {df['Value'][i]}")
    ax.axis('off')  # Hide axes for cleaner display

plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()
