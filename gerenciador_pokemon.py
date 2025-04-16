def espaço():
    print('=' * 40)

def todos(time):
    espaço()
    print(f'{"Código":<6}{"Nome":<15}{"Danos":<25}{"Total":<6}')
    espaço()
    for k, v in enumerate(time):
        print(f'{k:<6}{v["nome"]:<15}{str(v["danos"]):<25}{v["total"]:<6}')
    espaço()

def relatorio(time):
    while True:
        try:
            busca = int(input('Mostrar os dados de qual Pokémon? (digite 99 para sair) '))
        except ValueError:
            print("Número inválido.")
            continue

        if busca == 99:
            break
        elif 0 <= busca < len(time):
            print(f'\nLEVANTAMENTO DO POKÉMON {time[busca]["nome"]}: ')
            for i, g in enumerate(time[busca]["danos"]):
                print(f'  No jogo {i + 1} fez {g} danos')
            espaço()
        else:
            print(f'ERRO! Não existe Pokémon com o código {busca} ')

def batalha(time):
    while True:
        batalha = input('Deseja iniciar uma batalha entre dois Pokémons? [s/n]: ').strip().upper()
        if not batalha or batalha[0] not in 'SN':
            print('Digite S ou N.')
            continue

        if batalha[0] == 'N':
            break

        try:
            p1 = int(input('Código do primeiro Pokémon: '))
            p2 = int(input('Código do segundo Pokémon: '))

            if not (0 <= p1 < len(time)) or not (0 <= p2 < len(time)):
                print('Código inválido!')
                continue

            poke1 = time[p1]
            poke2 = time[p2]

            espaço()
            print(f"BATALHA: {poke1['nome']} VS {poke2['nome']}")
            print(f"{poke1['nome']} causou {poke1['total']} de dano")
            print(f"{poke2['nome']} causou {poke2['total']} de dano")

            if poke1['total'] > poke2['total']:
                print(f"{poke1['nome']} VENCEU A BATALHA!")
            elif poke1['total'] < poke2['total']:
                print(f"{poke2['nome']} VENCEU A BATALHA!")
            else:
                print('EMPATE!')
            espaço()

        except ValueError:
            print('Erro! Insira códigos válidos.')

# ----------------------------
# Programa Principal
# ----------------------------

time = []
campeao = {'nome': '', 'dano': -1}

while True:
    pokemon = {}
    pokemon['nome'] = input('Nome: ')

    while True:
        try:
            tot = int(input(f"Quantas partidas o {pokemon['nome']} jogou? "))
            break
        except ValueError:
            print("Digite um número inteiro válido.")

    danos = []
    for c in range(tot):
        while True:
            try:
                dano = int(input(f'Danos na partida {c + 1}: '))
                danos.append(dano)
                break
            except ValueError:
                print("Número inválido.")

    pokemon['danos'] = danos
    pokemon['total'] = sum(danos)
    time.append(pokemon)

    if pokemon['total'] > campeao['dano']:
        campeao['nome'] = pokemon['nome']
        campeao['dano'] = pokemon['total']

    while True:
        res = input('Deseja continuar [s/n]? ').strip().upper()
        if res and res[0] in 'SN':
            break
        print('Responda com S ou N.')

    if res[0] == 'N':
        break


# Exibição
todos(time)
relatorio(time)
batalha(time)

print(f'\n<<<< FIM DE JOGO! Campeão da rodada: {campeao["nome"]} com {campeao["dano"]} de dano! >>>>')
