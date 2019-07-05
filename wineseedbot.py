import discord
import random

d = discord.Client()



@d.event

async def on_ready():

    print("로그인 중........")



@d.event

async def on_message(message):
    if message.content.startswith("!날씨"):

         msg = message.content[4:]

         url = msg + "날씨"

         await message.channel.send("https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=" + url)

    if message.content.startswith("!검색"):

        msg2 = message.content[4:]

        await message.channel.send("https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=" + msg2)

    if message.content.startswith("/제작자"):

        await message.channel.send("와인씌인가.....아무튼 스트리머임")

    if message.content.startswith("!도움 준 사람"):

        await message.channel.send("준영맨입니다")
    
    if message.content.startswith("!와인씌 유튜브"):

        await message.channel.send("https://www.youtube.com/channel/UCvBQM82NnYbVXcm_VlqMx4g")

    if message.content.startswith("!와인씌 트위치"):

        await message.channel.send("https://www.twitch.tv/wineseed")

    if message.content.startswith("!제작자 정보"):

        await message.channel.send("게임:배그(스,카배),팀포,로블,카스")

        await message.channel.send("배그 정보:(카배)https://pubg.op.gg/user/twitchTVwineseed")

        await message.channel.send("배그 정보:(스배)https://pubg.op.gg/user/twitch_wineseed")

    if message.content.startswith("!명령어"):

        await message.channel.send("명령어,와인씌 유튜브,와인씌 트위치,검색,날씨,제작자,도움 준 사람,제작자 정보........등등")

    if message.content.startswith("/유튜브 검색"):

        msg3 = message.content[8:]

        await message.channel.send("https://www.youtube.com/results?search_query=" + msg3)
    if message.content.startswith("!저장"):
        global msg5
        global msg6
        msg5 = message.content[6:]
        msg6 = message.content[4:6]
        await message.channel.send(msg6 + "에" + msg5 + "가 저장되었습니다") 
    if message.content.startswith("!확인"):
        global msg8
        msg8 = message.content[4:]
        await message.channel.send(msg8 + "의 갚:" + msg5) 
    if message.content.startswith("!삭제"):
        msg5 = None
        await message.channel.send("갚이 삭제되었습니다") 
    food = ['카레', '스파게티', '집밥', '라면', '짜장면', '김치볶음밥', '우동', '쫄면', '국수', '돈까스', '엿(ㅗ)', '삼계탕', '치킨']
    if message.content.startswith("!안녕"):
        a = ['안녕! 나는 와인씌야!', '안녕! 내가 널 구하러 왔어!', '안녕! 어디서 많이 본거같은데...', '안녕! 무슨일이야?']
        await message.channel.send(random.choice(a))         
    if message.content.startswith("!운빨게임"):
        luck = ['니가 이김', '니가 짐', '비김']
        await message.channel.send(random.choice(luck))
    if message.content.startswith("!배고파"):
        await message.channel.send("배고파?")
        await message.channel.send("그럼 오늘은...")
        await message.channel.send(random.choice(food))
        await message.channel.send("어때?")
    if message.content.startswith("!도움"):
        await message.channel.send("내가 도와주지!")
        await message.channel.send("간드아!!!!!!!!!!")
        await message.channel.send("참고로 제작자는 와인씌입니다.")                                                                  
    if message.content.startswith("!바보"):
        await message.channel.send("흥!")                                  
    if message.content.startswith("!이스터에그"):
        await message.channel.send("음...나도 몰라.")
        await message.channel.send("하지만 제작자는 알지도?")                                
    if message.content.startswith("!멍청이"):
        await message.channel.send("흥!")
    if message.content.startswith("!제작자"):
        await message.channel.send("와인씌 입니다.")
    if message.content.startswith("!성별"):
        await message.channel.send("그런게 왜 중요해!")
    if message.content.startswith("!메롱"):
        await message.channel.send("흥!")
    if message.content.startswith("!와"):
        await message.channel.send("와! 샌즈! 파피루스!")
        await message.channel.send("아~ 언더테일 아시는구나~")
        await message.channel.send("참고로 겁.나.어.렵.습.니.다.")
        await message.channel.send(".. 라고 하네여")
    if message.content.startswith("!ㅎㅇ"):
        await message.channel.send("ㅎㅇ~")
    if message.content.startswith("!실명"):
        await message.channel.send("그건 바로 &*^*^*&*&(입막기)")
  
   
    if message.content.startswith("!배틀그라운드"):
        await message.channel.send("탕탕탕탕! 으악 사람이다 (사망)")
    if message.content.startswith("!레인보우식스"):
        await message.channel.send("그게 머임?")
    if message.content.startswith("!레식"):
        await message.channel.send("그게 머임?")
    if message.content.startswith("!나닛"):
        await message.channel.send("나닛--!!!")
    if message.content.startswith("!햄보칸플리퍼"):
        await message.channel.send("a제곱 더하기 b제곱은 c제곱 피타고라ㅅ..")
    if message.content.startswith("?"):
        await message.channel.send("뭐요....")
    if message.content.startswith("!모두"):
        await message.channel.send("@everyone")     
    if message.content.startswith("!소개"):
        await message.channel.send("전..영웅입니다")
    if message.content.startswith("!ㅂ"):
        await message.channel.send("그럼 안녕히.......")
    if message.content.startswith("!ㅋ"):
        await message.channel.send("ㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎ")
        await message.channel.send("LOL   하하하하핳하하ㅏ")
        await message.channel.send(".......뭐가 웃기죠?")
    if message.content.startswith("!옵치"):
        await message.channel.send("석양이.....으억")
    if message.content.startswith("!오버워치"):
        await message.channel.send("하늘에서! 정의가! 으억.....")
    if message.content.startswith("!ㄹㅇ"):
        await message.channel.send("진짜요!!!!")
    if message.content.startswith("!빠루"):
        await message.channel.send("고든프리맨, 그는 좋은박사였지만.....")
        await message.channel.send("(하프라이프 후속작 안나온대)")
    if message.content.startswith("!고든프리맨"):
        await message.channel.send("그는 자유인이다!!!!!")
    if message.content.startswith("욕"):
        await message.channel.send("뒤지실?")
    if message.content.startswith("!도배"):
        await message.channel.send("너 진짜 미친놈인가 보구나.")
        await message.channel.send("샌즈 올림")
    if message.content.startswith("!배그 전적"):
        msg9 = message.content[7:]
        await message.channel.send("https://pubg.op.gg/user/" + msg9)
    if message.content.startswith("안녕하세요"):
        luck = ['ㅎㅇㅎㅇ', '무시','???', '안녕하세요', '하와인']
        await message.channel.send(random.choice(luck))
                
d.run('NTg4NjIwMjE3MTU3MTU2ODY4.XRIqsw.ak9f8iwPSoEYQwctTyPV-dqVEoo')
        

