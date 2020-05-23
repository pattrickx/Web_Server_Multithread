# Web Server Multi Thread  
* Maria Eduarda de Otôni Espíndola Rocha;
* Patrick Martins de Lima;
* Rafael Almeida Albuquerque.

Servidor criado multi thread criado com python para executar os principais comandos do http baseado no [RFC 1945](https://tools.ietf.org/html/rfc1945).

### Inicializando 
Para inicializar basta abrir a pasta com na ide de python de sua preferencia e executar o arquivo *`server.py`*.
## GET
Faça o GET para o localhost:45654 e será retornado uma pagina html.

## HEAD
Faça o HEAD para o localhost:45654 e será retornado o cabeçalho com dados sobre o arquivo html.

## POST
Adicione uma mensagem no corpo com o seguinte padrão:
```
 chave=valor&msg=mensagem
``` 
Será inicializado um arquivo `post_index.txt` para armazenar chaves e valores salvos, caso esse arquivo já exista, ele será lido e transformado em um dicionario.

A mensagem será dividida em "&" para separar cada nova entrada de chave e valor.

Em seguida, a chave e valor serão divididos pelo caractere "=" e o valor será salvo no dicionario com a chave respectiva

Finalmente o dicionario será lido e salvo seus valores no arquivo post_index, onde cada entrada é uma linha e chave e valor estão separados por "=" .