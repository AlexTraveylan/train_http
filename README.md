# App d'entraiement pour requete HTTPs

## Objectif

Hack le classement

## Version

Developpement en python 3.12.1

## Clone
    
```bash
git clone git@github.com:AlexTraveylan/train_http.git
cd train_http
```

## Installation

```bash
python -m env venv
env\Scripts\activate
pip install -r requirements.txt
```

## Exemple utilisation docker 
> docker build -t httptrain . 
> docker run -t httptrain 

> docker compose up 

See the ip of the container with : 
> docker inspect httptrain | grep IPAddress
Acces in the browser : {ip_adress}:5000

