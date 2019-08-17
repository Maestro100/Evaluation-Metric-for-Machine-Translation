import math
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

#Bleu1gram("the cat is on the mat","the the the the the the the")

def Bleu2gram(ref, trans):
    list_ref=ref.split(" ")
    list_trans=trans.split(" ")
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
    if(transl2==0):
        return 0
    return (c/(transl2*1.0))

#Bleu2gram("the cat is on the mat","the cat mat the mat the the")

def Bleu3gram(ref, trans):
    list_ref=ref.split(" ")
    list_trans=trans.split(" ")
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
    if(transl3==0):
        return 0
    return (c/(transl3*1.0))

#Bleu3gram("the cat is on the mat","the cat is the mat the the")

def Bleu4gram(ref, trans):
    list_ref=ref.split(" ")
    list_trans=trans.split(" ")
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
    if(transl4==0):
        return 0
    return (c/(transl4*1.0))

#Bleu4gram("the cat is on the mat","the cat is on the mat the the")
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

def recall2gram(ref, trans):
    list_ref=ref.split(" ")
    list_trans=trans.split(" ")
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
    refl2=len(list2_ref)
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
    if(refl2==0):
        return 0
    return (c/(refl2*1.0))

def recall3gram(ref, trans):
    list_ref=ref.split(" ")
    list_trans=trans.split(" ")
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
    refl3=len(list3_ref)
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
    if(refl3==0):
        return 0
    return (c/(refl3*1.0))

def recall4gram(ref, trans):
    list_ref=ref.split(" ")
    list_trans=trans.split(" ")
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
    refl4=len(list4_ref)
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
    if(refl4==0):
        return 0
    return (c/(refl4*1.0))

def count_letters(word):  return len(filter(lambda x: x not in " ", word))

# Strict Brevity Penalty
def SBP(ref,trans):
    list_ref=ref.split(" ")
    list_trans=trans.split(" ")
    refl=len(list_ref)
    transl=len(list_trans)
    denominator=min(refl,transl)
    e=2.71828
    power=1-float(refl)/denominator
    return pow(e,power)

# Strict Redundancy Penalty
def SRP(ref,trans):
    list_ref=ref.split(" ")
    list_trans=trans.split(" ")
    refl=len(list_ref)
    transl=len(list_trans)
    numerator=max(refl,transl)
    e=2.71828
    power=1-float(numerator)/refl
    return pow(e,power)

# Character Based Strict Brevity Penalty
def CSBP(ref,trans):
    refl=count_letters(ref)
    transl=count_letters(trans)
    denominator=min(refl,transl)
    e=2.71828
    power=1-float(refl)/denominator
    return pow(e,power)

# Character Based Strict Redundancy Penalty
def CSRP(ref,trans):
    refl=count_letters(ref)
    transl=count_letters(trans)
    numerator=max(refl,transl)
    e=2.71828
    power=1-numerator/refl
    return pow(e,power)

# Short Word Difference Penalty
def SWDP(ref,trans):
    list_ref=ref.split(" ")
    list_trans=trans.split(" ")
    refl=len(list_ref)
    transl=len(list_trans)
    ref_small=0
    trans_small=0
    for i in range(refl):
        if len(list_ref[i])<=3:
            ref_small=ref_small+1
    for j in range(transl):
        if len(list_trans[j])<=3:
            trans_small=trans_small+1
    power=float(abs(ref_small-trans_small))/refl
    e=2.71828
    return pow(e,-power)

#Long Word Difference Penalty
def LWDP(ref,trans):
    list_ref=ref.split(" ")
    list_trans=trans.split(" ")
    refl=len(list_ref)
    transl=len(list_trans)
    ref_large=0
    trans_large=0
    for i in range(refl):
        if len(list_ref[i])>3:
            ref_large=ref_large+1
    for j in range(transl):
        if len(list_trans[j])>3:
            trans_large=trans_large+1
    power= float(abs(ref_large-trans_large))/refl
    e=2.71828
    return pow(e,-power)

