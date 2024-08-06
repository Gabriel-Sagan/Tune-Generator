import random
from scamp import *

class ChordProgressionGenerator:
    def __init__(self):
        self.reset()
        self.initialize_chords()
        
    def initialize_chords(self):
        
        self.Cmaj7 = [36, 40, 43, 47]
        self.Dmin7 = [38, 41, 45, 48]
        self.Emin7 = [40, 43, 47, 50]
        self.Fmaj7 = [41, 45, 48, 52]
        self.Gdom7 = [43, 47, 50, 53]
        self.Amin7 = [45, 48, 52, 55]
        self.Bdim7 = [47, 50, 53, 57]

        # Secondary dominants
        self.Ddom7 = [38, 42, 45, 48]
        self.Edom7 = [40, 44, 47, 50] # used in minor as V
        self.Adom7 = [45, 49, 52, 55]
        self.Bdom7 = [47, 51, 54, 57]
        self.Cdom7 = [36, 40, 43, 46]
        self.Gbdom7 = [42, 46, 49, 52]

        # Pre-dominants
        self.Edim7 = [40, 43, 46, 50]
        self.Fsdim7 = [42, 45, 48, 52]
        self.Gmin7 = [43, 46, 50, 53]
        self.Csdim7 = [37, 40, 43, 47]
        self.Bmin7 = [47, 50, 54, 57]
        self.Fsmin7 = [42, 45, 49, 52]

        # Other
        self.Afulldim7 = [45, 48, 51, 54]

        # Major AC and HCs
        self.V_I = [self.Gdom7, self.Cmaj7]
        self.ii_V = [self.Dmin7, self.Gdom7]
        self.MII_V = [self.Ddom7, self.Gdom7]

        # Minor AC and HCs
        self.V_i = [self.Edom7, self.Amin7]
        self.ii0_V = [self.Bdim7, self.Edom7]
        self.mII_V = [self.Bdom7, self.Edom7]

        # Dominant progressions in major
        self.MI = [self.Dmin7, self.Gdom7, self.Cmaj7]
        self.Mii = [self.Edim7, self.Adom7, self.Dmin7]
        self.Miii = [self.Fsdim7, self.Bdom7, self.Emin7]
        self.MIV = [self.Gmin7, self.Cdom7, self.Fmaj7]
        self.MV = [self.Amin7, self.Ddom7, self.Gdom7]
        self.Mvi = [self.Bdim7, self.Edom7, self.Amin7]

        # Dominant progressions in minor
        self.mii0 = [self.Csdim7, self.Gbdom7, self.Bmin7]
        self.mV = [self.Fsmin7, self.Bdom7, self.Edom7]

        # Chord rules
        self.major_first_chord = [self.Cmaj7]
        self.minor_first_chord = [self.Amin7]

        self.major_two_thru_five = [self.Mii, self.Miii, self.MIV, self.MV, self.Mvi]
        self.minor_two_thru_five = [self.mii0, self.MI, self.Mii, self.mV, self.MIV]

        self.major_diatonic_chords = [self.Cmaj7, self.Dmin7, self.Fmaj7, self.Amin7]
        self.minor_diatonic_chords = [self.Amin7, self.Dmin7, self.Fmaj7]
        
        self.major_predom = random.choice([self.Dmin7, self.Fmaj7])
        self.minor_predom = random.choice([self.Bdim7, self.Dmin7])
        self.diminished_prog = ([self.Afulldim7, self.Dmin7]) 


    def reset(self):
        self.chord_progression = []
        self.quality_choice = random.choice([True, False])
        self.B_quality = random.choice([True, False])
        self.transposition_factor = random.choice([True, False])
        self.transposition = random.randint(12, 24)

    def major_chord_progression(self):
        while len(self.chord_progression) < 5:
            chord_pick = random.choice(self.major_diatonic_chords)
            self.chord_progression.append(chord_pick)
    
            # Replaces first chord with diatonic chord
            self.chord_progression[0] = random.choice(self.major_first_chord)
            
            # 75% chance each to replace 2nd-4th and 3rd-5th chord with secondary dominant progression.
            if random.random() < .55:
                if random.choice([True, False]):
                    sec_dom = random.choice(self.major_two_thru_five)
                    self.chord_progression[1:4] = sec_dom
                else:
                    sec_dom2 = random.choice(self.major_two_thru_five)
                    self.chord_progression[2:5] = sec_dom2
            
        return self.chord_progression
    
    def minor_chord_progression(self):
        while len(self.chord_progression) < 5:
            chord_pick = random.choice(self.minor_diatonic_chords)
            self.chord_progression.append(chord_pick)
        
            # Replaces first chord with diatonic chord
            self.chord_progression[0] = random.choice(self.minor_first_chord)
            
            # 75% for another 50% chance to replace 2-4th bar or 3-5th bar with a secondary ii V I
            if random.random() < .55:
                if random.choice([True, False]):
                    sec_dom = random.choice(self.minor_two_thru_five)
                    self.chord_progression[1:4] = sec_dom
                else:
                    sec_dom2 = random.choice(self.minor_two_thru_five)
                    self.chord_progression[2:5] = sec_dom2
                
        return self.chord_progression

    def hc(self):
        # Major half cadences
        IV_ii_V = [self.Fmaj7, *self.ii_V]
        vi_ii_V = [self.Amin7, *self.ii_V]
        VI_ii_V = [self.Adom7, *self.ii_V]
        I_ii_V = [self.Cmaj7, *self.ii_V]
        
        IV_II_V = [self.Fmaj7, *self.MII_V]
        vi_II_V = [self.Amin7, *self.MII_V]
        VI_II_V = [self.Adom7, *self.MII_V]
        I_II_V = [self.Cmaj7, *self.MII_V]
        
        # Minor half cadences
        iv_ii0_V = [self.Dmin7, *self.ii0_V]
        VI_ii0_V = [self.Fmaj7, *self.ii0_V]
        sVI_ii0_V = [self.Gbdom7, *self.ii0_V]
        i_ii0_V = [self.Amin7, *self.ii0_V]
        
        iv_mII_V = [self.Dmin7, *self.mII_V]
        VI_mII_V = [self.Fmaj7, *self.mII_V]
        sVI_mII_V = [self.Gbdom7, *self.mII_V]
        i_mII_V = [self.Amin7, *self.mII_V]
        
        major_half_cadences = [IV_ii_V, vi_ii_V, VI_ii_V, I_ii_V, IV_II_V, vi_II_V, VI_II_V, I_II_V]
        minor_half_cadences = [iv_ii0_V, VI_ii0_V, sVI_ii0_V, i_ii0_V, iv_mII_V, VI_mII_V, sVI_mII_V, i_mII_V]

        return random.choice(major_half_cadences if self.quality_choice else minor_half_cadences)

    def ac(self):
        # Major authentic cadences
        ii_V_I = [self.Dmin7, *self.V_I]
        IV_V_I = [self.Fmaj7, *self.V_I]
        II_V_I = [self.Ddom7, *self.V_I]
        
        # Minor authentic cadences
        ii0_V_i = [self.Bdim7, *self.V_i]
        iv_V_i = [self.Dmin7, *self.V_i]
        II_V_i = [self.Bdom7, *self.V_i]
        
        major_authentic_cadences = [ii_V_I, IV_V_I, II_V_I]
        minor_authentic_cadences = [ii0_V_i, iv_V_i, II_V_i]

        return random.choice(major_authentic_cadences if self.quality_choice else minor_authentic_cadences)

    def B(self):
        
        B_progression = []
        
        while len(B_progression) < 6:
            if self.B_quality:
                chord_pick = random.choice(self.major_diatonic_chords)
            else:
                chord_pick = random.choice(self.minor_diatonic_chords)
                
            B_progression.append(chord_pick)
            
            
    
        # Replace first thru fourth chord with a ii V I or IV V I to establish new key center
        if self.B_quality:
            B_progression[0] = self.major_first_chord[0]
            B_progression[1] = self.major_predom
            B_progression[2:4] = self.V_I
        else:
            B_progression[0] = self.minor_first_chord[0]
            B_progression[1] = self.minor_predom
            B_progression[2:4] = self.V_i

        # 40% chance to use a diminished progression
        if random.random() < .4:
            B_progression[4:6] = self.diminished_prog
            
        for i in range(len(B_progression)):
            if not isinstance(B_progression[i], list):
                B_progression[i] = [B_progression[i]]

        # Transpose B section
        chromatic_mediant = random.choice([3, 4, 8, 9])
        dominant = random.choice([5, 7])
        Mm_chromatic_mediant = random.choice([0, 6, 7, 11])
        mM_chromatic_mediant = random.choice([0, 1, 5, 6])
        Mm_dominant = random.choice([8, 10])
        mM_dominant = random.choice([2, 4])

        if self.transposition_factor:
            for i in range(len(B_progression)):
                if self.quality_choice == self.B_quality:
                    B_progression[i] = [num + chromatic_mediant for num in B_progression[i]]
                elif self.quality_choice and not self.B_quality:
                    B_progression[i] = [num + Mm_chromatic_mediant for num in B_progression[i]]
                elif not self.quality_choice and self.B_quality:
                    B_progression[i] = [num + mM_chromatic_mediant for num in B_progression[i]]
        else:
            for i in range(len(B_progression)):
                if self.quality_choice == self.B_quality:
                    B_progression[i] = [num + dominant for num in B_progression[i]]
                elif self.quality_choice and not self.B_quality:
                    B_progression[i] = [num + Mm_dominant for num in B_progression[i]]
                elif not self.quality_choice and self.B_quality:
                    B_progression[i] = [num + mM_dominant for num in B_progression[i]]
        
        # Add a major or minor half cadence at the end 
        if self.quality_choice:
            M_B_hcs = random.choice([self.ii_V, self.MII_V])
            B_progression.extend(M_B_hcs)
        else:
            m_B_hcs = random.choice([self.ii0_V, self.mII_V])
            B_progression.extend(m_B_hcs)
            
        return B_progression
    
    def AABA(self):
        
        self.reset()
        first_5 = self.major_chord_progression() if self.quality_choice else self.minor_chord_progression()
        a = first_5 + self.hc()
        ap = first_5 + self.ac()
        b = self.B()
        aaba = a + ap + b + ap
        for i in range(len(aaba)):
            aaba[i] = [num + self.transposition for num in aaba[i]]
        return aaba

