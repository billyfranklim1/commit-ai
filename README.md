# Commit-AI

## Descrição

Commit-AI é uma ferramenta CLI desenvolvida para auxiliar desenvolvedores a gerar mensagens de commit para Git utilizando a inteligência artificial da OpenAI. É uma ferramenta versátil que pode ser utilizada em qualquer projeto, não sendo limitada apenas a projetos Python.

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

5. Torne o script `commit-ai` executável. Isso pode variar dependendo do seu sistema operacional. Para sistemas baseados em Unix, você pode usar:

```bash
chmod +x commit-ai
```

6. Adicione o diretório do script ao seu PATH para permitir a execução do comando `commit-ai` de qualquer lugar. Você pode adicionar a seguinte linha ao seu `.bashrc`, `.zshrc` ou outro arquivo de configuração de shell correspondente:

```bash
vim ~/.zshrc # Ou ~/.bashrc, ~/.bash_profile, etc.
```

```bash
export PATH="$PATH:/caminho/para/commit-ai"
export OPENAI_API_KEY='sua_chave_de_api_aqui'
```

```bash
source ~/.zshrc # Ou ~/.bashrc, ~/.bash_profile, etc.
```

Lembre-se de substituir `/caminho/para/commit-ai` pelo caminho absoluto do diretório onde o script reside.

## Uso

Após a instalação, navegue até o diretório de qualquer projeto git e execute:

```bash
commit-ai
```

Siga as instruções na tela para selecionar e editar a mensagem de commit sugerida.

## Contribuições

Contribuições são muito bem-vindas! Por favor, veja nosso guia de contribuição para mais detalhes.

## Licença

[MIT](LICENSE.txt)
