
from dbus_next.aio import (
	MessageBus,
	ProxyObject
)

class MessageBus(MessageBus):

	async def get_proxy_object(
		self,
		bus_name: str,
		path: str
	) -> ProxyObject:
		introspection = await self.introspect(
			bus_name,
			path
		)
		return super().get_proxy_object(bus_name, path, introspection)
