#Zad. 1:
#A)
#Sprawdź w interpreterze typ wyników określonych działań - type( x ) i wyjaśnij, co oznaczają poszczególne operatory?

a = 1 + 2      # dodawanie (+) int + int = int
b = 1 + 4.5    # dodawanie (+) int + float = float
c = 3 / 2      # dzielenie zmiennoprzecinkowe  (/) int / int = float
d = 4 / 2      # dzielenie zmiennoprzecinkowe(/) int / int = float
e = 3 // 2     # dzielenie całkowite (//) int // int = int
f = -3 // 2    # dzielenie całkowite (//) int //int = int
g = 11 % 2     # dzielenie modulo (%) int % int = int
h = 2 ** 10    # potęgowanie (**) int**int = int
i = 8 ** (1/3) # potęgowanie (**) int**float = float

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))
print(g, type(g))
print(h, type(h))
print(i, type(i))


#B) Sprawdź i wyjaśnij działanie następujących instrukcji:

print(int(3.0))    # (int) konwertuje na liczbę całkowitą: float 3.0 -> int 3
print(float(3))    # (float) konwertuje na liczbę zmiennoprzecinkową: int 3 -> float 3.0
print(float("3"))  # (float) konwertuje na liczbę zmiennoprzecinkową: str"3" -> float 3.0
print(str(12.4))   # (str)  konwertuje  na tekst: float 12.4 -> str "12.4"
print(bool(0))     # (bool) konwertuje na wartość logiczną: 0 -> False

#2 Zad. 2:
#Do zmiennej o nazwie uczelnia przypisz zdanie Studiuję na WSIiZ, Następnie korzystając z funkcji print() wydrukuj ten tekst do konsoli.
uczelnia = "Studiuję na WSIiZ"
print(uczelnia)


# Zad.3:
#Podane są poniższe zmienne:
#imię = 'Jan'
#wiek = 20
#wzrost = 178 Wykorzystując funkcję print() oraz podane zmienne wydrukuj poniższy tekst do konsoli.
#Nazywam się Jan i mam 20 lat.
#Mój wzrost to 178 cm.

imię  = "Jan"
wiek  =  20
wzrost = 178

print(f"Nazywam się {imię} i mam {wiek} lat. Mój wzrost to {wzrost},cm")


# 4
# Zad. 4:
# Do zmiennej Cena przypisz cenę produktu równą 39.99 PLN oraz do zmiennej Rabat przypisz wartość 0.2 (rabat 20%).
# Następnie policz cenę tego produktu po zastosowaniu podanego rabatu. Wynik wydrukuj do konsoli.
# Zwróć uwagę na odpowiednie formatowanie tekstu w funkcji print() tak, aby końcowa cena produktu została wyświetlona tylko do drugiego miejsca po przecinku.

Cena = 39.99
Rabat = 0.2
CenaPoRabacie = Cena - Cena*Rabat
print(f"Cena po rabacie to {CenaPoRabacie:.2f} PLN")