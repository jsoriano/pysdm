from constants import *

options = []
options.append( \
	{"blocksize":	[1, ["512"], _("Set blocksize"), G_O], \
	 "uid":		[1, ["root"], _("Owner user of the filesystem"), G_M], \
	 "gid":		[1, ["users"], _("Owner group of the filesystem"), G_M], \
	 "umask":	[1, ["227"], _("umask for file and directory permissions in octal"), G_M], \
	 "dmask":	[1, ["227"], _("umask for directory permissions in octal"), G_M], \
	 "fmask":	[1, ["227"], _("umask for file permissions in octal"), G_M], \
	 "check":	[2, ["normal", "relaxed", "strict"], _("Select level of character checking in file names"), G_O], \
	 "codepage":[1, ["437"], _("Sets the codepage for converting to shortname characters"), G_O], \
	 "conv":	[2, ["binary", "text", "auto"], _("Text format conversion mode"), G_O], \
	 "cvf_format": [1, [""], _("Forces the driver to use the CVF module instead of autodetection"), G_P], \
	 "cvf_option": [1, [""], _("Option passed to CVF module"), G_P], \
	 "debug":	[0, ["debug", ""], _("Display debug messages"), G_O], \
	 "fat":		[2, ["12", "16", "32"], _("Specify a 12, 16 or 32 bit fat"), G_O], \
	 "iocharset":	[1, ["iso8859-1"], _("Character set to use for file names"), G_O], \
	 "quiet":	[0, ["quiet", ""], _("Failures do not return errors"), G_O] \
	} \
	)

defaults = []
