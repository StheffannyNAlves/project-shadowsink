# 🕶️ Shadow Sink: Operação Espelho

> "Não é um site. É uma sala de interrogatório digital."  
> "Cada clique é uma confissão. Cada linha de código, um interrogatório."

![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/flask-000000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-323330.svg?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![RabbitMQ](https://img.shields.io/badge/Rabbitmq-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white)



## Visão Geral

**Shadow Sink** é um honeypot de alta interação focado em análise forense e comportamental. Desenvolvido em **Flask** e **PostgreSQL**, ele é projetado não apenas para *o quê* um invasor digita, mas *como* ele digita.

O sistema captura cada evento de digitação, movimento do mouse e metadado do navegador para construir uma "assinatura de interação" (fingerprint comportamental). Esses dados são então exfiltrados para um coletor seguro, onde são protegidos por uma cadeia de custódia forense e disponibilizados para análise e replay.

Destina-se a analistas de segurança, pesquisadores e *pentesters* que buscam compreender as Táticas, Técnicas e Procedimentos (TTPs) de adversários em tempo real.

## Arquitetura Estratégica: Sensor vs. Coletor

Para garantir a sobrevivência das evidências, o Shadow Sink opera em uma arquitetura desacoplada:

1.  **O Sensor (Este Repositório):** Um aplicativo Flask "descartável" que serve a fachada (`login.html`). Sua **única** função é capturar eventos de interação e *exfiltrá-los* imediatamente (via `rsyslog` ou Fila de Mensagens, ex: RabbitMQ). Ele **não** possui credenciais de banco de dados. Se o sensor for comprometido, nenhuma evidência é perdida.
2.  **O Coletor (Servidor Seguro):** Um *worker* de back-end (em um host/rede separada) que escuta a fila de mensagens. Ele é o **único** componente com acesso ao PostgreSQL. Ele recebe os dados brutos do Sensor, os valida, executa o Módulo Sentinel (hashing) e os persiste no banco de dados usando transações atômicas.

## Principais Funcionalidades

  - **Análise de Ritmo (Keystroke Dynamics):** Em vez de latência básica, o "Modo Espelho" analisa o *ritmo* da digitação. Ele foca em digrafos (ex: `t-h`), trigrafos (`t-h-e`) e heurísticas humanas (uso de `Backspace`) para diferenciar padrões cognitivos de *jitter* aleatório gerado por bots.
  - **Cadeia de Custódia Forense (Log Chaining):** O "Módulo Sentinel" não gera apenas hashes. Ele implementa uma **Cadeia de Hashes**: cada relatório de sessão JSON salvo contém o hash SHA256 da sessão *anterior*. Isso cria uma cadeia de custódia que garante a *integridade cronológica*, provando que os logs não foram adulterados ou inseridos retroativamente.
  - **Replay Visual 2.0:** Reconstrói logs JSON em uma linha do tempo animada, permitindo que o analista "reassista" a sessão do invasor em tempo real, observando digitação, erros e correções.
  - **Fingerprinting de Metadados:** Coleta passiva de `User-Agent`, resolução de tela, `timezone`, idioma do navegador e outros metadados para identificar o ambiente do adversário.
  - **Modo Treino:** Permite a simulação de logs falsos para testes de pipeline, demonstrações e desenvolvimento do módulo de replay.

## Estrutura do Projeto (O Sensor)

```bash
shadow-sink/
├── app/
│   ├── __init__.py         # Inicialização do Flask e Blueprints
│   ├── routes.py         # As rotas de captura (ex: /login)
│   ├── exfiltrator.py    # Lógica para enviar dados (syslog/RabbitMQ)
│   └── utils/
│       └── fingerprint.py  # Funções de coleta de metadados
│
├── static/
│   ├── css/style.css     # Estilo "Noir Corporativo" (FortPay)
│   └── js/capture.js     # JS para capturar eventos (keydown, mouse)
│
├── templates/
│   ├── login.html        # A fachada / armadilha
│   
│
├── venv/
├── requirements.txt
├── config.py
└── run.py                # Ponto de entrada do Gunicorn/Flask
```

*Nota: Os módulos de persistência (`db.py`, `models.py`), forense (`sentinel.py`), replay(`replay.py`), os templates de análise (`dashboard.html`, `evidence.html`) **não** existem neste repositório.* 
*Eles residem em um repositório **privado** e separado, o shadow-sink-collector, que é o único componente com credenciais para acessar o banco de dados.*

## Status do Desenvolvimento

> **Status:** PAUSADO (Pausa Estratégica para exames).
> **Retomada:** 22 de Dezembro de 2025.

>

<table>
  <thead>
    <tr>
      <th>Status</th>
      <th>Módulo / Sprint</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>✅ Concluído</td>
      <td><strong>Sprint 1: A Fachada</strong></td>
      <td>Interface de login falsa (<code>login.html</code>) "FortPay" finalizada. Estética Noir/Corporativa.</td>
    </tr>
    <tr>
      <td>✅ Concluído</td>
      <td><strong>Sprint 2: A Armadilha</strong></td>
      <td><code>capture.js</code> captura eventos de digitação e faz POST. <code>routes.py</code> recebe os dados brutos e simula falha de login.</td>
    </tr>
    <tr>
      <td>🎯 Próximo Objetivo</td>
      <td><strong>Sprint 3: A Exfiltração</strong></td>
      <td>Implementar <code>exfiltrator.py</code>. Configurar o Sensor Flask para enviar logs JSON para uma fila (RabbitMQ) ou syslog.</td>
    </tr>
    <tr>
      <td>❌ Pendente</td>
      <td><strong>Sprint 4: O Coletor &amp; DB</strong></td>
      <td>(Em novo repositório) Criar o <em>worker</em> que consome da fila e persiste os dados no PostgreSQL (Docker) usando transações.</td>
    </tr>
    <tr>
      <td>❌ Pendente</td>
      <td><strong>Sprint 5: Módulo Sentinel</strong></td>
      <td>Implementar a lógica da <strong>Cadeia de Hashes (Log Chaining)</strong> no Coletor.</td>
    </tr>
  </tbody>
</table>


## Tecnologias Principais

| Categoria | Tecnologias |
|---|---|
| **Sensor (Frontend)** | Flask, JavaScript (Vanilla) |
| **Arquitetura** | RabbitMQ (ou `rsyslog-ng`) para desacoplamento |
| **Coletor (Backend)** | Python (Worker), PostgreSQL (via Docker) |
| **Forense** | Módulo Sentinel (SHA256 Log Chaining), JSON Reports |
| **Análise** | Replay Visual (JS/HTML), Keystroke Dynamics |

## 💻 Como Executar (Sensor em Modo Desenvolvimento)

**Atenção:** Estas instruções executam apenas o **Sensor** localmente para fins de desenvolvimento da interface.

1.  **Clone o repositório**

    ```bash
    git clone https://github.com/StheffannyNAlves/project-shadowsink.git
    cd project-shadowsink
    ```

2.  **Crie e ative o ambiente virtual**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # (Linux/macOS)
    .\venv\Scripts\activate   # (Windows PowerShell)
    ```

3.  **Instale as dependências**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure a aplicação Flask**

    ```bash
    export FLASK_APP=run.py
    export FLASK_ENV=development
    ```

5.  **Execute o Sensor**

    ```bash
    flask run
    ```

    O honeypot (sensor) estará acessível em: `http://127.0.0.1:5000`

## Roadmap de Análise (Extensões Futuras)

  - **Detecção de Bots (Machine Learning):**
      - **Fase 1 (Classificação):** Treinar modelos (Random Forest/SVM) sobre as *features* estatísticas extraídas da Análise de Ritmo (digrafos, backspace, etc.).
      - **Fase 2 (Análise Sequencial):** Implementar modelos (LSTM/GRU) para classificar a *sequência bruta* de eventos de digitação, detectando padrões temporais complexos.
  - **AI Witness:** Um módulo de IA (LLM) para gerar resumos executivos automatizados de cada sessão de ataque.
  - **Integração ELK Stack:** Envio dos relatórios JSON do Coletor para o ElasticSearch para visualização e agregação no Kibana.
  - **API REST Forense:** Uma API segura no Coletor (`/api/sessions/<id>`) para puxar relatórios e dados de replay.
  - **Deploy em Docker:** Containerização completa do *Sensor* e do *Coletor* para deploy rápido e isolado.

## Aviso de Segurança

Este projeto é **apenas para pesquisa e educação em cibersegurança**.
**Nunca** execute em redes públicas, ambientes de produção ou máquinas corporativas.
Utilize **somente em laboratórios isolados** (Máquinas Virtuais ou redes Sandbox).

O autor **não se responsabiliza por uso indevido**.

## Licença

Distribuído sob a licença **MIT**.
Consulte o arquivo `LICENSE` para mais detalhes.

## Autor

**Stheffanny Nascimento**
Engenharia de Computação - UEFS
\-Cibersegurança, Forense Digital, Engenharia Reversa

Repositório oficial: [github.com/StheffannyNAlves/project-shadowsink](#)