options = []
options.append( \
	{"nls":		[1, ["iso8859-1"], "Character set to use for file names"], \
	 "utf8":	[0, ["utf8", ""], "Use UTF-8 for converting file names"], \
	 "uni_xlate": [2, ["no", "1", "2"], "Use escape sequences for unknown characters"], \
	 "posix":	[2, ["0", "1"], "If enabled (1), the file system distinguishes between upper and lower case."], \
	 "uid":		[1, ["root"], "Owner user of the filesystem"], \
	 "gid":		[1, ["users"], "Owner group of the filesystem"], \
	 "umask":	[1, ["227"], "umask for file permissions in octal"] \
	} \
	)

options.append( \
	{"iocharset": "nls" \
	} \
	)

defaults = ["ro", "nls=iso8859-1", "umask=000"]
