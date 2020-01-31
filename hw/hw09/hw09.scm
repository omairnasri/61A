
; Tail recursion


(define (replicate x n)
  (cond
      ((= n 0) ())
      (else 
          (cons x (replicate x (- n 1))))))

(define (accumulate combiner start n term)
  (if (= n 0)
  	start
  	(combiner (accumulate combiner
  							start
  							(- n 1)
  							term)
  			(term n))

  	)
)

(define (accumulate-tail combiner start n term)
	(if (= n 0)
	start
	( accumulate-tail combiner (combiner (term n) start) (- n 1) term)
)

; Streams

(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define multiples-of-three
  'YOUR-CODE-HERE
)


(define (nondecreastream s)
    'YOUR-CODE-HERE)

hy
(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))