#Chunk penalty
def CKP(ref,trans):
    transl=len(trans.split(" "))
    b=Bleu2gram(ref,trans)*(transl-1)
    a=Bleu1gram(ref,trans)*(transl)
    chunks=a-b
    if(a==0):
        return 1
    pen=1-(0.1*((float(chunks)/a)**3))
    return pen

#Continuity penalty
def CTP(ref,trans):
##    transl=len(trans.split(" "))
##    b1=Bleu1gram(ref,trans)*transl
##    b2=Bleu2gram(ref,trans)*(transl-1)
##    b3=Bleu3gram(ref,trans)*(transl-2)
##    b4=Bleu4gram(ref,trans)*(transl-3)
##    #need to know what is segment
##    s1=0
##    s2=0
##    s3=0
##    if b1!=s1:
##        a=b2/(b1-s1)
##    else:
##        a=0
##    if b2!=s2:
##        b=b3/(b2-s2)
##    else:
##        b=0
##    if b3!=s3:
##        c=b4/(b3-s3)
##    else:
##        c=0
##    e=2.71828
##    power=(-(a+b+c)/3.0)
##    d=pow(e,power)
    d=1
    return d

def NSCP(ref, trans):
    list_ref=ref.split(" ")
    list_trans=trans.split(" ")
    refl=len(list_ref)
    transl=len(list_trans)
    c=0;
    dict_ref={}         #used to find the number of common words
    common_list_trans_order=[]      #used to store order in which commmon words appear
    common_list_ref_order=[]        #used to store order in which commmon words appear

    #for storing frequency+1 of each word in the reference
    for j in list_ref:
        if j not in dict_ref:
            dict_ref[j]=1
        else:
            dict_ref[j]+=1;

    #for calculating the number of common words and storing their order in the translated sentence in the form of a list
    for i in list_trans:
       if( i in dict_ref and dict_ref[i]!=0):
            dict_ref[i]-=1
            c=c+1
            common_list_trans_order.append(i)

    #for getting the order of common words in the reference sentence
    for i in list_ref:
        if i in common_list_trans_order:
            common_list_ref_order.append(i)

    # Order for r1eference is assigned as 1,2,3,...,c
    ranks_ref=range(c+1)
    ranks_ref=ranks_ref[1:]

    #For obtaining list of rank of words in translated list
    ranks_trans=[]
    for i in common_list_trans_order:
        rank=common_list_ref_order.index(i)+1   #Since index starts from 0 but we want our ranks to start 1 onwards
        ranks_trans.append(rank)

    #Now we have both the lists, just need to calculate



    numerator=0
    for i in range(c):
        d=ranks_ref[i]-ranks_trans[i]
        numerator=numerator+d**2
        denominator=(c-1)*c*(c+1)
    rho=1 - float(numerator)/denominator
    penalty=(1+rho)/2.0
    return penalty

def NKCP(ref, trans):
    list_ref=ref.split(" ")
    list_trans=trans.split(" ")
    refl=len(list_ref)
    transl=len(list_trans)
    c=0;
    dict_ref={}         #used to find the number of common words
    common_list_trans_order=[]      #used to store order in which commmon words appear
    common_list_ref_order=[]        #used to store order in which commmon words appear

    #for storing frequency+1 of each word in the reference
    for j in list_ref:
        if j not in dict_ref:
            dict_ref[j]=1
        else:
            dict_ref[j]+=1;

    #for calculating the number of common words and storing their order in the translated sentence in the form of a list
    for i in list_trans:
       if( i in dict_ref and dict_ref[i]!=0):
            dict_ref[i]-=1
            c=c+1
            common_list_trans_order.append(i)

    #for getting the order of common words in the reference sentence
    for i in list_ref:
        if i in common_list_trans_order:
            common_list_ref_order.append(i)

    # Order for r1eference is assigned as 1,2,3,...,c
    ranks_ref=range(c+1)
    ranks_ref=ranks_ref[1:]

    #For obtaining list of rank of words in translated list
    ranks_trans=[]
    for i in common_list_trans_order:
        rank=common_list_ref_order.index(i)+1   #Since index starts from 0 but we want our ranks to start 1 onwards
        ranks_trans.append(rank)

    #Now we have both the lists, just need to calculate
    #We need the rank list of only translation

    n=len(ranks_trans)
    all_pairs=(n*(n-1))/2.0 #nC2
    increasing_pairs=0
    for i in range(n):
        for j in range(i+1,n):
            if(ranks_trans[j]>ranks_trans[i]):
                increasing_pairs=increasing_pairs+1
    tau=2*(float(increasing_pairs)/all_pairs) - 1
    penalty=(1+tau)/2.0
    return penalty

