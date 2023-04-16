Team1={}
Team2={}
n1=input()
n2=input()

for i in range(n1):
 a=input()
 Team1[a]=input()      #'A':20, 'B':34, 'G':52
for i in range(n2):
 a=input()
 Team2[a]=input()     #'V':50, 'F':19

building={}     #floors:rooms:caloriePerRoom
a=input()
building[a]=input()
b=building[a]
building[b]=input()

for i in range(building.key):
 for j in range(building[a]):
  for k in range(building[b]):
   for l in range(Team1.len()):
    if Team1.key!=0:
     d=1
     Team1.key-=1
     break
   for l in range(Team2.len()):
    if Team2.key!=0:
      e=1
      Team2.key-=1
      break
   if d==0:
    print("Team2 won")
   elif e==0:
    print("Team1 won")
   elif d==0 and e==0:
    print("Tie")
   


