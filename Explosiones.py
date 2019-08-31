def caso_explosion(): #definimos el algoritmo
    mezclas=int(input("digite el numero de mezclas "))#pedimos al usuario que introduzca un valor 
    nombre_o=[raw_input("ingrese el nombre del operario " + str (a+1)+ ": ")for a in range(5)]# establecemos los nombres de los operarios en la lista
    explosion=[[0 for a in range(mezclas)] for a in range(5)]#establecemos la matriz en cuanto a la explosion de 5 listas
    
    for a in range(5):#creamos un ciclo que itere 5 veces
        
        for l in range(mezclas):#dentro del ciclo volvemos a poner otro ciclo que itere (mezclas)veces
            explosion[a][l]=float(input("digite la fuerza de la mezcla " + str (l+1)+ ": "))#pedimos al usuario que ingrese valor
            while explosion[a][l]<=0:#condicionamos dentro del ciclo, no debe ser menor o igual a 0 de lo contrario se pedira otra vez
                explosion[a][l]= float(input("digite la fuerza de la mezcla " + str (l+1)+ ": "))
           
    
    sumador=[0 for i in range(5)]#establecemos un sumador 
    for j in range(5):#creamos un ciclo que itere 5 veces
        for i in range(0, mezclas):#dentro del ciclo volvemos a crear otro ciclo que itere (mezclas) veces
            sumador[j]+=explosion[j][i]#le vamos sumando al sumador
    prom=[sumador[i]/mezclas for i in range(5)]#identificamos la operacion para hallar el promedio
    
    
    for i in range(1,len(prom)):#creamos otro ciclo 
        for l in range(len(prom)-i):#creamos un ciclo dentro de otro ciclo para iterar
            if prom[l]>prom[l+1]:# condicionamos el algoritmo para establecer valores menores y mayores, utilizando la tecnica de la burbuja
                var=prom[l]
                var2=nombre_o[l]
                var3=explosion[l]
                prom[l]=prom[l+1]
                nombre_o[l]=nombre_o[l+1]
                explosion[l]=explosion[l+1]
                prom[l+1]=var
                nombre_o[l+1]=var2
                explosion[l+1]=var3
    
    
    posicion=3# se establece un contador           
    for r in range(2):#se crea un contador 
        for o in range(1,mezclas):#creamos otro ciclo que itere desde uno hasta (mezclas) veces
            for a in range(mezclas-o):#creamos otro ciclo que itere desde (mezclas) y a ese le restamos el valor de o
                if explosion[posicion][a]>explosion[posicion][a+1]:#condicionamos siempre y cuando los valores de la lista sea unos mayores que otros. utilizando la tecnica de la burbuja
                    var4=explosion[posicion][a]
                    explosion[posicion][a]=explosion[posicion][a+1]
                    explosion[posicion][a+1]=var4
        posicion+=1# se le aumente uno en valor al contador
        
    
    #en todo esto se imprimen los mensajes mostrandole al usuario los datos de promedio, operarios,explosion y el orden 
   
    print "los promedios fueron", prom
    print "operariso en orden", nombre_o
    print "explosiones en orden",explosion
    print  nombre_o[3],"la menor fuerza de la mezcla fue ", explosion[3][0],"_ su fuerza mayor fue ", explosion[3][mezclas-1],">>>",  nombre_o[4], " la fuerza menor fue de ", explosion[4][0], "_ y su fuerza mayor fue de ", explosion[4][mezclas-1]
   
    
  
caso_explosion()#cerramos el algoritmo para poder ejecutarlo