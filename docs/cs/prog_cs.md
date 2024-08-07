# Programátorská část 

## Struktura programu

Celý program se skládá z funkcí, které nenáleží žádné třídě a některé obsahují vnořené funkce. 
Program jsem si rozdělila do několika částí, které jsou oddělené multiline komentáři: 
- **Gaussova Eliminace**
- **Zpětná Substituce** 
- **Úprava výrazů** 
- **Main Program** 

Každá část obsahuje stejnojmennou hlavní funkci a pomocné funkce, které se používají v hlavní. 


### Gaussova Eliminace 

Funkce **gaussElim(A, b)**, z angličtiny Gaussian Elimination, je algoritmus na převedení matice A a vektoru pravé strany b do odstupňovaného (REF) tvaru. Takhle nejprve musíme matici upravit, abychom pro ní pak hledali řešení dané soustavy. 

Funkce prochází v cyklu celou matici. Na začátku nového cyklu najde první nenulové číslo v aktuálním sloupci a označí ho pivotem. Pokud zpočátku nebyl v row-tém řádku matice, *prohodíme* řádek s pivotem a row-tý řádek. 
Pokud naopak v daném sloupci nenajdeme nenulové číslo, pokračujeme do dalšího sloupce.

Poté, co jsme našli pivot, půjdeme po každém řádku, vynásobíme ho koeficientem, pak od daného odečteme násobek pivotního řádku. Nakonec v sloupci pod pivotem zbydou nuly. 
Koeficient u nepivotních řádků je podíl **"pivot / největší společný dělitel (pivotu a čísla pod ním)"**. Můžeme ho považovat i za vzorec pro **nejmenší společný násobek**. 
Koeficient u pivotu je **"číslo pod pivotem / největší společný dělitel"**
Stejným způsobem násobíme složky vektoru b a od nich odečítáme násobek pivotu. 

Je to výhodnější násobit řádky, než jenom odečítat násobky pivotu (jak jsme to dělali na cvičeních), abychom se potom zbavili přetečených desetinných čísel, které by vznikly dělením pivotem.

**Časová složitost**: $O(n^3)$ 

### Zpětná substituce

Funkce **back_substituion(mat, b)**, z matice a vektoru b v REF tvaru vypočítá řešení (vektor x) **rekurzí**. (Ax = b)
Obsahuje vnořenou *rekurzivní* funkci, která prochází celou matici do posledního sloupce, a pak počítá každou složku vektoru x zvlášť, a postupně se z rekurze dostává zpět. 

Před voláním rekurzivní funkce v těle vnější funkce předem ověříme, jestli daná soustava nemá nemá řešení. 
Funkce **back_substituion(mat, b)** také při průchodu matice počítá s volnými proměnnými - pro tento účel jsme vytvořili pomocné funkce:
- funkce **find_free_variables(mat)** - na začátku najde indexy pivotů, a pomocí toho zjistí indexy volných proměnných.
- funkce  **is_instance(exp: str)** - pokud výraz obsahuje volnou proměnnou, tak pro ní v rekurzivní funkci spočítáme koeficient 


**Časová složitost**: $O(n^2)$ 

### Úprava výrazů

**edit_expression(exp: str, col: int)** Algoritmus pro úpravu se podobá DFS (prohledávání do hloubky). Používá několik různých *zásobníků* pro proměnné, čísla a operátory. V cyklu prochází celý textový výraz po složkách (znacích) a podle podmínek ověřuje, jestli se jedná o proměnnou, číslo, operátor, závorku, nebo mezeru. 

**Časová složitost:** $O(n)$ 
### Main Program

Funkce main() se vyvolá v podmínce if "__name__ = main". Když běží, tak na začátku uživatel vidí dlouhý text, pak různé dotazy, na které odpoví vstupem. 
Daná funkce se skládá ze vstupní, výpočetní a výstupní části. 
- **vstupní**: control flow či if/else podmínky, které ověřují uživatelské vstupy. 
- **výpočetní:** volání funkcí *gaussElim(A,b)*, *back_substituion(A, b)* 
- **výstupní:** výsledek funkce *back_substituion(A, b)*, a dotaz, jestli uživatel chce pokračovat ve hře 

**Celková čásová složitost: $O(n^3)$ (polynomiální)**
