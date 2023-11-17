import requests  

url = "https://freegptapi.hop.sh/neural/api" 
while True:
        user_input = input('Sua pergunta: ')
        params = {"query": user_input}
        if user_input.lower() == 'exit':
            break
        
        print('\n\n\nThinking\n\n\n')
        response = requests.get(url, params=params) 
        data = response.json()  
        print(data)
        
        print('\n\n','for exit press: ctrl + z')