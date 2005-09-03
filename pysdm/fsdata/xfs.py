from constants import *

options = []
options.append( \
	{"dmapi":		[0, ["dmapi", ""], _("Enable the DMAPI (Data management API)"), G_O], \
	 "noalign":		[0, ["noalign", ""], _("Data allocations will not be aligned at stripe unit boundaries"), G_P], \
	 "norecovery":	[0, ["norecovery", ""], _("The file system will be mounted without running log recovery"), G_J], \
	 "nouuid":		[0, ["nouuid", ""], _("Ignore file system uuid"), G_O], \
	 "usrquota":	[0, ["usrquota", ""], _("Enable user disk quota"), G_Q], \
	 "grpquota":	[0, ["grpquota", ""], _("Enable group disk quota"), G_Q] \
	} \
	)

options.append( \
	{"dmapi":	"xdsm", \
	 "quota":	"usrquota", \
	 "uqnoenforce": "usrquota", \
	 "gqnoenforce": "grpquota", \
	} \
	)

defaults = []
