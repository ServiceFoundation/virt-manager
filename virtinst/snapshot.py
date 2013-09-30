#
# Copyright 2013 Red Hat, Inc.
# Cole Robinson <crobinso@redhat.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free  Software Foundation; either version 2 of the License, or
# (at your option)  any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA.

from virtinst import util
from virtinst.xmlbuilder import XMLBuilder, XMLProperty


class DomainSnapshot(XMLBuilder):
    @staticmethod
    def find_free_name(vm, collidelist):
        return util.generate_name("snapshot", vm.snapshotLookupByName,
                                  sep="", start_num=1, force_num=True,
                                  collidelist=collidelist)

    _XML_ROOT_NAME = "domainsnapshot"
    _XML_PROP_ORDER = ["name", "description", "creationTime"]

    name = XMLProperty("./name")
    description = XMLProperty("./description")
    state = XMLProperty("./state")
    creationTime = XMLProperty("./creationTime", is_int=True)
    parent = XMLProperty("./parent/name")

    # Missing bits:
    # <memory> @type and @file
    # <disks> block which has a psuedo VM disk device
    # <domain> block which tracks the snapshot guest XML
    # <active> which should list active status for an internal snapshot


    ##################
    # Public helpers #
    ##################

    def validate(self):
        if not self.name:
            raise RuntimeError(_("A name must be specified."))
