patrimonio = float(input("Bom dia cliente! Quanto de patrimônio você deseja alcançar para seu futuro ? "))
capital = float(input("Qual o seu capital inicial? "))
aportes = float(input("Quanto você deseja colocar aplicar por mês? "))
taxa = float(input("Qual a taxa de juros mensal aplicada oferecida pelo investimento? "))
                
saldo_atual = capital
meses = 0
                
while saldo_atual < patrimonio:
    print(f"Seu montante atual é de R$ {saldo_atual:.2f} e este é o {meses}º mês.")
    meses += 1
    saldo_atual = (saldo_atual * (1 + taxa/100)) + aportes
    
else:
    print()
    print("Resumo, você precisa investir durante",meses,"meses para alcançar seu objetivo!")
    print("Ou se preferir,",meses//12,"anos e",meses%12,"meses")

