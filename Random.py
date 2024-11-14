import random

# 캐릭터 리스트
character = ["황제", "황후", "황태자", "황태자비", "기사단장", "북부대공", "사생아", "공작", "백작", "남작", "시녀", "교황", "대신관", "성녀", "마왕", "마녀"]
#  키워드 리스트
keyword = ["시한부", "빙의", "환생", "회귀", "정략결혼", "소꿉친구", "첫사랑", "후회", "저주"]
#  사건 리스트
incident = ["폭탄발언", "비밀동맹", "새로운 경험", "두근거림", "은밀한 접촉", "데뷔당트", "무도회", "이혼", "전쟁"]

selected_characters = [2]

# 캐릭터 랜덤 선택 (중복 되지 않는 두명)
def random_character():
    # selected_characters = random.sample(character, 2)
    # print("등장인물 : {0}, {1}".format(selected_characters[0], selected_characters[1]))
    return random.sample(character, 2)

# 키워드 랜덤 선택
def random_keyword():
    n = random.randrange(len(keyword))
    # print("키워드 : {}".format(keyword[n]))
    return keyword[n]

# 사건 랜덤 선택
def random_incident():
    n = random.randrange(len(incident))
    # print("사건 : {}".format(incident[n]))
    return incident[n]

# selected_characters = random_character()
# print("등장인물 : {0}, {1}".format(selected_characters[0], selected_characters[1]))
# print("키워드 : {}".format(random_keyword()))
# print("사건 : {}".format(random_incident()))