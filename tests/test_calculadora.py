from pytest import mark
import pytest
from calculadora.calculadora import Calculadora

class TestCalculadora:
    
    @mark.calcular_soma    
    def test_soma_entre_dois_valores_positivos(self):             
        # Given(Dado)
        num1 = 10
        num2 = 20.5
        resultado = 30.5
        # When(Quando)   
        valor_resultado = Calculadora.soma(num1,num2) 
        # Then (Então)  
        assert resultado == valor_resultado

    @mark.calcular_subtracao    
    def test_subtracao_entre_dois_valores_positivos(self):
        num1 = 10
        num2 = 5
        resultado = 5
        valor_resultado = Calculadora.subtracao(num1,num2)
        assert resultado == valor_resultado

    @mark.calcular_multiplicacao   
    def test_multiplicacao_entre_dois_valores_positivos(self):
        num1 = 100
        num2 = 2.5
        resultado = 250
        valor_resultado = Calculadora.multiplicacao(num1,num2)
        assert resultado == valor_resultado       

    @mark.calcular_divisao    
    def test_divisao_entre_dois_valores_positivos(self):
        num1 = 12
        num2 = 3
        resultado = 4
        valor_resultado = Calculadora.divisao(num1,num2)
        print(valor_resultado)
        assert resultado == valor_resultado

    @mark.calcular_divisao_por_zero
    def test_divisao_com_denominador_zero(self):
        with pytest.raises(ZeroDivisionError):
            Calculadora.divisao(1500000,0)
    
    @mark.calcular_divisao    
    def test_divisao_entre_dois_valores_positivos_divisao_não_exata(self):
        num1 = 10
        num2 = 4
        resultado = 2.5
        valor_resultado = Calculadora.divisao(num1,num2)
        print(valor_resultado)
        assert resultado == valor_resultado





