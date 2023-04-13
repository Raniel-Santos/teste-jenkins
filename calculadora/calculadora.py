class Calculadora:
    #Funções
    def soma(a,b):
        return float(a+b)
    
    def subtracao(a,b):
        return float(a-b)
    
    def multiplicacao(a,b):
        return float(a*b)
        
    def divisao(a,b):        
        if b==0:
            raise ZeroDivisionError('o Denominador (b) não pode ser zero !')        
        if a%b == 0:
            return a/b
        else:
            return a/ float(b)
