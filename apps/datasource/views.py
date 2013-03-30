# Copyright (c) 2013 Riverbed Technology, Inc.
#
# This software is licensed under the terms and conditions of the 
# MIT License set forth at:
#   https://github.com/riverbed/flyscript-portal/blob/master/LICENSE ("License").  
# This software is distributed "AS IS" as set forth in the License.


# Create your views here.
import json
import datetime

from django.http import HttpResponse

from apps.datasource.models import Table

import logging
logger = logging.getLogger(__name__)


def poll(request, table_id):
    try:
        ts = request.GET['ts']
    except:
        ts = 1
    d = Table.objects.get(id=int(table_id))
    job = d.poll(ts)

    if not job.done():
        # job not yet done, return an empty data structure
        logger.debug("poll: Not done yet, %d%% complete" % job.progress)
        resp = job.json()
    else:
        resp = job.json(data=job.data())
        logger.debug("poll: Job complete")
        job.delete()

    dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime.datetime) else None
    return HttpResponse(json.dumps(resp, default=dthandler))

