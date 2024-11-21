import numpy as np

전자기기_여부 = [True,False]
인원수 = 0

complete = False
while complete == False:    
    if input("전자기기가 있습니까?, True, False로 대답하십시오") == True:
        전자기기_여부 = 전자기기_여부[0]
        if 전자기기_여부 == True:
            print("충전중")
            if 인원수 == 36:
                complete = True
        elif 전자기기_여부 == False:
            print("충전대기중")
            if 인원수 == 36:
                complete = True

    # if 1,2,3,4,5,6 not in (컴퓨터_앞자리[0],컴퓨터_앞자리[1])

    # 1.끝나게 할것
    # 2.인원수와 컴퓨터 자리, 찬 자리에 따라 print를 만들고 다 찬인원에 따라 또다른 pritn
    # 그리고 막는것 잘못되었고
    #시작하고 반복할때 그것이 무슨 자리가 남았는지 컴퓨터 자리에 따라
    # 그리고 추가적으로 무엇을 추가로 알고싶은지 구상하면 좋을듯. 에를 들면 몇번자리가 비어있나요 같은거
    #인원수와 추가된 자리수를 동일하게 말하면 자리가 없습니다
    #나중에 gui로 구현하는 것도 나쁘지 않을듯