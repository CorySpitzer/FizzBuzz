import System.IO
import Data.List

fizz :: [Int] -> [(Int, String)]
fizz l = 
  zip l [if x `mod` 3 == 0 then "fizz" else "" | x <- l]
    
buzz :: (Int, String) -> String
buzz t = 
  let s = snd t
  in if (fst t) `mod` 5 == 0
     then s ++ "buzz"
     else if null s
          then s ++ (show (fst t))
          else s ++ ""
            
fizzbuzz :: [Int] -> [String]
fizzbuzz l = 
  map buzz (fizz l)

main = 
  let s = fizzbuzz [1..100]
  in putStrLn (intercalate "\n" s)