import requests

response = requests.get('https://randomfox.ca/floof')
#print(response.status_code) #output: 200
#print(response.text) #output: {"image":"https:\/\/randomfox.ca\/images\/1.jpg","link":"https:\/\/randomfox.ca\/?i=1"}

print(response.json()) #output: {'image': 'https://randomfox.ca/images/1.jpg', 'link': 'https://randomfox.ca/?i=1'}

fox = response.json() 
print(fox['image']) #output: https://randomfox.ca/images/1.jpg





