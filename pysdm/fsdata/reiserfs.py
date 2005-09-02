from constants import *

options = []
options.append( \
	{"conv": 	[0, ["conv", ""], _("Updated filesystem from ReiserFS 3.5 to 3.6"), G_O], \
	 "hash":	[2, ["rupasov", "tea", "r5", "detect"], _("Specify hash function to find files"), G_P], \
	 "nolog":	[0, ["nolog", ""], _("Disable reiserfs journaling"), G_J], \
	 "notail":	[0, ["notail", ""], _("Disable efficient in-tree storage of small files"), G_P] \
	} \
	)

defaults = []
