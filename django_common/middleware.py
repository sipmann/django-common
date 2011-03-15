from django.conf import settings as django_settings
from django.http import HttpResponsePermanentRedirect


WWW = 'www'

class WWWRedirectMiddleware(object):
    """
    Redirect requests for example from http://www.mysirw.com/* to http://mysite.com/*
    """
    def process_request(self, request):
        if django_settings.IS_PROD and request.get_host() == '%s.%s' % (WWW, django_settings.DOMAIN_NAME):
            return HttpResponsePermanentRedirect('http://%s%s' % (django_settings.DOMAIN_NAME, request.get_full_path()))
        return None