options = []
options.append( \
	{"dmapi":		[0, ["dmapi", ""], "Enable the DMAPI (Data management API)"], \
	 "noalign":		[0, ["noalign", ""], "Data allocations will not be aligned at stripe unit boundaries"], \
	 "norecovery":	[0, ["norecovery", ""], "The filesystem will be mounted without running log recovery"], \
	 "nouuid":		[0, ["nouuid", ""], "Ignore file system uuid"], \
	 "usrquota":	[0, ["usrquota", ""], "Enable user disk quota"], \
	 "uqnoenforce":	[0, ["uqnoenforce", ""], "User disk quota limits enforced"], \
	 "grpquota":	[0, ["grpquota", ""], "Enable group disk quota"], \
	 "gqnoenforce":	[0, ["gqnoenforce", ""], "Group disk quota limits enforced"] \
	} \
	)

options.append( \
	{"dmapi":	"xdsm", \
	 "quota":	"usrquota" \
	} \
	)

defaults = []
