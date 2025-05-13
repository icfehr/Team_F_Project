screen ctc():
    zorder 30
    add "ctc"

init python:
    class CGController(object):
        default_timer = 1.0

        def __init__(self, min_zoom=0.1, max_zoom=5.0):
            self.imagepath = None
            self.scale = 1.0

            self.last_type = 0
            self.type = 0 # 0 - image, 1 - Movie

            self.last_image = None
            self.image = None
            self.overlay = None

            self.max_zoom = max_zoom
            self.min_zoom = min_zoom

            self.last_zoom = min_zoom
            self.zoom = min_zoom

            self.last_pos = (0, 0)
            self.pos = (0, 0)

            self.last_rotate = 0
            self.rotate = 0

            self.child = None
        ### Overlay function
        def set_overlay(self, overlay):
            if (img := renpy.get_registered_image(overlay)):
                self.overlay = img
            elif self.imagepath and isinstance(img, str):
                self.overlay = f"{self.imagepath}{overlay}.webp"
            else:
                self.overlay = img
            self.redraw(0)
        ### Image function
        def set_zoom(self, n):
            self.last_zoom = self.zoom
            self.zoom = float(clamp(n, self.min_zoom, self.max_zoom))

        def set_rotation(self, n):
            self.last_rotate = self.rotate
            self.rotate = n

        def set_pos(self, pos):
            self.last_pos = tuple(self.pos)
            self.pos = pos

        def set(self, zoom=None, rotate=None, pos=None, t=None, initialize=False, pause=False, image=None, overlay=False, trans=d1):
            if zoom is None:
                zoom=self.last_zoom
            if rotate is None:
                rotate=self.last_rotate
            if pos is None:
                pos=self.last_pos
            if t is None:
                t = self.default_timer

            self.set_zoom(zoom)
            self.set_rotation(rotate)
            self.set_pos(pos)

            if initialize:
                self.last_zoom = zoom
                self.last_rotate = rotate
                self.last_pos = pos

            if image:
                self.set_image(image, trans)

            if overlay is not False:
                self.set_overlay(overlay)

            self.redraw(t)

            if pause:
                renpy.pause(t)

        def redraw(self, t):
            if (d := self.image) is None:
                return

            if isinstance(d, Movie):
                self.scale = 2.0
                self.last_type = self.type
                self.type = 1
            else:
                self.scale = 1.0
                self.last_type = self.type
                self.type = 0

            if self.overlay:
                overlay = Transform(self.overlay, zoom=1.0/self.scale)
                d = Fixed(d, overlay, fit_first=True)

            last_zoom = self.last_zoom * self.scale
            zoom = self.zoom * self.scale

            self.child = At(d, CGCamera(last_zoom, zoom, self.last_pos, self.pos, self.last_rotate, self.rotate, t))

        def get_image(self):
            return self.child

default camera = CGController()

#### Transitions ##### 
# These were pulled pretty much directly from the renpy documentation
init offset = -1
define d1 = Dissolve(0.1)
define d2 = Dissolve(0.2)
define d3 = Dissolve(0.3)
define d4 = Dissolve(0.4)
define d5 = Dissolve(0.5)
define d6 = Dissolve(0.6)
define d7 = Dissolve(0.7)
define d8 = Dissolve(0.8)
define d9 = Dissolve(0.9)

define f1 = Fade(0.1, 0.0, 0.1)
define f2 = Fade(0.2, 0.0, 0.2)
define f3 = Fade(0.3, 0.0, 0.3)

define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
define flashbb = Fade(0.2, 0.0, 0.8, color='#000')
define flashblood = Fade(0.2, 0.0, 0.8, color='#f02424')
define kissiris = Fade(0.2, 0.0, 0.8, color='#fb8dc8')
define black_magic = Fade(0.2, 0.0, 0.5, color='#7f3590')
define blackfade = Fade(0.9, 0.5, 1, color='#000000')

define morph = ComposeTransition(Dissolve(0.9), before=Fade(0.1, 0.5, 0.5, color="#fff"), after=Dissolve(0.5))
define teleport = ImageDissolve("id_teleport.webp", 1.0, 0)

define faderight = ImageDissolve("interface/transitions/faderight.webp", 1.0)
define fadeleft = ImageDissolve("interface/transitions/faderight.webp", 1.0, reverse=True)
