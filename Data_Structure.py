#리스트형 선언 및 인덱싱
# bts_members = ['RM', '슈가', '진', '제이홉', '지민', '뷔', '정국']
#
# print('멤버 :', bts_members)
# print('타입 :', type(bts_members))
# print('크기 :', len(bts_members))
#
# print('리스트멤버 호출')
# print(bts_members[0])
# print(bts_members[1])
# print(bts_members[2])
# print(bts_members[3])
# print(bts_members[-1])
# print(bts_members[-2])
# print(bts_members[-3])
#####################################################################
#리스트형 추가/삭제
# sistar_members = ['효린', '소유']
# print('씨스타 \t:', sistar_members)
#
# sistar_members.append('다솜')
# print('append \t:', sistar_members)
# sistar_members.insert(1, '보라')
# print('insert \t:', sistar_members)
#
# sistar_members.remove('소유')
# print('remove \t:', sistar_members)
#
# pickup = sistar_members.pop(0)
# print('pop   \t:', sistar_members, end= ' ---> ')
# print(pickup)
####################################################################
#리스트 슬라이싱
# rainbow = ['빨강', '주황', '노랑', '초록', '파랑', '남색', '보라']
# print('\n무지개색깔 \t :', rainbow)
#
# result = rainbow[2:5]
# print('rainbow[2:5] :', result)
# result = rainbow[:3]
# print('rainbow[:3] :', result)
# result = rainbow[:]
# print('rainbow[ : ] :', result)
# result = rainbow[::2]
# print('rainbow[::2] :', result)
# result = rainbow[-3:]
# print('rainbow[-3: ] :', result)
# result = rainbow[::-1]
# print('rainbow[::-1] :', result)
#####################################################################
#리스트 응용
# solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성', '지구']
# print('태양계 :', solarsys)
#
# planet = '지구'
# pos = solarsys.index(planet)
# print('%s 행성은 태양계에서 %d번째에 위치하고 있습니다.' %(planet, pos))
# pos = solarsys.index(planet, 5)
# print('%s 행성은 태양계에서 %d번째에 위치하고 있습니다.' %(planet, pos))
#
# solarsys.pop(-1)
# print('태양계 :', solarsys)
#
# planet = '화성'
# pos = solarsys.index(planet)
# solarsys[pos] = 'Mars'
# print('태양계 :', solarsys)
#
# solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
# rock_planets = solarsys[1:5]
# gas_planets = solarsys[5: ]
#
# print('암석형 행성: ', end =''); print(rock_planets);
# print('가스형 행성: ', end =''); print(gas_planets);
#
# solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
# pos = solarsys.index('목성')
# solarsys.insert(pos, '소행성')
# print('태양계 :',  solarsys)
##########################################################################################
# #중첩리스트
# city = [
#     ['서울',  '도쿄',  '베이징'],
#     ['런던',  '파리',  '로마'  ],
#     ['워싱턴','시카고','잭슨빌']
# ]
#
# print('city      :', city)
# print('city[0]   :', city[0])
# print('city[1]   :', city[1])
# print('city[-1]  :', city[-1])
# print('city[0][0]:', city[0][0])
# print('city[0][1]:', city[0][1])
# print('city[0][2]:', city[0][2])
# print('city[1][1]:', city[1][1])
# print('city[-2][0]:', city[-2][0])
# print('city[-3][-3]:', city[-3][-3])

girl_group = ('트와이스', '레드벨벳', '에이핑크', '걸스데이', '우주소녀')

print('girl_group    \t: ', girl_group)
print('girl_group[:2] \t: ', girl_group[:2])
print('girl_group[-2:] : ', girl_group[-2:])