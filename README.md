[![Build Status](https://travis-ci.org/Dineshs91/crawler.svg?branch=test)](https://replit.com/@MayconDouglas24)

# Scripts em Python para Busca de Diretórios e Subdomínios

Este repositório contém dois scripts em Python que podem ser usados para buscar diretórios e subdomínios em um site.

## Script `diretorio.py`

O script `diretorio.py` é projetado para buscar diretórios em um site. Ele oferece as seguintes funcionalidades:

- Realiza uma busca em um site especificado em busca de diretórios.
- Pode ser configurado para buscar em profundidade, definindo o nível máximo de recursão.
- Fornece opções de saída flexíveis, como salvar os resultados em um arquivo de texto.
- É altamente configurável e pode ser usado para automatizar a identificação de diretórios em um site.

### Uso:

```bash
python diretorio.py -u <URL_do_site> -d <profundidade_de_busca> -o <arquivo_de_saida>
```

## Script `subdominio.py`

 O script `subdominio.py` é projetado para buscar subdomínios em um site. Ele oferece as seguintes funcionalidades:

- Realiza uma busca em um site especificado em busca de subdomínios.
- Suporta uma lista de subdomínios predefinidos para uma busca mais rápida.
- Oferece opções de saída flexíveis, como salvar os resultados em um arquivo de texto.
- É altamente configurável e pode ser usado para automatizar a identificação de subdomínios em um site.

### Uso:

```bash
python subdominio.py -u <URL_do_site> -l <lista_de_subdominios> -o <arquivo_de_saida>
```

### Pré-requisitos
- Antes de usar esses scripts, certifique-se de ter instalado Python em seu sistema.

### Contribuições
- Contribuições são bem-vindas! Sinta-se à vontade para melhorar esses scripts ou adicionar novos recursos.

### Autor
- Este projeto é mantido por Maycon Douglas.
- email: mayconwiner@gmail.com

### Licença

Lembre-se de substituir `<URL_do_site>`, `<profundidade_de_busca>`, `<arquivo_de_saida>`, `<lista_de_subdominios>` e `[Seu Nome]` com os valores e informações relevantes para seus scripts. Certifique-se também de incluir um arquivo `LICENSE` na raiz do seu repositório com os termos da licença que deseja aplicar ao seu código.

Este projeto é licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.
