GERADOR DE COMENTARIOS

import random

elogios = ["rápido", "no prazo", "cuidadoso", "perfeito", "eficiente", "antes_do_prazo", "seguro", "recomendo"]
criticas = ["atrasou", "atrasado", "amassado", "extraviado", "lento", "quebrado", "caro", "sumiu"]

todas_palavras = elogios + criticas

comentarios_simulados = [random.choice(todas_palavras) for _ in range(5000)]

with open("comentarios.txt", "w", encoding="utf-8") as arquivo:
    for comentario in comentarios_simulados:
        arquivo.write(comentario + "\n")


ANALISADOR CONTADOR

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










Comando	Para que serve?	Exemplo Prático
Counter(lista)	Inicializar a contagem: Transforma qualquer lista de palavras em um dicionário de frequências automaticamente.	meu_contador = Counter(palavras)
most_common(n)	Rankear os top resultados: Traz os n elementos mais repetidos da lista e a quantidade de vezes que apareceram.	meu_contador.most_common(3)
update(nova_lista)	Somar novos dados: Adiciona novos elementos a uma contagem que já existe, atualizando os totais.	meu_contador.update(["atraso", "perfeito"])











