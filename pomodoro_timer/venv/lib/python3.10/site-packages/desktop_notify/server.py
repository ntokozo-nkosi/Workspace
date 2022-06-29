
import desktop_notify

class Server():

	BUS       = 'org.freedesktop.Notifications'
	PATH      = '/org/freedesktop/Notifications'
	INTERFACE = 'org.freedesktop.Notifications'

	def __init__(self, app_name):
		self.__bus = None
		self.__iface = None

		self.app_name = app_name
		self.visible = {}

	def Notify(self, *args):
		Notify = self.notify_class
		return Notify(*args)\
			.set_server(self)

	def show(self, notify):
		raise NotImplementedError(desktop_notify.EXCEPTION_IMPLEMENT)

	def close(self, notify):
		raise NotImplementedError(desktop_notify.EXCEPTION_IMPLEMENT)

	def __event_closed(self, notify_id, reason):
		notify_id = int(notify_id)

		if (notify_id in self.visible):
			self.visible[notify_id].closed(reason)
			del self.visible[notify_id]

	def __event_action(self, notify_id, action_id):
		notify_id = int(notify_id)
		action_id = int(action_id)

		if (notify_id in self.visible):
			self.visible[notify_id]\
				.action_invoke(action_id)


	@property
	def iface(self):
		raise NotImplementedError(desktop_notify.EXCEPTION_IMPLEMENT)

	def subscribe_signals(self, iface):
		iface.on_notification_closed(
			self.__event_closed
		)
		iface.on_action_invoked(
			self.__event_action
		)

	@property
	def bus(self):
		raise NotImplementedError(desktop_notify.EXCEPTION_IMPLEMENT)

	@property
	def notify_class(self):
		raise NotImplementedError(desktop_notify.EXCEPTION_IMPLEMENT)
