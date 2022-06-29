
import asyncio

from dbus_next import Variant

from .consts import *
from .action import Action
from .server import Server as BaseServer
from .notify import Notify as BaseNotify

from desktop_notify.aio import *

async def main():
	import argparse

	parser = argparse.ArgumentParser(
		prog = 'desktop-notify',
		description = 'Send desktop notification. Returns created notification\'s id.',
		add_help = False
	)
	parser.add_argument(
		'--help',
		action='help',
		help='show this help message and exit'
	)
	parser.add_argument(
		'summary',
		metavar = 'Summary',
		type = str,
		help = 'The summary text briefly describing the notification.',
	)
	parser.add_argument(
		'body',
		metavar = 'Body',
		type = str,
		nargs = '?',
		help = 'The optional detailed body text. Can be empty.',
	)
	parser.add_argument(
		'--icon',
		'-i',
		type = str,
		default = '',
		help = 'The optional program icon of the calling application. Should be either a file path or a name in a freedesktop.org-compliant icon theme.',
	)
	parser.add_argument(
		'--id',
		metavar = 'REPLACE_ID',
		type = int,
		default = 0,
		help = 'An optional ID of an existing notification that this notification is intended to replace.',
	)
	parser.add_argument(
		'--timeout',
		'-t',
		type = int,
		default = -1,
		help = "The timeout time in milliseconds since the display of the notification at which the notification should automatically close.",
	)

	def hint_pair(arg):
		hint = arg.split(':')

		if (len(hint) != 3):
			raise argparse.ArgumentTypeError(
				'Each hint should match the template "key:signature:value". '
				+ 'Error parsing "' + arg + '".'
			)

		SIGN_INT = ('y', 'n', 'q', 'i', 'u', 'x', 't')
		SIGN_BOOL = 'b'
		SIGN_FLOAT = 'd'

		if (hint[1] in SIGN_INT):
			hint[2] = int(hint[2])
		elif (hint[1] == SIGN_BOOL):
			hint[2] = bool(hint[2])
		elif (hint[1] == SIGN_FLOAT):
			hint[2] = float(hint[2])

		return hint

	parser.add_argument(
		'--hints',
		'-h',
		type = hint_pair,
		nargs = '+',
		metavar = 'key:signature:value',
		default = [],
		help = 'use "--" to separate hints list from positional args'
	)

	args = parser.parse_args()

	server = Server('desktop_notify')
	notify = server.Notify(args.summary)

	args.body\
		and notify.set_body(args.body)

	args.icon\
		and notify.set_icon(args.icon)

	args.id\
		and notify.set_id(args.id)

	args.timeout\
		and notify.set_timeout(args.timeout)

	for hint_arg in args.hints:
		notify.set_hint(hint_arg[0], Variant(hint_arg[1], hint_arg[2]))

	await notify.show()

	print(notify.id)

def run():
	asyncio.run(main())

if __name__ == "__main__":
	run()
