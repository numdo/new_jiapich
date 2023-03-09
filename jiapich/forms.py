
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
        fields = ['id','organization','representative','establishment_Date','location','postal_address','email_address','website'
                  ,'telephone_number','training','promoting','cooperation','safeguarding','social_impact','cultural_diversity'
                  ,'harmony_building','leadership','viability','sustainability','disaster_management','awards','candidate','recommendation'
                  ,'curriculum_vitae','supporting_document']
    # def __str__(self) 메소드는 객체를 문자열로 표현할 때 사용하는 함수이다.
