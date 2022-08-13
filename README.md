# Silvia
Analisi stabilità veicolo tramite accelerometro

Obbiettivi: 
1) identificare un intervallo temporale in cui il processo stocastico $\left ( X_t \right )_{t \in \mathbb{Z}}$ avente come valori i dati dell'accelerometro sia stazionario
2) analizzare i dati

Lessico: 
- fz. di autocovarianza: indica quanto 'due variabili di un processo stocastico co-variano nel tempo', cioè variano insieme [vedi tesi, p.4]
- fz. di autocorrelazione: in pratica è la fz. di autocovarianza normalizzata
- processo stocastico stazionario: esso ha 'momenti secondi finiti, valore atteso costante e autocovarianza non dipendente dal tempo' [vedi tesi, p.4]

In generale: per un processo stazionario
- la fz. (matrice) di autocovarianza è simmetrica rispetto all'origine (alla diagonale principale)
- la funzione di autocorrelazione dipende solo dal passo $h$ tra i due istanti temporali

Per il segnale test del seno + rumore gaussiano ($\mu=0$, $\sigma=5$), anche detto 'rumore bianco' (white noise):
- db4 wavelet funziona bene quando il segnale non oscilla troppo velocemente (tipo per vel. angolare $\omega = 1$), male invece per $\omega=50$)
- il rumore si ripercuote sulla componente $0$ della trasformata di Fourier (e quindi anche sullo spettro di potenza), mentre il segnale vero e proprio (il seno) con $\omega = 1$ si 'scarica' ovviamente sulla prima componente dell'espansione di Fourier

Per il solo segnale test del seno: 
- db4 wavelet approssima bene: errore di approssimazione nell'ordine di $10^{-5}$ 



Idee per valutazione: 
- trovare raggruppamento dei dati oppure passo temporale t.c. l'autocovarianza (autocorrelazione) campionaria per un oscillazione abbia valore atteso costante
