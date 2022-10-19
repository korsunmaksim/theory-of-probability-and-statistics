import  matplotlib.pyplot as plt
import math

from sympy import re

def Line():
    return "==================================================================== \n"

def GetDataFromFile(filePath):
    inputFile=open(filePath,'r')
    movieViews={};
    k=0;
    for element in inputFile:
        if(k!=0):
            element=int(element)
            if element in movieViews:
                movieViews[element]+=1
            else:
                movieViews[element]=1
        k+=1
    inputFile.close()  
    movieViews=dict(sorted(movieViews.items()))
    return movieViews   
    
def  GetSumOfViews(movieViews):
    allViews=0
    for elem in movieViews:
        allViews+=movieViews[elem]
    return allViews    

def GetViewsArr(movieViews):
    viewsArr=[]
    for elem in movieViews:
        for i in range(movieViews[elem]):
            viewsArr.append(elem)
    return viewsArr        
    

def GetMostViewedMovie(movieViews):
    return max(movieViews.values())

def GetModa(movieViews):
    modaOfMovies={}
    for elem in movieViews:
        if (movieViews[elem]==GetMostViewedMovie(movieViews)):
            modaOfMovies[elem]=movieViews[elem]
    if(GetMostViewedMovie(movieViews)==1):
        return {"Moda doesn't exist":0};
    return modaOfMovies        

def GetMedian(movieViews):
    viewsArr=GetViewsArr(movieViews)
    if(len(viewsArr)%2):
        return ((viewsArr[int(len(viewsArr)/2)]+viewsArr[int(len(viewsArr)/2-1)])/2)
    return viewsArr[int(len(viewsArr)/2)]

def GetCumulativeFrequency(movieViews):
    cumulativeFrequencies={}
    tmp=0
    for elem in movieViews:
        cumulativeFrequencies[elem]=movieViews[elem]+tmp
        tmp=cumulativeFrequencies[elem]
    return cumulativeFrequencies    
       
def GetVariance(movieViews):
    average=0
    var=0
    for elem in movieViews:
        average+=elem*movieViews[elem]
        var+=(movieViews[elem]*pow(elem,2))
    average/=GetSumOfViews(movieViews)   
    var=(var/GetSumOfViews(movieViews))-pow(average,2)    
    return var

def GetStandartDeviation(movieViews):
    return math.sqrt(GetVariance(movieViews))  

def GetHistogram(movieViews):
    allViewsArr=GetViewsArr(movieViews)
    plt.hist(allViewsArr, bins =max(movieViews.keys()),color='blue',edgecolor='black',alpha=1) 
    plt.title("Frequency histogram")
    plt.show()

def spaces(n):
    str=''
    for i in range(n):
        str+=' '
    return str    

def Lab1(movieViews):
    results=open("result.txt",'w')
    results.truncate()
    results.write("Task1 \n")
    results.write(Line())   
    results.write("Movie index:"+spaces(10)+"Frequency"+spaces(10)+"Cumulative frequency \n")
    for elem in movieViews:
        results.write(str(elem)+spaces(25)+str(movieViews[elem])+spaces(28)+str(GetCumulativeFrequency(movieViews)[elem])+"\n")
    results.write("\nThe most viewed film: ")
    for elem in GetModa(movieViews):
        results.write(str(elem)+";")
    results.write("\n")    
    results.write(Line())    
    results.write("Task2 \n")
    results.write(Line())
    results.write("Moda: ")
    for elem in GetModa(movieViews):
        results.write(str(elem)+";")
    results.write("\n")    
    results.write("\n"+"Median ="+str(GetMedian(movieViews))+"\n")     
    results.write(Line())    
    results.write("Task3 \n")
    results.write(Line()) 
    results.write("Variance= "+str(GetVariance(movieViews))+"\n")
    results.write("Standart deviation= "+str(GetStandartDeviation(movieViews))+"\n")
    results.close() 
    GetHistogram(movieViews)
Lab1(GetDataFromFile(input()))


         
         























    
 


















    
