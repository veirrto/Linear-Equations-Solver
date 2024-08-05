"Zapoctovy program - Linearni funkce"

import fractions
from fractions import Fraction
#import re
import os

"""
vypocet soustavy Gaussovou eliminaci. 

matice (mxn)-> matice v REF

---------------------------------------------------
input: non-singular matrix A , nxn 
output: upper triangular form U, vector c 

a_mat ... 2d array

"""

"""GAUSSOVA ELIMINACE"""

#prohod radky matice 
def swapRowsMatrix(mat, i, j):

    n = len(mat[0]) #pocet sloupcu v matici, nebo-li delka radku 

    for k in range(0, n):
        temp = mat[i][k]
        mat[i][k] = mat[j][k]
        mat[j][k] = temp 


#prohod radky praveho vektoru 
def swapRowsRightVector(b, i, j): 

    temp = b[i]
    b[i] = b[j]
    b[j] = temp 

    
#najdi nevetsi spolecny delitel - Greatest Common Divisor 
def gcd(a, b):
    #1. aspon jedno ze dvou cisel a,b je 0
    if (a == 0):
        return b
    elif (b == 0):
        return a 
    
    #2. a, b != 0
    return gcd(b % a, a)



"Gaussova eliminace"

def gaussElim(mat, b): 
    
    
    m = len(mat) #počet řádků v matici A 
    n = len(mat[0]) #počet sloupců v matici len(mat[0])


    row = 0 #index pivotu řádku
    col = 0 #index pivotu sloupce

    #pivot = 0

    while (row < m-1 or col < n-1):

        pivot_max = 0 #pivot 
        i_max = row #pozice pivotu

        "Stará metoda: najdeme největší číslo v daném sloupci a označíme ho pivotem" 
        # for i in range(row, m):
        #     pivot_max = max(abs(mat[i][col]), pivot_max) #pivot
        #     if (pivot_max > abs(mat[i_max][col])): 
        #         i_max = i
            
        "Nová metoda: najdeme první nenulové číslo v sloupci a označíme ho pivotem" 
        for i in range(row, m):
            if (mat[i][col] != 0):
                i_max = i
                pivot_max = mat[i][col]
                break 
        

        if (pivot_max == 0): #pokud posledni prvek v danem sloupci je 0
            col += 1
            if (col > n - 1): 
                break 

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

                for j in range(col, n):
                    mat[i][j] *= formula_i #vynasobime i-ty radek
                    mat[i][j] = mat[i][j] - mat[row][j] * formula_row #odecteme nasobek pivotu od i-teho radku

                #stejne udelame s pravou stranou
                b[i] *= formula_i
                b[i] = b[i] - b[row] * formula_row

            row += 1
            col += 1
    
    return mat, b #vystup: matice a vektor prave strany v odstupnovanem tvaru
        


"""Zpětná substituce"""


"najdi volné proměnné" 
def find_free_variables(mat):
    "input: matice v REF tvaru"
    "output: indexy volnych promennych"

    piv = [] #indices for pivots 
    fv = [] #indices for free variables

    m = len(mat)
    n = len(mat[0])

    #hledame pivot 
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
        


#fce, ktera zjisti, jestli sloupec obsahuje volnou prommenou
def is_free_variable(j, fv):
    #fv - pole s indexy volnych promennych (sloupcu matice)
    #j - index pole matice 
    for i in range(len(fv)): 
        if (fv[i] == j):
            return True 
    return False 

#funkce, ktera zjisti, jestli je radek matice nulovy
def is_row_zero(arr):
    for i in range(len(arr)):
        if (arr[i] != 0):
            return False
        
    return True 


    
#BACK SUBSTITUION: pokud vyraz obsahuje x (volne promenne), vypocitame ve funkci back_sub koeficienty pro volne promenne 
def is_instance(exp: str):
    #input: string
    #output: true/false

    for l in exp:
        if (l == 'x'):
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
    #arr = sl.split(' ') 
    #str1 = " "
    for i in range(0, 2):
        if (sl[i] == '+'):
            sl = sl.replace(sl[i], "", 1)
            return sl
    return sl

    
    
