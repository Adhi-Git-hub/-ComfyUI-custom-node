import os
import numpy as np  # Added missing import
from PIL import Image, ImageDraw, ImageFont
import folder_paths
import torch  # Explicit torch import

class BeforeAfterCompare:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image1": ("IMAGE",),
                "image2": ("IMAGE",),
                "padding": ("INT", {"default": 10, "min": 0, "max": 100}),
                "layout": (["horizontal", "vertical"],),
                "show_labels": ("BOOLEAN", {"default": True}),
                "save_output": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("combined_image",)
    FUNCTION = "compare"
    CATEGORY = "image/compare"

    def compare(self, image1, image2, padding, layout, show_labels, save_output):
        # Convert tensors to PIL Images
        image1 = Image.fromarray((image1.numpy().squeeze() * 255).astype('uint8'))
        image2 = Image.fromarray((image2.numpy().squeeze() * 255).astype('uint8'))
        
        if layout == "horizontal":
            height = min(image1.height, image2.height)
            image1 = image1.resize((int(image1.width * height / image1.height), height))
            image2 = image2.resize((int(image2.width * height / image2.height), height))
            
            new_width = image1.width + image2.width + padding
            new_height = height
            combined = Image.new("RGB", (new_width, new_height), (30, 30, 30))
            combined.paste(image1, (0, 0))
            combined.paste(image2, (image1.width + padding, 0))
        else:
            width = min(image1.width, image2.width)
            image1 = image1.resize((width, int(image1.height * width / image1.width)))
            image2 = image2.resize((width, int(image2.height * width / image2.width)))
            
            new_width = width
            new_height = image1.height + image2.height + padding
            combined = Image.new("RGB", (new_width, new_height), (30, 30, 30))
            combined.paste(image1, (0, 0))
            combined.paste(image2, (0, image1.height + padding))

        if show_labels:
            draw = ImageDraw.Draw(combined)
            try:
                font = ImageFont.truetype("arial.ttf", 24)
            except:
                font = ImageFont.load_default()
            
            if layout == "horizontal":
                draw.text((10, 10), "Before", fill="white", font=font)
                draw.text((image1.width + padding + 10, 10), "After", fill="white", font=font)
            else:
                draw.text((10, 10), "Before", fill="white", font=font)
                draw.text((10, image1.height + padding + 10), "After", fill="white", font=font)

        if save_output:
            output_dir = folder_paths.get_output_directory()
            os.makedirs(output_dir, exist_ok=True)
            counter = len([f for f in os.listdir(output_dir) if f.startswith("comparison_")])
            save_path = os.path.join(output_dir, f"comparison_{counter:05d}.png")
            combined.save(save_path)
            print(f"Saved comparison image to: {save_path}")

        combined_tensor = torch.from_numpy(np.array(combined).astype(np.float32) / 255.0).unsqueeze(0)
        return (combined_tensor,)
