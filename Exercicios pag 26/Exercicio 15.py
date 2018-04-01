condicaoPagamento = int(input("Insira por favor, o codigo da condicao de pagamento: "))
precoVenda = float(input("Digite o valor total da venda: "))

if condicaoPagamento == 3:
    print("O valor da venda eh: R$ %.2f"%(precoVenda))

elif condicaoPagamento == 2:
    print("O valor da venda eh: R$ %.2f"%(precoVenda*0.95))

elif condicaoPagamento == 1:
    print("O valor da venda eh: R$ %.2f"%(precoVenda*0.90JS))

