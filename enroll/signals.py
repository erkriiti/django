from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, pre_save, pre_delete, post_init, post_save, post_delete, pre_migrate, post_migrate
from django.core.signals import request_started, request_finished, got_request_exception
from django.db.backends.signals import connection_created

@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
 print("----------------------------")
 print("Logged-in Signal... Run Intro..")
 print("User:", user)
@receiver(user_logged_out, sender=User)
def log_out(sender, request, user, **kwargs):
 print("----------------------------")
 print("Logged-out Signal... Run Outro..")
 print("User:", user)

