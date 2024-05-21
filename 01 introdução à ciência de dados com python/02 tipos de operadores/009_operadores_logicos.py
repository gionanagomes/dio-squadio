# and: para ser True, tudo tem que ser True
# or: para ser True, apenas um tem que ser True

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

print(True and False)
print(True and True)
print(False and False)

print(True or True)
print(True or False)
print(False or False)

print(exp)
print(exp_2)