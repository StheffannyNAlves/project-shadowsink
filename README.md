# Shadow Sink: Operação Espelho

> "Não é um site. É uma sala de interrogatório digital."

---

![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/flask-000000.svg?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-07405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-323330.svg?style=for-the-badge&logo=javascript&logoColor=F7DF1E)

---

## Visão Geral

**Shadow Sink** é um honeypot interativo desenvolvido em **Flask**, projetado para capturar, registrar e reproduzir o comportamento de invasores em páginas de login falsas.  
Ele combina **engenharia forense**, **fingerprinting comportamental** e **replay visual** para criar um registro completo da interação do atacante — do clique à digitação.

Este projeto foi criado para **analistas, pentesters e estudantes** que desejam compreender a psicologia e a técnica por trás de tentativas de intrusão, sem riscos reais.

---

## Principais Funcionalidades

### Modo Espelho  
Além de capturar entradas, o sistema grava padrões temporais como o tempo entre teclas, latência entre cliques e velocidade de digitação.  
Esses dados permitem criar uma **assinatura de interação** (*behavior fingerprint*) capaz de treinar modelos de detecção de bots e realizar replays precisos das sessões.

### Replay Visual 2.0  
Transforma logs em uma linha do tempo animada da interação do atacante.  
No dashboard, cada evento (`keypress`, `click`) é reproduzido visualmente na interface falsa, criando uma simulação em tempo real do ataque.

### Fingerprints e Metadados  
No momento do acesso, o honeypot captura **User-Agent**, **resolução da tela**, **timezone**, **idioma** e **coordenadas de clique**.  
Todos os dados são armazenados em uma tabela `fingerprints`, criando um perfil de interação único para cada sessão.

### Módulo Sentinel (Forense Integrado)  
Sistema responsável por calcular o **hash SHA256** de cada sessão e evento, gerar relatórios automáticos em JSON e exportar um “saco de provas” com logs, hash e timestamp, garantindo a integridade forense dos dados coletados.

### Modo Treino  
Permite alternar entre:
- `capture_mode = True`: coleta real de dados de interação;  
- `training_mode = True`: simula logs falsos para aprendizado e demonstrações.  

Cria um ambiente seguro para **prática forense** e **cibereducação**.

---

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
│   └── evidence_<session_id>.json
│
└── docs/
    └── ...


## Como Executar


1. ** Clone o repositório**

   ```bash
   git clone https://github.com/StheffannyNAlves/project-shadowsink.git
   cd shadow-sink



2. **Crie e ative o ambiente virtual**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure a aplicação Flask**

   * Linux/macOS:

     ```bash
     export FLASK_APP=app
     ```
   * Windows (PowerShell):

     ```bash
     $env:FLASK_APP = "app"
     ```

5. **Execute a aplicação**

   ```bash
   flask run
   ```

O honeypot estará acessível em **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## Identidade Visual

O projeto segue o tema de uma **“sala de interrogatório digital”**, com uma estética minimalista e sombria.
A paleta de cores usa **preto**, **cinza escuro** e **laranja queimado** (`#ff8c00`).
A tipografia recomendada é monoespaçada (como **Consolas** ou **JetBrains Mono**).
O dashboard deve manter um estilo **noir**, técnico e limpo, priorizando legibilidade e contraste.

---

## Extensões Futuras

* Integração com **ELK Stack (ElasticSearch + Kibana)** para visualização avançada de eventos.
* **API REST** para análise remota (`/api/sessions`).
* Deploy em container **Docker** isolado.
* Módulo **"AI Witness"** para sumarizar sessões capturadas usando IA.
* Integração opcional com **sandbox local**, simulando ataques automatizados para treino de resposta.
* Ferramenta CLI para análise forense offline das evidências geradas (`shadowcli analyze evidence_*.json`).

---

## Aviso de Segurança

Este projeto é uma ferramenta de **pesquisa e educação em cibersegurança**, não um sistema de defesa ativo.
**Nunca** o execute em redes públicas, ambientes de produção ou máquinas corporativas.
Use apenas em **laboratórios isolados** (máquinas virtuais ou redes sandbox).

---

## Licença

Distribuído sob a licença **MIT**.
Consulte o arquivo `LICENSE` para mais informações.

---

## Autor

**Stheffanny Nascimento**
Engenharia de Computação — UEFS
Cibersegurança • Forense Digital • Engenharia Reversa
Repositório oficial: [github.com/StheffannyNAlves/project-shadowsink](#)

---

> “Cada clique é uma confissão.
> Cada linha de código, um interrogatório.”


