# 마린: 공격윤싯, 군인 ,총쏨
name ="마린"
hp = 40 #체력
damage =5 #공격력
print(f'{name} 유닛이 생성됬습니다.')
print(f'체력 {hp}, 공격력 {damage}\n')
tank_name ="탱크"
tank_hp = 150
tank_damage = 35
print("{0}유닛이 생성되었습니다.".format(tank_name))
print("체력{0},공격력{1}\n".format(tank_hp, tank_damage))
def attack(name,location, damage):
    print(f'{name}:{location}방향으로 적군을 공격합니다.[공격력{damage}]')
attack(name,"서쪽",damage) 
attack(tank_name, "동쪽", tank_damage)
attack("jn", "남쪽",15)