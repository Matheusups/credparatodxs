import PySimpleGUI as sg

def janela_inicial():
    sg.theme('Default')
    layout = [
        [sg.Text('CPF:')],
        [sg.Input(key='cpf')],
        [sg.Text('Diga seu Score Serasa:')],
        [sg.Checkbox('700-799', key="e7"), sg.Checkbox('800-899', key="e8"),
         sg.Checkbox('900-999', key="e9")],
        [sg.Button('Consultar'), sg.Button('Sair')]
    ]
    return sg.Window('Consulte seu Empréstimo', layout=layout, finalize=True)


def janela_consulta9():
    sg.theme('reddit')
    a = 9000
    layout = [
        [sg.Text('Empréstimos:')],
        [sg.Checkbox(f'12x R${a} c/ 4% js.', key='a2'), sg.Checkbox(f'24x R${a} c/ 2%js.', key='a1')],
        [sg.Button('Concluir')]
    ]
    return sg.Window('Ofertas Disponíveis', layout=layout, finalize=True)


def janela_consulta8():
    sg.theme('reddit')
    b = 5000
    layout = [
        [sg.Text('Empréstimos:')],
        [sg.Checkbox(f'12x R${b} c/ 4% js.', key='b2'), sg.Checkbox(f'24x R${b} c/ 2%js.', key='b1')],
        [sg.Button('Concluir')]
    ]
    return sg.Window('Ofertas Disponíveis', layout=layout, finalize=True)


def janela_consulta7():
    sg.theme('reddit')
    c = 3000
    layout = [
        [sg.Text('Empréstimos:')],
        [sg.Checkbox(f'12x R${c} c/ 4% js.', key='c2'), sg.Checkbox(f'24x R${c} c/ 2%js.', key='c1')],
        [sg.Button('Concluir')]
    ]
    return sg.Window('Ofertas Disponíveis', layout=layout, finalize=True)


# janelas inicial
j1, j2, j3, j4 = janela_inicial(), None, None, None
while True:
    window, event, values = sg.read_all_windows()

    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    if window == j1 and event == 'Consultar' and values['e7'] == True:
        j4 = janela_consulta7()
        j1.hide()
    if window == j1 and event == 'Consultar' and values['e8'] == True:
        j3 = janela_consulta8()
        j1.hide()
    if window == j1 and event == 'Consultar' and values['e9'] == True:
        j2 = janela_consulta9()
        j1.hide()
        # score = 900-999
    if window == j2 and event == 'Concluir':
        if values['a2'] == True:
            sg.popup('Seu empréstimo estará disponível em até 24h')
        elif values['a1'] == True:
            sg.popup('Seu empréstimo estará disponível em até 24h')
        # score = 800-899
    if window == j3 and event == 'Concluir':
        if values['b2'] == True:
            sg.popup('Seu empréstimo estará disponível em até 24h')
        elif values['b1'] == True:
            sg.popup('Seu empréstimo estará disponível em até 24h')
        # score = 700-799
    if window == j4 and event == 'Concluir':
        if values['c2'] == True:
            sg.popup('Seu empréstimo de estará disponível em até 24h')
        elif values['c1'] == True:
            sg.popup('Seu empréstimo estará disponível em até 24h')
window.close()