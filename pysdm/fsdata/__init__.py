options = {}
defaults = {}

import default
options["default"] = default.options
defaults["default"] = default.defaults

import reiserfs
options["reiserfs"] = reiserfs.options
defaults["reiserfs"] = reiserfs.defaults

import swap
options["swap"] = swap.options
defaults["swap"] = swap.defaults
