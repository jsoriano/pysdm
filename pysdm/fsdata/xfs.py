options = []
options.append( \
	{"dmapi":		[0, ["dmapi", ""], _("Enable the DMAPI (Data management API)"), 1], \
	 "noalign":		[0, ["noalign", ""], _("Data allocations will not be aligned at stripe unit boundaries"), 1], \
	 "norecovery":	[0, ["norecovery", ""], _("The filesystem will be mounted without running log recovery"), 1], \
	 "nouuid":		[0, ["nouuid", ""], _("Ignore file system uuid"), 1], \
	 "usrquota":	[0, ["usrquota", ""], _("Enable user disk quota"), 0], \
	 "uqnoenforce":	[0, ["uqnoenforce", ""], _("User disk quota limits enforced"), 1], \
	 "grpquota":	[0, ["grpquota", ""], _("Enable group disk quota"), 0], \
	 "gqnoenforce":	[0, ["gqnoenforce", ""], _("Group disk quota limits enforced"), 1] \
	} \
	)

options.append( \
	{"dmapi":	"xdsm", \
	 "quota":	"usrquota" \
	} \
	)

defaults = []
