from midiutil import MIDIFile

def make_midi_file(notes, octave, output_path=None):

    midi = MIDIFile(1)

    track = 0
    time = 0
    channel = 0
    volume = 100

    midi.addTrackName(track, time, "Track")

    tempo = input("Zadejte tempo prosím: ")
    midi.addTempo(track, time, int(tempo))

    for note in notes:
        if isinstance(note, list):
            duration = 0
            for i in note:
                duration = durations.get(i[3:])

                pitch = note_defs.get(i[0] + str(int(i[1]) + 3 + octave))

                midi.addNote(track, channel, pitch, time, duration, volume)
            time += duration

        else:
            duration = durations.get(note[3:])

            pitch = note_defs.get(note[0] + str(int(note[1]) + 3 + octave))

            midi.addNote(track, channel, pitch, time, duration, volume)
            time += duration

    if output_path:
        # midi.addNote(track, channel, pitch, time, 4, 0)
        # And write it to disk.
        binfile = open(f"{output_path}/output.mid", 'wb')
        midi.writeFile(binfile)
        binfile.close()


note_defs = {
    "c1": 24,
    "d1": 26,
    "e1": 28,
    "f1": 29,
    "g1": 31,
    "a1": 33,
    "b1": 35,
    "c2": 36,
    "d2": 38,
    "e2": 40,
    "f2": 41,
    "g2": 43,
    "a2": 45,
    "b2": 47,
    "c3": 48,
    "d3": 50,
    "e3": 52,
    "f3": 53,
    "g3": 55,
    "a3": 57,
    "b3": 59,
    "c4": 60,
    "d4": 62,
    "e4": 64,
    "f4": 65,
    "g4": 67,
    "a4": 69,
    "b4": 71,
    "c5": 72,
    "d5": 74,
    "e5": 76,
    "f5": 77,
    "g5": 79,
    "a5": 81,
    "b5": 83,
    "c6": 84,
    "d6": 86,
    "e6": 88,
    "f6": 89,
    "g6": 91,
    "a6": 93,
    "b6": 95
}

# 1/32 = 0.125
# 1/16 = 0.25
# 1/8 = 0.5
# 1/4 = 1
# 1/2 = 2
# 1/1 = 4
durations = {
    "1": 4,
    "2": 2,
    "4": 1,
    "8": 0.5,
    "16": 0.25,
    "32": 0.125
}