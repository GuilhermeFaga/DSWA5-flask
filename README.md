## Configurações de entrega contínua no PythonAnyWhere

### Referências 

[Deploying to PythonAnywhere via GitHub](https://medium.com/@aadibajpai/deploying-to-pythonanywhere-via-github-6f967956e664)
[syncing Github with Pythonanywhere](https://stackoverflow.com/a/54268132/9044659)

### No Github

1. Criação de um webhook com o endpoint `https://{username}.pythonanywhere.com/api/update_server` e de um secret.

### No seu repositório

1. Criação do arquivo `requirements.txt` com as dependências do projeto
```bash
touch requirements.txt
echo "flask" > requirements.txt
echo "gitpython" > requirements.txt
echo "python-dotenv" > requirements.txt
```

2. Criação da função Helper `is_valid_signature`
```python
import hmac
import hashlib

def is_valid_signature(x_hub_signature, data, private_key):
    # x_hub_signature and data are from the webhook payload
    # private key is your webhook secret
    hash_algorithm, github_signature = x_hub_signature.split('=', 1)
    algorithm = hashlib.__dict__.get(hash_algorithm)
    encoded_key = bytes(private_key, 'latin-1')
    mac = hmac.new(encoded_key, msg=data, digestmod=algorithm) # type: ignore
    return hmac.compare_digest(mac.hexdigest(), github_signature)
```

3. Endpoint `/api/update_server` para atualizar o servidor
```python
from flask import request, Blueprint
from git import Repo

from helpers.check_signature import is_valid_signature

import traceback
import os

app.route('/update_server', methods=['POST'])
def webhook():
    try:
        GITHUB_WEBHOOK_TOKEN = os.getenv("GITHUB_WEBHOOK_TOKEN")
        x_hub_signature = request.headers.get('X-Hub-Signature')

        if x_hub_signature is None:
            return 'Missing X-Hub-Signature', 400
        
        if not x_hub_signature.startswith('sha1='):
            return 'Invalid X-Hub-Signature', 400
        
        if not is_valid_signature(x_hub_signature, request.data, GITHUB_WEBHOOK_TOKEN):
            return 'Invalid X-Hub-Signature', 400
        
        repo = Repo('./mysite')
        git = repo.git
        git.checkout('main')
        git.pull()
        return 'Updated PythonAnywhere successfully', 200
    except Exception as e:
        return traceback.format_exc(), 500
```

### No PythonAnyWhere

1. Habilitar HTTPS para seu Web App

2. Configuração do ambiente via Bash
```bash
# Clonar o repositório
git clone {seu_repositorio}
mv {seu_repositorio} ~/mysite

# Criação do .env
cd ~/mysite
touch .env
echo "GITHUB_WEBHOOK_TOKEN={seu_secret}" >> .env

# Criação do hook pull-merge para atualizar o servidor
cd ~/mysite/.git/hooks
touch post-merge
echo "pip install -r ~/mysite/requirements.txt" >> post-merge
echo "touch /var/www/{username}_pythonanywhere_com_wsgi.py" >> post-merge
```

## Rodar localmente

### Instalar virtualenv
```bash
apt install python3.10-venv
```

### Criar `venv`
```bash
python -m venv ./venv
```

### Ativar `venv`
```bash
source ./venv/bin/activate
```

### Instalar dependências
```bash
pip install -r requirements.txt
```

### Executar o Flask
```bash
flask --app flask_app.py --debug run
```