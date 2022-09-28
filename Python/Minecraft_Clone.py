# must download first the module ursina
# use pip

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


class Grass(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(parent=scene,
                         position=position,
                         model='cube',
                         texture='grass',
                         color=color.color(0, 0,
                                           random.uniform(.9, 1.0)),
                         )

    def input(self, key):
        if key == 'left mouse down':
            hit_info = raycast(
                camera.world_position,
                camera.forward, distance=5)
            if hit_info.hit and \
                    hit_info.entity.position \
                    == self.position:
                self.scale -= 0.1
                if self.scale.x <= 0.7:
                    destroy(self)


if __name__ == '__main__':
    app = Ursina()
    Sky()


    def input(key):
        hit_info = raycast(camera.world_position,
                           camera.forward, distance=5)
        if key == 'right mouse down':
            if hit_info.hit:
                Grass(position=
                      hit_info.entity.position
                      + hit_info.normal)


    def update():
        if held_keys['left mouse']:
            hand.position = (0.7, -0.2)
        elif held_keys['right mouse']:
            hand.position = (0.4, -0.5)
        else:
            hand.position = (0.8, -0.3)


    hand = Entity(model="cube",
                  position=(0.8, -0.3, 0.2)
                  , parent=camera.ui,
                  rotation=(30, -40),
                  scale=(0.2, 1, 0.3)
                  )

    for z in range(8):
        for x in range(8):
            voxel = Grass(position=(x, 0, z))

    FirstPersonController()
    app.run()
