from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Profile, UniversityProfile


@receiver(post_save, sender=User)
def create_related_profiles(sender, instance, created, **kwargs):
    if created:
        if instance.is_school_rep:
            Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_related_profiles(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()

