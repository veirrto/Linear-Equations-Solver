"Linear Equations Solver"

import fractions
from fractions import Fraction
#import re
import os


"""GAUSSIAN ELIMINATION"""

""" 
1. helper functions used in gaussElim
2. fce gaussElim
"""

#swap rows of a matrix - for gaussElim
def swapRowsMatrix(mat, i, j):

    """
    vstup: matice (2d pole), i, j -  prirozena cisla
    vystup: prohodi i-ty a j-ty radek dane matice
    """

    n = len(mat[0]) #pocet sloupcu v matici, nebo-li delka radku 

    for k in range(0, n): #prohodi kazdou slozku i-teho radku s j-tym
        temp = mat[i][k]
        mat[i][k] = mat[j][k]
        mat[j][k] = temp 


#prohod radky praveho vektoru - pro funkci gaussElim
def swapRowsRightVector(b, i, j): 

    """
    vstup: vektor b (1d pole), i, j -  prirozena cisla
    vystup: prohodi kazdou i-tou slozku s j-tou, ve vektoru b 
    """
    
    temp = b[i]
    b[i] = b[j]
    b[j] = temp 

    
#najdi nejvetsi spolecny delitel - Greatest Common Divisor - pro funkci gaussElim
def gcd(a, b):
    """
    rekurzivni funkce

    vstup: 2 (prirozena) cisla
    vystup: nejvetsi spolecny delitel danych cisel 
    
    """
    #1. pripad: aspon jedno ze dvou cisel a,b je 0
    if (a == 0):
        return b
    elif (b == 0):
        return a 
    
    #2. pripad: a, b != 0
    return gcd(b % a, a)



"Gaussova eliminace"

def gaussElim(mat, b): 
    
    """
    vstup: 2d pole (matice) - "mat", 1d pole (vektor pravé strany) - "b"
    výstup: upravené mat, b do odstupňovaného tvaru (REF)
    
    """

    m = len(mat) #počet řádků v matici A 
    n = len(mat[0]) #počet sloupců v matici len(mat[0])


    row = 0 #index pivotu řádku
    col = 0 #index pivotu sloupce

    "Průchod maticí od 1. řádku 1. sloupce do posledního řádku/sloupce"
    while (row < m-1 or col < n-1): 

        pivot_max = 0 #pivot 
        i_max = row #pozice pivotu

        "Najdeme první nenulové číslo v sloupci a označíme ho pivotem" 
        for i in range(row, m):
            if (mat[i][col] != 0):
                i_max = i
                pivot_max = mat[i][col]
                break 
        

        if (pivot_max == 0): #pokud pivot v danem sloupci je 0 
            col += 1
            if (col > n - 1): #dokud radek opravdu nema pivoty
                break 

        "kdyz pivot neni nulovy, provedeme nasledujici operace"
        else:
            "prochozeni pivotniho radku s jinym radkem"
            if (row != i_max):
                swapRowsMatrix(mat, row, i_max)
                swapRowsRightVector(b, row, i_max)


            "ERU a eliminace"
            for i in range(row + 1, m):

                #vzorec, kterym vynasobime radek pod pivotem, a pak od tohoto radku odecteme nasobek pivotniho radku 

                greatest_divisor = gcd(abs(mat[row][col]), abs(mat[i][col])) 
                formula_i = mat[row][col] // greatest_divisor #vzorec pro i-ty radek
                temp = mat[i][col]
                formula_row = temp // greatest_divisor #vzorec pro pivotni radek

                if (formula_row == 0): #pokud prvek pod pivotem v i-tem radku je nulovy, pokracujeme do dalsiho radku
                    continue 

                #od sloupce col po n vynasobime j-tou slozku (postupne cely radek) a prvni radek matice
                for j in range(col, n):
                    mat[i][j] *= formula_i #vynasobime i-ty radek
                    mat[i][j] = mat[i][j] - mat[row][j] * formula_row #odecteme nasobek pivotu od i-teho radku

                #stejne udelame s pravou stranou
                b[i] *= formula_i
                b[i] = b[i] - b[row] * formula_row

            #ikrementujeme radek a sloupec 
            row += 1
            col += 1
    
    return mat, b #vystup: matice a vektor prave strany v odstupnovanem tvaru
        


"""Zpětná substituce"""

""" 
1. Funkce použité ve funkci back_substituion
2. fce back_substituion
"""