def amber(ref,trans):
    bp=0.0;
    ref=ref.lower()
    trans=trans.lower()
    b1=Bleu1gram(ref,trans)
    b2=Bleu2gram(ref,trans)
    b3=Bleu3gram(ref,trans)
    b4=Bleu4gram(ref,trans)
    r=recall(ref,trans)
    r2=recall2gram(ref,trans)
    r3=recall3gram(ref,trans)
    r4=recall4gram(ref,trans)
    #AvgP=(b1*b2*b3*b4)**0.25
    #Modifying this code for AvgP
    if(b4==0):
        if(b3==0):
            if(b2==0):
                b=b1**0.25
            else:
                b=(b1*b2)**0.25
        else:
            b=(b1*b2*b3)**0.25
    else:
        b=(b1*b2*b3*b4)**0.25
    AvgP=b
    P_N=(b1+b2+b3+b4)/4
    R_M=r
    if(P_N==0 and R_M==0):
        F_mean=0
    else:
        F_mean=(P_N*R_M)/((0.9*P_N)+(0.1*R_M))




    if b1==0 and r==0:
        F1=0
        F2=0
        F3=0
        F4=0
    elif b2==0 and r2==0:
        F1=(b1*r)/((0.9*b1)+(0.1*r))
        F2=0
        F3=0
        F4=0
    elif b3==0 and r3==0:
        F1=(b1*r)/((0.9*b1)+(0.1*r))
        F2=(b2*r2)/((0.9*b2)+(0.1*r2))
        F3=0
        F4=0
    elif b4==0 and r4==0:
        F1=(b1*r)/((0.9*b1)+(0.1*r))
        F2=(b2*r2)/((0.9*b2)+(0.1*r2))
        F3=(b3*r3)/((0.9*b3)+(0.1*r3))
        F4=0
    else:
        F1=(b1*r)/((0.9*b1)+(0.1*r))
        F2=(b2*r2)/((0.9*b2)+(0.1*r2))
        F3=(b3*r3)/((0.9*b3)+(0.1*r3))
        F4=F4=(b4*r4)/((0.9*b4)+(0.1*r4))

    AvgF=(F1+F2+F3+F4)/4
    score=(0.3*AvgP)+(0.5*F_mean)+(0.2*AvgF)
    #To do all the penalties
    net_penalty=1
    #weight of each penalty
    weight_SBP=0.3
    net_penalty=net_penalty*pow(SBP(ref,trans),weight_SBP)
    weight_SRP=0.1
    net_penalty=net_penalty*pow(SRP(ref,trans),weight_SRP)
    weight_CSBP=0.15
    net_penalty=net_penalty*pow(CSBP(ref,trans),weight_CSBP)
    weight_CSRP=0.05
    net_penalty=net_penalty*pow(CSRP(ref,trans),weight_CSRP)
    weight_SWDP=0.1
    net_penalty=net_penalty*pow(SWDP(ref,trans),weight_SWDP)
    weight_LWDP=0.2
    net_penalty=net_penalty*pow(LWDP(ref,trans),weight_LWDP)
    weight_CKP=1
    net_penalty=net_penalty*pow(CKP(ref,trans),weight_CKP)
    weight_CTP=0.8
    net_penalty=net_penalty*pow(CTP(ref,trans),weight_CTP)
    weight_NSCP=0.5
    net_penalty=net_penalty*pow(NSCP(ref,trans),weight_NSCP)
    weight_NKCP=2
    net_penalty=net_penalty*pow(NKCP(ref,trans),weight_NKCP)
    net_score=score*net_penalty
    return net_score
