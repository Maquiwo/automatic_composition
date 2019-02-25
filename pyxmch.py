class PyxelMusicChanger:
    def change(tune):
        parts = []
        for par in tune:
            part = ""
            for ton in par:
                tone = PyxelMusicChanger.tlanslate(ton)
                part = part + tone
            parts.append(part)
        return parts



    def tlanslate(tone):
        if tone["name"] == "R":
            return "R"
        pyxelTone = tone["name"] + str(tone["octave"])
        pyxelTone.replace('♭', '-')
        return pyxelTone


