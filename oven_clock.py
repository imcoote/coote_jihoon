while True:
    try : 
        A,B=map(int,input().split())
    except ValueError:
        continue
    if A>=24 or A<0 or B>=60 or B<0:
        continue
    else:
        A,B
        break
while True:
    try : 
        C = int(input())
    except ValueError:
        continue
    if C>1000 or C < 0:
        continue
    else:
        C
        break

while True:
    if C >= 60:
        C-=60
        B+=60
    else:
        C
    if C<60:
        break
D = C+B

while True:
    if D >= 60:
        D-=60
        A+=1
    else:
        D
    if D<60:
        break
while True:
    if A >= 24:
        A-=24
    else:
        A
    if A < 24:
        break
print(A,D)