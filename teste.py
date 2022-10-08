import speech_recognition as sr

import os


# Função para ouvir e reconhecer a fala
def ouvir_microfone():
    # habilita o microfone do usuário
    global frase
    microfone = sr.Recognizer()

    # usando o microfone
    with sr.Microphone() as source:

        # chama um algoritmo de redução de ruidos no som
        microfone.adjust_for_ambient_noise(source)

        # frase para o usuário dizer algo
        print('Diga alguma coisa: ')

        # armazena o que foi dito numa variável
        audio = microfone.listen(source)

    try:

        # passa a variável para o algoritmo reconhecedor de padrões
        frase = microfone.recognize_google(audio, language='pt-BR')

        if 'navegador' in frase:
            os.system('start Chrome.exe')

        elif 'Excel' in frase:
            os.system('start Excel.exe')

        # retorna a frase pronunciada
        print('Você disse: ' + frase)

    # se não recoheceu o padrão de fala, exibe a mensagem
    except sr.UnknownValueError:
        print('Não entendi')

        return frase


ouvir_microfone()
