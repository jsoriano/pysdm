options = []
options.append( \
	{"acl":			[0, ["acl", ""], "Support POSIX access list"], \
	 "bsddf":		[0, ["minixdf", ""], "Minix behaviour for stat information"], \
	 "check":		[0, ["check", ""], "Check filesystem at mount time"], \
	 "debug":		[0, ["debug", ""], "Print debugging info"], \
	 "errors":		[2, ["continue", "remount-ro", "panic"], "Specify what to do in case of error"], \
	 "grpid":		[0, ["grpid", ""], "Get group id from the directory for a new file"], \
	 "nobh":		[0, ["nobh", ""], "Do not attach buffer_heads to file pagecache"], \
	 "nouid32":		[0, ["nouid32", ""], "Disables 32 bit user and group id"], \
	 "oldalloc":	[0, ["oldalloc", ""], "Use old new inode allocator"], \
	 "resgid":		[1, [""], "Group allowed to use reserved space"], \
	 "resuid":		[1, [""], "User allowed to use reserved space"], \
	 "sb":			[1, [""], "Use a especibic block as superblock"], \
	 "user_xattr":	[0, ["user_xattr", ""], "Support extended attributes"], \
	 "journal":		[1, ["update"], "Update journal or especify the inode where it is"], \
	 "noload":		[0, ["noload", ""], "Do not load journal on mounting"], \
	 "data":		[2, ["ordered", "journal", "writeback"], "Especify a journaling mode"], \
	 "commit":		[1, ["0"], "Synchronize data and metadata every specified seconds, 0 for default (5s.)"] \
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

