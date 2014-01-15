from django import forms

from apps.datasource.forms import fields_add_time_selection
from apps.datasource.modules.analysis import AnalysisTable
from apps.datasource.models import TableField, Table, Column
from libs.fields import Function

from apps.report.models import Report, Section
from apps.report.modules import raw

from . import criteria_functions as funcs

report = Report(title='Criteria Post Process Errors' )
report.save()

section = Section(report=report, title='Section 0')
section.save()

table = AnalysisTable.create('test-criteria-postprocess', tables={}, 
                             func = funcs.analysis_echo_criteria)

TableField.create('error', 'Error type', table)    
TableField.create('x', 'X Value', table,
                  hidden=True,
                  post_process_func = Function(funcs.postprocesserrors_compute))
    
Column.create(table, 'key', 'Key', iskey=True, isnumeric=False)
Column.create(table, 'value', 'Value', isnumeric=False)

raw.TableWidget.create(section, table, 'Table')