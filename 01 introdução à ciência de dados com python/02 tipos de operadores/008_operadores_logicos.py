saldo = 1000
saque = 200
limite = 100

saldo >= saque
saque <= limite

# operador e
saldo >= saque and saque <= limite

# operador ou 
saldo >= saque or saque <= limite

# operador negação
contatos_emergencia = [] 

not 1000 > 1500
not contatos_emergencia
not "saque 1500;"

# parênteses
conta_especial = True

saldo >= saque and saque <= limite or conta_especial and saldo >= saque
(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)