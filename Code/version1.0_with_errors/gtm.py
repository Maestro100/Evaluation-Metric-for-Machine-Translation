
def Bleu1gram(ref, trans):
    list_ref=ref.split(" ")
    list_trans=trans.split(" ")
    refl=len(list_ref)
    transl=len(list_trans)
    c=0;
    ans=0.0;
    dict_ref={}
    for j in list_ref:
        if j not in dict_ref:
            dict_ref[j]=1
        else:
            dict_ref[j]+=1;

    for i in list_trans:
       if( i in dict_ref and dict_ref[i]!=0):
            dict_ref[i]-=1
            c=c+1
    return (c/(transl*1.0))





#the recall based one
def recall(ref, trans):
    list_ref=ref.split(" ")
    list_trans=trans.split(" ")
    refl=len(list_ref)
    transl=len(list_trans)
    c=0;
    ans=0.0;
    dict_ref={}
    for j in list_ref:
        if j not in dict_ref:
            dict_ref[j]=1
        else:
            dict_ref[j]+=1

    for i in list_trans:
       if( i in dict_ref and dict_ref[i]!=0):
            dict_ref[i]-=1
            c=c+1
    return (c/(refl*1.0))

def gtm(ref,trans):
    a=Bleu1gram(ref,trans)
    b=recall(ref,trans)
    if(a==0 and b==0):
        return 0
    else:
        c=(2*a*b)/(a+b)
        return c
