bunbunbun = list(range(1,26)) # 1부터 25 까지 숫자를 만들어서 리스트로 bunbunbun에 저장
# sbunbunbun = ''.join(str(bunbunbun)) #bunbunbun을 문자형 리스트로 저장

print(bunbunbun)
banbun = [] # 번호를 저장할 반번이란 리스트를 만들자

for x in bunbunbun: # bunbunbun 리스트의 갯수를 세어서, for 문으로 반복 25개 있으면 25번 반복
        ## bunbunbun 의 갯수를 세라는 뜻에서, bunbunbun 이라는 변수 안의 내용을 하나씩 꺼내라는 뜻으로 바꿨다
        #### bunbunbun 변수 안에 있는 각 항목을 x 라고 했을때:
    xxxx = str(x).zfill(2) #zfill() 함수를 써서, 0$ 이런 모양으로 만듬. 만들어서 banbun 변수에 저장 
        #### x 를 문자열로 변환시킨 다음에 zfill(2) 함수가 시키는 대로 $$ 이런 형식의 숫자로 만들어서 banbun 이라는 변수에 넣어라
        #### 이 상태에선 banbun에 하나씩 넣으라는 것이 아니니까 하나씩 넣도록 만들어야겠다.
    # # 위의 babun 은 bunbunbun 이라는 길~~~다른 리스트를 통째로 가져오기 대문에 zfill()이 작동하지 않은 것 같다
    # # 따라서 zfill() 이 작동하게 하기 위해선 bunbunbun의 인수를 하나씩 꺼낸 다음에 그걸 작업하게 만들어야겠다.
    # banbun에다가 하나씩 기록하게 하자 append() 써먹자
    banbun.append(xxxx)
    # 해냈다!!! append로 하나씩 기록하게 하니까 작동하였다.
    


print(banbun) #banbun 변수를 출력
