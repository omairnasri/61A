; ;;;;;;;;;;;;;;
; ; Questions ;;
; ;;;;;;;;;;;;;;
; Scheme
(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))

(define (sign x)
  (cond 
    ((= x 0) 0)
    ((< x 0) -1)
    (else    1)
  )
)

(define (square x) (* x x))

(define (pow b n)
    (cond ((= n 0) 1)                                    
          ((even? n) (square (pow b (quotient n 2))))
          (else (* (pow b (- n 1)) b))))

; Goal is to define a nested function which accepts a list and an element - nested(val, list). If the val is present in the list - return 0, or else 
;(define (unique s) ()))