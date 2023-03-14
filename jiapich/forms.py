# Create your forms here.
# pip install django-taggit
# pip install django-widget-tweaks
# pip install pillow
# pip install pytz
# pip install -U pip setuptools wheel
# pip install pyopenssl ndg-httpsclient pyasn1

from django import forms
from jiapich.models import submitForm


# 모델 : 테이블 정의
class Form(forms.ModelForm):
    # PK(Primary Key)는 클래스에 지정해주지 않아도, 장고는 id라는 칼럼을 자동으로 만들어 준다.
    class Meta:
        model = submitForm
        fields = ['id', 'organization', 'representative', 'establishment_Date', 'continent', 'nation', 'postal_address',
                  'email_address', 'website'
            , 'telephone_number', 'training', 'promoting', 'cooperation', 'safeguarding', 'social_impact',
                  'cultural_diversity'
            , 'harmony_building', 'leadership', 'viability', 'sustainability', 'disaster_management', 'awards',
                  'candidate', 'recommendation'
            , 'curriculum_vitae', 'supporting_document']

class pageStep1(forms.ModelForm):
    class Meta:
        model = submitForm
        fields = ['organization', 'representative', 'establishment_Date', 'continent', 'nation', 'postal_address',
                  'email_address', 'website']


class pageStep2(forms.ModelForm):
    class Meta:
        model = submitForm
        fields =['telephone_number','training','promoting','cooperation','safeguarding']

class pageStep3(forms.ModelForm):
    class Meta:
        model = submitForm
        fields = ['social_impact','cultural_diversity','harmony_building']

class pageStep4(forms.ModelForm):
    class Meta:
        model = submitForm
        fields = ['leadership','viability','sustainability','disaster_management']

class pageStep5(forms.ModelForm):
    class Meta:
        model = submitForm
        fields = ['awards','candidate']

class pageStep6(forms.ModelForm):
    class Meta:
        model = submitForm
        fields = []