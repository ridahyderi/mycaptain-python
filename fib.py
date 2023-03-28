nterms=10
n1=0
n2=1
count=0
if nterms <=0:
    print("Pleaseenterapositiveinteger")
elif nterms==1:
    print("Fibonaccisequenceupto",nterms,":")
    print(n1)
else:
    print("Fibonaccisequenceupto",nterms,":")
    while count<nterms:
        print(n1,end=',')
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
