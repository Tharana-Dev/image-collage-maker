# 🖼️ Collage Maker

Create a grid collage from images in a folder.  
Two versions: **command‑line (CLI)** with optional captions, and **graphical (GUI)** for quick generation.

## ✨ Features

- Select any folder with `.jpg` or `.png` images.
- Choose grid size (rows × columns) and target image dimensions.
- **CLI version** – interactive prompts; you can add a caption for each image.
- **GUI version** – simple Tkinter window to select folder and parameters (no captions).
- Saves collage as `collage.jpg` in the current folder.

## 🚀 How to Run

### Prerequisites
```bash
pip install Pillow
```

### Command‑line interface
1. Run `python CLI.py`
2. Follow the prompts:
   - Enter the folder path containing images.
   - Enter number of rows and columns.
   - Enter target image width and height (in pixels).
   - Optionally, enter a caption for each image (press Enter to skip).
3. The collage will be saved as `collage.jpg`.

### Graphical interface
1. Run `python GUI.py`
2. A window appears:
   - Click **Browse** to choose an image folder.
   - Enter rows, columns, target width and height.
   - Click **Generate Collage**.
3. The collage is saved as `collage.jpg` (no captions).

## 📁 File Structure

```
collage-maker/
├── core.py       # Shared collage logic
├── CLI.py        # Command‑line interface
├── GUI.py        # Tkinter graphical interface
└── README.md     # This file
```

## 🛠️ How It Works

- The script scans the chosen folder for `.jpg` and `.png` files.
- It resizes each image to the target size.
- It arranges them in a grid with adjustable spacing (you can edit `core.py` to change spacing).
- If captions are provided (CLI only), they are drawn below each image.
- The final image is saved as `collage.jpg`.

## 🎨 Customisation

You can modify the constants inside `core.py` to change the layout:

- `horizontal_spacing` – space between columns (default 30)
- `vertical_spacing` – space between rows (default 10)
- `label_height` – height reserved for captions (default 30)
- Background colour – change the tuple `(200,200,20)` in the `Image.new` call.

## 📧 Contact

For questions or suggestions:  
[dev.tharana@gmail.com](mailto:dev.tharana@gmail.com)

## 🙏 Acknowledgements

Built as a portfolio project to demonstrate image processing (Pillow) and GUI programming (Tkinter).
