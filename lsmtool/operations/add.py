#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This operation implements adding of sources to the sky model
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

import logging

logging.debug('Loading ADD module.')


def run(step, parset, LSM):

    from tableio import inputColumnNames

    outFile = parset.getString('.'.join(["LSMTool.Steps", step, "OutFile"]), '' )
    colNamesVals = {}
    for colName in inputColumnNames:
        colNamesVals[colName] = parset.getString('.'.join(["LSMTool.Steps",
            step, inputColumnNames[colName]]), '' )

    result = add(LSM, colNamesVals)

    if outFile != '':
        LSM.write(outFile, clobber=True)

    return result


def add(LSM, colNamesVals):

    LSM.setRowValues(colNamesVals)
    return 0
