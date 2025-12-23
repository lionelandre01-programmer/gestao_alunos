from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver

@receiver(post_migrate)
def criar_grupos(sender, **kwargs):
    from .admin import grupos
    grupos()