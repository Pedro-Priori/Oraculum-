# Projeto Oraculum – Criando um chat que conversa com meus dados

Bem-vindo ao meu projeto "Oraculum"!

Este é o resultado de uma jornada de aprendizado incrível, onde desenvolvi uma aplicação de chat interativa capaz de conversar com diversas fontes de dados. O objetivo principal foi criar uma ferramenta poderosa e flexível para extrair informações valiosas de documentos, transformando dados brutos em diálogos inteligentes.

## 🚀 O que é o projeto?

No projeto "Oráculo", eu desenvolvi uma interface de conversação que me permite interagir com uma variedade de dados, incluindo vídeos do YouTube, arquivos CSV, PDFs e TXT. Com a flexibilidade de escolher entre provedores de modelos de linguagem, como a Grok (gratuito) e a OpenAI (pago), pude personalizar a experiência de conversação de acordo com as minhas necessidades.

Este projeto foi inspirado por uma aplicação criada pelo professor Rodrigo e, motivado pelo interesse da comunidade, decidi aprofundar e expandir suas capacidades. Adicionei novas funcionalidades e aumentei a flexibilidade, permitindo que o chat não apenas responda a perguntas, mas também se torne uma ferramenta poderosa de análise e extração de informações.

## 🧠 O que eu aprendi

Durante o desenvolvimento do "Oráculo", adquiri conhecimentos práticos em tecnologias de ponta e reforcei conceitos importantes de programação e inteligência artificial. Aqui estão os principais aprendizados:

* **Configuração do Ambiente:** Iniciei o projeto configurando meu ambiente de desenvolvimento do zero, preparando toda a estrutura necessária para construir a aplicação de chat.

* **Desenvolvimento do WebApp em Streamlit:** Criei uma interface de usuário amigável utilizando Streamlit. Desenvolvi uma *sidebar* (barra lateral) que permite selecionar e carregar arquivos, além de escolher o modelo de linguagem a ser utilizado, tornando a experiência muito mais intuitiva.

* **Integração com LangChain:** Aprendi a usar a biblioteca LangChain para conectar minha aplicação a grandes modelos de linguagem (LLMs). Essa ferramenta foi fundamental para orquestrar a lógica de conversação e o processamento dos dados.

* **`Document Loaders`:** Descobri como carregar e processar diferentes tipos de arquivos de forma eficiente. Utilizei os `document loaders` do LangChain para facilitar a leitura e a interpretação de dados de fontes variadas como PDFs, CSVs e transcrições de vídeos.

* **Construção da `Chain` de Conversação:** Desenvolvi a lógica principal do chat, conhecida como `chain`. Essa foi a parte em que construí o fluxo que permite à aplicação processar as minhas perguntas e respondê-las com base nas informações contidas nos documentos carregados.

* **Finalização do Projeto:** Integrei todos os componentes — a interface do usuário, a lógica de processamento e os modelos de IA — para criar uma aplicação coesa e funcional. O resultado é o "Oráculo", pronto para transformar informações em conversas significativas!

## 🛠️ Como o projeto funciona

O fluxo da aplicação é simples e direto:

1.  **Seleção do Modelo:** Na barra lateral, eu escolho qual modelo de linguagem desejo usar (Grok ou OpenAI).
2.  **Upload dos Dados:** Faço o upload de um arquivo (PDF, CSV, TXT) ou insiro o link de um vídeo do YouTube.
3.  **Processamento:** A aplicação utiliza os `document loaders` para ler e interpretar o conteúdo.
4.  **Interação:** Com os dados carregados, eu posso iniciar uma conversa, fazendo perguntas diretamente no chat.
5.  **Geração de Respostas:** A `chain` de conversação processa minha pergunta, busca a resposta nos dados carregados e utiliza o LLM selecionado para gerar uma resposta em linguagem natural.

Este projeto foi uma experiência fantástica que me permitiu explorar na prática o potencial da inteligência artificial e da manipulação de dados.
