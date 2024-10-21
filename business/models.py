from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

# dropdown options for industry field
INDUSTRY_CHOICES = [
    ('agriculture', 'Agriculture'), ('aerospace', 'Aerospace'),
    ('automotive', 'Automotive'), ('chemicals', 'Chemicals'),
    ('construction', 'Construction'), ('manufacturing', 'Manufacturing'),
    ('information_technology', 'Information Technology'), ('cybersecurity', 'Cybersecurity'),
    ('biotechnology', 'Biotechnology'), ('healthcare', 'Healthcare'),
    ('pharmaceuticals', 'Pharmaceuticals'), ('medical_devices', 'Medical Devices'),
    ('banking_finance', 'Banking and Finance'), ('insurance', 'Insurance'),
    ('real_estate', 'Real Estate'), ('retail', 'Retail'),
    ('food_beverage', 'Food and Beverage'), ('hospitality', 'Hospitality'),
    ('energy', 'Energy and Renewable Energy'), ('environmental_services', 'Environmental Services and Sustainability'),
    ('media', 'Media'), ('entertainment', 'Entertainment'),
    ('gaming', 'Gaming'), ('sports', 'Sports'),
    ('transportation', 'Transportation'), ('logistics', 'Logistics'),
    ('travel_tourism', 'Travel and Tourism'), ('education', 'Education'),
    ('others', 'Others'),
]


# The main Business model
class Business(models.Model):

    """
    class Industry(models.TextChoices):
        AGRICULTURE = 'AG', 'Agriculture'
        AEROSPACE = 'AE', 'Aerospace'
    """

    # class-based dropdown options for type-of-service field
    class ServiceType(models.TextChoices):
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
        related_name='business_analytics'
    )
    business_name = models.CharField(max_length=250)
    industry = models.CharField(max_length=50, choices=INDUSTRY_CHOICES, default='agriculture')
    type_of_service = models.CharField(
        max_length=2,
        choices=ServiceType.choices,
        default=ServiceType.PROJECT_MANAGEMENT
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-type_of_service']),
        ]

    def __str__(self):
        return f"{self.business_name}'s business"
