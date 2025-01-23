# Documentação do Aplicativo Flask com Execução de Script VBS

# Introdução
Este documento descreve o funcionamento e a implementação técnica de um script Python que utiliza o framework Flask para criar uma API RESTful para integração de uma balança de pesagem com um sistema de software. O script interage com a balança por meio de um executável externo e um arquivo VBS (Visual Basic Script).

# Requisitos de Sistema
* Python 3.x instalado
* Biblioteca Flask instalada (**pip install Flask**)
* Windows (por causa do uso do Visual Basic Script e do executável externo)

# Funcionalidades
Este script Python implementa um servidor Flask que disponibiliza uma rota **/load-scale** para ler os dados de peso de uma balança de pesagem. As principais funcionalidades são:

1. Inicia o servidor Flask.
2. Ao acessar a rota **/load-scale**, executa um executável externo que se comunica com a balança.
3. Executa um script VBS para processar os dados da balança.
4. Retorna os dados de peso da balança em formato JSON.

# Implementação Detalhada
## Bibliotecas Utilizadas
* **Flask**: Utilizado para criar o servidor web e gerenciar as rotas.
* **os**: Utilizado para realizar operações de sistema operacional, como verificar a existência de arquivos.
* **subprocess**: Utilizado para executar comandos externos ao Python, neste caso, para executar o executável e o script VBS.

# Variáveis Globais
* **filename**: Caminho do arquivo onde os dados de peso da balança são armazenados.
* **vbs_file**: Caminho do arquivo VBS (Visual Basic Script) utilizado para processar os dados da balança.
* **exe_file**: Caminho do executável que interage diretamente com a balança.

# Função read_file()
* Esta função é a view principal que é chamada quando a rota **/load-scale** é acessada.
* Utiliza **subprocess.run()** para executar o executável externo **vbpBalanca.exe** que interage com a balança.
* Em seguida, executa o script VBS **script.vbs** para processar os dados da balança.
* Verifica se o arquivo onde os dados foram gravados pela balança existe.
* Se o arquivo existe, lê os dados do arquivo e retorna um objeto JSON contendo as unidades de peso (kg) e o valor do peso.
* Se o arquivo não existe, retorna um objeto JSON indicando um erro de arquivo não encontrado.

# Função __main__
Inicia o servidor Flask na porta **5000**, tornando-o acessível a partir de qualquer interface de rede (**0.0.0.0**).

# Conclusão
Este documento fornece uma visão geral detalhada do funcionamento e implementação técnica do script Python que integra uma balança de pesagem com um sistema de software por meio de uma API RESTful usando Flask. O script executa comandos externos para interagir com a balança e processa os dados para fornecer uma resposta JSON através da rota **/load-scale**.
