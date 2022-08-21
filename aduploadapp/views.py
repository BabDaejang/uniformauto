from django.shortcuts import render

# Create your views here. 이제 뷰를 만들어 보자
from django.views.generic.list import ListView #제너릭 뷰로 만들 것이다, 뷰는 클래스(제너릭)뷰, 함수형 뷰가 있다.
from .models import Aduploadapp #Aduiploadapp 에 필요한 모델이다.

class AduploadappListView(ListView): # class Adupload의 ListView 란 뜻으로 만들었다
    model = Aduploadapp # db에 등록된 Aduploadapp 전체를 반환하여 준다
