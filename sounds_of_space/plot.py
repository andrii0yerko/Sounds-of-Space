import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA


def plot_rgb_proj(data):
    # Reshape the data into a 2D array
    data_2d = data.reshape(-1, data.shape[2])

    # Perform PCA to reduce the 2D data to three principal components
    n_components = 3
    pca = PCA(n_components=n_components)
    principal_components = pca.fit_transform(data_2d)

    # Normalize the principal components to the range [0, 255]
    normalized_components = (
        (principal_components - principal_components.min())
        / (principal_components.max() - principal_components.min())
        * 255
    )

    # Create an RGB image from the three normalized principal components
    rgb_image = normalized_components.reshape(
        data.shape[0], data.shape[1], n_components
    ).astype(np.uint8)

    return plt.imshow(rgb_image, cmap="viridis")
