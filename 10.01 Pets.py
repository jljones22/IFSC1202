class Pet():
    def __init__(self):
        self.m_name = ""
        self.m_type = ""
        m_age = -1

pets = open("10.01 Pets.txt", "rt")
line = pets.readline()

fido = Pet()
fluffy = Pet()
tweety = Pet()

p = []

while line != "":
    ls = line.strip().split(',')
    p.append(ls)

    line = pets.readline()

for i in range(len(p)):
    match p[i][0]:
        case 'Fido':
            fido.m_name = p[i][0]
            fido.m_type = p[i][1]
            fido.m_age = int(p[i][2])
        case 'Fluffy':
            fluffy.m_name = p[i][0]
            fluffy.m_type = p[i][1]
            fluffy.m_age = int(p[i][2])
        case 'Tweety':
            tweety.m_name = p[i][0]
            tweety.m_type = p[i][1]
            tweety.m_age = int(p[i][2])

print("{:>8} {:>8} {:>8}".format("Name", "Type", "Age"))
print(f"{fido.m_name:>8} {fido.m_type:>8} {fido.m_age:>8}")
print(f"{fluffy.m_name:>8} {fluffy.m_type:>8} {fluffy.m_age:>8}")
print(f"{tweety.m_name:>8} {tweety.m_type:>8} {tweety.m_age:>8}")