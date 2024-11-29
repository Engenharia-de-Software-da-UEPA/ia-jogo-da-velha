# Tic Tac Toe AI 🌟
Este projeto é um jogo da velha (Tic Tac Toe) controlado por uma inteligência artificial desenvolvida em Python e acessível via web utilizando Django. Você pode jogar contra a IA diretamente no navegador, inclusive de qualquer lugar da internet, configurando o acesso via Ngrok.

## 1. Clone o Repositório
```bash
git clone https://github.com/Engenharia-de-Software-da-UEPA/ia-jogo-da-velha.git
cd ia-jogo-da-velha-main
```

# 2. Instale as Dependências
```bash
pip install -r requirements.txt  
```

## 3. Inicie o Ngrok
Abra um terminal e execute o comando:
```bash
ngrok http 8000
```
Copie o link gerado pelo Ngrok, por exemplo:

```bash
https://0f69-187-73-106-27.ngrok-free.app 
```

## 4. Configure o Ngrok no Projeto
No arquivo settings.py, adicione o link gerado pelo Ngrok à variável ngrok. Por exemplo:
```python
ngrok = "0f69-187-73-106-27.ngrok-free.app"
```

## 5. Inicie o Servidor Django
Execute o comando para rodar o servidor:
```bash
python manage.py runserver
```

## 6. Acesse o Jogo
Localmente: http://127.0.0.1:8000/
Via Ngrok: por exemplo: https://0f69-187-73-106-27.ngrok-free.app/

## Melhorias Futuras
Melhorar a interface com animações e efeitos sonoros.
Implementar modos de dificuldade na IA.
Adicionar suporte a multiplayer online.

## Contribua
Contribuições são bem-vindas! Faça um fork deste repositório e envie um pull request.

## Contato
Caso tenha dúvidas, sugestões ou precise de ajuda, não hesite em entrar em contato comigo! Estou à disposição para ajudar.

Email: feliperaphaelpara@gmail.com
LinkedIn: https://www.linkedin.com/in/frcelipe7
GitHub: https://github.com/frcelipe7
Site: https://frcelipe7.github.io