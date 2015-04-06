import pytz

from django.utils import timezone


class TimezoneMiddleware(object):
    def process_request(self, request):
        # Right now we force the west coast TZ, but I'm keeping this extra
        # code here in case I decide to do it the right way someday
        request.session['django_timezone'] = 'America/Los_Angeles'
        tzname = request.session.get('django_timezone')
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()
