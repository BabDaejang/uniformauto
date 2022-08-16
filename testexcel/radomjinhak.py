#-*-coding:utf-8 -*-

# import openpyxl #엑셀을 제어하기 위한 openpyxl 임포트

## 다시 생각해보니 csv 파일로 일단 만들고 다 만들어진 파일을 엑셀로 변화하는게 낫겠다
# csv 파일 형식으로 랜덤하게 만든다

### https://www.datasciencemadesimple.com/generate-random-number-in-pandas-python-2/ 이 방법으로 랜덤하게 만들자

# import numpy as np ## 일단 넘파이는 안쓰니까 뺀다
import pandas as pd
import random

fname = "김이박최정강조윤장임한오서신권황안송전홍유고문양손배조" #첫번째 성
name1 = "명영정광중상재경종병진성제준종승민우예현지동순서은수윤태원" #중간 이름
name2 = "자순숙희미영경은정주연람진서빈지현원은재진호수훈준건호철길일남정형석" #마지막 이름

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
    iname = random_name() ## random_name() 이라는 함수를 한다. 근데 결과물을 차곡차곡 쌓고 싶은데? append() 를 써보자.
    ### append() 함수 문제를 해결하기 위해 append() 함수 안에 직접 넣었다. ~~아님~~ iname = 이라는 변수를 만들고, 그 변수의 결과물을 추가하게 하였다. ~~실패~~
    #### 위의 ###가 문제가 아니라 애당초 fname name1 name2 의 쉼표가 문제라는 걸 확인하였다.
    namelist.append(iname) # random_name()으로 만들어진 것을 namelist에 추가해 달라는 말이다.

# 이제 쉬워졌다. 원적교를 만들어주자

MschoolSource = ['아름중', '고운중', '도담중', '종촌중', '다정중', '새롬중', '두루중', '글벗중', 
'금호중', '반곡중', '보람중', '부강중', '새뜸중', '어진중', '양지중', '연동중', '연서중'] # 원적교 소스다. 이 리스트를 랜덤하게 뽑아서 bunho 횟수만큼 만들도록 하겠다.
BeforeSchool = [] # 원적교 리스트를 만들어주자

for i in range(len(bunho)):  # for 문을 통해 함수를 bunho의 갯수만큼 반복하자.
    BeforeSchool.append(random.choice(MschoolSource)) ## 따로 변수 지정을 안하고 append()함수를 바로 썼다// 잘 작동한다

# 같은 방법으로 진학교를 만들어주자

HschoolSource = ['다정고','도담고','두루고','반곡고','보람고','새롬고','세종고','세과영',
'국제고','대성고','세여고','예술고','장영실','하이텍','소담고'] # 진학교 소스다
PromoSchool = [] # 진학교 리스트를 만들어주자

for i in range(len(bunho)):  # for 문을 통해 함수를 bunho의 갯수만큼 반복하자.
    PromoSchool.append(random.choice(HschoolSource)) ## 따로 변수 지정을 안하고 append()함수를 바로 썼다// 잘 작동한다

# 이제 전화번호를 만들자 전화번호 만드는 건 쉽다.
phonenumber = [] #전화번호를 입력하기 위한 리스트.. 역시 for 문을 활용하여 랜덤하게 만들자

for i in range(len(bunho)):  # for 문을 통해 함수를 bunho의 갯수만큼 반복하자.
    r = str(random.random()) [2:6]
    j = str(random.random()) [2:6]
    rj = "010-"+r+"-"+j
    phonenumber.append(rj) ## 이제 폰넘버 리스트에 bunho 갯수만큼의 전화번호가 저장되었다.

## 이제 phnenumber, PromoSchool, BeforeSchool, namelist, bunho 까지 다 만들어졌다.
## pandas 를 활용하여 2차원 데이터프레임으로 만들고, 이걸 엑셀로 익스포트 시키겠다.

jinhakdata = pd.DataFrame() # jinhakdate 라는 데이타프레임을 만들자
jinhakdata['이름'] = namelist
jinhakdata['학번'] = bunho
jinhakdata['전적교'] = BeforeSchool
jinhakdata['진학교'] = PromoSchool
jinhakdata['전화번호'] = phonenumber

# 이제 to_excel() 함수를 통해 만들어진 jinhakdata 를 엑셀로 저장하겠다.
excelname = 'jinhak.xlsx'
jinhakdata.to_excel(excelname)

## 성!! 공!! 축!! 하!! 제대로 된 첫 번째 프로젝트의 첫 발을 성공하였다!!!



