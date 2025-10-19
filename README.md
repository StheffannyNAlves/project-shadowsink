# 🕶️ Shadow Sink: Operação Espelho

> "Não é um site. É uma sala de interrogatório digital."  
> "Cada clique é uma confissão. Cada linha de código, um interrogatório."

![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/flask-000000.svg?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-07405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-323330.svg?style=for-the-badge&logo=javascript&logoColor=F7DF1E)

## Visão Geral

**Shadow Sink** é um honeypot interativo desenvolvido em **Flask**, projetado para capturar, registrar e reproduzir o comportamento de invasores em páginas de login falsas.  
Combina **engenharia forense**, **fingerprinting comportamental** e **replay visual** para registrar cada detalhe da interação do atacante do clique à digitação.

Destinado a **analistas, pentesters e estudantes** que buscam compreender a psicologia e a técnica por trás das intrusões, sem riscos reais.

## Principais Funcionalidades

- **Modo Espelho** coleta tempos entre teclas, latência entre cliques e velocidade de digitação para criar uma assinatura comportamental.  
- **Replay Visual 2.0** converte logs em uma linha do tempo animada, simulando a sessão do atacante em tempo real.  
- **Fingerprints e Metadados** coleta `User-Agent`, resolução, timezone, idioma e coordenadas de clique.  
- **Módulo Sentinel (Forense Integrado)** gera hashes SHA256 por evento, relatórios JSON e um "saco de provas" completo com logs e timestamps.  
- **Modo Treino** alterna entre:
  - `capture_mode = True`: coleta real de dados;
  - `training_mode = True`: simulação de sessões para demonstrações.

## Estrutura do Projeto

```bash
shadow-sink/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── db.py
│   ├── replay.py
│   ├── sentinel.py
│   └── utils/
│       └── fingerprint.py
│
├── static/
│   ├── css/style.css
│   └── js/capture.js
│
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   └── ...
│
├── data/
│   └── database.db
│
├── reports/
│   └── evidence_session.json
│
└── docs/
    └── ...
```

## Status do Desenvolvimento

> **Fase atual:** Arquitetura *Sprint 1/6*  
> O projeto está em estruturação. O foco é construir a fundação e a fachada antes do sistema forense.

<table>
  <tr>
    <th>Status</th>
    <th>Módulo / Sprint</th>
    <th>Descrição</th>
  </tr>
  <tr>
    <td>✅ Concluído</td>
    <td><b>Arquitetura Core</b></td>
    <td>Inicialização do Flask com Blueprints (<code>app.py</code>, <code>app/routes.py</code>). Rotas modulares implementadas.</td>
  </tr>
  <tr>
    <td>✅ Concluído</td>
    <td><b>Sprint 1: A Fachada</b></td>
    <td>Interface de login falsa (<code>login.html</code>) finalizada, estética Noir/Corporativa ("FortPay").</td>
  </tr>
  <tr>
    <td>⚠️ Captura Ativa</td>
    <td><b>Sprint 2: A Armadilha</b></td>
    <td>Rotas de login capturam credenciais via POST, simulam falha e registram IP dados ainda salvos apenas em log de console.</td>
  </tr>
  <tr>
    <td>❌ Pendente</td>
    <td><b>Sprint 3: A Sala de Interrogatório</b></td>
    <td>Persistência de dados (<code>SQLite3</code>) não implementada. Projeto pausado nesta etapa.</td>
  </tr>
  <tr>
    <td>🎯 Próximo Objetivo</td>
    <td><b>Pausa de Fim de Ano</b></td>
    <td>Retomada em <b>22 de dezembro</b>. Prioridade: módulo <code>db.py</code> para persistência e ativação da camada forense.</td>
  </tr>
</table>

## Tecnologias Principais

| Categoria     | Tecnologias |
|----------------|-------------|
| **Backend** | Python, Flask |
| **Persistência** | SQLite3 *(em breve)* |
| **Forense** | Módulo Sentinel (SHA256 Hashing, JSON Reports) |
| **Análise** | Replay Visual 2.0 (JS/HTML), Fingerprinting Comportamental |

## 💻 Como Executar (modo desenvolvimento)

1. **Clone o repositório**

```bash
   git clone https://github.com/StheffannyNAlves/project-shadowsink.git
   cd project-shadowsink
```

2. **Crie e ative o ambiente virtual**

```bash
   python3 -m venv venv
   
     # Linux/macOS
   source venv/bin/activate        
   
     # PowerShell (Windows)
   .\venv\Scripts\activate
```

3. **Instale as dependências**

 ```bash
   pip install -r requirements.txt
```

4. **Configure a aplicação Flask**

   *Linux/macOS:*

   ```bash
   export FLASK_APP=app
   export FLASK_ENV=development
   ```

   *Windows (PowerShell):*

   ```powershell
   $env:FLASK_APP = "app"
   $env:FLASK_ENV = "development"
   ```

5. **Execute a aplicação**

   ```bash
   flask run
   ```

   O honeypot estará acessível em:
   👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

## 🎨 Identidade Visual

Tema: **Sala de Interrogatório Digital**
Estilo: minimalista, técnico.
Cores: preto, cinza escuro e laranja queimado (`#ff8c00`).
Fonte: monoespaçada (Consolas, JetBrains Mono).
Foco em contraste, legibilidade e atmosfera "noir corporativa".

## 🔮 Extensões Futuras

* Integração com **ELK Stack** (ElasticSearch + Kibana)
* **API REST** (`/api/sessions`) para análise remota
* **Docker** container para deploy isolado
* **AI Witness** sumarização automatizada via IA
* **Detecção de Bots (RL)** Implementação de algoritmos de Reinforcement Learning para analisar padrões de digitação e aprimorar, em tempo real, a detecção entre bots e humanos.
* **Sandbox local** para simulação de ataques automatizados
* **CLI Forense** (`shadowcli analyze evidence_*.json`)

## ⚠️ Aviso de Segurança

Este projeto é **apenas para pesquisa e educação em cibersegurança**.
**Nunca** execute em redes públicas, ambientes de produção ou máquinas corporativas.
Utilize **somente em laboratórios isolados** (máquinas virtuais ou redes sandbox).

O autor **não se responsabiliza por uso indevido**.

## 📜 Licença

Distribuído sob a licença **MIT**.
Consulte o arquivo `LICENSE` para mais detalhes.

## 👩🏿‍💻 Autor

**Stheffanny Nascimento**
Engenharia de Computação UEFS
Cibersegurança • Forense Digital • Engenharia Reversa

📦 Repositório oficial: [github.com/StheffannyNAlves/project-shadowsink](#)