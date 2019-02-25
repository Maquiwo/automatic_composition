import random
from mmaterial import MusicMaterial
from mmaterial import Note

class RandomMelodyPerfomer:
    def __init__(self):
        pass

    def performe(self, pitchKey, scale, barsLength):
        melody =[]
        for i in range(barsLength * 16):
            note = Note()
            s = random.randrange(len(scale) + 10)
            if s < len(scale):
                pitch = MusicMaterial.pitch( pitchName =pitchKey, syllableName = scale[s]["name"])
                note.setNote(pitch,3)
            melody.append(note.toDic())
        return melody

class GentleMelodyPerfomer:
    def __init__(self):
        pass

    def performe(self, pitchKey, scale, barsLength):
        melody =[]
        indicator = random.randrange(len(scale))
        for i in range(barsLength * 16):
            note = Note()
            indicator = indicator + random.randrange(7) -3
            pitch = MusicMaterial.pitch( pitchName =pitchKey, syllableName = scale[indicator // len(scale)]["name"])
            note.setNote(pitch,3)
            melody.append(note.toDic())
        return melody


class RythmicBasePlayer:
    def __init__(self):
        pass

    def performe(self, pitchKey, scale, barsLength):
        melody =[]
        pattern =[1,1,1,0]
        for i in range(barsLength * 16 // len(pattern)):
            for p in pattern:
                note = Note()
                s = random.randrange(100)
                if s > 90:
                    pass
                elif s > 80:
                    if p == 1:
                        pr = random.randrange(len(scale))
                        pitch = MusicMaterial.pitch( pitchName =pitchKey, syllableName = scale[pr]["name"])
                        note.setNote(pitch,1)
                else:
                    if p == 1:
                        pitch = MusicMaterial.pitch( pitchName =pitchKey, syllableName = scale[0]["name"])
                        note.setNote(pitch,1)
                melody.append(note.toDic())
        return melody

class RockDrumPlayer:
    def __init__(self):
        pass

    def performe(self, pitchKey, scale, barsLength):
        melody =[]
        pattern =[0,0,0,0,2,0,1,0,0,0,0,0,2,0,1,0]
        for i in range(barsLength * 16 // len(pattern)):
            for p in pattern:
                note = Note()
                if p == 0:
                    pitch = MusicMaterial.pitch( pitchName =pitchKey, syllableName = scale[0]["name"])
                    note.setNote(pitch,0)
                if p == 1:
                    pitch = MusicMaterial.pitch( pitchName =pitchKey, syllableName = scale[0]["name"])
                    note.setNote(pitch,3)
                if p == 2:
                    pitch = MusicMaterial.pitch( pitchName =pitchKey, syllableName = scale[0]["name"])
                    note.setNote(pitch,1)
                melody.append(note.toDic())
        return melody

