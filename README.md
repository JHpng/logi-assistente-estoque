# LOGI — Assistente de Gestão de Estoque

Chatbot de terminal que responde sobre estoque usando apenas
a base de conhecimento em `data/base.md` (RAG simples via prompt).

## Como rodar

```bash
pip install -r requirements.txt
cp .env.example .env      # cole sua GEMINI_API_KEY dentro
python src/app.py
```

## Estrutura
- `src/app.py` — aplicação
- `data/base.md` — base de conhecimento (fórmulas de PP, ABC, EOQ, giro)
