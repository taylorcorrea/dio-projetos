# Simulação de Phishing com SEToolkit

## 🚀 Objetivo
Demonstrar como funcionam ataques de engenharia social por meio da clonagem de páginas falsas e captura de credenciais, utilizando o **SEToolkit**, **Apache2** e **Kali Linux**, em um ambiente controlado de laboratório.

---

## 📄 Ferramentas Utilizadas
- Kali Linux (em VM)
- Social-Engineer Toolkit (SEToolkit)
- Apache2
- VirtualBox (modo bridge ou NAT com acesso local)
- Navegador Web (Host)

---

## ✅ Procedimento

### 1. Iniciar o SEToolkit
```bash
sudo setoolkit
```

### 2. Navegar pelos menus:
1. Social Engineering Attacks  
2. Website Attack Vectors  
3. Credential Harvester Attack Method  
4. Site Cloner  

### 3. Inserir a URL alvo:
```
https://www.facebook.com
```

### Obtendo o endereço da máquina:
```
ifconfig
```

### 5. SEToolkit clona a página e ativa escuta:
- Os dados ficam salvos em `/var/www/html`
- As credenciais capturadas aparecem no terminal da VM

---

## 📷 Evidências Visuais
--
Este laboratório foi executado em rede local. A máquina virtual Kali utilizou o IP 192.168.2.101 como servidor do ataque SEToolkit para demonstração.
--


## 🔢 Resultados
As credenciais digitadas foram capturadas com sucesso:

```bash
[+] WE GOT A HIT! Printing the output:
POSSIBLE USERNAME FIELD FOUND: user@example.com
POSSIBLE PASSWORD FIELD FOUND: 123456
```

---

## ⚠️ Considerações Éticas
> Esta atividade foi realizada em ambiente isolado. O uso dessas técnicas sem autorização é ilegal. O objetivo é educacional e voltado para a conscientização sobre ameaças de engenharia social.

---

## ⚖️ Melhorias Futuras
- Adição de redirecionamento via DNS Spoofing
- Testes com certificados falsos para HTTPS (mitmproxy)
- Geração automatizada de e-mails de phishing simulados (com autorização)

---

## 📊 Conclusão
> A prática evidenciou a facilidade de exploração de vítimas desprevenidas com ferramentas acessíveis. 
> Fica clara a importância de educar usuários e aplicar boas práticas de segurança em ambientes corporativos e pessoais.

---

## ⚠️ Aviso Legal

Este projeto foi desenvolvido com fins exclusivamente educacionais, como parte do Bootcamp de Cibersegurança promovido pela DIO e Santander. Todas as atividades foram realizadas em ambiente controlado e privado, sem afetar terceiros. O uso indevido das técnicas aqui demonstradas é ilegal e contra as diretrizes éticas da área de segurança da informação.


---
**Autor:** Taylor Correa  
**Data:** Junho de 2025
---
