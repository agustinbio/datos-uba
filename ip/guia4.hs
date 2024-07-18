--module guia4 where

esDivisible :: Integer->Integer->Bool
esDivisible 0 b = True
esDivisible a b |a<b = False
                |otherwise = esDivisible (a-b) b
                

sumaImpares :: Integer->Integer
sumaImpares  n  |n ==1 = 1
                |otherwise = 2*n-1 + sumaImpares (n-1)
                
                
medioFact :: Integer-> Integer
medioFact 1 = 1
medioFact 0 = 1
medioFact n = n*medioFact (n-2)


sacarUltimoDigito :: Integer-> Integer
sacarUltimoDigito n = div n 10

ultimoDigito :: Integer-> Integer
ultimoDigito n = mod n 10

sumaDigitos :: Integer-> Integer
sumaDigitos 0 = 0
sumaDigitos n = ultimoDigito n + sumaDigitos(sacarUltimoDigito n)

todosDigitosIguales ::Integer->Bool
todosDigitosIguales n |sacarUltimoDigito n == 0 = True
 |otherwise = ultimoDigito n == ultimoDigito(sacarUltimoDigito n) && todosDigitosIguales(sacarUltimoDigito n)
 
iesimoDigito :: Integer ->Integer->Integer
iesimoDigito n i |cantDigitos n == i = ultimoDigito n
 |otherwise = iesimoDigito (sacarUltimoDigito n) i
 
cantDigitos :: Integer ->Integer
cantDigitos n | sacarUltimoDigito n == 0 = 1
 |otherwise = 1 + cantDigitos(sacarUltimoDigito n )

--trae problemas con el 1000 por ejemplo
sacarPrimerDigito n = n - (iesimoDigito n 1) * 10^(cantDigitos n -1)

esCapicuaI i n = iesimoDigito n i == iesimoDigito n (cantDigitos n -i +1)

esCapicuaR i n | i> div (cantDigitos n) 2 = True
 |otherwise = esCapicuaI i n && esCapicuaR (i+1) n
 
esCapicua = esCapicuaR 1

ej10f1 0 = 0
ej10f1 n = 2^n+ej10f1 (n-1)

-- cómo hago ej10f2 :: Integer->(Floating t)=>t -> t
ej10f2 0 _ = 0
ej10f2 n q = q^n+ej10f2 (n-1) q

ej10f3 n q = ej10f2 (2*n) q

ej10f4Aux parar n q | (parar-1)==n =0
 |otherwise  = q^n+ej10f4Aux parar (n-1) q
ej10f4 n q = ej10f4Aux n (2*n) q 

factorial 0 = 1
factorial n = n * factorial(n-1)
eAprox 0 = 1
eAprox n = 1 / fromIntegral(factorial n) + eAprox (n-1)
e = eAprox 10

ej12 0 = 2
ej12 n = 2 + 1 / (ej12 (n-1)) --por qué no tengo que usar fromIntegral?
raizDe2Aprox n = ej12 n -1

ej13sumExt 0 m = 0
ej13sumExt n m = ej13sumInt n m + ej13sumExt (n-1) m
ej13sumInt i 0 = 0
ej13sumInt i m = i^m + ej13sumInt i (m-1)

sumaPotencias :: Integer->Integer->Integer->Integer
sumaPotencias _ 0 _ = 0
sumaPotencias q n m = sumaPotenciasInt q n m + sumaPotencias q (n-1) m
sumaPotenciasInt _ _ 0 = 0
sumaPotenciasInt q n m = q^(n+m) + sumaPotenciasInt q n (m-1)


sumaRacionales :: Integer-> Integer  ->Float
sumaRacionales 0 _ = 0
sumaRacionales n m = sumaRacionalesInt n m + sumaRacionales (n-1) m
sumaRacionalesInt _ 0 = 0
sumaRacionalesInt n m = fromIntegral(n) / fromIntegral(m) + sumaRacionalesInt n (m-1)


menorDivisor :: Integer->Integer
menorDivisor = menorDivisorDesdeI 2
menorDivisorDesdeI i n | mod n i == 0 = i
 | otherwise = menorDivisorDesdeI  (i+1)  n
 
esPrimo n  | menorDivisor n == n = True
   | otherwise = False
   
maxComunDivisor :: Integer->Integer->Integer
maxComunDivisor n m | n>m = maxComunDivisorAux n m m
                |otherwise = maxComunDivisorAux m n n
-- está bien usar esta función auxiliar?
maxComunDivisorAux n m i| (mod n i) == 0 && (mod m i) == 0 = i
 | otherwise = maxComunDivisorAux n m (i-1)

sonComprimos :: Integer->Integer->Bool
sonComprimos n m |maxComunDivisor n m == 1 = True
 |otherwise = False

-- está bien usar así la recursión?

nEsimoPrimo :: Integer->Integer
nEsimoPrimo = nEsimoPrimoAux 0 2
nEsimoPrimoAux k i n | k == n = i-1
            | esPrimo(i) = nEsimoPrimoAux (k+1) (i+1) n 
            | otherwise = nEsimoPrimoAux k (i+1) n 
            
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n-1) + fibonacci (n-2)

esFibonacci :: Integer -> Bool
esFibonacci = esFibonacciAux 0
esFibonacciAux k n | fibonacci k == n = True
         | k < n = esFibonacciAux (k+1) n
         | otherwise = False


mayorDigitoPar :: Integer->Integer
mayorDigitoPar n | digitoXesta 8 n = 8
 | digitoXesta 4 n = 4
 | digitoXesta 2 n = 2
 | otherwise = (-1)
  

digitoXesta x n | ultimoDigito n == 0 = False
 | ultimoDigito n == x = True
 | otherwise = digitoXesta x (sacarUltimoDigito n)


sumaInicialDePrimos i k | i == (k+1) = 0
 |otherwise = nEsimoPrimo i + sumaInicialDePrimos (i+1) k

sumaInicialDePrimosHasta k n | (sumaInicialDePrimos 1 k) <= n = sumaInicialDePrimosHasta (k+1) n
 |otherwise = sumaInicialDePrimos 1 (k-1)

esSumaInicialDePrimos n = (sumaInicialDePrimosHasta 1 n) == n


esDivisor n k = (mod n k) == 0
sumaDivisoresDesde n k | k == 0 = 0
                  | esDivisor n k = k + sumaDivisoresDesde n (k-1)
                  | otherwise = sumaDivisoresDesde n (k-1)
sumaDivisores n = sumaDivisoresDesde n n

tomaValorMax :: Integer->Integer->Integer
tomaValorMax k m | k==m = k
                 | sumaDivisores k <= sumaDivisores m = tomaValorMax (k+1) m
                 | otherwise = tomaValorMax k (m-1)
                 
pitagoras :: Integer->Integer->Integer->Integer
pitagoras 0 n r = pitagorasInt 0 n r
pitagoras m n r = pitagorasInt m n r + pitagoras (m-1) n r
pitagorasInt m 0 r = satisfacePitagoras m 0 r
pitagorasInt m n r = satisfacePitagoras m n r + pitagorasInt m (n-1) r

satisfacePitagoras p q r | p^2 + q^2 <= r^2 = 1
                   | otherwise = 0


