DJANGO_NOTIFY_ROUTING_KEY = 'model.{}.{}.{}'
DJANGO_NOTIFY_ROUTING_KEY_ARGS = ('name', 'author', 'pk')


class Notify(object):

    def __init__(self, when='CRUD', fields=None):
        super(Notify, self).__init__()

    def __call__(self, model):
        pass

class NotifyHandler(object):

    def __init__(self):
        self._callbacks = []

    def register_callback(self, callback):
        self._callbacks.append(callback)

    def handle(self, event):
        for callback in self._callbacks:
            if event.event_type in callback.events:
                callback.execute(event)


class NotifyCallback(object):
   pass
