# Elections Scraper pro volby.cz  
Projekt 3 pro Engeto: Elections Scraper  

## Co tento program dělá?
Tento Python script stahuje data z voleb do Poslanecké sněmovny v roce 2017. **https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ**
- Pro každou obec v konkrétním okrese stahuje údaje o volbách, včetně počtu registrovaných voličů, odevzdaných obálek a platných hlasů pro jednotlivé politické strany. 
- Získaná data jsou uložena do CSV souboru.

## Jak ho používat?
1. Stáhněte soubor **projekt_3.py** a **requirements.txt** a a vložte to do nějaké složky

2. Otevřete konzoli přes adresní řádek
   
![cmd](https://github.com/pavelkartin/Engeto-Projekt_3/assets/128692213/108830bd-684e-4e2e-a509-23beeb7bd914)  

nebo pomocí příkazu **cd** (např. `cd D:\Programming\Python\engeto_project_3`)

4. Nainstalujte všechny potřebné knihovny pomocí příkazu `pip install -r requirements.txt`

5. Spusťte program z příkazové řádky... Vložte potřebné argumenty: 
- První argument je URL webové stránky, ze které chcete stahovat data.

  Vyberte obec (**X**) na stránkách https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ

  např. Česká Lípa má URL: *https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=7&xnumnuts=5101*
     
![exa](https://github.com/pavelkartin/Engeto-Projekt_3/assets/128692213/5c6b2cfc-0389-48fb-85f7-f6c1b1a6cb1c)

- Druhý argument je název výstupního CSV souboru.

#### Vzor: `python projekt_3.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2106" "melnik.csv"`

Program bude postupně stahovat data pro každou obec a bude vás informovat o svém průběhu. Po dokončení stahování uloží všechna data do CSV souboru.

### Poznámky
Ujistěte se, že URL začíná řetězcem 'https://volby.cz/pls/ps2017nss/'. Jinak program skončí s chybou.

Ujistěte se, že název výstupního souboru končí příponou '.csv'. Jinak program skončí s chybou.

Pokud již existuje soubor se zadaným názvem výstupního souboru, program vás požádá o potvrzení, zda chcete tento soubor přepsat. Pokud neodpovíte 'yes', program vás vyzve, abyste to zkusili znovu.

## Příklad pro okres Karlovy Vary
Vstup konzole: `python projekt_3.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=5&xnumnuts=4102" "vary.csv"`

### Výstup konzole:
```
python projekt_3.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=5&xnumnuts=4102" "vary.csv"
Loading data...
1.82%
3.64%
5.45%
7.27%
9.09%
10.91%
12.73%
14.55%
16.36%
18.18%
20.00%
21.82%
23.64%
25.45%
27.27%
29.09%
30.91%
32.73%
34.55%
36.36%
38.18%
40.00%
41.82%
43.64%
45.45%
47.27%
49.09%
50.91%
52.73%
54.55%
56.36%
58.18%
60.00%
61.82%
63.64%
65.45%
67.27%
69.09%
70.91%
72.73%
74.55%
76.36%
78.18%
80.00%
81.82%
83.64%
85.45%
87.27%
89.09%
90.91%
92.73%
94.55%
96.36%
98.18%
100.00%
Data saved to vary.csv
```
### Ukázka výstupního .csv souboru:
![export](https://github.com/pavelkartin/Engeto-Projekt_3/assets/128692213/b69b9ad3-14f3-4bd1-89cf-27d6ff8abbcb)
