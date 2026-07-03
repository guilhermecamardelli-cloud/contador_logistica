import random

elogios = ["rápido", "no prazo", "cuidadoso", "perfeito", "eficiente", "antes_do_prazo", "seguro", "recomendo"]
criticas = ["atrasou", "atrasado", "amassado", "extraviado", "lento", "quebrado", "caro", "sumiu"]

todas_palavras = elogios + criticas

comentarios_simulados = [random.choice(todas_palavras) for _ in range(5000)]

with open("comentarios.txt", "w", encoding="utf-8") as arquivo:
    for comentario in comentarios_simulados:
        arquivo.write(comentario + "\n")