- k  hre je nutné mať nainštalovaný modul "tkInter"

Klasická hra dáma pre dvoch hráčov na šachovnici.

Hra pre dvoch hráčov - biely a čierny. 
Začína biely hráč. V termináli po každom ťahu napíše informácie o aktuálnom stave hry.

AKO HRAŤ: 
Kliknutím tlačidla vyberieme hraciu figúrku a následne myš klikneme na cieľovej destinácii. 
- PRE SKOK BEZ VYHODENIA KLIKNEME NA ZELENÉ POLÍČKO
- PRE SKOK S VYHODENÍM KLIKNEME NA MODRÉ POLÍČKO
- POKIAĽ PRI MOŽNOSTI DVOJSKOKU HO NECHCETE VYKONAŤ, KLIKNITE NA TLAČIDLO "Cancel Choice"

INFO PRE PROGRAMÁTORA:

* HRACIE POLE JE IMPLEMENTOVANÉ MATICOU (LIST V LISTE). HRA SA VYKRESĽUJE NA ZÁKLADE TEJTO MATICE.

- newGame():

začne novú hru, všetko reštartuje.

- endGameMenu():

Vykreslí tlačidlá na konci hry.

- checkForEnd()

Po každom ťahu pozrie, či sa neskončila hra.

- playField():

Vykreslí aktuálny stav hry.

- cancelChoice():

Zruší aktuálny výber, pri dvojskoku aj zmení hráča.

- changePlayer():

Zmení hráča.

- checkIfBecomeQueen():

Pri pohybe pešiakov kontroluje, či sa nemajú stať dámou.

- doubleJumpPossibility(x,y):

Po vyhodení kontroluje možnosť dvojskoku.
X je x-ová súradnica hráčovho aktuálneho pešiaka/dámy.
Y je y-ová súradnica hráčovho aktuálneho pešiaka/dámy.

- move(x,y):

Pohyb bez vyhodenia.
X je x-ová súradnica hráčovho aktuálneho pešiaka/dámy.
Y je y-ová súradnica hráčovho aktuálneho pešiaka/dámy.

- kickMove(x,y):

Pohyb s vyhodením.
X je x-ová súradnica hráčovho aktuálneho pešiaka/dámy.
Y je y-ová súradnica hráčovho aktuálneho pešiaka/dámy.

- possibleMoves(x,y):

Ukáže zeleným možnosti pohybu bez vyhodenia, modrým s vyhodením.
X je x-ová súradnica hráčovho aktuálneho pešiaka.
Y je y-ová súradnica hráčovho aktuálneho pešiaka.

- possibleMovesQueen(x,y):

Ukáže zeleným možnosti pohybu bez vyhodenia, modrým s vyhodením.
X je x-ová súradnica hráčovej aktuálnej dámy.
Y je y-ová súradnica hráčovej aktuálnej dámy.

- possibleMovesDJ(x,y):

Ukáže možnosti pohybu  modrým - s vyhodením (LEN PRI DVOJSKOKU).
X je x-ová súradnica hráčovho aktuálneho pešiaka.
Y je y-ová súradnica hráčovho aktuálneho pešiaka.

- possibleMovesQueenDJ(x,y):

Ukáže možnosti pohybu modrým - s vyhodením (LEN PRI DVOJSKOKU).
X je x-ová súradnica hráčovej aktuálnej dámy.
Y je y-ová súradnica hráčovej aktuálnej dámy.

- click(event):

Dodá súradnice myši pri kliknutí.




v3.0.1 23.02.20 
