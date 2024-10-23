from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

# dropdown options for sector category
SECTOR_CATEGORY_CHOICES = [
    ('no', '-------'),
    ('ngo', 'Non-governmental organization'),
    ('npo', 'Non-profit organization'),
    ('govs', 'Governmental organization'),
    ('others', 'Others'),
]

# dropdown options for status field
STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
    ('completed', 'Completed'),
]

# The main Public model
class Public(models.Model):
    class ServiceType(models.TextChoices):
        NONE = 'NO', '-------'
        PROJECT_MANAGEMENT = 'PM', 'Project Management'
        RESEARCH_POLICY = 'RP', 'Research and Policy Development'
        DATA_ANALYSIS = 'DA', 'Data Analysis and Management'
        MONITORING_EVALUATION = 'ME', 'Monitoring and Evaluation'
        STAKEHOLDER_ENGAGEMENT = 'SE', 'Stakeholder Engagement and Advocacy'
        CAPACITY_BUILDING = 'CB', 'Capacity Building and Training'
        OTHERS = 'OT', 'Others'

    username = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='public_sector'
    )

    category = models.CharField(max_length=100, choices=SECTOR_CATEGORY_CHOICES, default='no')
    type_of_service = models.CharField(
        max_length=2,
        choices=ServiceType.choices,
        default=ServiceType.NONE
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    project_title = models.CharField(max_length=500)
    project_description = models.TextField(max_length=5000, default='Describe in few words...')
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

