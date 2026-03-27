from core import make_collage
from pathlib import Path

def main():
    # Ask for folder
    while True:
        folder = input("Enter the path to your image folder: ").strip()
        folder_path = Path(folder)
        if not folder_path.exists():
            print("❌ Folder does not exist. Try again.")
        elif not folder_path.is_dir():
            print("❌ That's not a folder. Try again.")
        else:
            break

    # Ask for grid dimensions
    while True:
        try:
            rows = int(input("How many rows? "))
            cols = int(input("How many columns? "))
            if rows > 0 and cols > 0:
                break
            else:
                print("Please enter positive numbers.")
        except ValueError:
            print("Numbers only!")

    # Ask for target image size
    while True:
        try:
            target_width = int(input("Enter target image width in pixels: "))
            target_height = int(input("Enter target image height in pixels: "))
            if target_width > 0 and target_height > 0:
                break
            else:
                print("Width and height must be positive.")
        except ValueError:
            print("Numbers only!")

    # Collect captions (optional)
    # First, we need to know how many images will be used (min(total_images, rows*cols))
    folder_path = Path(folder)
    image_paths = list(folder_path.glob("*.jpg")) + list(folder_path.glob("*.png"))
    total_images = len(image_paths)
    num_cells = rows * cols
    use_count = min(total_images, num_cells)

    captions = []
    if use_count > 0:
        print("\n--- Enter captions for each image (press Enter to skip) ---")
        for i in range(use_count):
            caption = input(f"Caption for image {i+1}: ").strip()
            captions.append(caption)

    # Call the core function
    make_collage(folder, rows, cols, target_width, target_height, captions)

if __name__ == "__main__":
    main()
