
from typing import Callable

class Action():

	def __init__(self, label: str, callback: Callable):
		self.label = label
		self.callback = callback

	def __call__(self):
		return self._invoke()

	def _invoke(self, notify):
		return self.callback(notify)
