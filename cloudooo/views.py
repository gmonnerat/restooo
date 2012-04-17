from djangorestframework.views import View
from django.http import HttpResponse
from xmlrpclib import ServerProxy
from base64 import encodestring, decodestring
from django.conf import settings
import cStringIO as StringIO

def get_server_proxy(host):
  return ServerProxy(host)

class CloudoooView(View):

    def get(self, request=None):
        return 
    def post(self, request=None):
        file = request.FILES.values()[0]
        filename = file.name
        server_proxy = get_server_proxy(settings.CLOUDOOO_URL)
        try:
          data = server_proxy.convertFile(encodestring(file.read()), "odt", "html")
        except:
          return HttpResponse("Cloudooo server not available")
        document_in_memory = StringIO.StringIO()
        document_in_memory.write(decodestring(data))
        document_in_memory.seek(0)
        response = HttpResponse(document_in_memory.read())
        response['Content-Disposition'] = 'attachment; filename=%s.pdf' % filename
        response['Content-Length'] = document_in_memory.tell()
        return response
