bunho = [] # 학번이 기록될 리스트를 만들자
ban = ['01','02','03','04','05','06','07','08','09','10']  ## zfill() 함수를 사용하면 된다. 귀찮으니 그냥 반에다 넣지

# 반의 번호를 만들기 위해 순서대로 번호를 만들어주자
bunbunbun = list(range(1,26)) # 1부터 25 까지 숫자를 만들어서 리스트로 bunbunbun에 저장
banbun = [] # 번호를 저장할 반번이란 리스트를 만들자
for x in bunbunbun: # bunbunbun의 인수를 하나씩 꺼내서 x로 배당해서 반복한다
    xxxx = str(x).zfill(2) #zfill() 함수를 써서, 0$ 이런 모양으로 만듬. 만들어서 banbun 변수에 저장 
    banbun.append(xxxx) ## 이제 banbun 이라는 리스트에 0$ 형식으로 01~25까지가 만들어졌다

# print(banbun) banbun이 잘 만들어졌는지 테스트

## 이제 banbun 을 이용해서 bunho 를 만들자 / 목표는 3 + ban + banbun 을 순차적으로 만들어 bunho 에 넣는 것이다.

## banbun 을 꺼내서 ban 에 결합시킨다. ban 을 하나씩 꺼내야 한다.
for i in ban:
    # print(i) for 문이 잘 작동하는지 테스트
    for ii in banbun:
        hapche = "3"+i+ii
        bunho.append(hapche)

# print(bunho) #bunho 가 잘 만들어졌는지 테스트