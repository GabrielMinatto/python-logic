total_spent = 0
over1000 = 0
count = 0
while True:
    count += 1 
    product_name = str(input("Digite o nome do produto: "))
    product_price = float(input("Preço: "))
    while product_price <= 0:
        product_price = float(input(">>Digite um valor válido!! Preço: "))
    if count == 1:
        cheaper = product_price
        cheaper_name = product_name
    if product_price < cheaper:
        cheaper = product_price
        cheaper_name = product_name
    if product_price > 1000:
        over1000 += 1
    total_spent += product_price
    stop = str(input("Deseja continuar [S/N]: ")).strip().upper()[0]
    while stop not in 'SN':
        stop = str(input("Deseja continuar [S/N]: ")).strip().upper()[0]
    if stop == 'N':
        break
print(f'Total gasto na compra foi de R${total_spent}')
print(f'{over1000} produtos custam mais de R$1000')
print(f'O produto mais barato foi {cheaper_name} custando R${cheaper}')

    

