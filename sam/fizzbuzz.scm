(define (compute x)
  (cond ((and (equal? 0 (modulo x 3)) (equal? 0 (modulo x 5)))
	 (display "fizzbuzz") (newline))
	((equal? 0 (modulo x 3))
	 (display "fizz") (newline))
	((equal? 0 (modulo x 5))
	 (display "buzz") (newline))
	(else
	 (display x) (newline))))

(map compute (iota 100 1))
