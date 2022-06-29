
import desktop_notify
import desktop_notify.glib as glib

from .message_bus import MessageBus

class Server(desktop_notify.BaseServer):

	def show(self, notify):
		def reply(response, exception):
			notify_id = int(response[0])

			self.visible[notify_id] = notify

			notify.set_id(notify_id)
			notify.shown()

		self.iface.call_notify(
			self.app_name,
			notify.id,
			notify.icon,
			notify.summary,
			notify.body,
			notify.actions_enumerated,
			notify.hints,
			notify.timeout,
			reply
		)

	def show_sync(self, notify):
		response = self.iface.call_notify_sync(
			self.app_name,
			notify.id,
			notify.icon,
			notify.summary,
			notify.body,
			notify.actions_enumerated,
			notify.hints,
			notify.timeout
		)
		notify_id = int(response)

		self.visible[notify_id] = notify

		notify.set_id(notify_id)
		notify.shown()

	def close(self, notify):
		def reply(response, exception):
			pass

		self.iface.call_close_notification(
			notify.id,
			reply
		)

	def close_sync(self, notify):
		self.iface.call_close_notification_sync(
			notify.id
		)

	@property
	def iface(self):
		if (not self.__iface):
			bus = self.bus
			obj = bus.get_proxy_object(
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
			self.__bus = MessageBus().connect_sync()

		return self.__bus

	@property
	def notify_class(self):
		return glib.Notify
