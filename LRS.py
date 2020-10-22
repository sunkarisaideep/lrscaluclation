print('*****LAYOUT REGULARISATION SCHEME*****\n')
name=input('Enter Plot Owner Name:\n')
Ser=float(input('\nEnter Plot Area in Sqr.Yds:\n'))
sqm=Ser*0.836


if (sqm<=100):
    a=200*sqm

   


elif (sqm>=101 and sqm<=300):
    a=400*sqm

elif (sqm>=301 and sqm<=500):
    a=600*sqm

 
    
elif (sqm>=501):
    a=750*sqm
     

rmv=int(input('\nEnter the marketvalue of land as on 26-08-2020(sub registar value) per square yard:\n'))

if (rmv<=3000):
    b=0.25*a
  
 
elif (rmv>=3001 and rmv<=5000):
    b=0.50*a
   
 
elif (rmv>=5001 and rmv<=10000):
    b=0.75*a
      
    
elif (rmv>=10001):
    b=0.75*a
  
    
   


opt=int(input('\nIs your land under pro rate open space category??(0/1) \n'))
rml=int(input('\nEnter the marketvalue of land as on 26-08-2020(sub registar value): \n'))
c=0.14*rml        
 
if (opt==1):
    e=c+b
  
elif (opt==0):   
    e=b

f=1000
g=0.1*e
print('\n*****LRS Regularation Scheme *****')
print('\nPlot Owner :',name)  
print('Plot area in Sq.Yrds :',Ser)
print('Plot area in Sq.Mtrs :',sqm)
print('Basic Regularation Charges :',a)
print('Basic Regularation Charges with reference to marketvalue :',b)    
print('Marketvalue of land as on 26-08-2020(sub registar value) :',rml)
print('land under pro rate open space category :',opt)
print('Processing Fee and Application Fee :',f)
print('Total Amount to be Paid for LRS Schdeme :',e)
print('Amount to be paid :',f+g)
print('\n***NOTE: CLEAR THE PENDING LRS AMOUNT WITHIN SIX MONTHS :',0.9*e)
    
   
     