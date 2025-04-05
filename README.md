
# 📸 Screenshot Link

**Screenshot Link** é uma aplicação simples e prática que permite gerar uma captura de tela de uma página da web a partir do link fornecido pelo usuário.  

**In English**:

**Screenshot Link** is a simple and practical application that allows you to generate a screenshot of a web page from the link provided by the user.

---

## 🚀 Tecnologias Utilizadas

- **Front-end:** React, CSS
- **Back-end:** Python + Flask  
  - Biblioteca principal: [Pyppeteer](https://github.com/pyppeteer/pyppeteer)

---

## 🧠 Como Funciona?

Você informa o link de uma página da web na interface da aplicação. O back-end, por meio da biblioteca **Pyppeteer**, abre essa página no modo *headless* (sem interface gráfica) e tira uma captura de tela automaticamente, salvando-a na pasta `static`.

O front-end então recebe o **nome da imagem gerada** e acessa e acessa essa imagem através da URL pública exposta pelo Flask, que segue o padrão:
``http://127.0.0.1:5000/static/img/NOME_DA_IMAGEM``. Em seguida, a aplicação **inicia o download automático** da imagem no navegador do usuário.

---

## ⚠️ Atenção

O **Pyppeteer** depende do navegador **Google Chrome** para funcionar corretamente. No seu código, o Chrome está sendo invocado diretamente através do caminho:

```python
browser = await launch(
    executablePath="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    headless=True,
)
```

### ➡️ Isso significa que:

- É necessário ter o **Google Chrome instalado** na máquina.
- Caso o Chrome esteja em outro diretório, o caminho (`executablePath`) deve ser ajustado manualmente.
- Em sistemas operacionais diferentes (como Linux ou macOS), esse caminho também será diferente.

---

## 🛠️ Como Inicializar o Projeto

Siga os passos abaixo para rodar a aplicação localmente.

### 1. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/screenshot-link.git
cd screenshot-link
```

### 2. Instale as dependências do back-end (Python)

```bash
cd back-end
python -m venv venv
venv\Scripts\activate  # no Windows
source venv/bin/activate  # no Linux/macOS

pip install -r requirements.txt
```

> Certifique-se de que o Chrome está instalado e atualize o caminho de `executablePath` se necessário.

### 3. Inicie o servidor Python

```bash
python app.py
```


### 4. Instale as dependências do front-end (React)

Abra outro terminal:

```bash
cd front-end
npm install
```

### 5. Inicie o servidor React

```bash
npm start
```

A aplicação estará disponível em `http://localhost:3000`.

---

## Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias, correções ou sugestões!

---

## 👤 Autor


Desenvolvido por **Victor Souza de Queiroz Tavares**  
🔗[LinkedIn](https://www.linkedin.com/in/victor-tavares-profissional/)


---
