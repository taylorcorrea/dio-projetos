# 🛡️ Ransomware Python – Projeto de Cibersegurança

Este projeto tem como objetivo simular, para fins educacionais, o funcionamento básico de um **ransomware** utilizando a linguagem **Python**. Ele criptografa um arquivo específico (`teste.txt`) e permite sua posterior descriptografia usando uma chave derivada de uma senha.

> ⚠️ **Atenção:** Este projeto é estritamente educativo. O uso indevido pode ser ilegal e é de responsabilidade exclusiva de quem o utiliza. **Nunca utilize em sistemas de terceiros sem autorização explícita.**

---

## 📁 Estrutura do Projeto

```
Ransomware-python/
├── encrypter.py        # Criptografa o arquivo teste.txt
├── decrypter.py        # Descriptografa o arquivo teste.txt
├── teste.txt           # Arquivo de teste a ser criptografado
├── requirements.txt    # Dependências do projeto
├── images/             # (opcional) Capturas de tela da execução
└── README.md           # Este arquivo
```

---

## 🚀 Como funciona

- O `encrypter.py`:
  - Deriva uma chave a partir da palavra `"Teste"`.
  - Criptografa o conteúdo do `teste.txt`.
- O `decrypter.py`:
  - Usa a mesma derivação para restaurar o conteúdo original de `teste.txt`.

A chave é derivada via SHA-256 e transformada em formato compatível com Fernet (base64 URL-safe).

---

## ✅ Pré-requisitos

- Python 3.6 ou superior
- Biblioteca `cryptography`

Instale com:

```bash
pip install cryptography
```

Ou:

```bash
pip install -r requirements.txt
```

---

## 🧪 Como testar

1. Crie um arquivo chamado `teste.txt` com algum conteúdo.
2. Execute o `encrypter.py`:
   ```bash
   python encrypter.py
   ```
   O conteúdo será criptografado.

3. Execute o `decrypter.py`:
   ```bash
   python decrypter.py
   ```
   O conteúdo original será restaurado.

---

## 🔐 Sobre a chave

A chave usada é derivada da string `"Teste"`, com este trecho:

```python
import hashlib, base64
senha = b"Teste"
hash = hashlib.sha256(senha).digest()
chave = base64.urlsafe_b64encode(hash)
```

Esse método mantém a chave fixa de forma segura sem gerar uma nova a cada execução.

---

## 📷 Imagens 

---

## 📚 Objetivos de Aprendizagem

- Compreender a aplicação de criptografia simétrica (Fernet).
- Aprender a derivar chaves a partir de senhas.
- Manipular arquivos com segurança em Python.
- Simular o comportamento de ransomware como parte da **pós-exploração** em testes de segurança.

---

## ⚖️ Uso Responsável

Este projeto é **educacional**, voltado para o aprendizado de conceitos de segurança, criptografia e Python.  
**Jamais use esse tipo de script em sistemas alheios ou fora de ambientes controlados**.

---

## 👨‍💻 Autor

**Taylor Correa**  
Repositório criado como parte de estudos práticos do bootcamp Santander Cibersegurança + DIO.

---

## 📎 Referência útil

Repositório base sugerido pelo desafio:  
https://github.com/cassiano-dio/cibersecurity-desafio-ransomware
