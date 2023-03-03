from django.db import forms

# Create your forms here.
# pip install django-taggit
# pip install django-widget-tweaks
# pip install pillow
# pip install pytz
# pip install -U pip setuptools wheel
# pip install pyopenssl ndg-httpsclient pyasn1

from django import forms


# 모델 : 테이블 정의
class Post(forms.Form):
    # PK(Primary Key)는 클래스에 지정해주지 않아도, 장고는 id라는 칼럼을 자동으로 만들어 준다.
    organization = forms.CharField(label='organization', max_length=256)
    representative = forms.CharField(label='representative', max_length=256)
    establishment_Date = forms.TextInput()
    location = forms.CharField(label='location', max_length=256)
    Postal_address = forms.CharField(label='Postal_address', max_length=256)
    email_address = forms.CharField(label='email_address', max_length=256)
    website = forms.CharField(label='website', max_length=256)
    telephone_number = forms.CharField(label='label=telephone_number', max_length=256)
    training = forms.TextInput()
    promoting = forms.TextInput()
    cooperation = forms.TextInput()
    safeguarding = forms.TextInput()
    social_impact = forms.TextInput()
    cultural_diversity = forms.TextInput()
    harmony_building = forms.TextInput()
    leadership = forms.TextInput()
    viability = forms.TextInput()
    sustainability = forms.TextInput()
    disaster_management = forms.TextInput()
    awards = forms.TextInput()
    candidate = forms.TextInput()
    recommendation = forms.CharField(label='Recommendation',max_length=256)
    curriculum_vitae = forms.CharField(label='curriculum_vitae',max_length=256)
    supporting_document = forms.CharField(label='supporting_document',max_length=256)
    created_time = forms.DateTimeField(label='created_time', auto_now_add=True)
    updated_time = forms.DateTimeField(label='updated_time', auto_now=True)
    delete = forms.BooleanField(label='delete')


    # def __str__(self) 메소드는 객체를 문자열로 표현할 때 사용하는 함수이다.
