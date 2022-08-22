# 여기서 aduploadapp 의 하위 urls 를 컨프론트 해준다 ?

import imp
from multiprocessing.spawn import import_main_path
from django.urls import path
# from .views import  // 이건 조만간 해야 한다.
from .views import AduploadDeleteView, AduploadappCreateView, AduploadappListView #일단 AduploadappListView 를 불러온다
from .views import AduploadappDetailView # 아직 AduploadappDetailView 가 정의되지 않았다. 일단 url 과 urlpatterns 를 만들었다.
from .views import AduploadappUpdateView


urlpatterns = [
    # as_view() : 클래스형 뷰를 내부적으로 함수형으로 처리한단다.
    # name : 결과 페이지로 보여 줄 템플릿 파일에서 해당 URL을 호출할 때 쓰는 별칭
    path('',AduploadappListView.as_view(), name='list'), #http://127.0.0.1/Aduploadapp/ list ?
    path('add/',AduploadappCreateView.as_view(), name='add'), #http://127.0.0.1:8000/Aduploadapp/add
    path('detail/<int:pk>/', AduploadappDetailView.as_view(), name='detail'), 
    #http://127.0.0.1:8000/Aduploadapp/detail/1 ... <int:pk>를 써서 정수로 입력한 것의 번호가 차곡차곡 
    ## 왜 에러가 나오나 했더니 templates/aduploadapp_update.html 은 있는데, 여기 urls.py 에서 path 를 지정안함 당장해주자
    path('update/<int:pk>/', AduploadappUpdateView.as_view(), name='update'),
    # AduploadappUpdateView 를 만들기 위해 views 에서 임포트 해야 한다. 그것도 추가하자
    # 쌓이게 함 이제 views.py 를 바꾸자
    path('delete/<int:pk>/', AduploadDeleteView.as_view(), name='delete'),
]