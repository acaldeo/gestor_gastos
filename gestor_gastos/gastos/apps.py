from django.apps import AppConfig
from django.db.models.signals import post_save

class GastosConfig(AppConfig):
    name = 'gastos'

    def ready(self):
        from django.contrib.auth.models import User, Group
        from django.db.models.signals import post_save

        def add_to_user_group(sender, instance, created, **kwargs):
            if created and not instance.is_superuser:
                group, _ = Group.objects.get_or_create(name='usuarios_gastos')
                instance.groups.add(group)

        post_save.connect(add_to_user_group, sender=User)
