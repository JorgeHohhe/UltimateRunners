from ....graphics.images_loader import PORTALS
from ..component_class import Component


class Portal(Component):

    def __init__(self, x, y, angle, code):
        super().__init__(x, y, angle, PORTALS[code])
        self.code = code
        self.passed = False
