# input API arg spec json
# output ansible module option documentation skeleton
#
from __future__ import absolute_import, division, print_function
__metaclass__ = type

import sys
import json
import yaml


arg_spec = json.load(sys.stdin)


def option_doc_from_arg_spec(spec, append_spec={}):
    option_doc = {}
    for spec_name, spec_item in spec.items():
        if spec_name in ["options", "suboptions"]:
            option_doc[spec_name] = option_doc_from_arg_spec(spec_item, {"description": ""})
        else:
            option_doc[spec_name] = spec_item
        # if the spec item is a dict, it is a option or suboption, so add append spec to it
        if type(option_doc[spec_name]) is dict:
            option_doc[spec_name].update(append_spec)
    return option_doc


module_arg_docs = {}
for spec_name, spec in arg_spec.items():
    module_arg_docs[spec_name] = option_doc_from_arg_spec(spec)

sys.stdout.write(yaml.dump(module_arg_docs))
