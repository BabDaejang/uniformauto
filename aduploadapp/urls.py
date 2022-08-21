# 여기서 aduploadapp 의 하위 urls 를 컨프론트 해준다 ?

import imp
from multiprocessing.spawn import import_main_path
from django.urls import path
# from .views import  // 이건 조만간 해야 한다.
from .views import AduploadappCreateView, AduploadappListView #일단 AduploadappListView 를 불러온다


urlpatterns = [
    # as_view() : 클래스형 뷰를 내부적으로 함수형으로 처리한단다.
    # name : 결과 페이지로 보여 줄 템플릿 파일에서 해당 URL을 호출할 때 쓰는 별칭
    path('',AduploadappListView.as_view(), name='list'), #http://127.0.0.1/Aduploadapp/ list ?
    path('add/',AduploadappCreateView.as_view(), name='add'), #http://127.0.0.1:8000/Aduploadapp/add
]