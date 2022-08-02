# Silvia
Analisi stabilità veicolo tramite accelerometro

Obbiettivi: 
1) identificare un intervallo temporale in cui il processo stocastico \left ( X_t \right )_{t \in \mathbb{Z}} avente come valori i dati dell'accelerometro sia stazionario
2) analizzare i dati

Lessico: 
- fz. di autocovarianza: indica quanto 'due variabili di un processo stocastico co-variano nel tempo', cioè variano insieme [vedi tesi, p.4]
- fz. di autocorrelazione: in pratica è la fz. di autocovarianza normalizzata
- processo stocastico stazionario: esso ha 'momenti secondi finiti, valore atteso costante e autocovarianza non dipendente dal tempo' [vedi tesi, p.4]

In generale: per un processo stazionario
- la fz. (matrice) di autocovarianza è simmetrica rispetto all'origine (alla diagonale principale)
- la funzione di autocorrelazione dipende solo dal passo $h$ tra i due istanti temporali

Idee per valutazione: 
- trovare raggruppamento dei dati oppure passo temporale t.c. l'autocovarianza (autocorrelazione) campionaria per un oscillazione abbia valore atteso costante