options = []
options.append( \
	{"atime": 	[0, ["atime", "noatime"], "Update file time for each access"], \
	 "auto":	[0, ["", "noauto"], "The filesystem is mounted in boot time"], \
	 "dev": 	[0, ["", "nodev"], "Interpret character or block special devices on the file system"], \
	 "exec":	[0, ["", "noexec"], "Allow execution of binaries"], \
	 "user":	[0, ["user", ""], "Allows a user to mount the filesystem"], \
	 "users":	[0, ["users", ""], "Allows any user to mount the filesystem"], \
	 "group":	[1, [""], "Allow a group to mount this filesystem"], \
	 "_netdev": [0, ["_netdev", ""], "This file system requires network"], \
	 "owner":	[0,	["owner", ""], "The owner of the device can mount it"], \
	 "suid":	[0, ["suid", "nosuid"], "Allow set user identifier"], \
	 "ro":		[0, ["ro", ""], "Mount file system in read-only mode"], \
	 "sync":	[0,	["sync", ""], "I/O to the file system should be done synchronously"], \
	 "dirsync": [0, ["dirsync", ""], "All directory updates should be done synchronously"] \
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
