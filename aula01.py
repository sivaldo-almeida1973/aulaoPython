faturamento = 1200
custo = 700

novas_vendas = 800

faturamento = faturamento + novas_vendas
taxa_imposto = 0.1
imposto = taxa_imposto * faturamento

print('Faturamento: ', faturamento)
print('Imposto: ', imposto)
print('custo: ', custo)
print('lucro: ', faturamento - custo - imposto)
