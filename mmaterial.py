class MusicMaterial:
    # 音名クラス
    PITCH_CLASS_C = {"name":"C",  "class":0}
    PITCH_CLASS_C_SHARP = {"name":"C#", "class":1}
    PITCH_CLASS_D_FLAT  = {"name":"D♭", "class":1}
    PITCH_CLASS_D =       {"name":"D",  "class":2}
    PITCH_CLASS_D_SHARP = {"name":"D#", "class":3}
    PITCH_CLASS_E_FLAT  = {"name":"E♭", "class":3}
    PITCH_CLASS_E =       {"name":"E",  "class":4}
    PITCH_CLASS_F =       {"name":"F",  "class":5}
    PITCH_CLASS_F_SHARP = {"name":"F#", "class":6}
    PITCH_CLASS_G_FLAT  = {"name":"G♭", "class":6}
    PITCH_CLASS_G =       {"name":"G",  "class":7}
    PITCH_CLASS_G_SHARP = {"name":"G#", "class":8}
    PITCH_CLASS_A_FLAT  = {"name":"A♭", "class":8}
    PITCH_CLASS_A =       {"name":"A",  "class":9}
    PITCH_CLASS_A_SHARP = {"name":"A#",  "class":10}
    PITCH_CLASS_B_FLAT  = {"name":"B♭","class":10}
    PITCH_CLASS_B =       {"name":"B","class":11}
    PITCH_CLASSS = [PITCH_CLASS_C, PITCH_CLASS_C_SHARP, PITCH_CLASS_D_FLAT, PITCH_CLASS_D, PITCH_CLASS_D_SHARP,
     PITCH_CLASS_E_FLAT,  PITCH_CLASS_E, PITCH_CLASS_F, PITCH_CLASS_F_SHARP, PITCH_CLASS_G_FLAT, PITCH_CLASS_G, 
     PITCH_CLASS_G_SHARP, PITCH_CLASS_A, PITCH_CLASS_A_SHARP, PITCH_CLASS_B_FLAT, PITCH_CLASS_B]
    # 音名 0
    PITCH_C0 =       {"name":"C0",  "pitch":0 , "pitchclass":PITCH_CLASS_C}
    PITCH_C_SHARP0 = {"name":"C#0", "pitch":1 , "pitchclass":PITCH_CLASS_C_SHARP}
    PITCH_D_FLAT0  = {"name":"D♭0", "pitch":1 , "pitchclass":PITCH_CLASS_D_FLAT}
    PITCH_D0 =       {"name":"D0",  "pitch":2 , "pitchclass":PITCH_CLASS_D}
    PITCH_D_SHARP0 = {"name":"D#0", "pitch":3 , "pitchclass":PITCH_CLASS_D_SHARP}
    PITCH_E_FLAT0  = {"name":"E♭0", "pitch":3 , "pitchclass":PITCH_CLASS_E_FLAT}
    PITCH_E0 =       {"name":"E0",  "pitch":4 , "pitchclass":PITCH_CLASS_E}
    PITCH_F0 =       {"name":"F0",  "pitch":5 , "pitchclass":PITCH_CLASS_F}
    PITCH_F_SHARP0 = {"name":"F#0", "pitch":6 , "pitchclass":PITCH_CLASS_F_SHARP}
    PITCH_G_FLAT0  = {"name":"G♭0", "pitch":6 , "pitchclass":PITCH_CLASS_G_FLAT}
    PITCH_G0 =       {"name":"G0",  "pitch":7 , "pitchclass":PITCH_CLASS_G}
    PITCH_G_SHARP0 = {"name":"G#0", "pitch":8 , "pitchclass":PITCH_CLASS_G_SHARP}
    PITCH_A_FLAT0  = {"name":"A♭0", "pitch":8 , "pitchclass":PITCH_CLASS_A_FLAT}
    PITCH_A0 =       {"name":"A0",  "pitch":9 , "pitchclass":PITCH_CLASS_A}
    PITCH_A_SHARP0 = {"name":"A#0", "pitch":10 , "pitchclass":PITCH_CLASS_A_SHARP}
    PITCH_B_FLAT0  = {"name":"B♭0", "pitch":10 , "pitchclass":PITCH_CLASS_B_FLAT}
    PITCH_B0 =       {"name":"B0",  "pitch":11 , "pitchclass":PITCH_CLASS_B}
    PITCHS = [PITCH_C0, PITCH_C_SHARP0]
    # 音名 1
    PITCH_C1 =       {"name":"C1",  "pitch":12, "pitchclass":PITCH_CLASS_C}
    PITCH_C_SHARP1 = {"name":"C#1", "pitch":13, "pitchclass":PITCH_CLASS_C_SHARP}
    PITCH_D_FLAT1  = {"name":"D♭1", "pitch":13, "pitchclass":PITCH_CLASS_D_FLAT}
    PITCH_D1 =       {"name":"D1",  "pitch":14, "pitchclass":PITCH_CLASS_D}
    PITCH_D_SHARP1 = {"name":"D#1", "pitch":15, "pitchclass":PITCH_CLASS_D_SHARP}
    PITCH_E_FLAT1  = {"name":"E♭1", "pitch":15, "pitchclass":PITCH_CLASS_E_FLAT}
    PITCH_E1 =       {"name":"E1",  "pitch":16, "pitchclass":PITCH_CLASS_E}
    PITCH_F1 =       {"name":"F1",  "pitch":17, "pitchclass":PITCH_CLASS_F}
    PITCH_F_SHARP1 = {"name":"F#1", "pitch":18, "pitchclass":PITCH_CLASS_F_SHARP}
    PITCH_G_FLAT1  = {"name":"G♭1", "pitch":18, "pitchclass":PITCH_CLASS_G_FLAT}
    PITCH_G1 =       {"name":"G1",  "pitch":19, "pitchclass":PITCH_CLASS_G}
    PITCH_G_SHARP1 = {"name":"G#1", "pitch":20, "pitchclass":PITCH_CLASS_G_SHARP}
    PITCH_A_FLAT1  = {"name":"A♭1", "pitch":20, "pitchclass":PITCH_CLASS_A_FLAT}
    PITCH_A1 =       {"name":"A1",  "pitch":21, "pitchclass":PITCH_CLASS_A}
    PITCH_A_SHARP1 = {"name":"A#1", "pitch":22, "pitchclass":PITCH_CLASS_A_SHARP}
    PITCH_B_FLAT1  = {"name":"B♭1", "pitch":22, "pitchclass":PITCH_CLASS_B_FLAT}
    PITCH_B1 =       {"name":"B1",  "pitch":23, "pitchclass":PITCH_CLASS_B}
    # 音名2
    PITCH_C2 =       {"name":"C2",  "pitch":24, "pitchclass":PITCH_CLASS_C}
    PITCH_C_SHARP2 = {"name":"C#2", "pitch":25, "pitchclass":PITCH_CLASS_C_SHARP}
    PITCH_D_FLAT2  = {"name":"D♭2", "pitch":25, "pitchclass":PITCH_CLASS_D_FLAT}
    PITCH_D2 =       {"name":"D2",  "pitch":26, "pitchclass":PITCH_CLASS_D}
    PITCH_D_SHARP2 = {"name":"D#2", "pitch":27, "pitchclass":PITCH_CLASS_D_SHARP}
    PITCH_E_FLAT2  = {"name":"E♭2", "pitch":27, "pitchclass":PITCH_CLASS_E_FLAT}
    PITCH_E2 =       {"name":"E2",  "pitch":28, "pitchclass":PITCH_CLASS_E}
    PITCH_F2 =       {"name":"F2",  "pitch":29, "pitchclass":PITCH_CLASS_F}
    PITCH_F_SHARP2 = {"name":"F#2", "pitch":30, "pitchclass":PITCH_CLASS_F_SHARP}
    PITCH_G_FLAT2  = {"name":"G♭2", "pitch":30, "pitchclass":PITCH_CLASS_G_FLAT}
    PITCH_G2 =       {"name":"G2",  "pitch":31, "pitchclass":PITCH_CLASS_G}
    PITCH_G_SHARP2 = {"name":"G#2", "pitch":32, "pitchclass":PITCH_CLASS_G_SHARP}
    PITCH_A_FLAT2  = {"name":"A♭2", "pitch":32, "pitchclass":PITCH_CLASS_A_FLAT}
    PITCH_A2 =       {"name":"A2",  "pitch":33, "pitchclass":PITCH_CLASS_A}
    PITCH_A_SHARP2 = {"name":"A#2", "pitch":34, "pitchclass":PITCH_CLASS_A_SHARP}
    PITCH_B_FLAT2  = {"name":"B♭2", "pitch":34, "pitchclass":PITCH_CLASS_B_FLAT}
    PITCH_B2 =       {"name":"B2",  "pitch":35,  "pitchclass":PITCH_CLASS_B}
    # 音名3
    PITCH_C2 =       {"name":"C2",  "pitch":36, "pitchclass":PITCH_CLASS_C}
    PITCH_C_SHARP2 = {"name":"C#2", "pitch":37, "pitchclass":PITCH_CLASS_C_SHARP}
    PITCH_D_FLAT2  = {"name":"D♭2", "pitch":37, "pitchclass":PITCH_CLASS_D_FLAT}
    PITCH_D2 =       {"name":"D2",  "pitch":38, "pitchclass":PITCH_CLASS_D}
    PITCH_D_SHARP2 = {"name":"D#2", "pitch":39, "pitchclass":PITCH_CLASS_D_SHARP}
    PITCH_E_FLAT2  = {"name":"E♭2", "pitch":39, "pitchclass":PITCH_CLASS_E_FLAT}
    PITCH_E2 =       {"name":"E2",  "pitch":40, "pitchclass":PITCH_CLASS_E}
    PITCH_F2 =       {"name":"F2",  "pitch":41, "pitchclass":PITCH_CLASS_F}
    PITCH_F_SHARP2 = {"name":"F#2", "pitch":42, "pitchclass":PITCH_CLASS_F_SHARP}
    PITCH_G_FLAT2  = {"name":"G♭2", "pitch":42, "pitchclass":PITCH_CLASS_G_FLAT}
    PITCH_G2 =       {"name":"G2",  "pitch":43, "pitchclass":PITCH_CLASS_G}
    PITCH_G_SHARP2 = {"name":"G#2", "pitch":44, "pitchclass":PITCH_CLASS_G_SHARP}
    PITCH_A_FLAT2  = {"name":"A♭2", "pitch":44, "pitchclass":PITCH_CLASS_A_FLAT}
    PITCH_A2 =       {"name":"A2",  "pitch":45, "pitchclass":PITCH_CLASS_A}
    PITCH_A_SHARP2 = {"name":"A#2", "pitch":46, "pitchclass":PITCH_CLASS_A_SHARP}
    PITCH_B_FLAT2  = {"name":"B♭2", "pitch":46, "pitchclass":PITCH_CLASS_B_FLAT}
    PITCH_B2 =       {"name":"B2",  "pitch":47,  "pitchclass":PITCH_CLASS_B}
    # 階名
    SYLLABLE_DO = {"name":"DO", "interval":0}
    SYLLABLE_DI = {"name":"DI", "interval":1}
    SYLLABLE_RA = {"name":"RA", "interval":1}
    SYLLABLE_RE = {"name":"RE", "interval":2}
    SYLLABLE_RI = {"name":"RI", "interval":3}
    SYLLABLE_ME = {"name":"ME", "interval":3}
    SYLLABLE_MI = {"name":"MI", "interval":4}
    SYLLABLE_FA = {"name":"FA", "interval":5}
    SYLLABLE_FI = {"name":"FI", "interval":6}
    SYLLABLE_SE = {"name":"SE", "interval":6}
    SYLLABLE_SO = {"name":"SO", "interval":7}
    SYLLABLE_SI = {"name":"SI", "interval":8}
    SYLLABLE_LE = {"name":"LE", "interval":8}
    SYLLABLE_LA = {"name":"LA", "interval":9}
    SYLLABLE_LI = {"name":"LI", "interval":10}
    SYLLABLE_TE = {"name":"DI", "interval":10}
    SYLLABLE_TI = {"name":"DI", "interval":11}
    SYLLABLES = [SYLLABLE_DO, SYLLABLE_DI,SYLLABLE_RA,
     SYLLABLE_RE, SYLLABLE_RI, SYLLABLE_ME, SYLLABLE_MI,
     SYLLABLE_FA, SYLLABLE_FI, SYLLABLE_SE, SYLLABLE_SO,
     SYLLABLE_SI, SYLLABLE_LE, SYLLABLE_LA, SYLLABLE_LI,
     SYLLABLE_TE, SYLLABLE_TI]
    # 音階
    MAJOR_SCALE = [SYLLABLE_DO, SYLLABLE_RE, SYLLABLE_MI,
     SYLLABLE_FA, SYLLABLE_SO, SYLLABLE_LA, SYLLABLE_TI]
    HARMONIC_MAJOR_SCALE = [SYLLABLE_DO, SYLLABLE_RE, SYLLABLE_MI,
     SYLLABLE_FA, SYLLABLE_SO, SYLLABLE_LE, SYLLABLE_TI]

    LYDIAN_SCALE = [SYLLABLE_DO, SYLLABLE_RE, SYLLABLE_MI,
      SYLLABLE_FI,SYLLABLE_SO, SYLLABLE_LA, SYLLABLE_TI]
    

    def pitch(pitchName, *, syllableName = None, pitchNumber = None):
        # 音高の数字指定時は指定された数字を持つ音高を返す
        if pitchNumber is not None:
            for pit in MusicMaterial.PITCHS:
                if pitchNumber % 12 == pit["pitch"]:
                    return pit
        # 音名のみの指定時は指定された音名を持つ音高を返す
        pitch = None
        for pit in MusicMaterial.PITCHS:
            if pitchName == pit["name"]:
                pitch = pit
                break
        if syllableName is None:
            return pitch
        else:
            # 音名と階名が指定された場合は音名を基準に階名に相当する音高を返す
            syllable = MusicMaterial.syllable(syllableName)
            return MusicMaterial.pitch(None,pitchNumber = (pitch["pitch"] + syllable["interval"]))

         
    
    def syllable(syllableName):
        for syllable in MusicMaterial.SYLLABLES:
             if syllableName == syllable["name"]:
                 return syllable
        return None

class Note:
    REST = {"name":"R",  "pitch":-1}
    CONTINUE = {"name":"C", "pitch":-1}
    def __init__(self):
        self.note = Note.REST
        self.octave = -1

    def setNote(self, note, octave):
        self.note = note 
        self.octave = octave
    
    def toStr (self):
        if self.octave != -1:
            return self.note["name"] + str(self.octave)
        return self.note["name"]
    
    def toDic(self):
        return {"name":self.note["name"], "octave":self.octave}


