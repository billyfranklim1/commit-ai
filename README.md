# Commit-AI

Commit-AI é uma ferramenta de linha de comando (CLI) desenvolvida para auxiliar desenvolvedores a gerar mensagens de commit para Git utilizando a inteligência artificial da OpenAI. É uma ferramenta versátil, aplicável a qualquer projeto, independentemente da linguagem de programação.

## Instalação

### Pré-requisitos

- Git
- Python 3.6 ou superior

### Passos para Instalação

1. Clone o repositório do Commit-AI para sua máquina local:

   ```bash
   git clone https://github.com/billyfranklim1/commit-ai.git
   ```

2. Navegue até o diretório do projeto clonado:

   ```bash
   cd commit-ai
   ```

3. (Opcional) Crie e ative um ambiente virtual Python para evitar conflitos de dependências:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

4. Instale as dependências necessárias:

   ```bash
   pip install -r requirements.txt
   ```

5. Torne o script `commit-ai` executável:

   ```bash
   chmod +x commit-ai
   ```

6. Adicione o diretório do script ao seu PATH para permitir a execução do comando `commit-ai` de qualquer lugar. Adicione a seguinte linha ao seu arquivo de configuração de shell (e.g., `.bashrc`, `.zshrc`):

   ```bash
   vim ~/.zshrc  # Ou ~/.bashrc, ~/.bash_profile, etc.
   ```

   Adicione a seguinte linha:

   ```bash
   export PATH="$PATH:/caminho/para/commit-ai"
   export OPENAI_API_KEY='sua_chave_de_api_aqui'
   ```

   Recarregue o arquivo de configuração do shell:

   ```bash
   source ~/.zshrc  # Ou ~/.bashrc, ~/.bash_profile, etc.
   ```

   Substitua `/caminho/para/commit-ai` pelo caminho absoluto do diretório onde o script está localizado e `sua_chave_de_api_aqui` pela sua chave de API do OpenAI.

## Uso

Após a instalação, navegue até o diretório de qualquer projeto Git e execute:

```bash
commit-ai
```

Siga as instruções na tela para selecionar e editar a mensagem de commit sugerida.

## Contribuições

Contribuições são muito bem-vindas! Por favor, veja nosso [guia de contribuição](CONTRIBUTING.md) para mais detalhes sobre como você pode ajudar a melhorar esta ferramenta.

## Licença

Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo [LICENSE](LICENSE.txt) para mais detalhes.
