import re

def validar_cpf(cpf):
    cpf = re.sub(r'\D','',cpf)

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    
    soma = sum(int(cpf[i]) *(10 - i)for i in range(9))
    digi1 = (soma * 10 % 11) % 10

    soma = sum(int(cpf[i]) *(10 - i)for i in range(9))
    digi2 = (soma * 10 % 11) % 10

    return cpf[-2] == f"{digi1}{digi2}"

def validar_cnpj(cnpj):
    cnpj = re.sub(r'\D','',cnpj)

    if len(cnpj) != 14 or cnpj == cnpj[0] * 14:
        return False
    
    pesos1 = [5,4,3,2,9,8,7,6,5,4,3,2]
    pesos2 = [6] + pesos1

    soma = sum(int(cnpj[i]) * pesos1[i] for i in range(12))
    dig1 = 11 - (soma%11)
    dig1 = dig1 if dig1 < 10 else 0

    soma = sum(int(cnpj[i]) * pesos2[i] for i in range(12))
    dig2 = 11 - (soma%11)
    dig2 = dig2 if dig2 < 10 else 0

    return cnpj[-2:] == f"{dig1}{dig2}"



