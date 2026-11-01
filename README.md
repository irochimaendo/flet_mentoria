# 🎓 Flet Mentoria

Tela de **login mobile** desenvolvida em **Python** com **[Flet](https://flet.dev)**.

O projeto parte de um layout previamente desenhado no **Figma** e o reproduz em código, usando apenas componentes nativos do Flet (`Container`, `TextField`, `FilledButton`, `TextButton`, `Image` e `Row`). A janela segue as proporções de um smartphone (393 × 852 px), para que o resultado fique fiel ao protótipo.

## 📖 Sobre o projeto

A aplicação exibe uma tela de autenticação típica de aplicativos móveis, com:

- logotipo no topo;
- campos de **e-mail ou número de celular** e de **senha** (com botão para mostrar/ocultar a senha);
- link **"Esqueci minha senha"**;
- botão principal **Login**;
- opções de acesso por redes sociais (**Google**, **Apple** e **Facebook**);
- link **"criar uma conta"**.

Este é o ponto de partida de um fluxo de autenticação: nesta versão o foco é a **interface visual**. Os botões ainda não executam ações, e a validação de credenciais e a navegação entre telas são os próximos passos naturais (veja [Próximos passos](#-próximos-passos)).

## 🖼️ Pré-visualização do layout

```
┌─────────────────────────────┐
│                             │
│          [ LOGO ]           │
│                             │
│           Login             │
│                             │
│  👤 Email ou número de      │
│     celular                 │
│  ─────────────────────────  │
│  🔑 Senha              👁   │
│  ─────────────────────────  │
│                             │
│     Esqueci minha senha     │
│                             │
│   ┌─────────────────────┐   │
│   │        Login        │   │
│   └─────────────────────┘   │
│                             │
│       ou continue com       │
│                             │
│    [ G ]   [  ]   [ f ]     │
│                             │
│       criar uma conta       │
└─────────────────────────────┘
```

## ✨ Componentes da tela

| Componente | Descrição |
|---|---|
| **Logo** | Imagem centralizada (230 × 220 px) com ajuste `CONTAIN`, que preserva a proporção original. |
| **Título "Login"** | Texto em negrito, tamanho 30, centralizado. |
| **Campo de e-mail/celular** | `TextField` com borda inferior azul e ícone de pessoa. |
| **Campo de senha** | `TextField` com texto oculto, ícone de chave e botão para revelar a senha. |
| **Esqueci minha senha** | `TextButton` em azul (`#2F4EFF`). |
| **Botão Login** | `FilledButton` azul (`#2F4EFF`) com texto branco, largura de 327 px. |
| **ou continue com** | Texto auxiliar cinza (`#747474`). |
| **Login social** | Três botões quadrados (70 × 70 px) com os ícones do Google, Apple e Facebook. |
| **criar uma conta** | `TextButton` em azul (`#2F4EFF`). |

## 🧰 Tecnologias

| Camada | Tecnologia |
|---|---|
| Linguagem | Python 3.9+ |
| Interface | [Flet](https://flet.dev) (série 0.x, anterior à 1.0) |
| Design de referência | Figma |

> **Nota sobre versões:** o código usa recursos da API do Flet 0.x, como `ft.colors`, `ft.ImageFit` e `page.window_width`. Em versões 1.x do Flet, alguns deles foram renomeados ou removidos. Por isso, as instruções abaixo instalam a série 0.x.

## 📁 Estrutura do repositório

```
flet_mentoria/
├── README.md
└── flet_app/
    └── main.py      # Ponto de entrada: monta a tela de login e inicia o app
```

Todo o código da interface está em `main.py`, dentro da função `main(page)`, que configura a janela (título, dimensões, alinhamento e cor de fundo), cria cada componente como um `Container` e os adiciona à página com `page.add(...)`.

## 🚀 Como executar

**Pré-requisitos:** Python 3.9 ou superior e `pip`.

```bash
# 1. Clonar o repositório
git clone https://github.com/irochimaendo/flet_mentoria.git
cd flet_mentoria/flet_app

# 2. (Opcional) Criar e ativar um ambiente virtual
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
.venv\Scripts\activate           # Windows

# 3. Instalar a dependência
pip install "flet<1.0"

# 4. Executar como app desktop
flet run main.py

# ou como app web no navegador
flet run --web main.py
```

Também é possível iniciar com `python main.py`, pois o arquivo termina com `ft.app(target=main)`.

## 🖼️ Imagens utilizadas

A tela usa quatro imagens PNG, que **não ficam dentro do repositório**. O código as lê de caminhos absolutos da pasta *Downloads* do autor, em Windows:

| Imagem | Uso | Caminho esperado no código |
|---|---|---|
| `logo.png` | Logotipo no topo | `c:\Users\tiago\Downloads\logo.png` |
| `logo google.png` | Botão do Google | `c:\Users\tiago\Downloads\logo google.png` |
| `logo apple.png` | Botão da Apple | `c:\Users\tiago\Downloads\logo apple.png` |
| `facebook icon.png` | Botão do Facebook | `c:\Users\tiago\Downloads\facebook icon.png` |

Para rodar em outra máquina, crie uma pasta `assets/` ao lado do `main.py`, copie as quatro imagens para ela e troque os caminhos no código por caminhos relativos:

```python
# Logotipo
image_path = os.path.abspath("assets/logo.png")

# Botões sociais
ft.Image(src="assets/logo google.png", width=40, height=40)
ft.Image(src="assets/logo apple.png", width=40, height=40)
ft.Image(src="assets/facebook icon.png", width=40, height=40)
```

Para o modo web, é recomendável também passar o diretório de assets ao iniciar o app:

```python
ft.app(target=main, assets_dir="assets")
```

Se as imagens não forem encontradas, o restante da tela continua funcionando, mas os espaços do logotipo e dos ícones sociais aparecem vazios.

## ⚠️ Estado atual e limitações

- A tela é **apenas visual**: nenhum botão possui ação (`on_click`) associada.
- Não há validação de e-mail ou senha, nem integração com backend ou login social real.
- As dimensões da janela (393 × 852) são fixas e simulam um smartphone; a tela não foi pensada para redimensionamento.
- Os caminhos das imagens são absolutos e específicos do computador do autor (veja a seção acima).

## 🔭 Próximos passos

- Adicionar `on_click` ao botão **Login** e validar os campos.
- Implementar a navegação para as telas de **recuperação de senha** e **criação de conta**.
- Mover as imagens para uma pasta `assets/` versionada no repositório.
- Conectar o login a um backend ou serviço de autenticação.

## 👤 Autor

- **Tiago** — [@irochimaendo](https://github.com/irochimaendo)
