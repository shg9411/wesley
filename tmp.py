tmp = '''김채윤	Anna	1B4	phil0-2@hanmail.net
이은송	Erica	1B4	ericaeun2008@gmail.com
조성찬	Joy	2C2	point96100@naver.com
양재민	Jay	1E5	avocado84@naver.com
임강우	Ian	1D8	altla9912@gmail.com
전성준	Thomas	4A6	starthomas0125@naver.com'''.split('\n')

for t in tmp:
    x = t.split('\t')
    print('''Gospeaking 온라인 학습 정보
{} {}                                반명: {}
아이디: {}       패스워드: 0509
접속주소: new.gospeaking.com

고스피킹은 핸드폰, PC 둘다 학습이 가능하며
크롬 브라우저에서 원활히 학습 가능합니다.
(고스피킹 과제를 하기 위해선 헤드셋이 필요합니다.)'''.format(x[0], x[1], x[2], x[3]))
    print()
