import requests
import time
from colorama import Fore

url = "https://freegptapi.hop.sh/neural/api"
ascii_art = '''
                                                                    
    //    / /                          //   ) )  //   ) ) /__  ___/ 
   //___ / /  ___     //  ___         //        //___/ /    / /     
  / ___   / //___) ) // //   ) )     //  ____  / ____ /    / /      
 //    / / //       // //___/ /     //    / / //          / /       
//    / / ((____   // //           ((____/ / //          / /    
'''

print(Fore.BLUE + ascii_art)

print(Fore.BLUE + 'Welcome to Help GPT, the script that assists you with AI in resolving queries regarding EF Core and Z.EntityFramework.Extensions!')
time.sleep(4)
print('\n\n')

while True:
    user_input = input(Fore.RED + 'Your question: ')
    params = {"query": user_input}
    if user_input.lower() == 'exit':
        break

    print('\n\n\nThinking... Wait\n')
    print('For exit press: ctrl + z')
    response = requests.get(url, params=params)
    data = response.json()
    print(Fore.GREEN + str(data))  # converted data to string for printing

