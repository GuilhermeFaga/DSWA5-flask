Instalar virtualenv
```bash
apt install python3.10-venv
```

Criar `venv`
```bash
python -m venv ./venv
```

Ativar `venv`
```bash
source ./venv/bin/activate
```

Instalar dependências
```bash
pip install -r requirements.txt
```

Executar o Flask
```bash
flask --app flask_app.py --debug run
```