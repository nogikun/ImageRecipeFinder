from PIL import Image
import sys
import os
import numpy as np

class ImageToTerminal:
    def __init__(self, filepath=None, split_num=1, pattern=' '):
        self.filepath = filepath
        self.split_num = split_num
        self.pattern = pattern
        self.img = None

    def get_terminal_size(self):
        try:
            # Return terminal size as (columns, lines)
            return os.get_terminal_size()
        except:
            return (80, 24)  # Default size

    def process_image(self):
        if self.img is None:
            raise ValueError("No image to process")
        
        try:
            img = self.img
            terminal_size = self.get_terminal_size()
            terminal_width, terminal_height = terminal_size
            terminal_height = round((terminal_height - 1) / self.split_num)

            # Resize considering the aspect ratio of terminal character cells
            aspect_ratio = 0.5  # Assuming a character cell ratio of 1:2
            img_width = terminal_width
            img_height = int(terminal_height / aspect_ratio)
            img.thumbnail((img_width, img_height), Image.LANCZOS)
            
            width, height = img.size

            ascii_mark_num = '38' if self.pattern != ' ' else '48'
            ascii_mark_string = f'm{self.pattern[0]}'

            for y in range(0, height, 2):  # Process every 2 rows
                for x in range(width):
                    rgb = img.getpixel((x, y))
                    # Convert RGB values to range 0-255
                    outline = f"\033[{ascii_mark_num};2;{rgb[0]};{rgb[1]};{rgb[2]}{ascii_mark_string}"
                    sys.stdout.write(outline)
                sys.stdout.write("\033[0m\n")

        except Exception as e:
            print(f"Error processing image: {str(e)}")

    def run(self, array=None):
        if array is not None:
            # Convert array to 8-bit image if necessary
            array = (array * 255).astype(np.uint8)  # Ensure array values are in the range 0-255
            self.img = Image.fromarray(array).convert('RGB')
        elif self.filepath:
            self.img = Image.open(self.filepath).convert('RGB')
        if self.img:
            self.process_image()
        else:
            print("No image to process")

if __name__ == "__main__":
    image = np.random.rand(640, 480, 3) * 255 # 仮の画像データ
    image_processor = ImageToTerminal()
    image_processor.run(array=image)
