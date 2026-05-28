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

def gaussian_blur(image: np.ndarray, size: int = 5, sigma: float | int = 1.0) -> np.ndarray:
    # build and normalize the 1D Gaussian kernel
    ax = np.linspace(-(size // 2), size // 2, size) # create axis (neighbours) in groups of 5. for example [-2, -1, 0, 1, 2] for size = 5
    gauss = np.exp(-0.5 * np.square(ax) / np.square(sigma)) # gaussian formula at each point of axis
    gauss /= np.sum(gauss) # normalize axis values so they add up to 1. without this the brightness would be different

    # apply 1D kernel along each axis
    # 'same' mode keeps the output the same size as the input
    def convolve1d(arr):
        return np.convolve(arr, gauss, mode='same')

    # apply horizontally (axis=1), then vertically (axis=0). one channel at a time
    blurred = np.apply_along_axis(convolve1d, axis=1, arr=image.astype(np.float64))
    blurred = np.apply_along_axis(convolve1d, axis=0, arr=blurred)

    return np.clip(blurred, 0, 255).astype(image.dtype)

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
    image_path: str = "images/apple.png"
    original: np.ndarray = load_image(image_path)

    edit = original.copy()
    edit = gaussian_blur(edit, size=50, sigma=15)

    plt.imshow(edit, cmap='gray') # cmap is needed for proper grayscale
    plt.show()

if __name__ == '__main__':
    main()
