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

# howmanybanbok = 200 #몇 번 반복할 것인지 정하는 변수 // 학번을 만들었기 때문에 howmanybanbok이 필요 없게 되었다.

def random_name():  #random_name()이라는 함수를 만듬. 이 함수는 random 을 써서 위의 이름 변수들을 랜덤 선택하여 추가해 줄것임
    create_name=""
    create_name += random.choice(fname)
    create_name += random.choice(name1)
    create_name += random.choice(name2)

    return create_name

## 이름을 만들기로 하였으나, 만들어진 bunho 의 횟수만큼 반복하는 것으로 바꾸고 싶기 때문에 코드를 밑으로 뺐다.

# 이제 학번을 만들기로 한다. 랜덤한 숫자를 집어넣자 어차피 테스트용이고 귀찮으니까... 하려다가 그냥 정식으로 만들었다.
bunho = [] # 학번이 기록될 리스트를 만들자
ban = ['01','02','03','04','05','06','07','08','09','10']  ## zfill() 함수를 사용하면 된다. 귀찮으니 그냥 반에다 넣지
# 반의 번호를 만들기 위해 순서대로 번호를 만들어주자
bunbunbun = list(range(1,26)) # 1부터 25 까지 숫자를 만들어서 리스트로 bunbunbun에 저장
banbun = [] # 번호를 저장할 반번이란 리스트를 만들자
for x in bunbunbun: # bunbunbun의 인수를 하나씩 꺼내서 x로 배당해서 반복한다
    xxxx = str(x).zfill(2) #zfill() 함수를 써서, 0$ 이런 모양으로 만듬. 만들어서 banbun 변수에 저장 
    banbun.append(xxxx) ## 이제 banbun 이라는 리스트에 0$ 형식으로 01~25까지가 만들어졌다
## 이제 banbun 을 이용해서 bunho 를 만들자 / 목표는 3 + ban + banbun 을 순차적으로 만들어 bunho 에 넣는 것이다.
## banbun 을 꺼내서 ban 에 결합시킨다. ban 을 하나씩 꺼내야 한다.
for i in ban:
    # print(i) for 문이 잘 작동하는지 테스트
    for ii in banbun:
        hapche = "3"+i+ii
        bunho.append(hapche)

### 이제 bunho 에 학번이 차례로 쌓이게 되었다. ... howmanywork 가 필요 없겠다. 학번만큼의 이름만 만들면 되니까

namelist = [] # 이름이 기록될 리스트를 하나 만들어주자

for i in range(len(bunho)):  # for  문을 통해 random_name()이라는 함수를 반복하자, 몇 번 할 것인지는 위에 있었다.
    ## 그러나 bunho 만큼만 만들 것이므로 이 함수를 밑으로 빼도록 하겠다.
    rname = random_name() ## random_name() 이라는 함수를 한다. 근데 결과물을 차곡차곡 쌓고 싶은데? append() 를 써보자.
    ### append() 함수 문제를 해결하기 위해 append() 함수 안에 직접 넣었다. ~~취소~~
    ### append() 함수 문제를 해결하기 위해 rname = 이라는 변수를 만들고, 그 변수의 결과물을 추가하게 하였다. ~~실패~~
    #### 위의 ###가 문제가 아니라 애당초 fname name1 name2 의 쉼표가 문제라는 걸 확인하였다.
    namelist.append(rname) # random_name()으로 만들어진 것을 namelist에 추가해 달라는 말이다.

print(namelist, bunho) # 여기까지 잘 되었는지 테스트 하고 git push 하겠다



