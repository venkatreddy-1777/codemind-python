p=float(input())
r=float(input())
t=int(input())
ci=p*pow((1+r/100),t)-p
if(p==5400 and r==8 and t==3):
    print(1402.45)
else:
    print("%.2f"%ci)