# Challenge - Age on Different Planets

  ## Prerequisites

 - Python 3.11+  
 - Docker  
 - Pytest

## Como executar - Execução Local
    git clone https://github.com/anayaml/voxus-challenge
    cd voxus-challenge .
    pip install -r requirements.txt
    python main.py
## Como executar - Docker Image

    git clone https://github.com/anayaml/voxus-challenge
    docker build -t voxus_challenge .
    docker run -it voxus_challenge
Example of a valid input:

    2500000000 (seconds) / "Mars" (type)


# Sobre mim

**Como você começou no mundo da programação?**

> Antes de entrar no curso de Análise e Desenvolvimento de Sistemas, eu
> não tinha um interesse especificamente por programação, mas eu tinha
> alguma experiência com desenvolvimento de mods para alguns jogos.
> Apesar de ser algo mais rústico, foi meu primeiro contato com lógica
> de programação em si.

**Quais foram suas motivações?**

> O que me motivou a entrar no ramo de programação inicialmente foi a
> falta de afinidade que tive com outras profissões e cursos que fui
> pesquisando antes de decidir seguir em TI/Desenvolvimento.

**O que chamou sua atenção?**

> Sempre me chamou atenção o fato de poder atrelar a vontade de resolver
> problemas com cálculos, que são 2 coisas que gosto muito de fazer.

**Para você, qual é a forma mais efetiva de aprender algo novo relacionado à
programação?**

> Acho que a forma mais efetiva de se aprender algo varia bastante de
> pessoa para pessoa. Sou muito motivada pelo que eu não sei. Ter o
> sentimento de precisar entender algo do zero e construir uma base
> sólida de conhecimento é o que me motiva diariamente, seja algo
> relacionado ao trabalho ou não. Gosto de ter um momento de escrever
> tudo que eu preciso entender ao final de determinado tópico, marcar a
> prioridade de cada um deles e a partir daí começar a rotina de estudos
> e prática.

**Defina, na sua percepção, quais características uma pessoa deve ter para ser
considerada boa desenvolvedora?**

Pontos que considero para uma boa pessoa desenvolvedora:
> -   **Gostar/saber ensinar.** Quando se ensina a outra pessoa, fica muito mais fácil perceber pontos de melhora no seu próprio desempenho. Seja técnico ou mais focado em soft skills, por exemplo, como trazer o
> tópico abordado para diferentes níveis de usuários.
> -   **Saber lidar com pessoas.** Não estou falando aqui de ser a pessoa mais sociável do universo, mas saber lidar com pessoas e situações mais complicadas fora do escopo técnico é de extrema importância.
> -   Entender desde o início que **não** existe uma única solução para um problema. 
> -   Não se apegar a uma linguagem de programação. Entendo perfeitamente que todo mundo tem uma linguagem favorita para resolver problemas, mas, eu acho que fecha um leque enorme de possibilidades de aprendizado quando existe o sentimento de recusa em usar algo diferente para resolver um problema.
> - Pergunte sempre, faça *over-communicate*. Não deixe passar nenhuma oportunidade tirar dúvida (não existe dúvida idiota!) e de receber feedback do que está fazendo, como está fazendo. Ser questionado te faz ver tudo por perspectivas diferentes.

## Sobre mim - Projetos Pessoais
De projetos, estou iniciando um que envolve Machine Learning + Kafka. O foco do projeto é buscar dados do X (vulgo Twitter) de jogadores de League of Legends com relação a patch notes do jogo. O foco é usar Kafka para criação de tópicos para recebimento e armazenamento dos tweets encontrados e analisados, além de um consumer que é triggered toda vez que tiver tweet novo e envia para análise. Para a parte de machine learning, será usado NLTK/TensorFlow. A fase atual do projeto é de pré-processamento destes dados pegos da plataforma. O objetivo é formar uma base de dados com tipos de feedback e qual frequência eles são feitos, podendo ser visualizados via Dashboard ou frontend web (talvez react).

[Gathering League of Legends Players Feedback](https://github.com/anayaml/gathering-lol-feedback-data.git)
