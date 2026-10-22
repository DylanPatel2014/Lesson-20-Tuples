tuple=(0,0,1,1,1,1,0)
sunny=0
rainy=0
for i in range(0,7):
    if tuple[i]==0:
        rainy+=1
    else:
        sunny+=1
if sunny>rainy:
    print("The weather is most likely sunny.")
else:
    print("The weather is most likely rainy.")