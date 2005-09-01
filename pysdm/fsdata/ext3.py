options = []
options.append( \
	{"acl":			[0, ["acl", ""], _("Support POSIX access list"), 1], \
	 "bsddf":		[0, ["minixdf", ""], _("Minix behaviour for stat information"), 1], \
	 "check":		[0, ["check", ""], _("Check file system at mount time"), 1], \
	 "debug":		[0, ["debug", ""], _("Print debugging info"), 1], \
	 "errors":		[2, ["continue", "remount-ro", "panic"], _("Specify what to do in case of error"), 0], \
	 "grpid":		[0, ["grpid", ""], _("Get group id from the directory for a new file"), 1], \
	 "nobh":		[0, ["nobh", ""], _("Do not attach buffer_heads to file pagecache"), 1], \
	 "nouid32":		[0, ["nouid32", ""], _("Disables 32 bit user and group id"), 1], \
	 "oldalloc":	[0, ["oldalloc", ""], _("Use old new inode allocator"), 1], \
	 "resgid":		[1, [""], _("Group allowed to use reserved space"), 1], \
	 "resuid":		[1, [""], _("User allowed to use reserved space"), 1], \
	 "sb":			[1, [""], _("Use a especific block as superblock"), 1], \
	 "user_xattr":	[0, ["user_xattr", ""], _("Support extended attributes"), 0], \
	 "journal":		[1, ["update"], _("Update journal or specify the inode where it is"), 1], \
	 "noload":		[0, ["noload", ""], _("Do not load journal on mounting"), 0], \
	 "data":		[2, ["ordered", "journal", "writeback"], _("Specify a journaling mode"), 1], \
	 "commit":		[1, ["0"], _("Synchronize data and metadata every specified seconds, 0 for default (5s.)"), 1] \
	} \
	)
	
	 
options.append( \
	{"noacl":	"acl", \
	 "minixdf":	"bsddf", \
	 "nocheck": "check", \
	 "nogrpid": "grpid", \
	 "orlov":	"oldalloc", \
	 "nouser_xattr": "user_xattr" \
	}
	)

defaults = ["errors=remount-ro"]

