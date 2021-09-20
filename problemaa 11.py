x=int(input("scrieti numarul de elemente:"))
a=[]
print("a= afiseaza pe ecran componentele tabloului la un interval de 5 pozitii", *a[0:5])
print("introduceti", x, "elementele")
for i in range(0, x):
    y=int(input("scrieti elementul - "))
    a.extend([y])
print(a)
print("b= afişează pe ecran numerele în ordinea inversă a introducerii în calculator")
print(a[::-1])
print("c= sortează componentele tabloului în ordine descrescătoare")
m=sorted(a)
print(m[::-1])
print("d=  afişează pe ecran doar componentele pare")
d=[]
for i in range(0, len(a)):
    if a[i]%2==0:
        z=a[i]
        d.extend([z])
print(d)
print("e=  afişează pe ecran media aritmetică a componentelor pare")
if len(d)>0:
    print(sum(d)/len(d))
print("f= afişează pe ecran doar componentele impare")
f=[]
for i in range(0, len(a)):
    if a[i]%2!=0:
        v=a[i]
        f.extend([v])
print(f)
print ("g= afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y")
x=eval(input("x= "))
y=eval(input("y= "))
g=[]
for i in range(0, len(a)):
    if a[i]>x and a[i]%y!=0:
        w=a[i]
        g.extend([w])
print(g)
print("h= afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici decât y")
h=[]
for i in range(0, len(a)):
    if a[i]>x and a[i]<y:
        p=a[i]
        h.extend([p])
print(h)
print("i=  afişează pe ecran poziţiile (indicii) componentelor impare negative")
i=[]
for i in range(0, len(a)):
    if a[i]%2!=0 and a[i]<0:
        i.append(i)
print(i)
print("j= afişează pe ecran poziţiile (indicii) componentelor ce conţin doar două cifre semnificative")
j=[]
for i in range(0, len(a)):
    if a[i]/10>=1 and a[i]/10<10:
        q=a[i]
        j.extend([q])
print(j)
print("k= înlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv")
min=min(a)
r=[]
r=a[:]
r[0]=min
print(r)
print("l=  înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia")
t=[]
t=a[:]
indexmin=a.index(min)
t[indexmin]=t[0]
print(t)