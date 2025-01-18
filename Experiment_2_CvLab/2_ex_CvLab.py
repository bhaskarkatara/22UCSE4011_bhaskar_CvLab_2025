import numpy as np
import matplotlib.pyplot as plt

def load_image(file_path):
    # Simulating manual image reading using matplotlib
    img = plt.imread(file_path)
    if img.dtype != np.uint8:  # Convert to 0-255 scale if necessary
        img = (img * 255).astype(np.uint8)
    return img

def scale_image(image, scale_factor):
    height, width, channels = image.shape
    new_height, new_width = int(height * scale_factor), int(width * scale_factor)
    scaled_image = np.zeros((new_height, new_width, channels), dtype=np.uint8)

    for i in range(new_height):
        for j in range(new_width):
            # Map new pixel to the closest original pixel
            orig_i = int(i / scale_factor)
            orig_j = int(j / scale_factor)
            scaled_image[i, j] = image[orig_i, orig_j]

    return scaled_image

def rotate_image(image, angle):
    angle_rad = np.deg2rad(angle)
    cos_theta = np.cos(angle_rad)
    sin_theta = np.sin(angle_rad)

    height, width, channels = image.shape
    center_x, center_y = width // 2, height // 2

    rotated_image = np.zeros_like(image)

    for i in range(height):
        for j in range(width):
            # Translate point to origin
            translated_x = j - center_x
            translated_y = i - center_y

            # Rotate point
            new_x = int(translated_x * cos_theta - translated_y * sin_theta + center_x)
            new_y = int(translated_x * sin_theta + translated_y * cos_theta + center_y)

            # Assign pixel if within bounds
            if 0 <= new_x < width and 0 <= new_y < height:
                rotated_image[i, j] = image[new_y, new_x]

    return rotated_image

def flip_image(image, mode="horizontal"):
    height, width, channels = image.shape
    flipped_image = np.zeros_like(image)

    if mode == "horizontal":
        for i in range(height):
            for j in range(width):
                flipped_image[i, j] = image[i, width - j - 1]
    elif mode == "vertical":
        for i in range(height):
            for j in range(width):
                flipped_image[i, j] = image[height - i - 1, j]

    return flipped_image

def save_image(image, file_name):
    plt.imsave(f"{file_name}.jpg", image)
   
def main():
    image = load_image("Experiment_2_CvLab/img.jpeg")
    plt.imshow(image)
    plt.title("Original Image")
    plt.show()
    save_image(image, "output_original")

    # Perform scaling
    scale_factor = 0.5  # Reduce size by half
    scaled_image = scale_image(image, scale_factor)
    plt.imshow(scaled_image)
    plt.title("Scaled Image (50%)")
    plt.show()
    save_image(scaled_image, "output_scaled")

    # Perform rotation
    angle = 45  # Rotate by 45 degrees
    rotated_image = rotate_image(image, angle)
    plt.imshow(rotated_image)
    plt.title("Rotated Image (45 Degrees)")
    plt.show()
    save_image(rotated_image, "output_rotated")

    # Perform flipping
    flipped_image_h = flip_image(image, mode="horizontal")
    plt.imshow(flipped_image_h)
    plt.title("Flipped Image (Horizontal)")
    plt.show()
    save_image(flipped_image_h, "output_flipped_horizontal")

    flipped_image_v = flip_image(image, mode="vertical")
    plt.imshow(flipped_image_v)
    plt.title("Flipped Image (Vertical)")
    plt.show()
    save_image(flipped_image_v, "output_flipped_vertical")

if __name__ == "__main__":
    main()
