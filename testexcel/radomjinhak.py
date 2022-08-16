#-*-coding:euc-kr

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

fname = "김,이,박,최,정,강,조,윤,장,임,한,오,서,신,권,황,안,송,전,홍,유,고,문,양,손,배,조"
name1 = "명,영,정,광,중,상,재,경,종,병,진,성,제,준,종,승,민,우,예,현,지,동,순,서,은,수,윤,태"
name2 = "자,순,숙,희,미,영,경,은,정,주,연,람,진,서,빈,지,현,원,은,재,진,호,수,훈,준,건,호,철,길,일,남,정,형"

def random_name():
    created_name=""
    created_name += random.choice(fname)
    created_name += random.choice(name1)
    created_name += random.choice(name2)
    return created_name






