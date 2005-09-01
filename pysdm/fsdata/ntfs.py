from constants import *

options = []
options.append( \
	{"nls":		[1, ["iso8859-1"], _("Character set to use for file names"), G_O], \
	 "utf8":	[0, ["utf8", ""], _("Use UTF-8 for converting file names"), G_O], \
	 "uni_xlate": [2, ["no", "1", "2"], _("Use escape sequences for unknown characters"), G_O], \
	 "posix":	[2, ["0", "1"], _("If enabled (1), the file system distinguishes between upper and lower case."), G_O], \
	 "uid":		[1, ["root"], _("Owner user of the filesystem"), G_M], \
	 "gid":		[1, ["users"], _("Owner group of the filesystem"), G_M], \
	 "umask":	[1, ["227"], _("umask for file permissions in octal"), G_M] \
	} \
	)

options.append( \
	{"iocharset": "nls" \
	} \
	)

defaults = ["ro", "nls=iso8859-1", "umask=000"]
