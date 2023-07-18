from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver (user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    # print("----------")
    # print("logged-in signal.. RUN intro")
    ip = request.META.get('REMOTE_ADDR')#code for fetching ip address in django documentatio.
    # print("Client Id:",id)
    request.session['ip']=ip
