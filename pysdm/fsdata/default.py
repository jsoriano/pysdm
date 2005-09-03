from constants import *

options = []
options.append( \
	{"atime": 	[0, ["", "noatime"], _("Update file time for each access"), G_P], \
	 "diratime":[0, ["", "nodiratime"], _("Update directory time for each access"), G_P], \
	 "auto":	[0, ["", "noauto"], _("The file system is mounted at boot time"), G_M], \
	 "dev": 	[0, ["", "nodev"], _("Interpret character or block special devices on the file system"), G_S], \
	 "exec":	[0, ["", "noexec"], _("Permit execution of binaries"), G_S], \
	 "user":	[0, ["user", ""], _("Allow a user to mount and unmount the file system"), G_M], \
	 "users":	[0, ["users", ""], _("Allow any user to mount the file system"), G_M], \
	 "group":	[1, [""], _("Allow a group to mount this file system"), G_M], \
	 "_netdev": [0, ["_netdev", ""], _("This file system requires network"), G_O], \
	 "owner":	[0,	["owner", ""], _("The owner of the device can mount it"), G_M], \
	 "suid":	[0, ["", "nosuid"], _("Permit executables to change user/group identity"), G_S], \
	 "ro":		[0, ["ro", ""], _("Mount file system in read-only mode"), G_M], \
	 "sync":	[0,	["sync", ""], _("I/O to the file system should be done synchronously"), G_P], \
	 "dirsync": [0, ["dirsync", ""], _("All directory updates should be done synchronously"), G_P] \
	} \
	)

options.append( \
	{"noatime": "atime", \
	 "nodiratime": "diratime", \
	 "noauto":	"auto", \
	 "nodev":	"dev", \
	 "noexec":	"exec", \
	 "nosuid":	"suid", \
	 "nouser":	"user" \
	} \
	)

defaults = ["rw", "suid", "dev", "exec",  "auto",  "nouser", "async", "atime", "diratime"]
