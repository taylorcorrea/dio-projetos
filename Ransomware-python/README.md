# 🛡️ Desafio de Cibersegurança - Ransomware em Python

Este projeto faz parte do desafio proposto no **bootcamp Santander Bootcamp 2025 - Cibersegurança**, com o objetivo de desenvolver um ransomware **educacional** utilizando a linguagem Python.

> ⚠️ **Atenção**: este projeto é de caráter **educacional** e não deve ser utilizado para fins maliciosos. O uso indevido é crime conforme previsto em lei.

---

## 🎯 Objetivos do Projeto

- Desenvolver um **criptografador (encrypter)** de arquivos;
- Desenvolver um **descriptografador (decrypter)** para restaurar os arquivos;
- Aplicar técnicas reais de pós-exploração ofensiva, em ambiente controlado;
- Organizar um repositório público com documentação clara, utilizando Git e GitHub.

---

## 🗂️ Estrutura do Projeto

-encrypter.py # Código para criptografar arquivos
-decrypter.py # Código para descriptografar arquivos
-requirements.txt # Dependências do projeto
-README.md # Documentação completa do projeto
-images/ # Capturas de tela e evidências (opcional)
-encrypt-example.png
-decrypt-example.png
---

## 🔐 Funcionamento

### `encrypter.py`
- Gera uma chave de criptografia usando a biblioteca `cryptography`;
- Percorre os arquivos da pasta-alvo;
- Criptografa cada arquivo encontrado;
- Salva a chave de forma segura (ou exibe para uso manual no decrypter).

### `decrypter.py`
- Solicita a chave gerada anteriormente;
- Percorre os arquivos criptografados;
- Descriptografa e restaura os arquivos ao estado original.

---

## 💻 Como Executar

### 1. Clone o repositório
```bash
git clone https://github.com/taylorcorrea/dio-projetos.git
cd dio-projetos/Ransomware-python


![Exemplo de Criptografia](images/encrypt-example.png)
![Exemplo de Descriptografia](images/decrypt-example.png)
