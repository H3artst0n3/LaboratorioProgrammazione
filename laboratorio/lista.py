def list_sum(the_list):
 sum=0
 for item in the_list:
    sum = sum + item
    print("Somma: {}".format(sum))
list_sum([1,4,10])

# idea numero iterazioni poi for e per ogni cella vado a inserire il valore sottoforma di input e infinta si aggiunge la somma alla somma precedente 
#funzione builtin len per la lunghezza