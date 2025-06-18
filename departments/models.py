from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey('auth.User',
                                related_name='departments',
                                on_delete=models.CASCADE,
                                null=True,  # ✅ this makes it optional
                                blank=True,  # ✅ optional in forms
                                )

    class Meta:
        ordering = ['-id']