"Zpětná substituce"
def back_substitution(mat, b): #A, b jsou v REF tvaru
    
    m = len(b) #pocet radku
    n = len(mat[0]) #pocet sloupcu
    x = [0 for _ in range(n)] #pole pro cislene reseni
    sol = [str("") for _ in range(n)] #pole pro reseni v podobe stringu
    
    #1 reseni - 1
    #0 reseni - 0
    #oo reseni - 2

    free_vars = find_free_variables(mat) #funkce, ktera najde indexy sloupcu s volnymi promennymi

    for f in free_vars:
        sol[f] = f"x{f+1}" 


    print("Řešení dané soustavy:")

    row = 0
    col = 0

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
    for k in dict:
        dict[k] = 0
    return dict 



#uprav vyraz
def edit_expression(exp: str, col: int):

    #napr. 3x+2y = 10(5 + x) + 5y
    # vrati: '-7x - 3y = 50'

    dict = { #slovnik, ve kterem muzeme obnovovat hodnoty promennych
        'x': 0,
        'y': 0,
        'z': 0
    }

    braces_dict = { #stejny ucel jako dict, ale uvnitr zavorek 
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
    #op = "+-*/"
    before_brac = 0 #number before brackets
    const_var = 0 #konstanta 
    sign = "+" #znamenko

    #prochazime cely retezec
    while (i < len(exp)):

        #pokud je to mezera
        if (exp[i] == " "):
            i += 1 
            continue


        #pokud znak je "leva zavorka"
        elif (exp[i] == "("):
            ops.append(exp[i]) #pridej do zasobniku operatoru
            sign = "+"
            before_brac = val[-1]


        #pokud znak je cislo
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

            #pokud nema pred sebou promennou, pricteme hodnotu k c 
            if (exp[i + 1] not in symbols):
                if ("=" in ops):
                    const_var += val[-1]
                    #-abs(val[-1])
                else:
                    const_var -= val[-1]

           
        #pokud znak je x, y, nebo z
        elif (exp[i] in symbols):
            param.append(exp[i])
            #pokud je promenna v zavorkach, vypocitame jeji koeficient do pomocneho slovniku
            if (before_brac in val):
                if (not exp[i-1].isdigit()):
                    if (sign == "-"):
                        val.append(-1)
                        braces_dict[exp[i]] -= 1
                    else:
                        val.append(1) 
                        braces_dict[exp[i]] += 1
                else:
                    braces_dict[exp[i]] += val[-1]

            #pokud vne zavorek, ale promenna nema koeficient pred sebou
            elif ((not exp[i-1].isdigit())):
                    if (sign == "-" and "=" in ops):
                        val.append(-1)
                        dict[exp[i]] += 1
                    elif (sign == "-" or (sign == "+" and "=" in ops)): 
                        val.append(-1)
                        dict[exp[i]] -= 1
                    else:
                        val.append(1) 
                        dict[exp[i]] += 1
            #pokud ma koeficient 
            else:
                #pokud bylo rovnitko, prevedeme hodnotu na druhou stranu
                if ("=" in ops):
                    dict[exp[i]] -= val[-1]
                else:
                    dict[exp[i]] += val[-1]


        #pokud znak je pravá zavorka 
        elif (exp[i] == ")"):

            #cyklus, ve kterem postupne odstranujeme cisla z val (zasobniku), promenne z param (zasobniku), a menime hodnoty u c a ve slovniku

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
                    if ("=" in ops):
                        const_var += v * before_brac #konstanta, ktera bude na druhe strane
                    else:
                        const_var -= v * before_brac
                
                ops.pop()

            val.pop() #odstran before_brac, nebo-li koeficient pred zavorkami 

            #obnov vsechny hodnoty na puvodni
            braces_dict = set_dict_to_default(braces_dict)

                
        #pokud znak je operator: +-*/=
        else:

            if (exp[i] == "-"):
                sign = "-"
            else:
                sign = "+"

            ops.append(exp[i])

        i += 1

    #vytiskni odpověď 
    new_str = ""
    if (col == 3): 
        new_str = f"{dict["x"]}x + {dict["y"]}y = {const_var} "
    elif (col == 4):
        new_str = f"{dict["x"]}x + {dict["y"]}y + {dict["z"]}z = {const_var} "


    return new_str



#najdi cisla v úpraveném výrazu
def find_ints(s: str):
    arr = []
    i = 0
    j = 0

    while (i < len(s) and j < len(s) - 1): 
        h = 0
        if (s[i].isdigit()):
            j = i
            while (s[i].isdigit()):
                h = h * 10 + int(s[i])
                i += 1
        
            if (s[j-1] == "-"):
                arr.append(-abs(h))
            else:
                arr.append(h) 
        else:
            i += 1
        #j += 1

    return arr


    

#pokud 1 reseni - x1, ... xn
#pokud oo reseni - reseni s parametrem 
#pokud 0 reseni - mes "Soustava rovnic nema zadne reseni."

if __name__=="__main__":


    game_on = True
    count = 0
    

    while (game_on): 


        "vstup"


        text = """VÍTÁME TĚ V \"LINEAR EQUATIONS SOLVER\" (ŘEŠIČ LINEÁRNÍCH ROVNIC). \n 

        Linear Equations Solver funguje tak, že do konzole zadáš soustavu rovnic, a program Ti vytiskne řešení dané soustavy. \n 
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
        m = input()
        if (not m.isnumeric()):
            raise ValueError("Tvůj vstup není číslo.")
        
        m = int(m)
        
        print("Počet sloupců: ")
        n = input()
        if (not n.isnumeric()):
            raise ValueError("Tvůj vstup není číslo.")
        
        n = int(n)

        #ověř, jestli to vyhovuje podmínkám  
        if ((m < 2 or n < 2) or (m > 10 or n > 11)):
            print("Nesprávný rozměr soustavy. Program končí.")
            game_on = False
            break 



        #matice
        A = []
        b = [] #z odpovědi uživatele vytvoříme pravou stranu 

       
        text_param = [] 
        count = 0

        #2. zadej kazdou rovnici ze soustavy na kazdy radek 
        print("")

        #Jakym zpusobem chceme zapsat soustavu
        print("Jakým způsobem si chcete zapsat soustavu? ")
        inp = input().upper()

        if (inp == 'M'): #pokud matice

            if ((m < 2 or n < 3) or (m > 10 or n > 11)):
                print("Rozměr matice má být min. 2x3 a max. 10x11.")
                break 
            
            print("Zadej matici: \n")
            x = []

            for i in range(m):
                x = list(map(int, input().split(" ")))
                A.append(x[0:-1])
                b.append(x[-1]) 
        elif (inp == 'T'): #pokud text
            #A = [] 
            #b = []
            #x, y, z = symbols('x, y, z')
            if ((m < 2 or n < 3) or (m > 3 or n > 4)):
                print("Rozměr soustavy má být min. 2x3 a max. 3x4")
                break 
            

            print("Zadej rovnici či výraz s nejvýše" + f" {n-1}" + " proměnnými): ")
            s = ""

            for i in range(m):
                s = input() #5x + 2y = 5
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


        "vystup"
        rref_A, rref_b = gaussElim(A, b) 
        back_substitution(A, b)

        print("\nChceš opakovat hru? (A / N)")
        usr = input().upper()

        if (usr == 'A'):
            os.system('cls')
        else:
            game_on = False
            #break 
            


    


    #A = np.array([[1,-1,1,3],[2,1,8,18],[4,2,-3,-2]]) #napr. 

    #A = [[1, 4, 3, 2, 1], [2, 8, 4, 0, 0], [0, 0, 3, 6, 9], [2, 8, 7, 6, 3]]
    #A = A.astype(Fraction)
    #b = [1, 0, 5, 3] #right_side 
    #b = b.astype(Fraction)

    #A = np.array([[2, -3, 4], [4, 1, 2], [1, -1, 3]])
    #b = np.array([2, 2, 3])


    #A = np.array([[3, 4], [4, -2]])
    #b = np.array([7, 5])

    #A = np.array([[3, 2, 1], [2, 3, 1], [2, 1, 3], [5, 5, 2]])
    #b = np.array([5, 1, 11, 6])


    #A = np.array([[2, 2, 8, -3, 9], [2, 2, 4, -1, 3], [1, 1, 3, -2, 3], [3, 3, 5, -2, 3]])
    #b = np.array([2, 2, 1, 1])

    #A = np.array([[0, 1, 0, 1], [3, -2, -3, 4], [1, 1, -1, 1], [1, 0, -1, 0]])
    #b = np.array([1, -2, 2, 1])





    


    
