--import guia4

longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

ultimo :: [t] -> t
ultimo [x] = x
ultimo (x:xs) = ultimo xs

principio :: [t]->[t]
principio [x] = []
principio (x:xs) = x:(principio xs)

reverso :: [t] -> [t]
reverso [] = []
reverso (x:xs) = (reverso xs) ++ [x]

pertenece:: (Eq t)=> t -> [t] -> Bool

pertenece _ [] = False
pertenece y (x:xs) = x==y || pertenece y xs

todosIguales :: (Eq t)=> [t] -> Bool
todosIguales [] = False
todosIguales [x] = True
todosIguales (x:y:xs) = x==y && todosIguales (y:xs)

todosDistintos :: (Eq t)=> [t] -> Bool
todosDistintos [] = True
todosDistintos (x:xs) = not (pertenece x xs) && todosDistintos xs

hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos [x] = False
hayRepetidos (x:y:xs) = x==y || hayRepetidos (y:xs)

quitar:: (Eq t)=> t -> [t] -> [t]
quitar y [] = []
quitar y (x:xs) |x == y = xs
  | otherwise =  [x] ++ quitar y xs
  
quitarTodos ::(Eq t) => t -> [t] -> [t]
quitarTodos y [] = []
quitarTodos y (x:xs) |x == y = quitarRecursivo
  | otherwise =  [x] ++ quitarRecursivo
  where quitarRecursivo = quitarTodos y xs

eliminarRepetidos:: (Eq t)=> [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) = x:eliminarRepetidos (quitarTodos x xs)

mismosElementos::(Eq t)=>[t]->[t]->Bool
mismosElementos x y = (mismosElementos1sentido x y) && (mismosElementos1sentido y x)
mismosElementos1sentido [] y = True
mismosElementos1sentido (x:xs) y = (pertenece x y) && (mismosElementos1sentido xs y)

capicua :: (Eq t)=> [t] -> Bool
capicua x = x == (reverso x)



--Ejercicio 3

sumatoria:: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs


productoria:: [Integer] -> Integer
productoria [] = 1
productoria (x:xs) = x * productoria xs

maximo :: [Integer]->Integer
maximo [x] = x
maximo (x:y:xs) | x>=y = maximo(x:xs)
              | otherwise = maximo(y:xs)

sumarN::Integer->[Integer]->[Integer]
sumarN _ [] = []
sumarN n (x:xs) = (n+x):(sumarN n xs)

sumarElPrimero :: [Integer]->[Integer]
sumarElPrimero (x:xs) = sumarN x (x:xs)

sumarElUltimo :: [Integer]->[Integer]
sumarElUltimo x = sumarN (ultimo x) x

pares::[Integer]->[Integer]
pares [] = []
pares (x:xs) | mod x 2 == 0 = x:pares(xs)
             | otherwise = pares(xs)

multiplosDeN::Integer->[Integer]->[Integer]
multiplosDeN _ [] = []
multiplosDeN n (x:xs) | mod x n == 0 = x:(multiplosDeN n xs)
             | otherwise = multiplosDeN n xs


ordenar1::[Integer]->[Integer]
ordenar1 [x] = [x]
ordenar1 (x:y:xs) | x > y = (y:ordenar1(x:xs))
               | otherwise = (x:ordenar1(y:xs))

ordenar::[Integer]->[Integer]
ordenar x | (ordenar1 x) == x = x
          | otherwise = ordenar ( ordenar1 x)


--  Ejercicio 5
sumatoriaR:: (Num t) =>[t] -> t
sumatoriaR [] = 0
sumatoriaR (x:xs) = x + sumatoriaR xs

sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada [] = []
sumaAcumulada x = sumaAcumulada(principio x) ++ [sumatoriaR x]


menorDivisor :: Integer->Integer
menorDivisor = menorDivisorDesdeI 2
menorDivisorDesdeI i n | mod n i == 0 = i
 | otherwise = menorDivisorDesdeI  (i+1)  n
 
esPrimo n  | menorDivisor n == n = True
   | otherwise = False

descomponerNenPrimos :: Integer ->[Integer]
descomponerNenPrimos n = descomponerNenPrimosAux 2 n

