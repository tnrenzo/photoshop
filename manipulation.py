import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

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

"""
Numpy array: array[:, :, x]
 - channel 0 ... red
 - channel 1 ... green
 - channel 2 ... blue
"""
def set_green(image: np.ndarray, rgb_value: int) -> np.ndarray:
    if rgb_value < 0 or rgb_value > 255:
        print("Invalid RGB Value")
        return image

    image[:, :, 1] = rgb_value
    return image

def set_red(image: np.ndarray, rgb_value: int) -> np.ndarray:
    if rgb_value < 0 or rgb_value > 255:
        print("Invalid RGB Value")
        return image

    image[:, : , 0] = rgb_value
    return image

def set_blue(image: np.ndarray, rgb_value: int) -> np.ndarray:
    if rgb_value < 0 or rgb_value > 255:
        print("Invalid RGB Value")
        return image

    image[:, :, 2] = rgb_value
    return image

def main() -> None:
    image_path: str = "images/example02.jpg"
    original: np.ndarray = load_image(image_path)

    edit = original.copy()
    edit = grayscale(edit)

    plt.imshow(edit, cmap='gray') # cmap is needed for proper grayscale
    plt.show()

if __name__ == '__main__':
    main()
