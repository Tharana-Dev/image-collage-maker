from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

def make_collage(folder, rows, cols, target_width, target_height, captions=None):
    """
    Create a collage from images in `folder`.

    Parameters:
        folder (str): Path to folder containing images (.jpg, .png).
        rows (int): Number of rows in the grid.
        cols (int): Number of columns in the grid.
        target_width (int): Width (in pixels) each image will be resized to.
        target_height (int): Height (in pixels) each image will be resized to.
        captions (list of str, optional): List of captions for each image.
            If None, no captions are added. If provided, length must match number of images used.
    """
    # -------------------- Font setup --------------------
    try:
        font = ImageFont.truetype("arial.ttf", 25)
    except:
        print("Default font used (no arial.ttf found).")
        font = ImageFont.load_default()

    # -------------------- Get images --------------------
    folder = Path(folder)
    image_paths = list(folder.glob("*.jpg")) + list(folder.glob("*.png"))
    if not image_paths:
        print("❌ No .jpg or .png images found in that folder.")
        return

    print(f"✅ Found {len(image_paths)} images.")

    num_cells = rows * cols
    total_images = len(image_paths)

    # Decide how many images to use
    if total_images < num_cells:
        print(f"⚠️ Warning: only {total_images} images available, but grid needs {num_cells}.")
        print(f"Using all images and leaving {num_cells - total_images} empty cells.")
        use_images = image_paths
    else:
        use_images = image_paths[:num_cells]
        print(f"✅ Using first {num_cells} images (grid full).")

    # -------------------- Captions --------------------
    if captions is None:
        captions = [""] * len(use_images)
    else:
        # Ensure captions list length matches images used
        if len(captions) < len(use_images):
            captions += [""] * (len(use_images) - len(captions))
        elif len(captions) > len(use_images):
            captions = captions[:len(use_images)]

    # -------------------- Resize images --------------------
    resized_images = []
    for path in use_images:
        img = Image.open(path)
        resized = img.resize((target_width, target_height)).convert("RGB")
        resized_images.append(resized)

    width, height = target_width, target_height

    # Spacing and label height
    horizontal_spacing = 30
    vertical_spacing = 10
    label_height = 30

    cell_height = height + label_height
    canvas_width = cols * width + (cols - 1) * horizontal_spacing
    canvas_height = rows * cell_height + (rows - 1) * vertical_spacing

    canvas = Image.new("RGB", (canvas_width, canvas_height), (200, 200, 20))
    draw = ImageDraw.Draw(canvas)

    for row in range(rows):
        for col in range(cols):
            idx = row * cols + col
            if idx >= len(resized_images):
                break

            img = resized_images[idx]
            x = col * (width + horizontal_spacing)
            y = row * (height + label_height + vertical_spacing)
            canvas.paste(img, (x, y))

            caption = captions[idx]
            if caption:
                bbox = font.getbbox(caption)
                text_width = bbox[2] - bbox[0]
                centered_x = x + (width - text_width) // 2
                y_label = y + height + 2
                draw.text((centered_x, y_label), caption, fill="black", font=font)

    output_filename = "collage.jpg"
    canvas.save(output_filename)
    print(f"\n✅ Done! Collage saved as {output_filename}")
