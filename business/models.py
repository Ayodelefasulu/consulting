from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

# dropdown options for industry field
INDUSTRY_CHOICES = [
    ('no', '-------'),
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

STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
    ('completed', 'Completed'),
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
        NONE = 'NO', '-------'
        CUSTOMER_PREFERENCE = 'CP', 'Customer Preference and Sentiment Analysis'
        PRICE_PREDICTION = 'PP', 'Price/Stock Prediction and Fluctuation Analysis'
        HUMAN_RESOURCES = 'HR', 'Human Resources Analysis'
        BUSINESS_PROPOSAL = 'BP', 'Business Proposal Writing'
        OTHERS = 'OT', 'Other Business Analytics Services'

    username = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='business_analytics'
    )
    business_name = models.CharField(max_length=250)
    industry = models.CharField(max_length=50, choices=INDUSTRY_CHOICES, default='no')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    type_of_service = models.CharField(
        max_length=2,
        choices=ServiceType.choices,
        default=ServiceType.NONE
    )
    project_description = models.TextField(max_length=5000, default='Describe in few words...')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-type_of_service']),
        ]

    def short_description(self):
        return (self.project_description[:100] + '...') if len(self.project_description) > 100 else self.project_description

    # Add a human-readable name for the admin
    # short_description.short_description = 'Project Description'

    def __str__(self):
        return f"{self.business_name}'s business"
