# -*- coding: utf-8 -*-
# Copyright (c) 2013 Riverbed Technology, Inc.
#
# This software is licensed under the terms and conditions of the 
# MIT License set forth at:
#   https://github.com/riverbed/flyscript-portal/blob/master/LICENSE ("License").  
# This software is distributed "AS IS" as set forth in the License.

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from apps.datasource.models import Device, Column
from apps.report.models import Report, Table
from apps.datasource.modules.shark import SharkTable, create_shark_column
import apps.report.modules.yui3 as yui3

#### Customize devices and authorization here

tm08 = Device.objects.get(name="tm08-1")
v10 = Device.objects.get(name="vdorothy10")

#
# Define a Shark Report and Table
#
report = Report(title="Shark", position=3)
report.save()

t = SharkTable.create(name='Packet Traffic', devicename=v10, view='jobs/Flyscript-tests-job', duration=10, aggregated=False)


create_shark_column(t, 'ip_src', label='Source IP', iskey=True, extractor='ip.src')
create_shark_column(t, 'ip_dst', label='Dest IP', iskey=True, extractor='ip.dst')
create_shark_column(t, 'generic_packets', label='Packets', iskey=False, extractor='generic.packets', operation='sum')

#foo()

yui3.TableWidget.create(report, t, "Shark Packets (last 10 minutes)", width=12)

t = SharkTable.create(name='MicroburstsTotal', devicename=v10, view='jobs/Flyscript-tests-job', duration=10, aggregated=True)

create_shark_column(t, 'max_microburst_1ms_packets', extractor='generic.max_microburst_1ms.packets', operation='max', label='Microburst 1ms Pkts')
create_shark_column(t, 'max_microburst_10ms_packets', extractor='generic.max_microburst_10ms.packets', operation='max',  label='Microburst 10ms Pkts')
create_shark_column(t, 'max_microburst_100ms_packets', extractor='generic.max_microburst_100ms.packets', operation='max',  label='Microburst 100ms Pkts')

yui3.TableWidget.create(report, t, "Microburst Packets (last 10 minutes)", width=12)


t = SharkTable.create(name='MicroburstsTime', devicename=v10, view='jobs/Flyscript-tests-job', duration=10, aggregated=False)

create_shark_column(t, 'time', extractor='generic.absolute_time', iskey=True, label='Time (ns)')
create_shark_column(t, 'max_microburst_1ms_packets', extractor='generic.max_microburst_1ms.packets', operation='max', label='Microburst 1ms Pkts')

yui3.TimeSeriesWidget.create(report, t, "Microburst Packets Timeseries (last 10 minutes)", width=12)

#
