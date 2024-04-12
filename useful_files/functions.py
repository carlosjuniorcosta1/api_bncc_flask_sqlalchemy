
def replace_curr_names(palavra):
    if palavra == "Arte":
        palavra = palavra.replace(palavra, "arte")
    elif palavra == "Língua Portuguesa":
        palavra = palavra.replace(palavra, "portugues")
    elif palavra == "Matemática":
        palavra = palavra.replace(palavra, "matematica")
    elif palavra == "História":
        palavra = palavra.replace(palavra, "historia")
    elif palavra == "Geografia":
        palavra = palavra.replace(palavra, "geografia")
    elif palavra == "Ensino Religioso":
        palavra = palavra.replace(palavra, "ensino_religioso")
    elif palavra == "Ciências":
        palavra = palavra.replace(palavra, "ciencias")
    elif palavra == "Educação Física":
        palavra = palavra.replace(palavra, "educacao_fisica")
    elif palavra == "Língua Inglesa":
        palavra = palavra.replace(palavra, "ingles")
    return palavra 
  