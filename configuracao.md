# Passo a passo para configuração do ambiente e API da balança

1. Verificar a instalação do Python
Execute o comando para confirmar a versão instalada:

**python --version**

2. Adicionar o arquivo **app.py**

Coloque o arquivo **app.py** na pasta da balança:

**C:\balanca\load-scale**

3. Criar um ambiente virtual (env)

Na pasta da balança, crie um ambiente virtual:

* python -m venv env
* env\Scripts\activate

4. Instalar as bibliotecas necessárias

Com o ambiente virtual ativado, instale as dependências:
**pip install -r requirements.txt**

5. Adicionar o **nssm**

Copie o nssm para a raiz do disco:
# C:\

6. Adicionar o **nginx**

Copie o **nginx** para a raiz do disco:
# C:\

7. Configurar o **nginx**

* Acesse a pasta de configuração:
**C:\nginx-1.26.2\conf**

* Substitua o arquivo **nginx.conf** pelo arquivo correto disponível no repositório.

8. Criar o serviço com o **nssm**

* Acesse o diretório do **nssm**:
**C:\nssm-2.24\win64**

* Crie o serviço executando:
**nssm install <nome-do-serviço>**

* Na tela de configuração que será exibida, preencha os campos:

    * Path:
    **C:\balanca\load-scale\env\Scripts\python.exe**

