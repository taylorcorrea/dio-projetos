from cryptography.fernet import Fernet
# usar senha comum	Derive com hashlib + base64
import hashlib
import base64

# Deriva a mesma chave a partir da palavra 'Teste'
senha = b"Teste"
hash = hashlib.sha256(senha).digest()
chave = base64.urlsafe_b64encode(hash)

fernet = Fernet(chave)

# Lê os dados criptografados
with open("teste.txt", "rb") as file:
    dados_criptografados = file.read()

# Tenta descriptografar
try:
    dados_descriptografados = fernet.decrypt(dados_criptografados)

    # Escreve os dados originais no arquivo
    with open("teste.txt", "wb") as file:
        file.write(dados_descriptografados)

    print("Arquivo descriptografado com sucesso!")

except Exception as e:
    print("Erro ao descriptografar:", str(e))