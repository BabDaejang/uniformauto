from django.contrib import admin
from .models import Aduploadapp # models.py 에서 class Aduploadapp 을 정의했다. 이걸 임포트 시켜준다.

admin.site.register(Aduploadapp) # class Aduploadapp 을 등록시켰고, 이제 어드민 계정으로 관리가 가능해졌다.

# Register your models here.
