# Template — Minicurso Pipeline de Dados (ETL)

Este repositório é o **template com o código inicial** que usaremos no minicurso de Pipeline de Dados (ETL), no dia **02/10**. Ele contém a estrutura do projeto e as funções que vamos implementar juntos durante o minicurso (`extract`, `transform`, `load`, etc.) — por isso o código ainda está incompleto, isso é esperado.

O restante deste documento traz os **requisitos que você precisa instalar e configurar antes do minicurso**. O objetivo é não gastarmos tempo de aula com instalação de ferramentas — se tudo estiver pronto com antecedência, começamos direto na prática.

Leia com calma e siga o checklist. Em caso de dúvida ou erro em qualquer etapa, entre em contato com a organização do minicurso **antes do dia do evento**.

---

## Checklist rápido

- [ ] Python 3.11 instalado
- [ ] Git instalado
- [ ] Visual Studio Code instalado
- [ ] Extensão **Python** (Microsoft) instalada no VS Code
- [ ] Repositório do minicurso baixado/clonado na sua máquina
- [ ] Ambiente virtual criado e dependências instaladas (`pip install -r requirements.txt`)

Se todos os itens acima funcionarem, você está pronto para o minicurso.

---

## 1. Sistema operacional

O material funciona em **Windows**, **macOS** e **Linux**. As instruções abaixo cobrem os três casos — siga apenas a seção do seu sistema.

## 2. Python 3.11

O projeto foi desenvolvido e testado com a **versão 3.11** do Python. Recomendamos usar exatamente essa versão para evitar incompatibilidades com as bibliotecas do projeto.

### Windows

1. Baixe o instalador em: https://www.python.org/downloads/release/python-3119/ (role até "Files" e baixe o **Windows installer (64-bit)**).
2. Ao iniciar a instalação, **marque a opção "Add python.exe to PATH"** antes de clicar em "Install Now". Esse passo é o que mais causa problemas quando esquecido.
3. Confirme a instalação abrindo o terminal (PowerShell ou Prompt de Comando) e rodando:
   ```
   py -3.11 --version
   ```
   O retorno esperado é algo como `Python 3.11.9`.

### macOS

1. Instale via [Homebrew](https://brew.sh/) (recomendado):
   ```
   brew install python@3.11
   ```
2. Ou baixe o instalador oficial em: https://www.python.org/downloads/release/python-3119/ (arquivo "macOS 64-bit universal2 installer").
3. Confirme com:
   ```
   python3.11 --version
   ```

### Linux (Ubuntu/Debian)

Na maioria das distribuições recentes o Python 3.11 já está disponível. Verifique com `python3.11 --version`. Se não estiver instalado:
```
sudo apt update
sudo apt install python3.11 python3.11-venv
```

---

## 3. Git

O código do minicurso está hospedado no GitHub. O Git é usado para baixar (clonar) o repositório.

- **Windows**: baixe e instale em https://git-scm.com/download/win (pode manter todas as opções padrão do instalador).
- **macOS**: `brew install git` ou instale via Xcode Command Line Tools (`xcode-select --install`).
- **Linux**: `sudo apt install git`.

Confirme a instalação com:
```
git --version
```

> Caso você não tenha familiaridade com Git, também é possível baixar o repositório como um arquivo `.zip` diretamente pelo GitHub (botão **Code → Download ZIP**), sem precisar instalar o Git. Nesse caso, basta descompactar o arquivo em uma pasta de sua preferência.

---

## 4. Visual Studio Code (VS Code)

Usaremos o VS Code como editor de código durante o minicurso.

1. Baixe e instale em: https://code.visualstudio.com/download
2. Abra o VS Code e instale a extensão oficial **Python** (publicada pela Microsoft):
   - Vá em **Extensions** (ícone de blocos na barra lateral esquerda, ou `Ctrl+Shift+X` / `Cmd+Shift+X`).
   - Busque por "Python" e instale a extensão da Microsoft (ela já inclui o Pylance, usado para autocomplete e checagem de tipos).
3. (Opcional, mas recomendado) Instale também a extensão **GitLens**, útil para visualizar histórico e alterações do Git direto no editor.

---

## 5. Terminal

Vamos rodar comandos pelo terminal integrado do VS Code (menu **Terminal → New Terminal**, ou atalho `` Ctrl+` ``).

**Atenção usuários de Windows**: por padrão, o PowerShell bloqueia a execução de scripts (necessário para ativar o ambiente virtual). Se ao ativar o ambiente virtual aparecer um erro de "execution policy", rode o comando abaixo **uma única vez** no PowerShell:
```
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

---

## 6. Baixando o projeto e instalando as dependências

Com Python, Git e VS Code instalados, clone o repositório e prepare o ambiente:

### Linux / macOS
```bash
git clone git@github.com:felipe-monteiro16/template_minicurso_dados.git
cd template_minicurso_dados
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Windows
```bash
git clone git@github.com:felipe-monteiro16/template_minicurso_dados.git
cd template_minicurso_dados
py -3.11 -m venv venv
./venv/Scripts/activate
pip install -r ./requirements.txt
```

> Se você usou o "Download ZIP" em vez do `git clone`, pule o comando `git clone` e apenas navegue (`cd`) até a pasta onde extraiu o projeto.

Se o `pip install` terminar sem erros, o ambiente está pronto. Você pode testar rodando:
```
python main.py
```

---

## Dúvidas

Qualquer problema durante a instalação, entre em contato com a organização do minicurso com antecedência, para que possamos resolver antes do dia do evento.
