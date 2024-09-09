import requests

def run():
    response = requests.post('http://localhost:5000/hello', json={"name": "World"})
    print("REST client received: " + response.json()['message'])

if __name__ == '__main__':
    run()
