f :: Integer -> Integer
f 1 = 8
f 4 = 131
f 16 = 16

g :: Integer -> Integer
g 8 = 16
g 16 = 4
g 131 = 1

h x = f(g(x))
k x = g(f(x))


absoluto :: Integer -> Integer
absoluto x | x>=0 = x
           | otherwise = -x

maximoabsoluto :: Integer -> Integer -> Integer
maximoabsoluto x y | absoluto(x)>=absoluto(y) = absoluto(x)
                   | otherwise = absoluto(y)

maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 x y z | x>=y && y>=z = x
              | y>=x && y>=z = y
              | z>=x && z>=y = z

algunoEs01 :: Float -> Float -> Bool
algunoEs01 0 x = True
algunoEs01 y 0 = True
algunoEs01 x y | x/= 0 && y/=0 = False

ambosSon0 :: Float -> Float -> Bool
ambosSon0 x y | x==0 && y==0 = True
              | otherwise = False

mismoIntervalo:: Float->Float->Bool
mismoIntervalo x y | (x<=3 && y<=3 ) || ((3<x && x<=7)&&(3<y && y <=7)) || (x>7 && y>7) = True
                   | otherwise = False

sumaDistintos:: Integer->Integer ->Integer->Integer
sumaDistintos a b c | a == b && b == c = c
                    | a == b = b+c
                    | b == c = a+b
                    | c == a = b+a
                    | otherwise =a+b+c

esMultiploDe :: Integer->Integer->Bool
esMultiploDe x y =mod x y == 0

estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados a b | mod a b == 0 = True
                      | otherwise = False

prodInteger :: (Float,Float)-> (Float,Float) -> Float
prodInteger (x, y) (z, w) = x*z + y*w

todoMenor :: (Float,Float)-> (Float,Float) -> Bool
todoMenor (x,y) (z,w) = x<z && y <w

distanciaPuntos :: (Float,Float)-> (Float,Float) -> Float
distanciaPuntos (x ,y) (z,w) = sqrt((x-z)^2+(y-w)^2)

sumarSoloMultiplos ::(Integer,Integer,Integer) -> Integer -> Integer
sumarSoloMultiplos (x,y,z) w = sumaSi (x,y,z) (sonMultiplos (x,y,z) w)

sumaSi ::(Integer,Integer,Integer) -> (Integer,Integer,Integer) -> Integer
sumaSi (x,y,z) (xB, yB,zB) = x*xB+y*yB+z*zB
tomaSi ::(Integer,Integer,Integer) -> (Bool,Bool,Bool) -> Integer -> Integer
tomaSi (x,y,z) (xB, yB, zB) cual  | cual == 1 && xB = x
                                  | cual == 2 && yB = y
                                  | cual == 3 && zB = z
                                  | otherwise = 0

sonMultiplos ::(Integer,Integer,Integer) -> Integer -> (Integer,Integer,Integer)
sonMultiplos (x,y,z) w = (esMultiplo x w, esMultiplo y w, esMultiplo z w)

esMultiplo ::Integer -> Integer -> Integer
esMultiplo dividendo divisor   | (dividendo `mod` divisor) == 0 = 1
                               | otherwise = 0
posPrimerPar :: (Integer, Integer, Integer) -> Integer
posPrimerPar (x,y,z) | (mod x 2 == 0) = 1
                     | (mod y 2 == 0) = 2
                     | (mod z 2 == 0) = 3
                     | otherwise = 4

crearPar :: t1->t2->(t1,t2)
crearPar a b = (a,b)

invertir :: (t2,t1)->(t1,t2)
invertir (a, b) = (b,a)

f2::Integer->Integer
f2 n |n<=7 = n^2
     |n>7 = 2*n-1
g2::Integer->Integer
g2 n |mod n 2 == 0 = div n 2
     |otherwise = 3*n+1

todosMenores:: (Integer,Integer,Integer)-> Bool
todosMenores (n1, n2, n3) | f2(n1) > g2(n1) && f2(n2)>g2(n2) && f2(n3)>g2(n3) = True
                          | otherwise = False

bisiesto::Integer->Bool
bisiesto anio | mod anio 4 /= 0 || (mod anio 100 == 0 && mod anio 400 /= 0) = False
              | otherwise = True

distanciaManhattan:: (Float,Float,Float) -> (Float, Float, Float) -> Float
distanciaManhattan (p1,p2,p3) (q1,q2,q3) = abs (p1-q1) + abs (p2-q2) + abs (p3-q3)

sumaUltimosDosDigitos:: Integer -> Integer
sumaUltimosDosDigitos x = mod x 10 + mod (div x 10) 10

comparar:: Integer->Integer->Integer
comparar a b |sumaUltimosDosDigitos(a) < sumaUltimosDosDigitos(b) = 1
             |sumaUltimosDosDigitos(a) > sumaUltimosDosDigitos(b) = (-1)
             |sumaUltimosDosDigitos(a) == sumaUltimosDosDigitos(b) = 0
