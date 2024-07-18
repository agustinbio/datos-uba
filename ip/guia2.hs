cursada1 = [("Algebra I",9),("Analisis I",10),("AED I",7)]
cursada2 = [("Algebra I",10)]
test1 = [("Agustin Herrera",cursada1),("Ana Blejer",cursada2)]

--promedioDeAlumno :: [(String,Integer)] -> Integer

nMayorIgualQue :: Integer -> [(String,Integer)] -> Bool
nMayorIgualQue _ [] = True
nMayorIgualQue n (z:zs) = (n >= snd(z)) && (nMayorIgualQue n zs)

materiaMayorNota :: [(String,Integer)] -> String
materiaMayorNota [z] = fst(z)
materiaMayorNota (z:zs) | nMayorIgualQue (snd z) zs = fst(z)
                        | otherwise = materiaMayorNota zs
