
from typing import Callable

import desktop_notify
import desktop_notify.glib as glib

class Notify(desktop_notify.BaseServer):

	def show(self):
		self.__id = self.server.show(self)

	def show_sync(self):
		self.__id = self.server.show_sync(self)

	def close(self):
		if (self.__id):
			self.server.close(self)

	def close_sync(self):
		if (self.__id):
			self.server.close_sync(self)

	def set_server(self, server: glib.Server):
		return super().set_server(server)

	@property
	def server_class(self):
		return glib.Server