"najdi volné proměnné" 
def find_free_variables(mat):
    "vstup: matice v REF tvaru"
    "vystup: indexy volnych promennych"

    piv = [] #pole pro indexy pivotu 
    fv = [] #pole pro volne promenne

    m = len(mat) #pocet radku
    n = len(mat[0]) #pocet sloupcu

    #hledame indexy pivotnich sloupcu v matici 
    for i in range(m): 
        for j in range(i, n):
            if (mat[i][j] != 0):
                p_index = j #index pivotu
                piv.append(p_index) 
                break 
    
    #z indexu pivotu urcime indexy volnych promennych
    for k in range(0, n):
        if (not is_free_variable(k, piv)):
            fv.append(k)

    return fv #vrati pole s indexy volnych promennych
        

def is_free_variable(j, fv):
    #fce, ktera zjisti, jestli sloupec obsahuje volnou prommenou

    #vstup: fv - pole s indexy volnych promennych (sloupcu matice), j - index sloupce 
    #vystup: True nebo False 

    for i in range(len(fv)): 
        if (fv[i] == j): #pokud ano, vrati True
            return True 
    return False #pokud neni tam volna promenna, vrati False 


def is_row_zero(arr):
    #funkce, ktera zjisti, jestli je radek matice nulovy
    """
    vstup: radek matice (1d pole) - "arr"
    vystup: True nebo False 
    """
    for i in range(len(arr)):
        if (arr[i] != 0):
            return False
        
    return True 


    
#BACK SUBSTITUION: pokud vyraz obsahuje x (volne promenne), vypocitame ve funkci back_sub koeficienty pro volne promenne 
def is_instance(exp: str):
    #input: vyraz (string)
    #output: true/false

    for l in exp:
        if (l == 'x'): #pokud vyraz obsahuje x 
            return True 
        
    return False 


#nastavuje operační známenko podle známenka daného čísla 
def get_sign(num):
    #return "+" pokud num > 0
    #return "-" pokud num < 0

    if (num < 0):
        return " - "
    
    return " + "


#odstraň zbytečné "+" ve vypisu reseni
def delete_plus_beginning(sl: str): 

    #vstup: vypis reseni (sl)
    #vystup: sl neobsahuje na zacatku + (pokud cislo neni kladne)

    for i in range(0, 2): #najdeme plus na zacatku vypisu reseni 
        if (sl[i] == '+'):
            sl = sl.replace(sl[i], "", 1) #nahradime plusko prazdnym prostorem, 1krat
            return sl
    return sl #pokud neni zadne plusko

    
"Zpětná substituce"
def back_substitution(mat, b): #A, b jsou v REF tvaru

    """
    vstup: A, b - matice, vektor prave strany v REF tvaru
    vystup:
        - neni zadne reseni (Reseni 0)
        - vypis reseni z pole "sol": x1: ... , x2: ..., ..., xn: ...

    
    rec(row, col): #Rekurzivni funkce 
        vstup: row, col - radek, sloupec matice 
        vystup: vyplni 2 pole: x, sol

    
    #pokud 1 reseni - x1, ... xn
    #pokud oo reseni - reseni s parametrem 
    #pokud 0 reseni - mes "Soustava rovnic nema zadne reseni."

    """
    
    m = len(b) #pocet radku
    n = len(mat[0]) #pocet sloupcu
    x = [0 for _ in range(n)] #pole pro cislene reseni
    sol = [str("") for _ in range(n)] #pole pro reseni v podobe stringu
    

    free_vars = find_free_variables(mat) #funkce, ktera najde indexy sloupcu s volnymi promennymi

    for f in free_vars:
        sol[f] = f"x{f+1}" 


    print("Řešení dané soustavy:")

    row = 0
    col = 0

    #rekurzivni funkce 
    def rec(row, col):
        #base case
        if (row >= m or col >= n): 
            return
        
        if (is_free_variable(col, free_vars) or mat[row][col] == 0): #pokud jsme na volne promenne, nebo na nule, pokracujeme do dalsiho sloupce
            rec(row, col + 1) #rekurze 

        else:
            rec(row + 1, col + 1) #rekurze 
            piv = mat[row][col] #pivot v aktualnim radku a sloupci
            x[col] = b[row]

            for i in range(col + 1, n):
                #pokud vyraz obsahuje volnou promennou
                if (is_instance(sol[i]) and mat[row][i] != 0):
                    fv_coef = Fraction((-1) * mat[row][i] / piv).limit_denominator()
                    sol[col] += get_sign(fv_coef)
                    sol[col] += f"{abs(fv_coef)}x{i+1}" 
                else:
                    #jinak, vypocitame konstantu 
                    x[col] -= mat[row][i] * x[i]

            #vypocet konstanty
            x[col] = Fraction(x[col]/piv).limit_denominator() 

            #do reseni pridame znamenko x{i} a x{i}
            sol[col] += get_sign(x[col]) + str(abs(x[col]))

    #pokud nulový řádek, ale nenulová pravá strana = soustava nemá řádné řešení. Nemusime rekurzivne volat. 
    if(is_row_zero(mat[m-1]) and b[m-1] != 0):
        print("Žádné (0 řešení)")
        return 
    
    rec(row, col) #rekurze - na zacatku rekurzivne prochazime matici, pak hledane reseni 

    for i in range(len(sol)):
        sol[i] = delete_plus_beginning(sol[i]) #odstran plusko na zacatku vypisu x{i} - esteticky ucel 
        print(f"x{i+1}: " + str(sol[i])) #vytisknuti x{i}
    

