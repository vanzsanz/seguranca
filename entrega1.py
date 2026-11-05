
# PROJETO SECUREUSER
# ENTREGA 1 - CRIPTOGRAFIA ASSIMÉTRICA
# Assinatura digital utilizando Ed25519

from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey
)

from cryptography.exceptions import InvalidSignature


# 1. Gerando o par de chaves
chave_privada = Ed25519PrivateKey.generate()

# Obtendo a chave pública correspondente
chave_publica = chave_privada.public_key()


# 2. Criando uma mensagem
mensagem = b"Esta mensagem pertence ao sistema Aegis."

# 3. Assinando a mensagem com a chave privada
assinatura = chave_privada.sign(mensagem)

print("Mensagem original:", mensagem.decode())
print("Assinatura digital gerada com sucesso!")


# 4. Verificando a assinatura
try:
    chave_publica.verify(assinatura, mensagem)
    print("Assinatura válida! A mensagem é autêntica.")

except InvalidSignature:
    print("Assinatura inválida! A mensagem foi alterada.")


# 5. Testando uma mensagem adulterada
mensagem_adulterada = b"Esta mensagem foi modificada!"

print("\nTestando mensagem adulterada:")

try:
    chave_publica.verify(assinatura, mensagem_adulterada)
    print("Assinatura válida!")

except InvalidSignature:
    print("Assinatura inválida! A mensagem foi adulterada.")
