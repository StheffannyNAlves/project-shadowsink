# ShadowSink: Honeypot Interativo de Engenharia Social

**Uma sala de interrogatório digital para capturar e analisar o comportamento de atacantes em tempo real.**

---

![Python](https://img.shields.io/badge/python-3.9+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

## Visão Geral do Projeto

**ShadowSink** não é um honeypot passivo tradicional. Em vez de apenas registar um endereço IP e uma tentativa de login, ele foi projetado como uma ferramenta de aquisição de dados forenses para estudar a metodologia de um atacante. O projeto simula uma falsa página de administração e regista secretamente cada interação do utilizador, desde a digitação de credenciais até aos movimentos do rato e cliques, para reconstruir a linha do tempo de um ataque.

O foco não está em bloquear o atacante, mas em **compreender as suas ações, passo a passo.**

## Funcionalidades Principais

* **Fachada Credível:** Uma página de login web construída com Flask, desenhada para parecer uma área administrativa legítima.
* **Logging Forense Detalhado:** Captura de credenciais, cada tecla pressionada (`keypress`), cada clique (`click`) e os movimentos do rato (`mousemove`).
* **Comunicação Furtiva:** As interações são enviadas de forma assíncrona do front-end para o back-end, sem alertar o utilizador.
* **Armazenamento Seguro:** Todas as sessões e eventos são armazenados numa base de dados SQLite para análise posterior.
* **Painel de Análise (Dashboard):** Uma interface para rever as sessões capturadas e reproduzir a sequência cronológica de eventos de cada ataque.

## Propósito Estratégico

Este projeto serve como a fundação prática da **"Operação Quimera"**, desenvolvendo competências essenciais que transcendem o desenvolvimento web:

1.  **Desenvolver a Mentalidade Forense:** A disciplina de capturar, ordenar com carimbo de tempo e analisar uma sequência de eventos de software é o treino direto para a análise de incidentes em sistemas embarcados.
2.  **Construir Ferramentas de Análise:** A criação de um dashboard para visualizar dados de ataque é o protótipo para futuras interfaces de análise de dumps de firmware ou de dados de canal lateral.
3.  **Dominar a Interação Cliente-Servidor:** O fluxo de dados assíncrono entre o JavaScript e o Flask é conceptualmente idêntico à comunicação entre um dispositivo de hardware e o seu software de controlo via UART ou outros protocolos.

## 🛠️ Configuração e Instalação do Laboratório

Siga estes passos para configurar o ambiente de desenvolvimento.

1.  **Clonar o repositório:**
    ```bash
    git clone [URL-DO-SEU-REPOSITÓRIO]
    cd project-shadowsink
    ```

2.  **Criar e ativar o ambiente virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instalar as dependências:**
    ```bash
    pip install Flask
    ```

4.  **Executar a aplicação:**
    ```bash
    flask --app app run
    ```
    O honeypot estará acessível em `http://127.0.0.1:5000`.

## AVISO DE SEGURANÇA

**Este projeto é uma ferramenta de pesquisa e NUNCA deve ser implantado em redes públicas ou de produção.** Foi projetado exclusivamente para ser executado em ambientes de laboratório isolados e controlados (como uma Máquina Virtual) para fins educacionais. O autor não se responsabiliza por qualquer uso indevido desta ferramenta.

## Status do Projeto

Este projeto segue um plano de execução faseado em Sprints. **A execução ainda não foi iniciada.**

| Sprint | Objetivo Principal | Status |
| :--- | :--- | :--- |
| **Sprint 0** | Preparação do Terreno e Estrutura do Projeto | Concluído |
| **Sprint 1** | Construção da Fachada (Página de Login) | Em Execução |
| **Sprint 2** | Implementação da Armadilha Básica (Captura de Credenciais) | 📝 Planeado |
| **Sprint 3** | A Sala de Interrogatório (Logging Forense de Interações) | 📝 Planeado |
| **Sprint 4** | O Replay (Desenvolvimento do Dashboard de Análise) | 📝 Planeado |
| **Sprint 5** | Métricas e Inteligência (Análise Estatística de Comportamento) | 📝 Planeado |

```eof
