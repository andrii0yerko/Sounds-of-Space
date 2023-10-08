import numpy as np
import pandas as pd

from sounds_of_space.array_utils import windowed
from sounds_of_space.io import create_midi_file, read_img
from sounds_of_space.midi_utils import VEL_MAX, VEL_MIN, init_notes, map_value

if __name__ == "__main__":
    fname = "data/t1143_mrrde_10n263_0256_3"

    note_names, note_midis = init_notes()

    data = read_img(fname).asarray()

    x = max(data.shape[:2]) // 100
    data2 = windowed(data, (data.shape[0], x, data.shape[2])).mean(axis=(2, 3, 4))

    # Reshape the data into a 2D array
    data_2d = data2.reshape(-1, data.shape[2])

    idx = np.array(list(np.ndindex(data2.shape[:2])))
    xs = idx[:, 0]
    ys = idx[:, 1]

    df = pd.DataFrame(data_2d)
    df.reset_index(inplace=True)
    df["x"] = xs
    df["y"] = ys
    df["mean"] = data_2d.mean(axis=1)
    df["std"] = data_2d.std(axis=1)

    time_label = "index"
    note_label = "mean"
    velocity_label = "std"
    duration_label = "mean"

    times = map_value(
        df[time_label], df[time_label].min(), df[time_label].max(), 0, 1
    ).to_list()
    notes = (
        map_value(
            df[note_label],
            df[note_label].min(),
            df[note_label].max(),
            0,
            len(note_midis) - 1,
        )
        .astype("int")
        .apply(lambda x: note_midis[x])
        .to_list()
    )
    velocities = (
        map_value(
            df[velocity_label],
            df[velocity_label].min(),
            df[velocity_label].max(),
            VEL_MIN,
            VEL_MAX,
        )
        .round()
        .astype("int")
        .to_list()
    )
    durations = (
        map_value(
            df[duration_label], df[duration_label].min(), df[duration_label].max(), 2, 1
        )
        .round()
        .astype("int")
        .to_list()
    )

    create_midi_file(
        notes, velocities, times, durations, ticks_per_beat=960, filename="output.mid"
    )
