from datetime import datetime

from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from django.core.urlresolvers import reverse

from users.models import UserTicket


class UserMiddleware(MiddlewareMixin):

    def process_request(self, request):

        paths = ['/users/login/', '/users/register/', '/']
        if request.path in paths:
            return None

        ticket = request.COOKIES.get('ticket')

        if not ticket:
            return HttpResponseRedirect(reverse('users:login'))

        user = UserTicket.objects.filter(ticket=ticket).first()
        if not user:
            return HttpResponseRedirect(reverse('users:login'))

        if user.out_time.replace(tzinfo=None) < datetime.now():
            user.delete()
            return HttpResponseRedirect(reverse('users:login'))

        request.user = user.user
