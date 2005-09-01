options = []
options.append( \
	{"atime": 	[0, ["atime", "noatime"], _("Update file time for each access"), 1], \
	 "auto":	[0, ["", "noauto"], _("The file system is mounted at boot time"), 0], \
	 "dev": 	[0, ["", "nodev"], _("Interpret character or block special devices on the file system"), 1], \
	 "exec":	[0, ["", "noexec"], _("Permit execution of binaries"), 0], \
	 "user":	[0, ["user", ""], _("Allow a user to mount and unmount the file system"), 0], \
	 "users":	[0, ["users", ""], _("Allow any user to mount the file system"), 0], \
	 "group":	[1, [""], _("Allow a group to mount this file system"), 1], \
	 "_netdev": [0, ["_netdev", ""], _("This file system requires network"), 1], \
	 "owner":	[0,	["owner", ""], _("The owner of the device can mount it"), 1], \
	 "suid":	[0, ["suid", "nosuid"], _("Allow set user identifier"), 1], \
	 "ro":		[0, ["ro", ""], _("Mount file system in read-only mode"), 0], \
	 "sync":	[0,	["sync", ""], _("I/O to the file system should be done synchronously"), 1], \
	 "dirsync": [0, ["dirsync", ""], _("All directory updates should be done synchronously"), 1] \
	} \
	)

options.append( \
	{"noatime": "atime", \
	 "noauto":	"auto", \
	 "nodev":	"dev", \
	 "noexec":	"exec", \
	 "nosuid":	"suid", \
	 "nouser":	"user" \
	} \
	)

defaults = ["rw", "suid", "dev", "exec",  "auto",  "nouser", "async"]
