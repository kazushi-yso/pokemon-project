class pokemon:
    def __init__(self,name,type,hp,at,df):
        self.name=name
        self.type=type
        self.hp=hp
        self.at=at
        self.df=df


    def attack(self, enemy):
        # 相性の検証
        damage_rate = check_compatibility(self.type, enemy.type)

        # ヒコザルがナエトルに80ダメージを与える
        enemy.hp-= self.at*damage_rate-enemy.df*1/20


def check_compatibility(attacker_type, receiper_type):
    if attacker_type == receiper_type:
        return 1
    elif attacker_type == "ほのお" and receiper_type == "みず":
        return 0.8
    elif attacker_type == "ほのお" and receiper_type == "くさ":
        return 1.2
    elif attacker_type == "くさ" and receiper_type == "みず":
        return 1.2
    elif attacker_type == "くさ" and receiper_type == "ほのお":
        return 0.8
    elif attacker_type == "みず" and receiper_type == "くさ":
        return 0.8
    elif attacker_type == "みず" and receiper_type == "ほのお":
        return 1.2

hikozaru=pokemon("ヒコザル","ほのお",450,50,100)
naetoru=pokemon("ナエトル","くさ",450,50,100)

pocchama=pokemon("ポッチャマ","みず",450,50,100)

hikozaru.attack(naetoru)

print(naetoru.hp)