# -*- coding: utf-8 -*-
# Copyright (c) 2013 Riverbed Technology, Inc.
#
# This software is licensed under the terms and conditions of the 
# MIT License set forth at:
#   https://github.com/riverbed/flyscript-portal/blob/master/LICENSE ("License").  
# This software is distributed "AS IS" as set forth in the License.

from rvbd_portal.apps.datasource.models import Column
from rvbd_portal.apps.report.models import Report, Section
import rvbd_portal.apps.report.modules.maps as maps
import rvbd_portal.apps.report.modules.yui3 as yui3

from rvbd_portal_profiler.datasources.profiler import GroupByTable

#
# Google Map example
#

# Google Map example
report = Report(title="Response Time Map", position=4)
report.save()

section = Section.create(report)

# Define a map and table, group by location
table = GroupByTable.create('maploc2', 'host_group', duration=60)

Column.create(table, 'group_name', iskey=True, label='Group Name')
Column.create(table, 'response_time', label='Resp Time', datatype='metric')
Column.create(table, 'network_rtt', label='Net RTT', datatype='metric')
Column.create(table, 'server_delay', label='Srv Delay', datatype='metric')
Column.create(table, 'avg_bytes', label='Response Time', datatype='metric')
Column.create(table, 'peak_bytes', 'Peak Bytes/s', datatype='bytes', units='B/s')
Column.create(table, 'avg_bytes_rtx', 'Avg Retrans Bytes/s', datatype='bytes', units='B/s')
Column.create(table, 'peak_bytes_rtx', 'Peak Retrans Bytes/s', datatype='bytes', units='B/s')

# Create a Map widget
maps.MapWidget.create(section, table, "Response Time Map", width=12, height=500)

# Create a Table showing the same data as the map
yui3.TableWidget.create(section, table, "Locations", width=12)
