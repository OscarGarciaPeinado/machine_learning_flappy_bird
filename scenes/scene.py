class Scene:
    def __init__(self, game):
        self.game = game

    def on_update(self):
        raise NotImplemented()

    def on_event(self, event):
        raise NotImplemented()

    def on_draw(self, screen):
        raise NotImplemented()
