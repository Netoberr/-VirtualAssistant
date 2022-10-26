import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import requests
import json
import os
from googletrans import Translator


audio = sr.Recognizer()
maquina = pyttsx3.init()
translate=Translator()

def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Ouvindo..')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'ladila' in comando:
                comando = comando.replace('ladila', '')
                maquina.say(comando)
                maquina.runAndWait()

    except:
        print('Microfone não está ok')

    return comando

def comando_voz_usuario():
    comando = executa_comando()
    API_KEY = "4ba56d6d3266c4c9183bc31d24b0c7e0"

    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()
    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'toque' in comando:
        musica = comando.replace('toque','')
        resultado = pywhatkit.playonyt(musica)
        maquina.say(f'Tocando música {musica}')
        maquina.runAndWait()
    elif 'qual a cotação do dólar' in comando:
        requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
        cotacao = requisicao.json()
        maquina.say(f"a cotação do dolár hoje é {cotacao['USD']['bid']} reais")
        maquina.runAndWait()
    elif 'traduza para inglês' in comando:
        texto = comando.replace('traduza para inglês','')
        resultado = translate.translate(texto,'en')
        resultado = resultado.text
        maquina.say(f'{resultado}')
        maquina.runAndWait()
    elif 'qual a previsão do tempo para' in comando:
        cidade = comando.replace('qual a previsão do tempo para','')
        link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"
        requisicao = requests.get(link)
        requisicao_dic = requisicao.json()
        descricao = requisicao_dic['weather'][0]['description']
        temperatura = requisicao_dic['main']['temp'] - 273.15
        maquina.say(f'A previsão do tempo para {cidade} é {descricao} e a temperatura é {temperatura}ºC')
        maquina.runAndWait() 
    elif 'abra o bloco de notas' in comando:
        cmd = 'notepad'
        os.system(cmd) 
        maquina.say('abrindo bloco de notas')
        maquina.runAndWait()  
    elif 'desligue o computador em' in comando:
        timer = comando.replace('desligue o computador em','')
        resultado = pywhatkit.shutdown(timer)
        maquina.say(f'desligando o computador em {timer} segundos')
        maquina.runAndWait() 


comando_voz_usuario()