import numpy as np
# A dictionary that maps the labels to RGB values.
# in this case, n the dataset: A = 1, G = 2 , C = 3 , T = 4 and N = 0.
label_to_rgb = {
    0: (255, 255, 255),
    1: (255, 0, 0),
    2: (255, 255, 0),
    3: (0, 255, 0),
    4: (0, 0, 255),
}

# a function that tooks the dataframe, width, height of the image and the label and returns the image
def get_image(df, width, height, label):
    images = []
    for i in range(df.shape[0]):
        sequence = df.iloc[i].values
        image = np.zeros((height, width, 3), dtype=np.uint8)
        for j in range(height * width):
            rgb_value = label_to_rgb[sequence[j]]
            x = j % width
            y = j // width
            image[y, x] = rgb_value
        images.append(image)
    return images