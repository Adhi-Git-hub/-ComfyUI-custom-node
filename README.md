# 🖼️ Before/After Comparer for ComfyUI

A custom node for comparing two images side-by-side or vertically in ComfyUI workflows.

![Node Preview]( https://github.com/Adhi-Git-hub/-ComfyUI-custom-node/blob/main/images/Screenshot%202025-05-29%20113808.png) 

## 🌟 Features
- Horizontal or vertical comparison layouts
- Adjustable padding between images
- Optional "Before/After" labels
- One-click PNG export
- Maintains aspect ratios

## 📦 Installation
1. Clone or download this repository
2. Place the `my_custom_nodes` folder in:ComfyUI/custom_nodes/
3. Restart ComfyUI

## 🛠️ Node Reference

### Inputs
| Parameter      | Type      | Description                          | Default |
|---------------|-----------|--------------------------------------|---------|
| `image1`      | IMAGE     | "Before" image                       | -       |
| `image2`      | IMAGE     | "After" image                        | -       |
| `padding`     | INT       | Space between images (px)            | 10      |
| `layout`      | COMBO     | `horizontal` or `vertical`           | horizontal |
| `show_labels` | BOOLEAN   | Display "Before/After" text          | True    |
| `save_output` | BOOLEAN   | Auto-save as PNG to output directory | False   |

### Outputs
- `combined_image` (IMAGE): The generated comparison image

## 🖥️ Usage Guide
1. Add the node via:
- Search menu (`🖼️ Before/After Comparer`)
- Image/Compare category
2. Connect two image inputs
3. Adjust settings as needed
4. Run your workflow

![Example Workflow]( https://github.com/Adhi-Git-hub/-ComfyUI-custom-node/blob/main/images/Screenshot%202025-05-29%20113801.png) 
