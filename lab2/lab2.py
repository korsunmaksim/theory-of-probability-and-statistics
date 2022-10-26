import  matplotlib.pyplot as plt
import math

def spaces(n):
    str=''
    for i in range(n):
        str+=' '
    return str    

def Line():
    return "==================================================================== \n"

def GetAverage(grades):
    sumOfGrades=0
    for elem in grades:
        sumOfGrades+=elem
    return sumOfGrades/len(grades)    

def GetGrades(filePath):
    inputFile=open(filePath,'r')
    grades=[]
    for elem in inputFile:
        elem=int(elem)
        grades.append(elem)
    grades.pop(0)    
    grades.sort()
    inputFile.close()  
    return grades 

def GetQ1(grades):
    i=int(0.25*(len(grades)+1))-1
    q1=grades[i]+0.25*(grades[i+1]-grades[i])
    return q1

def GetQ3(grades):
    i=int(0.75*(len(grades)+1))-1
    q3=grades[i]+0.75*(grades[i+1]-grades[i])
    return q3

def GetP90(grades):
     i=int(0.9*(len(grades)+1))-1
     p90=grades[i]
     return p90


def GetMeanDeviation(grades):
    quadSumOfGrades=0
    for elem in grades:
        quadSumOfGrades+=pow(elem,2) 
    mean=(quadSumOfGrades/len(grades))-pow(GetAverage(grades),2)
    return round(mean,2)

def GetStandartDeviation(grades):
    return round(pow(GetMeanDeviation(grades),0.5),2)

def GetCoefficients(grades,newAverage,newMax):
    a=round((newMax-newAverage)/(newMax-GetAverage(grades)),2)
    b=newMax-newMax*a
    newMean=round(pow(a,2)*GetMeanDeviation(grades),2)
    newStandart=round(abs(a)*GetStandartDeviation(grades),2)
    return a,b,newMean,newStandart

def GetStemAndLeafDiagram(grades):
    diagramSL={}
    for i in range(len(grades)):
        key=int(grades[i]/10)
        if(key not in diagramSL):
            diagramSL[key]=[grades[i]%10]
        else:
            diagramSL[key].append(grades[i]%10)
    return diagramSL        

def GetBoxPlot(grades):
    plt.title("Box plot diagram")
    plt.boxplot(grades)
    plt.show()

def Lab2(grades):
    results=open("results.txt",'w')
    results.truncate()
    results.write("Lab2 \n")
    results.write(Line())
    results.write("Task1 \n")
    results.write(Line())   
    results.write("Q1 = "+str(GetQ1(grades))+"\n")
    results.write("Q3 = "+str(GetQ3(grades))+"\n")
    results.write("P90 = "+str(GetP90(grades))+"\n")
    results.write(Line())
    results.write("Task2 \n")
    results.write(Line()) 
    results.write("Mean deviation = " +str(GetMeanDeviation(grades))+"\n")
    results.write("Standart deviation = " +str(GetStandartDeviation(grades))+"\n")
    results.write(Line())
    results.write("Task3 \n")
    results.write(Line()) 
    a,b,newMean,newStandart=GetCoefficients(grades,95,100)
    results.write("y = "+str(a)+"x + "+str(b)+"\n")
    results.write("New mean deviation = "+str(newMean)+"\n")
    results.write("New standart deviation = "+str(newStandart)+"\n")
    results.write(Line())
    results.write("Task4 \n")
    results.write(Line()) 
    results.write("Stem and Leaf Diagram: \n")
    diagramSL=GetStemAndLeafDiagram(grades)
    for key in diagramSL:
        results.write(str(key)+ " |")
        for leaf in diagramSL[key]:
            results.write(str(leaf)+" ")
        results.write("\n")
    results.write("\nKey : 10 |0 = 100")
    results.close() 
    GetBoxPlot(grades)
Lab2(GetGrades(input()))


    

         
         















