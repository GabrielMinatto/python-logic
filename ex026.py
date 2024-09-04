
speed = int(input('Digite a velocidade que passou no radar em km/h: '))

if speed > 80:
    speed_ticket = (speed - 80) * 7
    print(f"Você receberá uma multa de R$ {speed_ticket}")
else:
    print(f"Você não será multado")