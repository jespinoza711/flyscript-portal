# Copyright (c) 2013 Riverbed Technology, Inc.
#
# This software is licensed under the terms and conditions of the 
# MIT License set forth at:
#   https://github.com/riverbed/flyscript-portal/blob/master/LICENSE ("License").  
# This software is distributed "AS IS" as set forth in the License.

from apps.report.models import Widget

import logging
logger = logging.getLogger(__name__)


class TableWidget(object):
    @classmethod
    def create(cls, section, table, title, width=6, rows=1000, height=300):
        w = Widget(section=section, title=title, rows=rows, width=width, height=height,
                   module=__name__, uiwidget=cls.__name__)
        w.compute_row_col()
        w.save()
        w.tables.add(table)

    @classmethod
    def process(cls, widget, data):
        return data