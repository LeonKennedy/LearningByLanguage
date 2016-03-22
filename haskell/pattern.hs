import Data.List
--模式匹配
lucky ::(Integral a) => a -> String
lucky 7 = "LUCKY NUMBER SERVER"
lucky x = "Sorry, you are out luck, pal!"

sayMe ::(Integral a) => a -> String
sayMe 1 = "one"
sayMe 2 = "two"
sayMe 3 = "three"
sayMe 4 = "four"
sayMe 5 = "five"
sayMe x = "out of range!"

factorial :: (Integral a) => a -> a
factorial 0 = 1
factorial x = x * factorial (x-1)

addVectors :: (Num a) => (a, a)->(a, a) -> (a, a)
addVectors (x, y)  (m, n) = (x+m, y+n)

head' :: [a] -> a
head' [] = error "The list is empty!"
head' (x:_) = x

{-
tell :: (show a) => [a]->String
tell [] = "The list is empty!"
tell (x:[]) =  "The list only " ++ show x
tell (x:y:[]) = "The list two elements first is " ++ show x ++ "second is " ++ show y
tell (x:_) = "The list has lot of elements"
-}

length' :: (Num b) => [a] -> b
length' [] = 0
length' (_:xs) = 1 + length' xs

--as模式
capital :: String -> String   
capital "" = "Empty string, whoops!"   
capital all@(x:xs) = "The first letter of " ++ all ++ " is " ++ [x]  

--门卫

bmiTell :: (RealFloat a) => a -> String   
bmiTell bmi   
    | bmi <= 18.5 = "You're underweight, you emo, you!"   
    | bmi <= 25.0 = "You're supposedly normal. Pffft, I bet you're ugly!"   
    | bmi <= 30.0 = "You're fat! Lose some weight, fatty!"   
    | otherwise   = "You're a whale, congratulations!"  

bmiTell' :: (RealFloat a) => a -> a -> String   
bmiTell' weight height   
    | bmi <= skinny = "You're underweight, you emo, you!"   
    | bmi <= normal = "You're supposedly normal. Pffft, I bet you're ugly!"   
    | bmi <= fat    = "You're fat! Lose some weight, fatty!"   
    | otherwise     = "You're a whale, congratulations!"   
    where bmi = weight / height ^ 2   
          skinny = 18.5   
          normal = 25.0   
          fat = 30.0

myCompare :: (Ord a) => a -> a -> Ordering   
a `myCompare` b   
    | a > b     = GT   
    | a == b    = EQ   
    | otherwise = LT  


--where
calcBmis :: (RealFloat a) => [(a, a)] -> [a]   
calcBmis xs = [bmi w h | (w, h) <-xs ]
    where bmi weight height = weight / height ^ 2  

--let
cylinder :: (RealFloat a)=>a->a -> a
cylinder r h =
	let sideArea = 2 * pi * r * h
	    topArea = pi * r^2
	in sideArea + 2 * topArea

calcBmis' :: (RealFloat a) => [(a, a)] -> [a]
calcBmis' xs = [bmi | (w, h) <- xs ,let bmi = w / h^2 , bmi >= 25]

--case
describeList :: [a] -> String   
describeList xs = "The list is " ++ case xs of [] -> "empty."   
                                               [x] -> "a singleton list."    
                                               xs -> "a longer list."  

-- --=>
describeList' :: [a] -> String   
describeList' xs = "The list is " ++ what xs   
    where what [] = "empty."   
          what [x] = "a singleton list."   
          what xs = "a longer list."  

-- my zip
zip' :: [a]->[b] -> [(a,b)]
zip' _ [] = []
zip' [] _ = []
zip' (x:xz) (y:yz) = (x,y):zip' xz yz

-- quick sort
quicksort :: (Ord a)=>[a] -> [a]
quicksort [] = []
quicksort (x:xz) =  
	let left = quicksort [ a | a <- xz, a <= x]
	    right = quicksort [ a | a <- xz, a > x]
	in left ++ [x] ++ right


--ghci> zipWith' (zipWith' (*)) [[1,2,3],[3,5,6],[2,3,4]] [[3,2,2],[3,4,5],[5,4,3]]
--[[3,4,6],[9,20,30],[10,12,12]]

--ghci> map fst [(1,2),(3,5),(6,3),(2,6),(2,5)]
--[1,3,6,2,2]

--ghci> let notNull x = not (null x) in filter notNull [[1,2,3],[],[3,4,5],[2,2],[],[],[]]
--[[1,2,3],[3,4,5],[2,2]]

--filter (>3) [1,2,4,6,3,4,1,5,6,2]
--[4,6,4,5,6]

--ghci> sum (takeWhile (<10000) (filter odd (map (^2) [1..])))
--166650

--Main> flip zip [1,2,3] "abc"
--[('a',1),('b',2),('c',3)]
--Main> zip [1,2,3] "abc"
--[(1,'a'),(2,'b'),(3,'c')]

chain :: (Integral a)=>a -> [a]
chain 1 = [1]
chain n 
	| even n = n : chain (n `div` 2)
	| odd n  = n : chain (n*3 + 1)

numLongChains::Int
numLongChains = length ( filter isLong(map chain [1..100]))
	where isLong xz = length xz > 15

numLongChains' ::Int
numLongChains' = length ( filter (\xz -> length xz > 15)(map chain [1..100]))

-- *
flip' :: (a->b -> c)->b->a -> c
flip' f = \x y ->f y x

--ghci> map (negate . abs) [5,-3,-6,7,-3,2,-19,24]
--[-5,-3,-6,-7,-3,-2,-19,-24]

--ghci> map (negate . abs) [5,-3,-6,7,-3,2,-19,24]
--[-5,-3,-6,-7,-3,-2,-19,-24]

numUniques :: (Eq a)=>[a] -> Int
numUniques = length . nub
