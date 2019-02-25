import pyxel
from tune import Tune
from pyxmch import PyxelMusicChanger

class App:

    

    def __init__(self):
        pyxel.init(255, 143, caption='自動作曲習作', scale= 3, fps=60, border_width=0, border_color = 0x101012)
        self.isPlay = False
        self.tune = PyxelMusicChanger.change(Tune().play())
        print(self.tune)
        pyxel.run(self.update, self.draw)

        
        

    def update(self):
        if not self.isPlay:
            for i in range(len(self.tune)):
                pyxel.sound(i).set_note(self.tune[i])
                pyxel.sound(i).speed = 10
            pyxel.sound(1).set_tone('S')
            pyxel.sound(1).set_effect('F')
            pyxel.sound(2).set_tone('N')
            pyxel.sound(2).set_effect('F')
            if len(self.tune) > 0:
                pyxel.music(0).set_ch0([0])
            if len(self.tune) > 1:
                pyxel.music(0).set_ch1([1])
            if len(self.tune) > 2:
                pyxel.music(0).set_ch2([2])
            if len(self.tune) > 3:
                pyxel.music(0).set_ch3([3])
            
            pyxel.playm(0, loop=True)
            self.isPlay = True




    def draw(self):
        pass

        
        

App()