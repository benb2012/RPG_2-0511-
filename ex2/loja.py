"""
loja.py - Regras da loja do jogo.

O catálogo é uma LISTA de itens:
    [{"nome": "Poção de Vida", "tipo": "Poção", "preco": 15}, ...]

O herói é um DICIONÁRIO, e o inventário dele é outro dicionário
que diz quantos de cada item ele tem:
    {"nome": "Gork", "ouro": 100, ..., "inventario": {"Poção de Vida": 2}}

TAREFA: complete as funções marcadas com TODO e rode testes_ex2.py.
"""


def buscar_item(catalogo, nome):
    """Procura o item pelo nome (sem diferenciar maiúsculas).
    Devolve o dicionário do item, ou None se não achar.
    Dica: percorra o catálogo com for e compare item["nome"].lower() com nome.lower()"""
    # TODO

    contagem = 0
    for item in catalogo:
        if item['nome'].lower() == nome.lower():
            contagem +=1
            return item 
    if contagem == 0:
        return None
    


def mostrar_catalogo(catalogo):
    """Mostra os itens da loja, numerados a partir de 1, por exemplo:
        1. Poção de Vida      Poção       15 moedas"""
    # TODO
    contagem = 1
    for item in catalogo:
        print(f"{contagem}. {item['nome']}      {item['tipo']}      {item['preco']}")
        contagem +=1
    raise NotImplementedError


def mostrar_inventario(heroi):
    """Mostra o ouro e os itens do herói. (PRONTA)"""
    print(f"{heroi['nome']} tem {heroi['ouro']} moedas.")
    if len(heroi["inventario"]) == 0:
        print("Inventário vazio.")
    for nome, quantidade in heroi["inventario"].items():
        print(f"  {quantidade} x {nome}")


def comprar(heroi, catalogo, nome, quantidade=1):
    # Tenta comprar um item. Altera o herói e devolve uma mensagem.

    # Passos:
    #   1. Busque o item com buscar_item. Se não achar, devolva
    #      "Esse item não existe na loja."
    item = buscar_item(catalogo, nome)
    if item == None:
            return "Esse item não existe na loja."


    #   2. Se quantidade for menor que 1, devolva "Quantidade inválida."
    if quantidade < 1:
        return "Quantidade inválida."
    #   3. custo = preço do item * quantidade. Se o herói não tiver ouro suficiente,
    #      devolva f"Ouro insuficiente: custa {custo} e você tem {heroi['ouro']}."
    custo = item['preco'] * quantidade
    if heroi['ouro'] < custo:
        return f"Ouro insuficiente: custa {custo} e você tem {heroi['ouro']}."
    
    
    #   4. Tire o custo do ouro do herói.
    heroi['ouro'] -= custo
    #   5. Some a quantidade no inventário (se o item ainda não estiver lá, crie a chave).
    #      Use o nome do CATÁLOGO (item["nome"]), não o que a pessoa digitou.
    
    if item['nome'] not in heroi['inventario']:
        heroi['inventario'][item['nome']] = quantidade
    
    else: heroi['inventario'][item['nome']] += quantidade
    #   6. Devolva f"Comprou {quantidade} x {item['nome']} por {custo} moedas."
    return f"Comprou {quantidade} x {item['nome']} por {custo} moedas."
    # 
    raise NotImplementedError


def vender(heroi, catalogo, nome, quantidade=1):
    # """DESAFIO: vende um item do inventário pela METADE do preço
    # (arredondado para baixo: preço // 2), vezes a quantidade.
    

   


    #   - Item que não existe na loja -> "Esse item não existe na loja."
    item = buscar_item(catalogo, nome)
    if item == None:
        return "Esse item não existe na loja."

    #quantos itens o heroi tem
    tem = heroi["inventario"].get(item["nome"], 0)
    
    #   - Quantidade menor que 1 ou maior do que o herói tem -> f"Você só tem {tem} x {item['nome']}."
    if quantidade < 1 or quantidade > heroi['inventario'][item['nome']]:
        return f"Você só tem {heroi['inventario'][item['nome']]} x {item['nome']}."

    # fazer a venda
    valor = (item["preco"] // 2) * quantidade

    heroi["ouro"] += valor                          
    heroi["inventario"][item["nome"]] -= quantidade 




    
    
    #   - Se a quantidade no inventário chegar a zero, apague o item:
    #     del heroi["inventario"][item["nome"]]
    if (heroi['inventario'][item['nome']]) == 0:
        del heroi["inventario"][item["nome"]]


    
    #   - Devolva f"Vendeu {quantidade} x {item['nome']} por {valor} moedas."

    return f"Vendeu {quantidade} x {item['nome']} por {valor} moedas."
    
    # Dica: heroi["inventario"].get(item["nome"], 0) dá 0 se o herói não tiver o item.
    # """
    # TODO
    raise NotImplementedError
