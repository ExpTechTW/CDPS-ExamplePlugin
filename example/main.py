from cdps.plugin.events import onServerStartEvent
from cdps.plugin.manager import Listener, event_listener


@event_listener(onServerStartEvent)
class onServerStartListener(Listener):

    def on_event(self, event):
        print("Hello World")