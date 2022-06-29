
import desktop_notify

from typing import Callable

class Notify():

	def __init__(
		self,
		summary: str = '',
		body: str = '',
		icon: str = '',
		timeout: int = -1
	):
		self.__server = None
		self.__id = 0
		self.__summary = summary
		self.__body = body
		self.__icon = icon
		self.__timeout = timeout

		self.__actions = []
		self.__hints = {}

		self.__on_show = None
		self.__on_close = None

		self.visible = False

	def show(self):
		raise NotImplementedError(desktop_notify.EXCEPTION_IMPLEMENT)

	def close(self):
		raise NotImplementedError(desktop_notify.EXCEPTION_IMPLEMENT)

	def action_invoke(self, action_id):
		self.actions[action_id]._invoke(self)

	def shown(self):
		self.visible = True

		if (self.on_show):
			self.on_show(self)

	def closed(self, reason):
		self.visible = False

		if (self.on_close):
			self.on_close(self, reason)


	@property
	def server(self):
		if (not self.__server):
			import os
			Server = self.server_class
			self.__server = Server(
				os.urandom(4).hex()
			)

		return self.__server

	@server.setter
	def server(self, server):
		self.set_server(server)

	def set_server(self, server):
		self.__server = server

		return self


	@property
	def id(self):
		return self.__id

	@id.setter
	def id(self, _id: str):
		self.__id = _id

	def set_id(self, _id: str):
		self.id = _id

		return self


	@property
	def summary(self):
		return self.__summary

	@summary.setter
	def summary(self, summary: str):
		self.__summary = summary

	def set_summary(self, summary: str):
		self.summary = summary

		return self


	@property
	def body(self):
		return self.__body

	@body.setter
	def body(self, body: str):
		self.__body = body

	def set_body(self, body: str):
		self.body = body

		return self


	@property
	def icon(self):
		return self.__icon

	@icon.setter
	def icon(self, icon: str):
		self.__icon = icon

	def set_icon(self, icon: str):
		self.icon = icon

		return self


	@property
	def timeout(self):
		return self.__timeout

	@timeout.setter
	def timeout(self, timeout):
		self.__timeout = timeout

	def set_timeout(self, timeout):
		self.timeout = timeout

		return self


	@property
	def hints(self):
		return self.__hints

	def set_hint(self, key, value):
		self.hints[key] = value

		return self

	def get_hint(self, key):
		return self.hints[key]

	def del_hint(self, key):
		del self.hints[key]

		return this


	@property
	def actions(self):
		return self.__actions

	def add_action(self, action):
		self.actions.append(action)

		return self

	def del_action(self, action):
		self.actions.remove(action)

		return this

	@property
	def actions_enumerated(self):
		pairs = []
		for i, action in enumerate(self.actions):
			pairs.append(str(i))
			pairs.append(action.label)

		return pairs


	@property
	def on_show(self):
		return self.__on_show

	@on_show.setter
	def on_show(self, callback: Callable):
		self.__on_show = callback

	def set_on_show(self, callback: Callable):
		self.on_show = callback

		return self

	@property
	def on_close(self):
		return self.__on_close

	@on_close.setter
	def on_close(self, callback: Callable):
		self.__on_close = callback

	def set_on_close(self, callback: Callable):
		self.on_close = callback

		return self

	@property
	def server_class(self):
		raise NotImplementedError(desktop_notify.EXCEPTION_IMPLEMENT)
