import stick
import random
import constantes
import time


class Target:
    def __init__(self):
        self.target = [stick.Stick(random.randint(1,constantes.maxheight)) for _ in range(constantes.sticknum)]
        # self.target = [stick.Stick(
        # i*constantes.heightmulti+constantes.addedheight)
        # for i in range(constantes.sticknum)]
        # random.shuffle(self.target)
        self.progress = 0

    def draw(self,window):
        for index, stick in enumerate(self.target):
            try:
                window.canvas.delete(stick.image)
            except:
                pass
            stick.image = window.canvas.create_rectangle(
            constantes.xtrans+ constantes.xmultiplier* index,
            constantes.height-(constantes.ytrans + constantes.ymultiplier * stick.height),
            constantes.xtrans+ constantes.xmultiplier* index+ constantes.xmultiplier,
            constantes.height,
            fill = stick.get_fill()
            )
        window.window.update()

    def sort(self,window):
        swapping = False
        window.canvas.itemconfig(self.target[self.progress].image,fill = 'green')
        minindex = self.progress
        minitem = self.target[minindex]
        minitem.current = True
        for index, stick in enumerate(self.target[self.progress:]):
            stick.selected = True
            if stick.height < minitem.height:
                minitem.min = False
                if not minitem.current:
                    window.canvas.itemconfig(minitem.image,fill = 'black')
                minitem.current = False
                minindex = index+self.progress
                minitem = stick
                minitem.min = True
            window.canvas.itemconfig(stick.image,fill = stick.get_fill())
            stick.selected = False
            window.window.update()
            window.canvas.itemconfig(stick.image,fill = stick.get_fill())
            if constantes.tscale !=0:
                time.sleep(constantes.tscale)
        self.target[self.progress] , self.target[minindex] = self.target[minindex], self.target[self.progress]
        self.target[self.progress].sorted = True
        swapping = False
        self.progress +=1
        self.draw(window)


    def clear(self,window):
        for item in self.target:
            window.canvas.delete(item.image)
