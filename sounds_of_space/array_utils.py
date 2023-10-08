import numpy as np


def windowed(original_array, window_shape):
    num_windows = original_array.shape // np.array(window_shape)

    windows = np.empty(
        tuple(num_windows) + tuple(window_shape), dtype=original_array.dtype
    )
    # Iterate through the non-overlapping windows
    for i in range(num_windows[0]):
        for j in range(num_windows[1]):
            for k in range(num_windows[2]):
                # Calculate the slice for the current window
                start_i, start_j, start_k = (
                    i * window_shape[0],
                    j * window_shape[1],
                    k * window_shape[2],
                )
                end_i, end_j, end_k = (
                    start_i + window_shape[0],
                    start_j + window_shape[1],
                    start_k + window_shape[2],
                )

                # Extract the window
                window = original_array[start_i:end_i, start_j:end_j, start_k:end_k]
                windows[i, j, k] = window

    return windows
