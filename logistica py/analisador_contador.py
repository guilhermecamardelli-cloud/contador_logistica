from collections import Counter
with open("comentarios.txt", "r", encoding="utf-8") as arquivo:
    palavras = [linha.strip().lower() for linha in arquivo if linha.strip()]

contador_palavras = Counter(palavras)
top_3 = contador_palavras.most_common(3)

print("=" * 50)
print("     RODOLFO EXPRESS - ANÁLISE DE FEEDBACK    ")
print("=" * 50)
print(f"Total de entregas avaliadas: {len(palavras)}\n")
print("Principais indicadores citados pelos clientes:")

for posicao, (palavra, frequencia) in enumerate(top_3, start=1):
    porcentagem = (frequencia / len(palavras)) * 100
    print(f"{posicao}º lugar: '{palavra}' -> {frequencia} menções ({porcentagem:.1f}%)")
print("=" * 50)