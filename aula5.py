# enquanto
# realiza o loop enquanto uma condição for atendida, sendo assim ele deve ser true


#i=0
#while i<10: # enquanto i for menor que 10
#    print("Valor de i: ", i)
#    i+=1 # p valor de i muda a cada rodada sendo somado a ele um valor



while true:
    # strip() = aqui vou limpar os espaços em branco
    # [0] pegando somente a primeira letra
    # lower() transformando em letra minuscula
    resposta=input("Deseja continuar sim ou não").strip()[0].lower()

    if resposta=="n": # entro na condição
        break # posso quebrar meu loop

print("Sai do sistema!")
