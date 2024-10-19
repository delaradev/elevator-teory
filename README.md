# Elevator Theory

## 💭 Definição

Em uma cidade, existe um prédio de 6 andares, sendo que no primeiro andar está o térreo, sem apartamentos, e os demais 5 andares possuem 3 apartamentos cada.


    ________________
    | __ | __ | __ |
    | 13 | 14 | 15 |
    | __ | __ | __ |
    | 10 | 11 | 12 |
    | __ | __ | __ |
    | 07 | 08 | 09 |
    | __ | __ | __ |
    | 04 | 05 | 06 |
    | __ | __ | __ |
    | 01 | 02 | 03 |
    | __ | __ | __ |
    |              |
    | TÉ   RR   EO |
    | __   __   __ |



---



### Regras Específicas do Prédio

1. **Acesso ao Elevador**: Para entrar ou sair de seu apartamento, as pessoas só podem utilizar o elevador. Não existe nenhuma outra forma de ingressar ou sair senão utilizando o elevador.

2. **Capacidade do Elevador**: O elevador transporta somente uma pessoa por viagem.

3. **Sem Visitas**: As pessoas desse prédio não visitam seus vizinhos; elas somente entram no prédio e ocupam um andar, e saem dele, desocupando o apartamento.

4. **Alojamento Único**: Os apartamentos só comportam uma pessoa por vez.



## 🌟 Objetivo do Projeto

O objetivo deste projeto é desenvolver cálculos que estimem a **eficiência energética**, analisando a relação entre o **gasto energético** e a **velocidade de resposta** do sistema.



## 🛠️ Estrutura do Projeto

O projeto é dividido em duas fases principais:

### 1. Simulação de Viagens Aleatórias
Nesta fase inicial, o sistema gera viagens de elevador de forma **aleatória**, permitindo simular cenários de utilização cotidianos.

### 2. Estratégias de Movimentação Forçada
Na segunda fase, o elevador adota **estratégias de movimentação forçada**. Ou seja, o elevador pode se deslocar para áreas onde é mais provável que novas solicitações de viagem ocorram, mesmo que não haja passageiros no momento.



## 📊 Cenário de Exemplo

Para ilustrar a lógica do projeto, considere o seguinte cenário:

1. O prédio está vazio, e o elevador também se encontra sem passageiros no andar térreo.
2. Um usuário solicita uma viagem do **térreo** para o **4º andar**.
3. Após essa viagem, o elevador fica vazio no 4º andar, enquanto 14 pessoas ainda podem ingressar no prédio a partir do térreo.
4. Apenas uma pessoa no 4º andar pode querer descer.



### Decisões do Elevador

- **Descer vazio para o térreo**: Visto que podem haver 14 pessoas possivelmente desejando ingressar no prédio, essa decisão pode parecer uma boa opção para aumentar a velocidade de resposta;
- Porém, se o elevador descer vazio, e a próxima chamada for no 4º andar, para descer a única pessoa que está no prédio, terá ocorrido um gasto energético desnecessário, além de um tempo de resposta muito maior, reduzindo a eficiência;



## 🔍 Conclusão

"ainda não foi possível obter resultados"



## 📌 Tecnologias Utilizadas

- Python



## 📁 Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/delaradev/elevator-teory.git
2. Navegue até o diretório do projeto:
    ```bash
    cd elevator-teory
3. Execute o projeto:
    ```bash
    python main.py