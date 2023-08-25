def gayFun(num):
    num = int(num)
    if num > 1000:
        num = 1000
    num = round(num / 100, 0)
    num = int(num)
    if num < 1:
        num = 1
    return str(num)



reader = open("users.txt","r")
count = 0
for x in reader:
    if count !=0:
        splitter = x.split(":")
        uuid = splitter[41]
        wood = gayFun(splitter[5])
        fight = gayFun(splitter[12])
        archery = gayFun(splitter[11])
        farm = gayFun(splitter[9])
        mine = gayFun(splitter[1])
        fish = gayFun(splitter[34])
        acrobatics = gayFun(splitter[14])
        exc = gayFun(splitter[10])
        gay = """uuid: """ + uuid + """
skills:
  farming:
    level: """ + farm+"""
    xp: 1.1
  foraging:
    level: """ + wood+"""
    xp: 1.1
  mining:
    level: """ + mine +"""
    xp: 1.1
  fishing:
    level: """ + fish+"""
    xp: 1.1
  excavation:
    level: """ + exc+"""
    xp: 1.1
  archery:
    level: """ + archery+"""
    xp: 1.1
  defense:
    level: 1
    xp: 1.1
  fighting:
    level: """ + fight +"""
    xp: 0.0
  endurance:
    level: 1
    xp: 1.1
  agility:
    level: """ + acrobatics+"""
    xp: 206.8
  alchemy:
    level: 1
    xp: 1.1
  enchanting:
    level: 1
    xp: 1.1
  sorcery:
    level: 1
    xp: 1.1
  healing:
    level: 1
    xp: 1.1
  forging:
    level: 1
    xp: 1.1
mana: 0
locale: en
"""


        f = open(uuid + ".yml", "w")



        f.writelines(gay)
        f.close()
    

        
    count +=1
    


