# osscap2020
2020 오픈소스 기초설계 프로젝트
==================
(LED 스마트 스피커 / 공룡게임)
-----------------

* 처음 사용하기

> 미리 설치해야 되는 파이썬 라이브러리 : pygame, GPIO, beautifulsoup4, schedule

> 준비물 : Raspberry Pi 4, USB 마이크, 3.5파이용 스피커, 16x32 LED matrix, LED matrix에 추가 전력을 공급할 5V/2A power adopter

    git clone https://github.com/Jaehong-Cho/osscap2020.git
  
    python3 main.py
    
실행시 처음 보이는 문구는 Google_info.py로 google assistant의 이용안내 문구를 스크롤링 하는 모습을 보실 수 있습니다.

마이크에 "헤이 구글"을 말한 이후 궁금한 정보나 간단한 대화를 나눠보실 수 있습니다.
이후 LED에서도 날씨 정보에 대한 이모티콘, 현재 기온, 최고 기온, 최저 기온, 미세먼지 농도, 초미세먼지 농도를 출력해줍니다.
날씨에 대한 정보는 1시간 간격으로 자동 업데이트됩니다.

구글 어시스턴트 이용시 주의사항
---------

    구글 어시스턴트는 개별 등록이 필요한 서비스 입니다.
    
    아래의 Googole API 링크를 통해서 단계에 따라서 수행하신 후에 이용가능합니다.
    
    기기를 등록한 후에, 라즈베리파이 부팅시 자동 실행을 원하신다면
    
    해당 repo의 ai_speaker --> make_auto_start.txt를 참고해주시기 바랍니다.

이후 메뉴에는 1, 2, 3, 4, 5번이 있습니다.

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

메뉴 4번은 텍스트 스크롤링으로 가장 처음에 보여준 어시스턴트 안내 문구를 보여줍니다.

메뉴 5번은 프로그램을 종료해 줍니다.

![all](https://user-images.githubusercontent.com/70634938/100569833-9492ab00-3312-11eb-9484-67228aa0d84f.jpg)

----------------------
> 공룡게임 오픈소스 https://github.com/byunkyunho/chrome-dino-game

> 웹 스크래핑 오픈소스 https://github.com/norangLemon/naverWeather

> 구글 API(assistant) https://developers.google.com/assistant/sdk/guides/service/python/
