from PIL import Image

# Function to create a single-color image
def create_pixel_art(color, filename):
    img = Image.new('RGB', (100, 100), color)  # Create a 100x100 pixel image
    img.save(filename)

# Colors to use for your pixel art
colors = [
    (255, 0, 0),   # Red
    (0, 255, 0),   # Green
    (0, 0, 255),   # Blue
    (255, 255, 0), # Yellow
    (255, 0, 255), # Magenta
    (0, 255, 255)  # Cyan
]

# Generate and save images
for i, color in enumerate(colors):
    filename = f"pixel_art_{i + 1}.png"
    create_pixel_art(color, filename)
    print(f"Saved: {filename}")
