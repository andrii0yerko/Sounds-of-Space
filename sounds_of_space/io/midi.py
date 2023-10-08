from mido import Message, MidiFile, MidiTrack


def create_midi_file(
    notes, volumes, times, durations, ticks_per_beat=960, filename="output.mid"
):
    midi_file = MidiFile(ticks_per_beat=ticks_per_beat)

    track = MidiTrack()
    midi_file.tracks.append(track)

    for note, volume, time, duration in zip(notes, volumes, times, durations):
        absolute_time = int(time * ticks_per_beat)
        duration_ticks = int(duration * ticks_per_beat)
        track.append(Message("note_on", note=note, velocity=volume, time=absolute_time))
        track.append(
            Message("note_off", note=note, velocity=volume, time=duration_ticks)
        )

    midi_file.save(filename)
