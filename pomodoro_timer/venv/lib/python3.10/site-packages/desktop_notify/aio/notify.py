
import desktop_notify
import desktop_notify.aio as aio

class Notify(desktop_notify.BaseNotify):

	async def show(self):
		self.__id = await self.server.show(self)

		self.shown()

	async def close(self):
		if (self.__id):
			await self.server.close(self)

	def set_server(self, server: aio.Server):
		return super().set_server(server)

	@property
	def server_class(self):
		return aio.Server
