#cs 
# Uživatelská část 


## Spuštění programu

Program se skládá z jednoho hlavního souboru. Můžete ho buď stáhnout z GitLabu, nebo překopírovat do vývojového prostředí (IDE), ve kterém pracujete. 
Existuje několik možnosti, jak ho můžete spustit (ve Windows, Linux):

- **v IDE**: tlačítko Run, nebo přes terminál 
	- **VSCode**: 
		- tři tečky => Run => Run without Debugging
		- nebo *příkaz* v terminálu: **py linearEquations.py** 
- v **cmd** / **PowerShell** 
	1. zkopírujte cestu souboru (stáhnutý soubor je obvykle v *Downloads*)
	2. **cd** "cesta souboru" (cd - change directory (příkaz))
	3. **py** linearEquations.py 

Pokud chcete zastavit program, stačí napsat něco **nesprávně**, nebo v případě dotazu "**Zadej rovnici či výraz s nejvýše x proměnnými: "**, napíšte **q** nebo **quit**. 

## Reprezentace vstupních dat

Jakmile se program spustí, na začátku se objeví text o tom, jak se program ovládá, a ve stejné době už můžete zadávat vstupní data. Tady předvedeme výpis toho, co se od uživatele očekává:

- **Počet řádků (m):** int, nebo-li celé číslo
- **Počet sloupců (n):** int, nebo-li celé číslo
- **Jakým způsobem si chcete zapsat soustavu?:** písmeno t/T, nebo m/M (na velikosti nezáleží)
	- v případě **t/T**: 
		- **počet řádků** musí být v rozsahu: 2 <= m <= 3
		- **počet sloupců**: 3 <= n <= 4 
	- v případě **m/M**:
		- **počet řádků** musí být v rozsahu: 2 <= m <= 10
		- **počet sloupců**: 3 <= n <= 11
- **Zadej rovnici či matici:** 
	- zadávejte rovnici/řádek matici na *každý samostatný řádek* (nejvýše **m**-krát)
	- v případě **t/T**: 
		- print(Zadej rovnici či výraz s nejvýše x proměnnými:)
		- **vstupem** může být:
			- **rovnice** v podobě: $ax + by (+cz) = d$, kde (a, b, c, d) jsou celá čísla 
			- nebo **výraz** obsahující proměnné *x, y, nebo z*, např. $5x - 2y = 10(3-y) + 2x$ 
			- v případě **q/quit**: Program se ukončí 
	- v případě **m/M**:
		- print("Zadej matici: ") 
		- **vstupem** je řádek matice skládající se **pouze z čísel**. 
	
- **Chceš opakovat hru? (A / N):**
	- **a/A** - terminál se vyčistí, opět se objeví hlavní text a možnost zadat vstup ("Počet řádků")
	- **n/N/cokoliv jiného** - Program se ukončí. 


Pokud u daného dotazu, místo požádaných datových typů budete zadávat něco jiného (nepočítáme dotaz: *Zadej rovnici či výraz s nejvýše x proměnnými*), program vypíše chybovou zprávu a ukončí se. 

## Reprezentace výstupných dat 

Výstupní data můžeme rozdělit na:
1. Řešení soustavy (ze vstupu program zgeneruje matici a vypočítá ji)
	- *Žádné řešení* (0 řešení)
	- *Řešení dané soustavy*: x1: .., x2: ..., x3: ... (... - reálná čísla, v podobě zlomku nebo celého čísla)
2. Chybová zpráva 
	- pokud u nějakého dotazu zadáte nesprávný typ. Program se ukončí.