"""/////////////////////////////////////////////////////////////////////////////////////////////////////////////"""

"Uprava vyrazu"

#nastav slovnik na puvodni (nulove) hodnoty
def set_dict_to_default(dict):
    #vstup: slovnik (dict)
    #vystup: zmenene hodnoty klicu na 0

    for k in dict:
        dict[k] = 0
    return dict 



#uprav vyraz
def edit_expression(exp: str, col: int):

    #napr. 3x+2y = 10(5 + x) + 5y
    # vrati: '-7x - 3y = 50'

    """
    vstup: vyraz (exp), sloupec matice (col) 
    vystup: vypis reseni (pomoci "col")
    """

    dict = { #slovnik, ve kterem muzeme obnovovat hodnoty promennych
        'x': 0,
        'y': 0,
        'z': 0
    }

    braces_dict = { #pomocny slovnik - stejny ucel jako dict, ale uvnitr zavorek 
        'x': 0,
        'y': 0,
        'z': 0
    }
    symbols = {'x', 'y', 'z'} #mnozina pro promenne 

            
    #op = "+-="
    ops = [] #zasobnik na operatory
    val = [] #zasobnik na cisla 
    param = [] #zasobnik na promenne
    i = 0 #counter
    before_brac = 0 #number before brackets
    const_var = 0 #konstanta 
    sign = "+" #znamenko

    #prochazime cely retezec
    while (i < len(exp)):

        """pokud je to mezera"""
        if (exp[i] == " "):
            i += 1 
            continue


        """pokud znak je "leva zavorka"""
        elif (exp[i] == "("):
            ops.append(exp[i]) #pridej do zasobniku operatoru
            sign = "+"
            before_brac = val[-1]


        """pokud znak je cislo"""
        elif (exp[i].isdigit()):

            v = 0
            j = i
             
            # Tady muze byt vic nez jedna cislice
            while (j < len(exp) and exp[j].isdigit()):
                v = (v * 10) + int(exp[j])
                j += 1
            
            #pridej do val (zasobniku cisel)
            if (sign == "-"):
                val.append(-abs(v))
            else:
                val.append(v) 


            #pokud rozdil i a j vetsi nez 1, pokracuj dale 
            if (abs(j - i) > 1): 
                i += abs(j - i)
                continue 

            #pokud pristi prvek je zavorka
            if (exp[i + 1] == "(" or before_brac in val):
                i += 1
                continue

            #pokud cislo nema pred sebou promennou, pricteme ho k c 
            if (exp[i + 1] not in symbols):
                if ("=" in ops):
                    const_var += val[-1]
                else:
                    const_var -= val[-1]

           
        """pokud znak je x, y, nebo z"""
        elif (exp[i] in symbols):
            param.append(exp[i])
            #pokud je promenna v zavorkach (a tedy v zasobniku je before_brac, ktery pozdeji odstranime)
            #=> vypocitame koeficient promenne do pomocneho slovniku
            if (before_brac in val): 
                if (not exp[i-1].isdigit()): #pokud promenna nema pred sebou koeficient, ale znamenko 
                    if (sign == "-"): #pokud je znamenko zaporne, odecteme 1 u teto promenne
                        val.append(-1)
                        braces_dict[exp[i]] -= 1
                    else:
                        val.append(1) #pokud je znamenko kladne, pricteme 1 k teto promenne
                        braces_dict[exp[i]] += 1
                else:
                    braces_dict[exp[i]] += val[-1] #pricteme cislo, ktere je v zavorkach, k promenne

            #pokud vne zavorek, ale promenna nema koeficient 
            elif ((not exp[i-1].isdigit())): 
                    if (sign == "-" and "=" in ops): #pokud je znamenko minus a "=" je v zasobniku
                        val.append(-1) 
                        dict[exp[i]] += 1 #pricteme jednicku
                    elif (sign == "-" or (sign == "+" and "=" in ops)): 
                        #pokud znamenko je minus a "=" neni v zasobniku, nebo plus a "=" je 
                        val.append(-1) 
                        dict[exp[i]] -= 1 #odcteme jednicku
                    else: 
                        #v ostatnich pripadech (napr. kdyz znamenko je plus, a "=" neni v zasobniku)
                        val.append(1) 
                        dict[exp[i]] += 1 #pricteme jednicku

            #pokud ma koeficient 
            else:
                #pokud bylo rovnitko, prevedeme hodnotu na levou stranu
                if ("=" in ops):
                    dict[exp[i]] -= val[-1] 
                else:
                    dict[exp[i]] += val[-1] #jinak pricteme hodnotu (jsme na leve strane)


        """pokud znak je pravá zavorka"""
        elif (exp[i] == ")"):

            #cyklus, ve kterem postupne odstranujeme cisla z val (zasobniku), promenne z param (zasobniku),
            # a menime hodnoty const_var, a ve slovniku

            while(len(ops) != 0 and val[-1] != before_brac):

                v = val.pop()
                if (braces_dict[param[-1]] == v): #pokud tento clen ma hodnotu v pomocnem slovniku
                    if ("=" in ops):
                        dict[param[-1]] -= v * before_brac #obnovime hodnotu tohoto clenu v hlavnim slovniku
                        #prevedeme na druhou stranu
                    else:
                        dict[param[-1]] += v * before_brac
                    param.pop()
                else: 
                    if ("=" in ops): #pokud jsme na prave strane
                        const_var += v * before_brac #pricteme novou hodnotu ke konstante
                    else:
                        const_var -= v * before_brac #pokud na leve s, odecteme hodnotu 
                
                ops.pop() 

            val.pop() #odstrani before_brac, nebo-li koeficient pred zavorkami 

            #obnovi vsechny hodnoty pomocneho slovniku na puvodni
            braces_dict = set_dict_to_default(braces_dict)

                
        """pokud znak je operator: +-*/="""
        else:

            if (exp[i] == "-"):
                sign = "-"
            else:
                sign = "+"

            ops.append(exp[i])

        i += 1

    #vytiskne odpověď 
    new_str = ""
    if (col == 3): 
        new_str = f"{dict["x"]}x + {dict["y"]}y = {const_var} "
    elif (col == 4):
        new_str = f"{dict["x"]}x + {dict["y"]}y + {dict["z"]}z = {const_var} "


    return new_str



