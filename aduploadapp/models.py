from django.db import models

# Create your models here.
# 여기선 데이타베이스를 모델링 하는 곳이다. ... pyxlsx 파이 엑셀로부터 정보를 받은 것을
# 여기 어딘가 모델에 저장을 해야 할 것이다.
# class Url(models.Model):
#     link = models.URLField(max_length=200)
#     new_link = models.URLField(default="")

from django.db import models

class Aduploadapp(models.Model):
    site_name = models.CharField(max_length=200)
    url = models.URLField(verbose_name='Site URL') #Site URL 이 뭐지? .. 아 별병을 설정함. 이걸로 보인다.

    #모델의 클래스 인스턴스 생성시 __str__ 로 출력되도록 해본다... 왜지?
    def __str__(self):
        return '클래스 인스턴스 이름: ' + self.site_name + ', 주소(URL) : ' + self.url    
    # 자 이제 update 관련된 모델을 만들어야 한다. get_absolute_url() 함수로 어떻게든 진행되게 만든다

    def get_abolute_url(self):
        return reverse('detail', kwargs={'pk':self.id})
        #뭔소린지 모르겠지만, args = [str(self.id)] or kwargs = {'pk':self.id} 란뜻이다
