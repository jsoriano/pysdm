options = []
options.append( \
	{"blocksize":	[1, ["512"], _("Set blocksize"), 1], \
	 "uid":		[1, ["root"], _("Owner user of the filesystem"), 1], \
	 "gid":		[1, ["users"], _("Owner group of the filesystem"), 1], \
	 "umask":	[1, ["227"], _("umask for file and directory permissions in octal"), 0], \
	 "dmask":	[1, ["227"], _("umask for directory permissions in octal"), 1], \
	 "fmask":	[1, ["227"], _("umask for file permissions in octal"), 1], \
	 "check":	[2, ["normal", "relaxed", "strict"], _("Select level of character checking in file names"), 1], \
	 "codepage":[1, ["437"], _("Sets the codepage for converting to shortname characters"), 1], \
	 "conv":	[2, ["binary", "text", "auto"], _("Text format conversion mode"), 1], \
	 "cvf_format": [1, [""], _("Forces the driver to use the CVF module instead of autodetection"), 1], \
	 "cvf_option": [1, [""], _("Option passed to CVF module"), 1], \
	 "debug":	[0, ["debug", ""], _("Display debug messages"), 1], \
	 "fat":		[2, ["12", "16", "32"], _("Specify a 12, 16 or 32 bit fat"), 1], \
	 "iocharset":	[1, ["iso8859-1"], _("Character set to use for file names"), 1], \
	 "quiet":	[0, ["quiet", ""], _("Failures do not return errors"), 0] \
	} \
	)

defaults = []
