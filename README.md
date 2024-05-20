# oito_rainhas
Resolução do problema das oito rainhas utilizando algoritmo genético.

## Descrição do problema
O problema das oito rainhas consiste em conseguir posicionar oito rainhas em um tabuleiro de xadrez sem que nenhum rainha possa atacar nenhuma outra. Ou seja, cada rainha posicionada não pode estar na mesma vertical, horizontal ou diagonal de todas as outras rainhas do tabuleiro. Caso nenhuma rainha possa atacar as demais, o número de pares de rainhas não atacantes será de 28.

## Descrição do algoritmo genético utilizado
Para resolução do problema é considerada uma população de diversos tabuleiros possíveis em que para cada indivíduo da população é calculado o número de rainhas que não se atacam, a intenção é maximizar esse número até que seja atingido 28 pares não atacantes. Para tal, os melhores indivíduos (que possuam menos rainhas atacantes) são selecionados para realizarem 'crossover' e compor a próxima geração de indivíduos. Após algumas gerações é possível atingir o número ótimo de 28 pares de rainhas não atacantes.