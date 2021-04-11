import random
print("total games=",5)
n=['snake','water','gun']
x=random.choice(n)
i=0
h=0
t=0
while i<5:
 x=random.choice(n)
 y=input("enter a choice snake,water or gun::")
 if y in n:
  i+=1
  if y=="snake":
   if x=="snake":
    print("draw")
   elif x=="water":
    print("you win")
    h+=1
   elif x=="gun":
    print("you lose")
    t+=1
   print("choices left",5-i)
  elif y=="water":
   if x=="snake":
    print("you lose")
    t+=1
   elif x=="water":
    print("draw")
   elif x=="gun":
    print("you win")
    h+=1
   print("choices left",5-i)
  elif y=="gun":
   if x=="snake":
    print("you win")
    h+=1
   elif x=="water":
    print("you lose")
    t+=1
   elif x=="gun":
    print("draw")
   print("choices left",5-i)
 else:
  print("wrong choice")
if h>t:
    print(f"you won by {h-t} matches and scorecard={h}-{t}")
if h<t:
 print(f"you lost by {t-h} matches and scorecard={h}-{t}")
elif h==t:
 print(f"draw and scorecard={h}-{t}")
