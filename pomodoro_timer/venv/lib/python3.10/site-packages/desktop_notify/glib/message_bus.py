
from dbus_next.glib import (
	MessageBus,
	ProxyObject
)

class MessageBus(MessageBus):

	def get_proxy_object(
		self,
		bus_name: str,
		path: str
	) -> ProxyObject:
		introspection = self.introspect_sync(
			bus_name,
			path
		)
		return super().get_proxy_object(bus_name, path, introspection)
