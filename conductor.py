from mmaterial import MusicMaterial, Note
from mperfomer import GentleMelodyPerfomer,RandomMelodyPerfomer, RythmicBasePlayer,RockDrumPlayer

class Conductor:
    def __init__(self):
        self.tuneStructure = {"performer":[GentleMelodyPerfomer(), RythmicBasePlayer(),RockDrumPlayer()],
            "pitchKey":"D", "scale":MusicMaterial.LYDIAN_SCALE,"bars":4}


    def play(self):
        parts = []
        for per in self.tuneStructure["performer"]:
            parts.append(per.performe("D", MusicMaterial.LYDIAN_SCALE, 4))
        return parts
