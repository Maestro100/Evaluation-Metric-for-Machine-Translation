import math
def Bleu1gram(ref, trans):
    list_ref=ref.split()
    list_trans=trans.split()
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
   # print c
    return (c/(transl*1.0))


def Bleu2gram(ref, trans):
    list_ref=ref.split()
    list_trans=trans.split()
    refl=len(list_ref)
    transl=len(list_trans)
    list2_ref=[]
    list2_trans=[]
    c=0;
    ans=0.0;
    for i in range((refl-1)):
        list2_ref.append(list_ref[i]+" "+list_ref[i+1])
    for j in range((transl-1)):
        list2_trans.append(list_trans[j]+" "+list_trans[j+1])
    transl2=len(list2_trans)
    dict_ref={}
    for j in list2_ref:
        if j not in dict_ref:
            dict_ref[j]=1
        else:
            dict_ref[j]+=1;
    for i in list2_trans:
       if( i in dict_ref and dict_ref[i]!=0):
            dict_ref[i]-=1
            c=c+1
    if (transl2==0):
        return 0
    return (c/(transl2*1.0))

def Bleu3gram(ref, trans):
    list_ref=ref.split()
    list_trans=trans.split()
    refl=len(list_ref)
    transl=len(list_trans)
    list3_ref=[]
    list3_trans=[]
    c=0;
    ans=0.0;
    for i in range((refl-2)):
        list3_ref.append(list_ref[i]+" "+list_ref[i+1]+" "+list_ref[i+2])
    for j in range((transl-2)):
        list3_trans.append(list_trans[j]+" "+list_trans[j+1]+" "+list_trans[j+2])
    transl3=len(list3_trans)
    dict_ref={}
    for j in list3_ref:
        if j not in dict_ref:
            dict_ref[j]=1
        else:
            dict_ref[j]+=1;
    for i in list3_trans:
       if( i in dict_ref and dict_ref[i]!=0):
            dict_ref[i]-=1
            c=c+1
    if (transl3==0):
        return 0
    return (c/(transl3*1.0))

def Bleu4gram(ref, trans):
    list_ref=ref.split()
    list_trans=trans.split()
    refl=len(list_ref)
    transl=len(list_trans)
    list4_ref=[]
    list4_trans=[]
    c=0;
    ans=0.0;
    for i in range((refl-3)):
        list4_ref.append(list_ref[i]+" "+list_ref[i+1]+" "+list_ref[i+2]+" "+list_ref[i+3])
    for j in range((transl-3)):
        list4_trans.append(list_trans[j]+" "+list_trans[j+1]+" "+list_trans[j+2]+" "+list_trans[j+3])
    transl4=len(list4_trans)
    dict_ref={}
    for j in list4_ref:
        if j not in dict_ref:
            dict_ref[j]=1
        else:
            dict_ref[j]+=1;
    for i in list4_trans:
       if( i in dict_ref and dict_ref[i]!=0):
            dict_ref[i]-=1
            c=c+1
    if (transl4==0):
        return 0
    return (c/(transl4*1.0))

def Bleu(ref,trans):
    bp=0.0;
    ref=ref.lower()
    trans=trans.lower()
    b1=Bleu1gram(ref,trans)
    b2=Bleu2gram(ref,trans)
    b3=Bleu3gram(ref,trans)
    b4=Bleu4gram(ref,trans)
    if(b4==0):
        if(b3==0):
            if(b2==0):
                b=b1
            else:
                b=(b1*b2)**0.5
        else:
            b=(b1*b2*b3)**0.33
    else:
        b=(b1*b2*b3*b4)**0.25
    list_ref=ref.split(" ")
    list_trans=trans.split(" ")
    transl=len(list_trans)
    refl=len(list_ref)
    if (transl>=refl):
        bp=1;
    else:
        bp=math.exp(1-(refl/(transl*1.0)))

    bfinal=b*bp
    #print bfinal
    return bfinal
#Bleu("this of a species","how  marine oday tom")
