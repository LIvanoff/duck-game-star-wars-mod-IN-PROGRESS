
# TODO: имплементировать сетап с инфой по каждому кадру анимации (словарь/джсон)
class Animation:
    def __init__(self, imgs, imgDuration=5, loop=True) -> None:
        self.imgs = imgs
        self.imgDuration = imgDuration
        self.loop = loop
        self.done = False
        self.frame = 0

    
    def copy(self):
        return Animation(self.imgs, self.imgDuration, self.loop)
    

    def update(self):
        if self.loop:
            self.frame = (self.frame + 1) % (self.imgDuration * len(self.imgs))
        else:
            self.frame = min(self.frame + 1, self.imgDuration * len(self.imgs))
            if self.frame >= self.imgDuration * len(self.imgs) - 1:
                self.done = True


    def img(self):
        return self.imgs[int(self.frame / self.imgDuration)]