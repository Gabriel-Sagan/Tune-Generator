import os
import random
from scamp import *
from music21 import *
from melody import chord_seq, mel_format
from seed import seed_generator


def generate_chords():
    random.seed(seed_generator())
    chord_sequence = chord_seq()
    return chord_sequence

s = Session(tempo=120)
s.fast_forward_to_beat(4000)
mel = s.new_part("piano")
accomp = s.new_part('piano')
s.start_transcribing()

def notes():
    for notes, durations in mel_format():
        mel.play_note(notes, 1, durations)

def chords():
    for notes in generate_chords():
        accomp.play_chord(notes, 0.6, 4)

fork(chords)
notes()

performance = s.stop_transcribing()

output_dir = r'\..\xmls'
os.makedirs(output_dir, exist_ok=True)

performance.to_score().export_music_xml(os.path.join(output_dir, 'Generated Tune.xml'))

score = converter.parse(r'\..\xmls\Generated Tune.xml')

for measure in score.parts[1].getElementsByClass('Measure'):
    for element in measure:
        if isinstance(element, chord.Chord):
            element.simplifyEnharmonics(inPlace = True)
            symbol = harmony.chordSymbolFigureFromChord(element)
            chord_symbol = harmony.ChordSymbol(symbol)
            measure.insert(element.offset, chord_symbol)
            measure.remove(element)

    for element in measure.getElementsByClass('Clef'):
        measure.remove(element)
        
score.metadata.composer = 'Generated with Tune Generator 0.1 written by Gabriel Sagan'

#Must run once to use music21, remove after setup
configure.run()

score.show()
