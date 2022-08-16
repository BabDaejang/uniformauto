#-*-coding:utf-8 -*-

# import random #랜덤한 데이터를 만들어 보자. 랜덤 데이터를 만들어서 엑셀 형식으로 저장한다.
# import openpyxl #엑셀을 제어하기 위한 openpyxl 임포트

## 다시 생각해보니 csv 파일로 일단 만들고 다 만들어진 파일을 엑셀로 변화하는게 낫겠다
# csv 파일 형식으로 랜덤하게 만든다

# 학년은 동일하다 (반복하여 삽입)
# 파일이 만들어지는 순서대로 반이 만들어진다
# 번이 1~25에 다다르면 반이 바뀐다

### https://www.datasciencemadesimple.com/generate-random-number-in-pandas-python-2/ 이 방법으로 랜덤하게 만들자

import numpy as np
import pandas as pd
import random

fname = "김이박최정강조윤장임한오서신권황안송전홍유고문양손배조" #첫번째 성
name1 = "명영정광중상재경종병진성제준종승민우예현지동순서은수윤태" #중간 이름
name2 = "자순숙희미영경은정주연람진서빈지현원은재진호수훈준건호철길일남정형" #마지막 이름

howmanybanbok = 200 #몇 번 반복할 것인지 정하는 변수

def random_name():  #random_name()이라는 함수를 만듬. 이 함수는 random 을 써서 위의 이름 변수들을 랜덤 선택하여 추가해 줄것임
    created_name=""
    created_name += random.choice(fname)
    created_name += random.choice(name1)
    created_name += random.choice(name2)

    return created_name

namelist = [] # 이름이 기록될 리스트를 하나 만들어주자

for i in range(howmanybanbok):  # for  문을 통해 random_name()이라는 함수를 반복하자, 몇 번 할 것인지는 위에 있고
    rname = random_name() ## random_name() 이라는 함수를 한다. 근데 결과물을 차곡차곡 쌓고 싶은데? append() 를 써보자.
    ### append() 함수 문제를 해결하기 위해 append() 함수 안에 직접 넣었다. ~~취소~~
    ### append() 함수 문제를 해결하기 위해 rname = 이라는 변수를 만들고, 그 변수의 결과물을 추가하게 하였다. ~~실패~~
    #### 위의 ###가 문제가 아니라 애당초 fname name1 name2 의 쉼표가 문제라는 걸 확인하였다.
    namelist.append(rname) # random_name()으로 만들어진 것을 네임 리스트에 추가해 달라는 말이다.


# print(namelist) #잘 되었는지 테스트 해보자






