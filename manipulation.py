import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

class EditedImage:
    def __init__(self, path: str):
        self.path = path

        self.original: np.ndarray = self._load_image()
        self.edited: np.ndarray = self.original

    def _load_image(self):
        if not self.path:
            print("Need a image path!")
        img = Image.open(self.path)
        return np.array(img)

    def grayscale(self):
        image = self.edited
        # average each channel using weighted averages
        gray = (image[:, :, 0] * 0.299 +
                image[:, :, 1] * 0.587 +
                image[:, :, 2] * 0.114)
        # clamp the result to 0-255 and round floats
        self.edited = np.clip(gray, 0, 255).astype(np.uint8)

    def invert(self):
        inverted = 255 - self.edited
        self.edited = inverted

    def red_channel(self, rgb_value: int):
        # clamp
        if 0 < rgb_value < 255:
            print("Invalid RGB Value! Allowed range is 0-255")

        self.edited[:, :, 0] = rgb_value

    def green_channel(self, rgb_value: int):
        if 0 < rgb_value < 255:
            print("Invalid RGB Value! Allowed range is 0-255")

        self.edited[:, :, 1] = rgb_value

    def blue_channel(self, rgb_value: int):
        if 0 < rgb_value < 255:
            print("Invalid RGB Value! Allowed range is 0-255")

        self.edited[:, :, 2] = rgb_value


def load_image(image_path) -> np.ndarray:
    img = Image.open(image_path)
    return np.array(img)

def grayscale(image: np.ndarray) -> np.ndarray:
    # average each channel using weighted averages
    gray = (image[:, :, 0] * 0.299 +
            image[:, :, 1] * 0.587 +
            image[:, :, 2] * 0.114)
    # clamp the result to 0-255 and round floats
    return np.clip(gray, 0, 255).astype(np.uint8)

def invert(image: np.ndarray) -> np.ndarray:
    inverted = 255 - image
    return inverted

def set_green_channel(image: np.ndarray, rgb_value: int) -> np.ndarray:
    if rgb_value < 0 or rgb_value > 255:
        print("Invalid RGB Value")
        return image

    image[:, :, 1] = rgb_value
    return image

def set_red_channel(image: np.ndarray, rgb_value: int) -> np.ndarray:
    if rgb_value < 0 or rgb_value > 255:
        print("Invalid RGB Value")
        return image

    image[:, :, 0] = rgb_value
    return image

def set_blue_channel(image: np.ndarray, rgb_value: int) -> np.ndarray:
    if rgb_value < 0 or rgb_value > 255:
        print("Invalid RGB Value")
        return image

    image[:, :, 2] = rgb_value
    return image

def main() -> None:
    image_path: str = "images/apple.jpg"

    image = EditedImage(image_path)

    image.red_channel(0)
    image.grayscale()
    image.invert()

    plt.imshow(image.edited, cmap='gray') # cmap is needed for proper grayscale
    plt.show()

if __name__ == '__main__':
    main()
