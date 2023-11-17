import requests  

url = "https://freegptapi.hop.sh/neural/api" 
params = {"query": input('your question: ') }
print('\n\nThinking...\n\n')
response = requests.get(url, params=params) 
data = response.json()  

print(data)