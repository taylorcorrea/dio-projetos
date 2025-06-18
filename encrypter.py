from cryptography.fernet import Fernet
# usar senha comum	Derive com hashlib + base64
import hashlib
import base64

# Deriva a chave segura a partir da palavra 'Teste'
senha = b"Teste"
hash = hashlib.sha256(senha).digest()  # gera 32 bytes
chave = base64.urlsafe_b64encode(hash)  # converte para formato aceito pelo Fernet

fernet = Fernet(chave)

# Lê o conteúdo original do arquivo
with open("teste.txt", "rb") as file:
    dados = file.read()

# Criptografa os dados
dados_criptografados = fernet.encrypt(dados)

# Escreve o conteúdo criptografado no mesmo arquivo
with open("teste.txt", "wb") as file:
    file.write(dados_criptografados)

print("Arquivo criptografado com sucesso!")