descomponerNenPrimosAux :: Integer -> Integer -> [Integer]
descomponerNenPrimosAux p 1 = []
descomponerNenPrimosAux p n | (esPrimo p) && (mod n p) == 0 && (mod(div n p) p) == 0 = p:(descomponerNenPrimosAux (p) (div n p))
                            | (esPrimo p) && (mod n p) == 0 && (mod(div n p) p) /= 0 = p:(descomponerNenPrimosAux (p+1) (div n p))
                            | otherwise = descomponerNenPrimosAux (p+1) n

descomponerEnPrimos::[Integer]->[[Integer]]
descomponerEnPrimos [] = []
descomponerEnPrimos (x:xs) = (descomponerNenPrimos x):(descomponerEnPrimos xs)


sacarBlancosRepetidos1 :: [Char] -> [Char]
sacarBlancosRepetidos1 [x] = [x]
sacarBlancosRepetidos1 (x:y:xs) | x==' ' && y==' ' = x:sacarBlancosRepetidos(xs)
                                | otherwise = x:y:sacarBlancosRepetidos(xs)
sacarBlancosRepetidos :: [Char] -> [Char]      
sacarBlancosRepetidos [] = []                         
sacarBlancosRepetidos x |sacarBlancosRepetidos1 x == x = x
                        |otherwise = sacarBlancosRepetidos(sacarBlancosRepetidos1 x)

sacarEspaciosRepetidos :: [Char] -> [Char]
sacarEspaciosRepetidos [] = []
sacarEspaciosRepetidos (x:[]) = [x]
sacarEspaciosRepetidos (x:y:xs) | x==y && x==' ' = sacarEspaciosRepetidos (y:xs)
                                | otherwise =  x:(sacarEspaciosRepetidos (y:xs) )
                                                               
sacarBlancos :: [Char] -> [Char]
sacarBlancos [] = []     
sacarBlancos  (x:xs) | x==' ' = sacarBlancos(xs)
                     | otherwise = x:sacarBlancos(xs)
                     
sacarBlancoInicio  :: [Char] -> [Char]
sacarBlancoInicio [] = []
sacarBlancoInicio (x:xs) | x == ' ' =xs
                         | otherwise = (x:xs)

sacarBlancoFin  :: [Char] -> [Char]
sacarBlancoFin [] = []
sacarBlancoFin x | ultimo x == ' ' = principio(x)
                 | otherwise = x

contarEspacios :: [Char] -> Integer
contarEspacios [] = 0
contarEspacios (x:xs) | x == ' ' =1+contarEspacios(xs)  
                      | otherwise = contarEspacios(xs)

limpiarTexto  :: [Char] -> [Char]
limpiarTexto x = sacarBlancoInicio (sacarBlancoFin (sacarBlancosRepetidos x))
         
contarPalabras :: [Char] -> Integer
contarPalabras x = contarEspacios (limpiarTexto x) + 1

primeraPalabra  :: [Char] -> [Char]
primeraPalabra [x] = [x]
primeraPalabra (x:xs) |x == ' ' = []
                      |otherwise = x:(primeraPalabra xs)

sacarPrimeraPalabra  :: [Char] -> [Char]
sacarPrimeraPalabra [] = []
sacarPrimeraPalabra (x:xs) |x == ' ' = xs
                           |otherwise = sacarPrimeraPalabra xs
                           
palabrasTextoLimpio  :: [Char] -> [[Char]]
palabrasTextoLimpio [] = []                          
palabrasTextoLimpio x = (primeraPalabra x):(palabrasTextoLimpio (sacarPrimeraPalabra x))

palabras  :: [Char] -> [[Char]]
palabras x = palabrasTextoLimpio (limpiarTexto x)

aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar (x:xs) = x ++ (aplanar xs)

aplanarConNBlancos :: [[Char]] -> Integer -> [Char]
aplanarConNBlancos [x] _ = x
aplanarConNBlancos (x:y:xs) n = x ++ (nBlancos n) ++ (aplanarConNBlancos (y:xs) n)

aplanarConBlancos :: [[Char]] -> [Char]
aplanarConBlancos x = aplanarConNBlancos x 1

nBlancos ::Integer -> [Char]
nBlancos 0 = []
nBlancos n = " "++nBlancos (n-1)
