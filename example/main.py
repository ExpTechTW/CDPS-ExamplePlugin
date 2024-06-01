from cdps.plugin.manager import Manager, Listener
from cdps.plugin.events import onServerStartEvent


class onServerStartListener(Listener):
    event = onServerStartEvent

    def on_event(self, event):
        print(event.pid)


event_manager = Manager()
event_manager.register_listener(onServerStartListener())
