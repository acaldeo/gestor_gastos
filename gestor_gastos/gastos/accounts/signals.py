from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from django.dispatch import receiver

@receiver(post_save, sender=User)
def add_user_to_gastos_group(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='Usuarios Gastos')
        instance.groups.add(group)
        instance.is_staff = True  # Necesario para acceder al admin
        instance.save()
