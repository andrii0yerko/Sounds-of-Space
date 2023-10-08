from audiolazy import str2midi

VEL_MIN, VEL_MAX = 35, 127  # minimum and maximum note velocity


def init_notes():
    note_names = [
        "C1",
        "C2",
        "G2",
        "C3",
        "E3",
        "G3",
        "A3",
        "B3",
        "D4",
        "E4",
        "G4",
        "A4",
        "B4",
        "D5",
        "E5",
        "G5",
        "A5",
        "B5",
        "D6",
        "E6",
        "F#6",
        "G6",
        "A6",
    ]
    note_midis = [str2midi(n) for n in note_names]
    return note_names, note_midis


def map_value(value, min_value, max_value, min_result, max_result):
    """maps value (or array of values) from one range to another"""
    result = min_result + (value - min_value) / (max_value - min_value) * (
        max_result - min_result
    )
    return result
