import re
import os
import gtk

import gettext
gettext.install("pysdm")

rule2block = {"KERNEL":"name", \
			  "BUS": "bus", \
			  "SYSFS{vendor}":"vendor", \
			  "SYSFS{model}":"model", \
			  "SYSFS{serial}":"serial"}

CONDITIONS = {"KERNEL": _("Name is"), \
			  "BUS": _("Bus is"), \
			  "SYSFS{vendor}": _("Vendor is"), \
			  "SYSFS{model}": _("Model is"), \
			  "SYSFS{serial}": _("Serial is")}

ACTIONS = {"NAME": _("Specify a device file name"), \
		   "MODE": _("Specify users rigths"), \
		   "GROUP": _("Specify owner group"), \
		   "OWNER": _("Specify owner user"), \
		   "SYMLINK": _("Create a link with this name"), \
			} 

class RulesMakerDialog(gtk.Dialog):
	def __init__(self, block, udev_rule=None, *args, **kwds):
		super(RulesMakerDialog, self).__init__(*args, **kwds)
		if udev_rule == None:
			udev_rule = UdevRule()

		self.box_conditions = gtk.VBox()
		self.box_actions = gtk.VBox()
		self.conditions = []
		self.actions = []

		for condition in CONDITIONS:
			attribute = block.attributes[rule2block[condition]]
			if attribute != None:
				widget = gtk.CheckButton(CONDITIONS[condition] + " " + attribute)
				self.box_conditions.pack_start(widget)
				self.conditions.append([condition, widget, attribute])
				if udev_rule.conditions.has_key(condition):
					widget.set_active(True)

		for action in ACTIONS:
			box = gtk.HBox()
			check = gtk.CheckButton(ACTIONS[action])
			entry = gtk.Entry()
			box.pack_start(check)
			box.pack_start(entry)
			self.box_actions.pack_start(box)
			self.actions.append([action, check, entry])
			if udev_rule.actions.has_key(action):
				check.set_active(True)
				entry.set_text(udev_rule.actions[action])

		box = gtk.VBox()
		frame = gtk.Frame(_("Conditions"))
		frame.set_shadow_type(gtk.SHADOW_NONE)
		frame.set_border_width(12)
		frame.add(self.box_conditions)
		box.pack_start(frame)

		frame = gtk.Frame(_("Actions"))
		frame.set_border_width(12)
		frame.set_shadow_type(gtk.SHADOW_NONE)
		frame.add(self.box_actions)
		box.pack_start(frame)

		self.get_child().pack_start(box)

		self.show_all()

	def get_rule(self):
		rule = ""
		for condition in self.conditions:
			if condition[1].get_active():
				rule = rule + ", " + condition[0] + "==\"" + condition[2] + "\""

		for action in self.actions:
			if action[1].get_active():
				rule = rule + ", " + action[0] + "=\"" + action[2].get_text() + "\""

		return rule[2:]

class Block:
	def __init__(self, name, parent):
		block_path = "/sys/block/" + parent 
		if parent!=name:
			block_path = block_path + "/" + name
		self.parent = parent
		self.name = name
		nums = re.split("[:\n]",file(block_path + "/dev").readlines()[0])
		self.major = nums[0]
		self.minor = nums[1]

		self.attributes = {}
		self.attributes["name"] = name
		for att_name in ["vendor", "model", "serial"]:
			try:
				f = file("/sys/block/" + parent + "/device/" + att_name, "r")
				self.attributes[att_name] = re.split("[\n ]+", f.read())[0]
			except IOError:
				self.attributes[att_name] = None

		if name.find("hd")==0: self.attributes["bus"] = "ide"
		else: self.attributes["bus"] = "scsi"
		
		majorminor = "%x,%x" % (int(self.major),int(self.minor))
		if os.popen("stat -c %t,%T /dev/" + self.name + " 2> /dev/null").readline() == majorminor:
			self.dev = "/dev/" + self.name
		else:
			for file_name in os.popen("find /dev -type b -regex \"[^\.]*\"").readlines():
				ps = os.popen("stat -c %t,%T " + file_name)
				stat = ps.readline()
				ps.close()
				if stat.find(majorminor)==0:
					self.dev = file_name[:len(file_name)-1]
					return

class UdevRule:
	def __init__(self, rule=""):
		self.rule = rule
		self.conditions = {}
		self.actions = {}
		self.line = 0

		if len(rule)==0: return

		regexp_condition = re.compile("([\w{}]+)==\"([\w\-\*\[\]\,]+)\"")
		regexp_action = re.compile("(\w+)=\"(.+)\"")

		parameters = re.split(",\s\s*",rule)

		for parameter in parameters:
			match = regexp_condition.match(parameter)
			if match:
				self.conditions[match.groups()[0]]=match.groups()[1]
			else:
				match = regexp_action.match(parameter)
				
				if match:
					self.actions[match.groups()[0]]=match.groups()[1]
				else:
					print "Warning: Unidentified token: " + parameter

	def match(self, block):
		match = True
		for condition in self.conditions:
			regex = re.compile(self.conditions[condition])
			attribute = block.attributes[rule2block[condition]]
			if attribute == None: return False
			match = match and (regex.match(attribute)!=None)
		return match

	def __repr__(self):
		rrepr = ""
		for condition in self.conditions:
			rrepr = rrepr + ", " + condition + '=="' + self.conditions[condition] + '"'
		for action in self.actions:
			rrepr = rrepr + ", " + action + '="' + self.actions[action] + '"'
		return rrepr[2:] + "\n"

class UdevFile:
	def __init__(self, rules_file):
		self.rules_file = rules_file
		try:
			f = file(rules_file, "r")
			self.lines = f.readlines()
			f.close()
		except IOError:
			self.lines = []
		self.rules = {}

		for i in range(len(self.lines)):
			line = self.lines[i]
			if line.find(",")>0 and line[0]!="#":
				rule = UdevRule(line)
				rule.line = i
				self.rules[i] = rule

	def get_matching_rules(self, block):
		m_rules = []
		for rule in self.rules:
			if self.rules[rule].match(block):
				m_rules.append(self.rules[rule])
		return m_rules

	def add_rule(self, rule):
		rule = UdevRule(rule)
		if len(rule.actions)==0 or len(rule.conditions)==0:
			return
		rule.line = len(self.lines)
		self.rules[rule.line] = rule
		self.lines.append(rule.__repr__())

	def del_rule(self, rule_line):
		del self.rules[rule_line]
		del self.lines[rule_line]
		for rule in self.rules:
			if self.rules[rule].line > rule_line:
				self.rules[rule].line = self.rules[rule].line - 1

	def set_rule(self, rule_line, rule):
		rule = UdevRule(rule)
		if len(rule.actions)==0 or len(rule.conditions)==0:
			self.del_rule(rule_line)
			return
		rule.line = rule_line
		self.rules[rule_line] = rule
		self.lines[rule_line] = rule.__repr__()

	def switch_rule(self, rule_line1, rule_line2):
		rule_aux = self.rules[rule_line2]
		self.rules[rule_line2] = self.rules[rule_line1]
		self.rules[rule_line1] = rule_aux

		self.rules[rule_line1].line = rule_line1
		self.lines[rule_line1] = self.rules[rule_line1].__repr__()
		self.rules[rule_line2].line = rule_line2
		self.lines[rule_line2] = self.rules[rule_line2].__repr__()

	def write(self):
		f = file(self.rules_file, "w+")
		for line in self.lines:
			f.write(line)
		f.close()
