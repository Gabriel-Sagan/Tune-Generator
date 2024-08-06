from scamp import *
import random
from chord import ChordProgressionGenerator
from seed import seed_generator

def chord_seq():
    random.seed(seed_generator())
    generator = ChordProgressionGenerator()
    chord_sequence = generator.AABA()
    return chord_sequence

melody_notes = []
duration_seq = []
sum_4_notes = []
durations = [0.5, 1, 2]

while sum(duration_seq) < 128:
    current_sum = 0
    segment = []
    
    while current_sum < 4:
        choice = random.choice(durations)
        
        if current_sum + choice > 4:
            choice = 4 - current_sum
            
        segment.append(choice)
        current_sum += choice
        
    duration_seq.extend(segment)

total = 0
count = 0

for duration in duration_seq:
    total += duration
    count += 1
    
    if total >= 4:
        sum_4_notes.append(count)
        total = 0
        count = 0

def melody():
    
    ionian = [36, 38, 40, 43, 45, 47]
    dorian = [36, 38, 39, 43, 46]
    mixolydian = [36, 40, 43, 46]
    half_locrian = [36, 39, 42, 46]
    full_locrian = [36, 39, 42, 45]
    
    while len(melody_notes) < 32:
        for i, chord in enumerate(chord_seq()):
            note_dif = chord[0] - 36
            
            if chord[3] - chord[0] == 11:
                transposed_ionian = [note + note_dif for note in ionian]
                for _ in range(sum_4_notes[i]):
                    melody_notes.append(random.choice(transposed_ionian))
                
            elif chord[3] - chord[0] == 10 and chord[1] - chord[0] == 4:
                transposed_mixolydian = [note + note_dif for note in mixolydian]
                for _ in range(sum_4_notes[i]):
                    melody_notes.append(random.choice(transposed_mixolydian))
                
            elif chord[1] - chord[0] == 3 and chord[2] - chord[0] == 7:
                transposed_dorian = [note + note_dif for note in dorian]
                for _ in range(sum_4_notes[i]):
                    melody_notes.append(random.choice(transposed_dorian))
                
            elif chord[2] - chord[0] == 6 and chord[3] - chord[0] == 10:
                transposed_half_locrian = [note + note_dif for note in half_locrian]
                for _ in range(sum_4_notes[i]):
                    melody_notes.append(random.choice(transposed_half_locrian))
                    
            elif chord[2] - chord[0] == 6 and chord[3] - chord[0] == 9:
                transposed_full_locrian = [note + note_dif for note in full_locrian]
                for _ in range(sum_4_notes[i]):
                    melody_notes.append(random.choice(transposed_full_locrian))
                          
    return melody_notes

def note_octavize():
    note_seq = melody()
    formatted_seq = []
    
    for note in note_seq:
        if note < 60:
            note += 12
            formatted_seq.append(note)
            
        elif note > 77:
            note -= 12
            formatted_seq.append(note)
            
        else:
            formatted_seq.append(note)
                 
    return formatted_seq


def melody_and_duration():
    
    note_durations = list(zip(note_octavize(), duration_seq))
    return note_durations

def mel_format():
    
    output = melody_and_duration()
    
    #full A section
    i = 36
    L = sum(duration_seq[:i])
    while L > 32:
        i -= 1
        L = sum(duration_seq[:i])
          
    SectionA = output[:i]
    
    #first 5 bars of A
    f = 24
    G = sum(duration_seq[:f])
    while G > 20:
        f -= 1
        G = sum(duration_seq[:f])
        
    A_first_five = output[:f]
    
    #shows end of second A or start of B
    j = 68
    N = sum(duration_seq[:j])
    while N > 64:
        j -= 1
        N = sum(duration_seq[:j])
    
    #first 5 of second A
    c = 56
    D = sum(duration_seq[:c])
    while D > 52:
        c -= 1
        D = sum(duration_seq[:c])
        
    Ap_last_three = output[c:j]
    
    SectionAp = A_first_five + Ap_last_three
    
    #full B section    
    q = 36
    R = sum(duration_seq[j:q+j])
    while R > 32:
        q -= 1
        R = sum(duration_seq[j:q+j])
           
    SectionB = output[j:q+j]
        
    full_mel = SectionA + SectionAp + SectionB + SectionAp
    
    return full_mel
    