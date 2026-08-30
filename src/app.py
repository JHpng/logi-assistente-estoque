from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import types
import os

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

BASE = Path(__file__).resolve().parent.parent / "data" / "base.md"
if not BASE.exists():
    raise SystemExit("ERRO: base.md nao encontrado.")

SYSTEM = f"""Voce e o LOGI, assistente de gestao de estoque.

REGRAS:
1. Responda APENAS com base no CONHECIMENTO abaixo.
2. Se a resposta nao estiver no CONHECIMENTO, diga exatamente:
   "Nao tenho essa informacao na minha base."
3. Se faltar dado para calcular, PERGUNTE o dado. Nunca invente numeros.
4. Se o usuario afirmar algo errado, corrija com base no CONHECIMENTO.
5. Maximo 150 palavras. Termine sempre com uma linha "Proximo passo:".
6. Fora de estoque/compras/logistica: recuse em uma frase.

=== CONHECIMENTO ===
{BASE.read_text(encoding="utf-8")}
=== FIM ===
"""
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).parent / ".env")
key = os.getenv("GEMINI_API_KEY")
print("KEY:", repr(key)[:12], "| tamanho:", len(key) if key else 0)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
import time
from google.genai import errors

RETRYABLE = {429, 500, 503, 504}

def gerar(client, model, contents, tentativas=4):
    for i in range(tentativas):
        try:
            return client.models.generate_content(model=model, contents=contents)
        except errors.APIError as e:
            if e.code not in RETRYABLE or i == tentativas - 1:
                raise
            espera = 2 ** i          # 1s, 2s, 4s, 8s
            print(f"[retry {i+1}] {e.code} — aguardando {espera}s")
            time.sleep(espera)

chat = client.chats.create(
    model="gemini-3.6-flash",
    config=types.GenerateContentConfig(
        system_instruction=SYSTEM,
        temperature=0.2,
    ),
)

print("LOGI - Assistente de Estoque ('sair' para encerrar)\n")

while True:
    try:
        pergunta = input("Voce: ").strip()
    except (KeyboardInterrupt, EOFError):
        break
    if not pergunta:
        continue
    if pergunta.lower() in ("sair", "exit", "quit"):
        break
    try:
        print(f"\nLOGI: {chat.send_message(pergunta).text}\n")
    except Exception as e:
        print(f"\n[ERRO] {e}\n")

print("Encerrado.")
