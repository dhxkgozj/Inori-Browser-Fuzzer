# Inori-Browser-Fuzzer-fail..-
html 생성 관련 py 입니다.

제가 지금 만들고 있는 브라우저 퍼저 버전 0.1 입니다..
파일 구성은 아래와 같습니다.
[파일 구성]
- Create_Html.py [ Html 파일 생성 ]
- css [ css 관련 생성 ]
- html_dom [ DOM 컨트롤 및 자바 스크립트 생성 ]
- html [ html 관련 생성 ]

[사용 방법]
python Create_Html.py

if __name__=="__main__":
	create  = create_html()
	while(1):
		create.create_html('/Users/gimdong-wan/VM share/test.html')
		time.sleep(30)

저기 create_create_html 인자에 있는 path에 test.html이 생성 됩니다.

연구를 제대로 안하고 짠탓에 이걸 계속 쓰긴 힘들것 같아서 처음부터 다시 짜려고 합니다.

구조는 한가 할때 다시 업뎃 하겠습니다.
css, html , dom method 같은것들이 정의 되어 있으니 필요하신분은 가져다 쓰세요.