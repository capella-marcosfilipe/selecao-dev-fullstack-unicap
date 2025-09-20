# Analisador de Entidades com IA (Desafio FASA/UNICAP)

Este projeto foi feito por Marcos Filipe Capella ([LinkedIn](https://linkedin.com/in/capella-marcosfilipe) | [Email](mailto:marcosfilipe.gc@gmail.com)).

![Prévia da Aplicação](https://i.imgur.com/BfKXYGs.png)

Este é um projeto full-stack desenvolvido como parte do [desafio de seleção para a vaga de Desenvolvedor Estagiário Full-Stack + IA na FASA/UNICAP](https://github.com/FASA-UNICAP/selecao-dev-fullstack-ia-2025-09/). A aplicação permite que um usuário insira um texto em português, que é então processado por uma API de back-end que utiliza um modelo de Machine Learning para realizar a **Extração de Entidades Nomeadas (NER)**. O resultado é exibido de forma clara e interativa, destacando as entidades diretamente no texto original.

O objetivo principal foi não apenas entregar um MVP funcional, mas também demonstrar a aplicação de boas práticas de desenvolvimento, arquitetura de software limpa (SOLID) e qualidade de código em todas as camadas da aplicação.

**URLs em Produção:**
-   **Frontend (Vercel):** `https://selecao-dev-fullstack-unicap.vercel.app`
-   **Backend API (Render):** `https://analisador-de-entidades-api.onrender.com/api/v1`

---

## 🛠️ Stack de Tecnologias

**Backend:**
-   Python 3.10
-   FastAPI
-   spaCy

**Frontend:**
-   Angular 20

**Deploy:**
-   Render (Backend)
-   Vercel (Frontend)
-   Git & GitHub

---

## ✨ Features e Diferenciais

-   **Backend Robusto em FastAPI:** Uma API Python rápida, escalável e pronta para produção.
-   **IA Local com spaCy:** Utiliza o modelo `pt_core_news_sm` para uma análise de NER eficiente e offline.
-   **Frontend Reativo em Angular:** Interface moderna e performática construída com as melhores práticas do Angular, incluindo o uso de `signals` para um gerenciamento de estado reativo e granular.
-   **UX Avançada:** As entidades reconhecidas são destacadas diretamente no texto original, proporcionando uma visualização intuitiva e imediata do resultado da IA. O código está comentado para compreensão da adição dos estilos.
-   **Cache de Performance:** Implementação de um **cache LRU** no back-end para otimizar drasticamente o tempo de resposta para textos repetidos, demonstrando conhecimento em otimização.
-   **Deploy Contínuo (CI/CD):** O back-end e o front-end estão implantados em plataformas de nuvem (Render e Vercel) a partir de um repositório Git, simulando um ambiente de produção real.

---

## 🏛️ Decisões de Arquitetura

A arquitetura do back-end foi projetada para ser modular e escalável, seguindo os princípios SOLID. A decisão mais importante foi a implementação de um padrão de **Dispatcher (ou "Gerente/Especialista")**:

1.  **A Rota (`/analyze`):** Atua como um "Gerente". Sua única responsabilidade é receber a requisição, validar a tarefa solicitada e delegar o trabalho para o especialista correto.
2.  **O Registro (`task_registry`):** Um mapa central que associa um tipo de tarefa (ex: `NER`) a um serviço especialista.
3.  **Os Serviços Especialistas (ex: `NerService`):** Cada serviço é focado em uma única tarefa de IA. Ele contém toda a lógica de negócio, processamento e medição de performance para aquela tarefa específica.

Essa abordagem segue o **Princípio Aberto/Fechado**, permitindo que novas tarefas de IA (como Análise de Sentimento ou OCR) sejam adicionadas ao sistema apenas criando um novo serviço e registrando-o, sem a necessidade de modificar o código da rota principal.

---

## 🚀 Como Rodar o Projeto Localmente

### Pré-requisitos
-   Node.js v20+
-   Python 3.10+
-   Angular CLI (`npm install -g @angular/cli`)

### 1. Backend
```bash
# Clone o repositório
git clone https://github.com/capella-marcosfilipe/selecao-dev-fullstack-unicap
cd SEU_REPOSITORIO/backend

# Crie e ative um ambiente virtual
python -m venv .venv
# No Windows:
# .\.venv\Scripts\activate
# No Linux/macOS:
# source .venv/bin/activate

# Este projeto foi feito gerenciado pela ferramenta uv.

# Instale as dependências
pip install .

# Baixe o modelo spaCy
python -m spacy download pt_core_news_sm

# Rode o servidor de desenvolvimento
uvicorn api.main:app --reload
```
O backend estará disponível em `http://127.0.0.1:8000`.

### 2. Frontend
```bash
# Em outro terminal, a partir da raiz do projeto
cd ../frontend

# Instale as dependências
npm install

# Rode a aplicação
ng serve --open
```
A aplicação estará disponível em `http://localhost:4200/`.

---

## 📡 Exemplo de Uso da API

Você pode interagir com a API através da rota `POST /api/v1/analyze`.

**Exemplo de Requisição (`curl`):**
```bash
curl -X 'POST' \
  'https://analisador-de-entidades-api.onrender.com/api/v1/analyze' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "task": "ner",
  "input_text": "A executiva Ana Paula anunciou em São Paulo que a InnovaTech firmou uma parceria com a Google."
}'
```

**Exemplo de Resposta:**
```json
{
  "id": "a1b2c3d4-e5f6-a7b8-c9d0-e1f2a3b4c5d6",
  "task": "ner",
  "engine": "local:pt_core_news_sm",
  "result": {
    "entities": [
      { "text": "Ana Paula", "label": "PER" },
      { "text": "São Paulo", "label": "LOC" },
      { "text": "InnovaTech", "label": "ORG" },
      { "text": "Google", "label": "ORG" }
    ]
  },
  "elapsed_ms": 65,
  "received_at": "2025-09-20T12:00:00.123456"
}
```
