# vorodi = [10 , 5 ,3 ,7 ,9 ,2 ,20,15,13,14,18,17,4]
# zoj = 0
# fard = 0
# for vord in vorodi :
#    if vord % 2 == 0:
#       zoj += 1
#       print({zoj})
#    elif vord % 2 != 0 :
#        fard += 1
#        print({fard})


vorodi = [10 , 5 ,3 ,7 ,9 ,2 ,20,15,13,14,18,17,4]
zoj = []
fard = []
for vord in vorodi :
   if vord % 2 == 0:
      zoj.append(vord)
   else:
      fard.append(vord)
print(zoj)
print(fard)