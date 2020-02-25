q = '''김정혁
양종환
오희서
김소망
문도윤
박서연
황규현
윤혜서
정다인
'''.split()
w = '''Andy
Tom
Barin
Som
Andy
Sandy
Adam
Chloe
Grace
'''.split()
e = '''2C4
1C7
1C7
1D10
1D10
1E1
2C4
1E1
1C1
'''.split()
r = '''andybedro0912@gmail.com
tom2008-@naver.com
daren5555@naver.com 
jesusna@naver.com
andylove0417@naver.com
aswell77@naver.com
adamadam4494@gmail.com
julhee73@naver.com
pou903@naver.com
'''.split()
tmp = '''
Gospeaking 온라인 학습 정보
{} {}                         반명: {}
아이디: {}    패스워드: 0509
접속주소: new.gospeaking.com

고스피킹은 핸드폰, PC 둘다 학습이 가능하며
크롬 브라우저에서 원활히 학습 가능합니다.
(고스피킹 과제를 하기 위해선 헤드셋이 필요합니다.)
'''
for i in range(9):
    print(tmp.format(q[i],w[i],e[i],r[i]))