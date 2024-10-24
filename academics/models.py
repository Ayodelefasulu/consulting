from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

# dropdown options for status field
STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
    ('completed', 'Completed'),
]
# dropdown options for type-of-service field
SERVICE_CHOICES = [
    ('no', '-------'),
    ('full_project', 'Full Project Dissertation/Thesis'),
    ('proposal', 'Project Proposal'),
    ('data_analysis', 'Data Analysis and Interpretation'),
    ('other', 'Other Academic Services'),
]

class Academic(models.Model):
    class AcademicLevel(models.TextChoices):
        NONE = 'NO', '-------'
        DIPLOMA = 'DP', 'Diploma'
        UNDERGRADUATE = 'UG', 'Undergraduate'
        GRADUATE = 'GR', 'Graduate'
        POST_GRADUATE = 'PG', 'Post-Graduate'
        DOCTORAL = 'DR', 'Doctoral'
        POSTDOCTORAL = 'PD', 'Postdoctoral'


    username = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='academics'
    )
    academic_level = models.CharField(
        max_length=2,
        choices=AcademicLevel.choices,
        default=AcademicLevel.NONE,
    )
    name_of_institution = models.CharField(max_length=500)
    type_of_service = models.CharField(
        max_length=50,
        choices=SERVICE_CHOICES,
        default='no',
    )
    project_title = models.CharField(max_length=500)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-type_of_service']),
        ]

    def __str__(self):
        return self.project_title
