import requests
import time
from colorama import Fore
import webbrowser
import textwrap


url = "https://freegptapi.hop.sh/neural/api"
ascii_art = '''
                                                                    
    //    / /                          //   ) )  //   ) ) /__  ___/ 
   //___ / /  ___     //  ___         //        //___/ /    / /     
  / ___   / //___) ) // //   ) )     //  ____  / ____ /    / /      
 //    / / //       // //___/ /     //    / / //          / /       
//    / / ((____   // //           ((____/ / //          / /    
'''

print(Fore.WHITE + ascii_art)

print(Fore.WHITE + 'Welcome to Help GPT, the script that assists you with AI in resolving queries regarding EF Core and Z.EntityFramework.Extensions!')
time.sleep(4)
print(Fore.WHITE + '\n\nselect an option')
print(Fore.WHITE + '\n [1] Assistent with IA \n [2] Config \n [3] Github (credits) \n [4] Exit')
num = int(input("Typing a option: "))

if num == 1:
    print('\n\n\n All right, make your question \n')
    while True:
        user_input = input(Fore.RED + 'Your question: ')
        params = {"query": user_input}
        if user_input.lower() == 'exit':
            break

        print('\n\n\nThinking...')
        print('For exit press: ctrl + z')
        response = requests.get(url, params=params)
        data = response.json()

        if 'answer' in data:
            answer_text = data['answer']
            formatted_text = textwrap.fill(answer_text, width=80)  # Ajuste a largura conforme desejado
            print(Fore.GREEN + formatted_text)

if num == 2:
    print('Sorry, this option has not yet been developed')

if num == 3:
    print('visit the github ')
    print(url)
    url = 'https://github.com/NeuronNix/HelpGPT'
    time.sleep(3)
    webbrowser.open(url)

if num == 4:
    print('Bye - Bye')
    ascii_art = '''
⠀⠀⠀⢀⡴⠟⠛⢷⡄⠀⣠⠞⠋⠉⠳⡄⠀⠀⠀⠀
⠀⠀⠀⣸⠁⠀⠀⠈⣧⢰⠇⠀⠀⠀⢠⡇⠀⠀⠀⠀
⠀⠀⠀⠸⣆⠀⠀⠀⠘⣿⠀⠀⠀⠀⡞⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠹⣦⠀⠀⠀⠘⡄⠀⠀⠀⡇⠀⠀⠀⠀⠀
⠀⠀⠀⡴⠚⠙⠳⣀⡴⠂⠁⠒⢄⠀⢿⡀⠀⠀⠀⠀
⠀⠀⢸⡇⠀⢀⠔⠉⠀⠀⠀⡀⠀⠂⠘⣇⠀⠀⠀⠀
⠀⠀⠀⢳⡀⠘⢄⣀⣀⠠⠶⠄⠀⠀⠀⡿⠀⠀⠀⠀
⠀⠀⠀⠀⠻⣕⠂⠁⠀⠀⠀⠀⠀⠀⣰⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠹⣅⠒⠀⠒⠂⠐⠒⢉⡼⢁⣤⠀⠀⠀
⠀⢀⣼⣻⣆⣤⢈⣙⣒⠶⠶⣶⣞⢿⣸⡟⠳⣾⣂⣤
⠸⢿⣽⠏⢠⡿⠋⣿⣭⢁⣈⣿⣽⣆⠙⢷⣄⠙⠋⠁
⠀⠀⠀⠀⠛⠃⠰⠿⣤⠄⠀⠸⠷⠟⠀⠀⠁⠀⠀⠀
'''
print(ascii_art)
time.sleep(2)