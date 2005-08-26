#!/usr/bin/env python
# -*- coding: UTF8 -*-

import gtk
import re
import fsdata

OP_CHECK = 0
OP_ENTRY = 1
OP_COMBO = 2
OP_PERMISSION = 3

class option_dialog(gtk.Dialog):
	
	def __init__(self, filesystem, *args, **kwds):
		super(option_dialog, self).__init__(*args, **kwds)

		self.op_widgets = {}
		self.filesystem = filesystem
		self.defaults = fsdata.defaults['default']

		for op in fsdata.options['default'][0]:
			op_info = fsdata.options['default'][0][op]
			self.add_option(op_info[0], op, op_info[1], op_info[2])
		try:
			self.defaults = self.defaults + fsdata.defaults[filesystem]
			for op in fsdata.options[filesystem][0]:
				op_info = fsdata.options[filesystem][0][op]
				self.add_option(op_info[0], op, op_info[1], op_info[2])
		except KeyError:
			print "Warning: Unknown especial options for " + filesystem + " filesystem"

		self.get_child().show_all()

	def set_value(self, value):
		if len(value) == 0 or not cmp(value[0], "defaults"):
			self.set_value(self.defaults)
		else:
			for option in value:
				op_name = re.compile("([\w_]+)=?.*").match(option).groups()[0]
				try:
					if self.op_widgets.has_key(op_name):
						widget = self.op_widgets[op_name]
					elif fsdata.options['default'][1].has_key(op_name):
						widget = self.op_widgets[fsdata.options['default'][1][op_name]]
					elif fsdata.options.has_key(self.filesystem) and \
							fsdata.options[self.filesystem][1].has_key(op_name):
						widget = self.op_widgets[fsdata.options['default'][1][op_name]]
					else:
						print "Warning: Unknown option: " + option
						continue
				except:
					print "Warning: Unknown option: " + option
					continue
				widget.set_value(option)

	def get_value(self):
		value = []
		op_widgets = self.get_child().get_children()

		for op_widget in op_widgets:
			try:
				op_value = op_widget.get_value()
			except AttributeError:
				continue
			if len(op_value) > 0:
				value.append(op_value)
		return value
	
	def add_option(self, op_type, op_name, options, description):
		box = self.get_child()
		
		if op_type == OP_CHECK:
			op_widget = option_check(op_name, options, description)
		elif op_type == OP_ENTRY:
			op_widget = option_entry(op_name, options, description)
		elif op_type == OP_COMBO:
			op_widget = option_combo(op_name, options, description)
		elif op_type == OP_PERMISSION:
			print ("Warning: " + op_name + ": unimplemented option type OP_PERMISSION")
			return
		else:
			print ("Warning: " + op_name + ": unknown option type " + str(op_type))
			return
		box.pack_start(op_widget)
		self.op_widgets[op_name] = op_widget







class option_check(gtk.CheckButton):

	def __init__(self, op_name, options, description):
		super(option_check, self).__init__(description, False)
		self.op_name = op_name
		self.options = options
		self.description = description	

	def set_value(self, value):
		if not cmp(value, self.options[0]) or (len(self.options[0])==0 and not cmp(self.op_name,value)):
			self.set_active(True)
			return
		elif not cmp(value, self.options[1]) or (len(self.options[1])==0 and not cmp(self.op_name,value)):
			self.set_active(False)
			return
		print "Warning: " + value + " is not suitable for " + self.op_name 

	def get_value(self):
		if self.get_active():
			return self.options[0]
		else:
			return self.options[1]






class option_entry(gtk.HBox):
	
	def __init__(self, op_name, options, description):
		super(option_entry, self).__init__()
		self.op_name = op_name
		self.options = options
		self.description = description

		self.check = gtk.CheckButton(description + "\t" + op_name + "=", False)
		self.check.connect("toggled", self.on_toggled)
		self.entry = gtk.Entry()
		self.entry.set_text(options[0])
		self.entry.set_sensitive(False)
		
		self.pack_start(self.check, False, False)
		self.pack_start(self.entry, False, False)

	def on_toggled(self, widget, *args):
		self.entry.set_sensitive(self.check.get_active())

	def set_value(self, value):
		parsed_value = re.compile("([\w_]+)=?(.*)").match(value).groups()
		if not cmp(parsed_value[0], self.op_name):
			print "Warning: " + value + " can be not suitable for " + self.op_name
		self.entry.set_text(parsed_value[1])
		self.check.set_active(True)

	def get_value(self):
		if self.check.get_active():
			value = self.op_name
			if len(self.entry.get_text()) > 0:
				value = value + "=" + self.entry.get_text()
			return value
		else:
			return ""

class option_combo(gtk.HBox):

	def __init__(self, op_name, options, description):
		super(option_combo, self).__init__()
		self.op_name = op_name
		self.options = options
		self.description = description

		self.check = gtk.CheckButton(description + "\t" + op_name + "=", False)
		self.check.connect("toggled", self.on_toggled)

		self.combo = gtk.combo_box_new_text()
		self.n = 0
		for option in options:
			self.n = self.n + 1
			self.combo.append_text(option)
		self.combo.set_active(0)
		self.combo.set_sensitive(False)

		self.pack_start(self.check,False, False)
		self.pack_start(self.combo, False, False)

	def on_toggled(self, widget, *args):
		self.combo.set_sensitive(self.check.get_active())

	def set_value(self, value):
		parsed_value = re.compile("([\w_]+)=?(.*)").match(value).groups()
		i = 0
		while i < self.n:
			self.combo.set_active(i)
			print parsed_value[1], self.combo.get_active_text()
			if not cmp(parsed_value[1], self.combo.get_active_text()):
				self.check.set_active(True)
				return
			else:
				i = i + 1
		print "Warning: " + value + " is not suitable for " + self.op_name

	def get_value(self):
		if self.check.get_active():
			return self.op_name + "=" + self.combo.get_active_text()
		else:
			return ""
	
