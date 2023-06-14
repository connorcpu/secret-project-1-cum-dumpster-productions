# Secret project 1
#### *cum dumpster productions*

## introductie
Dit is de documentatie van secret project #1 ontworpen, developed en geproduceerd door Cum
Dumpster Productions (CDP). Wij hebben volgens de handleiding op somtoday een ganzenbord game
gemaakt en deze vervolgens aan gevuld met extra functionaliteit. Iedere (kleine) afwijking van de handlei-
ding word toegevoegd aan de onderstaande lijst van toegevoegde functionaliteit.

## feature list
* gebruik de --debug vlag op de command line om extra informatie over het spel te krijgen en automatische spelernamen in te laten vullen
* wanneer een speler meer dan 63 gooit word deze terug gestuurd
* naam systeem, vul aan het begin de namen van de spelers in
* informatie op het scherm, wat er is gegooid en wie aan de beurt is, geïntegreerd met het naam systeem
* nametags onder de pionnen
* health systeem
  * health bar
  * health aftrek als je de devils dice gebruikt
* visuele dobbelsteen waar je op kan drukken om te rollen
* visuele ’devil dice’ (no exact specifications) (placeholder -16 until 20)
  * voor meer risko maar de mogelijk heid om hoger te rollen, maar je kan ook negatief rollen
    * negatief rollen kan er voor zorgen dat de positie negatief is, dit word gecorrigeerd naar 0
  * voor elke keer gooien gaat er heath vanaf
  * het gemiddelde van de devils dice ligt iets hoger dan de normale dobbelsteen
