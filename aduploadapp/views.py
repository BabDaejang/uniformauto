from django.shortcuts import render

# Create your views here. 이제 뷰를 만들어 보자
from django.views.generic.list import ListView #제너릭 뷰로 만들 것이다, 뷰는 클래스(제너릭)뷰, 함수형 뷰가 있다.
from django.views.generic.edit import CreateView #클래스(제너릭)뷰 중 CreateView를 추가한다.
from .models import Aduploadapp #Aduploadapp 에 필요한 모델이다.


class AduploadappListView(ListView): # class Adupload의 ListView 란 뜻으로 만들었다
    model = Aduploadapp # db에 등록된 Aduploadapp 데이터 전체를 반환하여 준다

class AduploadappCreateView(CreateView): #5행에서 임포트한 CreateView를 받는 클래스를 만든다.
    model = Aduploadapp # 이걸 만들고 다시 aduploadapp/urls.py 를 수정해준다.
    fields = ['site_name','url'] #데이터를 입력(추가)하거나 수정 뷰인 경우, 
                                #대상 필드를 지정해야 한다는 의미 (field=[]추가)
    template_name_suffix = "_create" #추가해준다.