"""Main program"""

#najdi cisla v úpraveném výrazu
def find_ints(s: str):
    #vstup: upraveny vyraz - retezec
    #vystup: pole koeficientu (int)
    #abychom je pak dosadili do matice, kterou bychom vyreseli GaussovouEliminaci

    arr = [] #pole koeficientu
    i = 0
    j = 0

    while (i < len(s) and j < len(s) - 1): #pruchod retezcem
        h = 0
        if (s[i].isdigit()):
            j = i
            while (s[i].isdigit()): #sestavime cislo z cislic 
                h = h * 10 + int(s[i])
                i += 1
        
            if (s[j-1] == "-"): #pokud je znamenko pred cislem zaporne
                arr.append(-abs(h))
            else:
                arr.append(h) #jinak 
        else:
            i += 1
        #j += 1

    return arr


"Main"
def main():

    game_on = True
    count = 0
    

    while (game_on): 


        "vstup"


        text = """VÍTÁME TĚ V \"LINEAR EQUATIONS SOLVER\" (ŘEŠIČ LINEÁRNÍCH ROVNIC). \n 

        Linear Equations Solver funguje tak, že do konzole zadáš soustavu rovnic, \n
        a program Ti vytiskne řešení dané soustavy. \n 
        Můžeš zadat soustavu rovnic buď v podobě: \n
            - Textové (MIN. rozměr: 2x3 (3. sloupec - pravá strana rovnice), MAX. rozměr: 3x4) - s proměnnými x, y, z \n
                př. 2x + 3y = 5 \n
                    x  - y  = 1 \n
                
            - Maticové (MIN. rozměr: 2x3 (3. sloupec - pravá strana rovnice), MAX. rozměr: 9x10) - čísla\n
                př. (poslední sloupec - pravá strana) \n
                    2 3 5 \n
                    1 -1 1 \n

        Pro prokračování ve hře, napište A nebo a (nezáleží na velikosti písmene.)
        Pro ukončení Řešiče, odpověďte N/n (nebo jakýmkoliv znakem) 

        """

        print(text)

        
        print("\n")

        #1. zadej rozmery matice (pocet rovnic a promennych), vektor prave strany '
        print("Zadej rozměry soustavy rovnic (na samostatné řádky): \n")
        print("Počet řádků: ")
        m = input("m = ")
        if (not m.isnumeric()):
            #raise ValueError("Tvůj vstup není číslo.")
            print("Tvůj vstup není číslo.")
            break
        
        m = int(m)
        
        print("Počet sloupců: ")
        n = input("n = ")
        if (not n.isnumeric()):
            #raise ValueError("Tvůj vstup není číslo.")
            print("Tvůj vstup není číslo.")
            break
        
        n = int(n)

        #2. Vytvoříme matici A a vektor b

        #nová matice
        A = []
        b = [] #z odpovědi uživatele vytvoříme pravou stranu 

       
        text_param = [] 
        count = 0
        to_run = False 

        print("")

        #Jakym zpusobem chceme zapsat soustavu
        print("Jakým způsobem si chcete zapsat soustavu? ")
        inp = input().upper()

        #Pokud matice
        if (inp == 'M'): 

            #overeni velikosti soustavy (matice)
            if ((m < 2 or n < 3) or (m > 10 or n > 11)):
                print("Rozměr matice má být min. 2x3 a max. 10x11.")
                break 
            

            print("Zadej matici: \n")
            x = []
            x_int = []

            for i in range(m):
                #radek bude obsahovat retezce
                x = list(map(str, input().split(" ")))

                #pak projdeme pres radek a zjistime, jestli obsahuje pouze cisla. 
                for j in range(len(x)):
                    if (not x[j].isnumeric()): #pokud neni to cislo, tak program skonci 
                        print("V řádku musí být pouze čísla. Program končí.") 
                        to_run = True
                        break 

                    #jinak pridame slozky radku do pole celych cisel
                    x_int.append(int(x[j]))
                
                #pokud to_run je True, opustime podminku
                if (to_run):
                    break 

                A.append(x_int[0:-1])
                b.append(x_int[-1]) 
                x_int = []

        #Pokud text
        elif (inp == 'T'): 

            #overeni velikosti soustavy
            if ((m < 2 or n < 3) or (m > 3 or n > 4)):
                print("Rozměr soustavy má být min. 2x3 a max. 3x4")
                break 
            

            print("Zadej rovnici či výraz s nejvýše" + f" {n-1}" + " proměnnými): ")
            s = ""
            

            for i in range(m):
                s = input() #5x + 2y = 5

                #pokud chceme vystoupit z programu 
                if (s == "q") or (s == "quit"): 
                    to_run = True 
                    break
                    
                s += " "
                s = edit_expression(s, n)

                #int_arr = re.findall('[-+]?\d+', s)
                int_arr = find_ints(s)


                row = []
    
                for j in range(0, n-1):
                    #A[i][j] = int(int_arr[j])
                    row.append(int(int_arr[j]))
                A.append(row)

                #A.append(int(int_arr[:-1]))
                b.append(int(int_arr[-1]))
                #b[i] = int(int_arr[-1]) 
        else:
            print("Nesprávné písmeno.")
            break 

        #pokud chceme vystoupit z celého programu
        if (to_run): 
            break 

        "vypočet"
        rref_A, rref_b = gaussElim(A, b) 
        back_substitution(A, b)

        "vystup"

        print("\nChceš opakovat hru? (A / N)")
        usr = input().upper()

        if (usr == 'A'):
            os.system('cls')
        else:
            game_on = False
            #break 


if __name__=="__main__":
    main()





    


    
