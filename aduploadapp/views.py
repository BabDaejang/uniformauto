from django.shortcuts import render

# Create your views here. 이제 뷰를 만들어 보자
from django.views.generic.list import ListView #제너릭 뷰로 만들 것이다, 뷰는 클래스(제너릭)뷰, 함수형 뷰가 있다.
from django.views.generic.edit import CreateView #클래스(제너릭)뷰 중 CreateView를 추가한다.
# DetailView 를 만들어야 하니까 이것이 뭘 의미하는지 추가해 주어야 한다.
from django.views.generic.detail import DetailView # 장고의 제너릭 뷰...여기서 detail 에 대한 내부 정의가 있었고,
                                                   # 여기서 DetailView 라는 걸 임포트 했다
from django.urls import reverse_lazy # reverse_lazy 라는 걸 쓴다.... 데이터 입력 완료 후 redirect 할 곳을 찾는건가
from .models import Aduploadapp #Aduploadapp 에 필요한 모델이다.


class AduploadappListView(ListView): # class Adupload의 ListView 란 뜻으로 만들었다
    model = Aduploadapp # db에 등록된 Aduploadapp 데이터 전체를 반환하여 준다

class AduploadappCreateView(CreateView): #5행에서 임포트한 CreateView를 받는 클래스를 만든다.
    model = Aduploadapp # 이걸 만들고 다시 aduploadapp/urls.py 를 수정해준다.
    fields = ['site_name','url'] # 데이터를 입력(추가)하거나 수정 뷰인 경우, 
                                 # 대상 필드를 지정해야 한다는 의미 (field=[]추가)
    success_url = reverse_lazy('list') # 성공 후 redirect url 을 지정한다는 뜻이다
    template_name_suffix = "_create" # 추가해준다. create 과 update 는 모델명_form.html을 불러오기 때문에
                                     #suffix 변경 하여 사용한다고 한다 ???읭??? 뭔소리야 이게

class AduploadappDetailView(DetailView): # 한 개의 object를 반환한다는 뜻이다... DetailView 를 임포트 안했다.
# urls.py 를 바꿨으니 그에 해당하는 것이 어떻게 보이는지 views.py에서 class를 만들어 준다.
    model = Aduploadapp # class AduploadappDetailView 에서 돌아가는 구문이므로 들여쓰기 놓치지 말자
    # 자 이제 AduploadappDetailView 를 만들었으니 templates 에서 html 을 만들자



