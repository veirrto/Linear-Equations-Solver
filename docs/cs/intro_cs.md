#cs
# Dokumentace k zápočtovému programu "Lineární rovnice"

## 1. Úvod a cíl práce 
### 1.1. Anotace

**Linear Equations Solver** řeší uživatelsky zadanou soustavu lineárních rovnic či matici. Uživatel si může vybrat, jakým způsobem chce zadat soustavu rovnic, a to buď v *maticové*, nebo *textové podobě*. Ze vstupu vytvoří matici, zjednoduší ji do odstupňovaného tvaru a vypíše její řešení. 

### 1.2. Přesné zadání, cíle programu

Cílem mé práce bylo vytvořit program, který dokáže vypočítat řešení z textového vstupu (5x - 3y = 2, 3x+2y = 10(5 + x) - 3y) nebo maticového vstupu, který představuje soustavu lineárních rovnic, a vypsat ho do konzole. 
Textový vstup je výraz obsahující maximálně tři proměnné (x,y nebo z) - jedná se o způsob řešení lineárních rovnic, který se vyučuje na středních školách. Pokud je textovým vstupem složený výraz používající například závorky, program jej upraví do podoby matice, kterou následně vypočítá. Pokud si uživatel přeje zadat matici místo textu, zadá do konzoly pouze číslice a matice se okamžitě vytvoří. 
