from constants import *

options = []
options.append( \
	{"acl":			[0, ["acl", ""], _("Support POSIX access list"), G_O], \
	 "bsddf":		[0, ["minixdf", ""], _("Minix behaviour for stat information"), G_O], \
	 "check":		[0, ["check", ""], _("Check file system at mount time"), G_M], \
	 "debug":		[0, ["debug", ""], _("Print debugging info"), G_O], \
	 "errors":		[2, ["continue", "remount-ro", "panic"], _("Specify what to do in case of error"), G_P], \
	 "grpid":		[0, ["grpid", ""], _("Get group id from the directory for a new file"), G_P], \
	 "nobh":		[0, ["nobh", ""], _("Do not attach buffer_heads to file pagecache"), G_P], \
	 "nouid32":		[0, ["nouid32", ""], _("Disables 32 bit user and group id"), G_O], \
	 "oldalloc":	[0, ["oldalloc", ""], _("Use old new inode allocator"), G_P], \
	 "resgid":		[1, [""], _("Group allowed to use reserved space"), G_O], \
	 "resuid":		[1, [""], _("User allowed to use reserved space"), G_O], \
	 "sb":			[1, [""], _("Use a especific block as superblock"), G_P], \
	 "user_xattr":	[0, ["user_xattr", ""], _("Support extended attributes"), G_M] \
	} \
	)
	 
options.append( \
	{"noacl":	"acl", \
	 "minixdf":	"bsddf", \
	 "nocheck":	"check", \
	 "nogrpid":	"grpid", \
	 "orlov":	"oldalloc", \
	 "nouser_xattr": "user_xattr" \
	}
	)

defaults = ["errors=remount-ro"]
