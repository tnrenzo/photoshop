import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

class EditedImage:
    def __init__(self, image_path: str = None):
        self.original_image = None
        self.original_image_array = None
        self.image_copy = None


        if image_path is not None:
            self.open_image(image_path) # fills original_image and original_image_array as well as image_copy

        # resets
        self.reset_index = 0
        self.reset_history: dict[int, np.ndarray] = {}

    def open_image(self, file_path):
        if file_path is None:
            return
        to_open = Image.open(file_path)
        self.original_image = to_open.copy()
        self.original_image_array = np.array(to_open).copy()
        self.image_copy = self.original_image_array.copy()

    def save_image(self, file_path: str):
        to_save = Image.fromarray(self.image_copy.copy())
        to_save.save(fp=file_path)

    def save_edit_state(self):
        self.reset_index += 1
        self.reset_history[self.reset_index] = self.image_copy.copy()

    def undo_edit(self):
        if self.reset_index > 0:
            self.reset_index -= 1
            self.image_copy = self.reset_history[self.reset_index].copy()

    def redo_edit(self):
       if self.reset_index < max(self.reset_history.keys()):
            self.reset_index += 1
            self.image_copy = self.reset_history[self.reset_index].copy()

    def return_final(self) -> np.ndarray:
        return self.image_copy

    def return_final_as_pil_type(self) -> Image.Image:
        return Image.fromarray(self.image_copy)

    def grayscale(self) -> None:
        image = self.image_copy
        # average each channel using weighted averages
        gray = (image[:, :, 0] * 0.299 +
                image[:, :, 1] * 0.587 +
                image[:, :, 2] * 0.114)
        # clamp the result to 0-255 and round floats
        self.image_copy = np.clip(gray, 0, 255).astype(np.uint8)
        self.save_edit_state()

    def invert(self) -> None:
        inverted = 255 - self.image_copy
        self.image_copy = inverted
        self.save_edit_state()

    def gaussian_blur(self, size: int = 15, sigma: float | int = 1.0):
        # build and normalize the 1D Gaussian kernel
        ax = np.linspace(-(size // 2), size // 2, size) # normalize: create axis (neighbours) in groups of 5. for example [-2, -1, 0, 1, 2] for size = 5
        gauss = np.exp(-0.5 * np.square(ax) / np.square(sigma)) # gaussian formula at each point of axis
        gauss /= np.sum(gauss) # normalize axis values so they add up to 1. without this the brightness would be different

        # small helper function called in np.apply_long_axis below
        # apply 1D kernel along each axis
        # 'same' mode keeps the output the same size as the input
        def convolve1d(arr):
            return np.convolve(arr, gauss, mode='same')

        # apply horizontally (axis=1), then vertically (axis=0). one channel at a time
        blurred = np.apply_along_axis(convolve1d, axis=1, arr=self.image_copy.astype(np.float64))
        blurred = np.apply_along_axis(convolve1d, axis=0, arr=blurred)

        self.image_copy = np.clip(blurred, 0, 255).astype(self.image_copy.dtype)
        self.save_edit_state()

    """
    Numpy array: array[:, :, x]
     - channel 0 ... red
     - channel 1 ... green
     - channel 2 ... blue
    """
    def set_color_channel(self, channel: str, rgb_value: int):
        # checking for rgb_value is done in each function
        if channel.lower() == "red":
            self.set_red(rgb_value)
        elif channel.lower() == "green":
            self.set_green(rgb_value)
        elif channel.lower() == "blue":
            self.set_blue(rgb_value)
        else:
            print("""
            Invalid color channel:
            - channel 0 ... red
            - channel 1 ... green
            - channel 2 ... blue
            """)

    def set_red(self, rgb_value: int):
        if rgb_value < 0 or rgb_value > 255:
            print("Invalid RGB Value")
        else:
            self.image_copy[:, : , 0] = rgb_value

    def set_green(self, rgb_value: int):
        if rgb_value < 0 or rgb_value > 255:
            print("Invalid RGB Value")
        else:
            self.image_copy[:, :, 1] = rgb_value

    def set_blue(self, rgb_value: int):
        if rgb_value < 0 or rgb_value > 255:
            print("Invalid RGB Value")
        else:
            self.image_copy[:, :, 2] = rgb_value

def main() -> None:
    image = EditedImage("./images/apple.png")

    image.set_color_channel(channel="red", rgb_value=50)
    image.gaussian_blur(size=105, sigma=60)
    image.set_color_channel(channel="green", rgb_value=25)
    image.invert()
    image.grayscale()

    plt.imshow(image.return_final(), cmap='gray') # cmap is needed for proper grayscale
    plt.show()

if __name__ == '__main__':
    main()
