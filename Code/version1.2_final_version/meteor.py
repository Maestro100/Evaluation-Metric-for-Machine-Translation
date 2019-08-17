def Bleu1gram(ref, trans):
    list_ref=ref.split()
    list_trans=trans.split()
    refl=len(list_ref)
    transl=len(list_trans)
    c=0;
    ans=0.0;
    print(list_ref)
    print(list_trans)
    dict_ref={}
    for j in list_ref:
        if j not in dict_ref:
            dict_ref[j]=1
        else:
            dict_ref[j]+=1;
    print (dict_ref)

    for i in list_trans:
       if( i in dict_ref and dict_ref[i]!=0):
            dict_ref[i]-=1
            c=c+1
    print (c/(transl*1.0))
    return (c/(transl*1.0))









#the recall based one
def recall(ref, trans):
    list_ref=ref.split()
    list_trans=trans.split()
    refl=len(list_ref)
    transl=len(list_trans)
    c=0;
    ans=0.0;
    print(list_ref)
    print(list_trans)
    dict_ref={}
    for j in list_ref:
        if j not in dict_ref:
            dict_ref[j]=1
        else:
            dict_ref[j]+=1
    print (dict_ref)

    for i in list_trans:
       if( i in dict_ref and dict_ref[i]!=0):
            dict_ref[i]-=1
            c=c+1
    print (c/(refl*1.0))
    return (c/(refl*1.0))



def bb(tr_idx,j,rf_idx,k,i):
     we=k
     for qw  in range(j,(j+i)):
          if(tr_idx[qw] or rf_idx[we]):
            return False
          we+=1
     return True



def n_grams(s,n):
    arr=s.split()
    ngram=[]
    for i in range(len(arr)-n+1):
        t=""
        for j in range(i,(i+n)):
            if (j!=i):
                t=t+" "
            t=t+arr[j]
        ngram.append(t)
    return ngram








def frag(ref,trans):
    f=0
    w=0
    tr=trans.split()
    tr_idx=[False]*len(tr)
    rf=ref.split()
    rf_idx=[False]*len(rf)
    m=min(len(tr),len(rf))
    for i in range(m,0,-1):
        tr_igram=n_grams(trans,i)
        rf_igram=n_grams(ref,i)
        for j in range(len(tr_igram)):
              for k in range(len(rf_igram)):
                   if((tr_igram[j]==rf_igram[k]) and bb(tr_idx,j,rf_idx,k,i)):
                        we=k
                        for qw in range(j,(j+i)):
                            tr_idx[qw]=True
                            rf_idx[we]=True
                            we+=1
                        f+=1
                        w+=i
    #print(w)
    #print (f)
    ffw=(f-1)/(w-1)
    return ffw




def meteor(ref,trans):
    ref=ref.lower()
    trans=trans.lower()
    a=Bleu1gram(ref,trans)
    b=recall(ref,trans)
    if (a==0 and b==0):
        return 0
    else:
         fm=(10*a*b)/((9*a)+b)
    fr=frag(ref,trans)
    df=0.5*(fr**3)
    c=(1-df)*fm
    #print c
    return c







#meteor("this is a boy","how long will place")
