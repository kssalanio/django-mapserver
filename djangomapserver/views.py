import os

from django.http import HttpResponse
from django.http import Http404

import models
import ows

def wms_endpoint(request, mapfile=None):
    """
    WMS endpoint.
    """

    if mapfile is None:
        try:
            m = models.MapObj.objects.all()[0]
        except IndexError:
            raise Http404
    else:
        try:
            m = models.MapObj.objects.get(name=mapfile)
        except models.MapObj.DoesNotExist:
            raise Http404
    print('map name: {}'.format(m.name))
    print('map projection: {}'.format(m.projection))
    map_obj = m.build()
    # TODO: fix this, mapfile should be saved to a correct location
    map_obj.save(os.path.expanduser("~/Desktop/mapfile_teste.map"))
    result, ct = ows.process_request(request, map_obj)
    content_type = ows.get_content_type(ct)
    response = HttpResponse(content_type=content_type)
    response.write(result)
    return response


