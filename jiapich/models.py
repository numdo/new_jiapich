
# Create your models here.
# pip install django-taggit
# pip install django-widget-tweaks
# pip install pillow
# pip install pytz
# pip install -U pip setuptools wheel
# pip install pyopenssl ndg-httpsclient pyasn1

from django.db import models


# 모델 : 테이블 정의
class submitForm(models.Model):
    # PK(Primary Key)는 클래스에 지정해주지 않아도, 장고는 id라는 칼럼을 자동으로 만들어 준다.
    organization = models.CharField('organization', max_length=256)
    representative = models.CharField('representative', max_length=256)
    establishment_Date = models.TextField('CONTENT')
    location = models.CharField('location', max_length=256)
    postal_address = models.CharField('postal_address', max_length=256)
    email_address = models.CharField('email_address', max_length=256)
    website = models.CharField('website', max_length=256)
    telephone_number = models.CharField('telephone_number', max_length=256)
    training = models.TextField('training')
    promoting = models.TextField('promoting')
    cooperation = models.TextField('cooperation')
    safeguarding = models.TextField('safeguarding')
    social_impact = models.TextField('social_impact')
    cultural_diversity = models.TextField('cultural_diversity')
    harmony_building = models.TextField('harmony_building')
    leadership = models.TextField('leadership')
    viability = models.TextField('viability')
    sustainability = models.TextField('sustainability')
    disaster_management = models.TextField('disaster_management')
    awards = models.TextField('awards')
    candidate = models.TextField('candidate')
    recommendation = models.CharField('recommendation',max_length=256)
    curriculum_vitae = models.CharField('curriculum_vitae',max_length=256)
    supporting_document = models.CharField('supporting_document',max_length=256)
    created_time = models.DateTimeField('created_time', auto_now_add=True)
    updated_time = models.DateTimeField('updated_time', auto_now=True)
    delete = models.BooleanField('delete',default=False)

    def __str__(self):
        return self.organization

    class Meta:
        app_label = 'jiapich'