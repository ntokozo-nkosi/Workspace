
import asyncio

import desktop_notify
import desktop_notify.aio as aio

from .message_bus import MessageBus

class Server(desktop_notify.BaseServer):

	async def show(self, notify):
		iface = await self.iface
		notify_id = int(
			await iface.call_notify(
				self.app_name,
				notify.id,
				notify.icon,
				notify.summary,
				notify.body,
				notify.actions_enumerated,
				notify.hints,
				notify.timeout
			)
		)

		self.visible[notify_id] = notify

		return notify_id

	async def close(self, notify):
		iface = await self.iface
		await iface.call_close_notification(
			notify.id
		)

	@property
	async def iface(self):
		if (not self.__iface):
			bus = await self.bus
			obj = await bus.get_proxy_object(
				self.__class__.BUS,
				self.__class__.PATH
			)
			self.__iface = obj.get_interface(
				self.__class__.INTERFACE
			)

			self.subscribe_signals(self.__iface)

		return self.__iface

	@property
	def bus(self):
		if (not self.__bus):
			self.__bus = MessageBus().connect()

		return self.__bus

	@property
	def notify_class(self):
		return aio.Notify
