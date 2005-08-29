options = []
options.append( \
	{"conv": 	[0, ["conv", ""], _("Updated filesystem from ReiserFS 3.5 to 3.6"), 1], \
	 "hash":	[2, ["rupasov", "tea", "r5", "detect"], _("Especify hash function to find files"), 1], \
	 "nolog":	[0, ["nolog", ""], _("Disable reiserfs journaling"), 0], \
	 "notail":	[0, ["notail", ""], _("Disable packing of files into the tree"), 0] \
	} \
	)

defaults = []
