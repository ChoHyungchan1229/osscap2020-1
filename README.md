# osscap2020
2020 오픈소스 기초설계 프로젝트
(LED 스마트 스피커 / 공룡게임)

git clone 이후 python3 main.py 를 통해 프로젝트를 실행할 수 있습니다.
마이크에 "헤이 구글"을 말한 이후 날씨정보에 대한 내용을 물어보면 현재 위치 정보에 대한 날씨를 알려줍니다.
이후 LED에서도 날씨 정보에 대한 이모티콘, 현재 기온, 최고 기온, 최저 기온, 미세먼지 농도, 초미세먼지 농도를 출력해줍니다.
날씨에 대한 정보는 1시간 간격으로 자동 업데이트됩니다.

이후 메뉴 1, 2, 3, 4번이 있습니다.
1번은 공룡게임을 진행합니다.
키보드에서 space bar를 누르면 공룡이 점프하며, 장애물을 피할 수 있습니다.
어느 정도 점수에 도달하게 되면 보스 몬스터가 warning 메세지가 출력된 이후 LED화면에 오른쪽에서 천천히 나타납니다. 
공룡이 장애물이나 보스 몬스터의 공격에 맞게 되면, game over 메세지와 점수가 함께 출력되고 게임이 종료됩니다.
이후 메뉴창이 다시 나타나게 되면 alt키 + tab키를 누른 후에 다시 공룡게임을 실행할지 날씨 정보를 출력할 지 선택할 수 있습니다.
공룡게임을 재실행하면, alt키 + tab키 한번 더 눌러주어야 공룡이 점프할 수 있습니다. 

메뉴 2번은 날씨 정보를 1회 재출력합니다.
출력되는 정보는 처음 출력되었던 날씨 정보와 동일합니다.

메뉴 3번은 날씨 정보를 100회 재출력합니다.
출력되는 정보는 처음 출력되었던 날씨 정보와 동일합니다.

메뉴 4번은 실행을 종료합니다.
