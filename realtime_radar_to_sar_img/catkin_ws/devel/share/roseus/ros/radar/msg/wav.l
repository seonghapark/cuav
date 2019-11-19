;; Auto-generated. Do not edit!


(when (boundp 'radar::wav)
  (if (not (find-package "RADAR"))
    (make-package "RADAR"))
  (shadow 'wav (find-package "RADAR")))
(unless (find-package "RADAR::WAV")
  (make-package "RADAR::WAV"))

(in-package "ROS")
;;//! \htmlinclude wav.msg.html


(defclass radar::wav
  :super ros::object
  :slots (_data _sync _num _sr ))

(defmethod radar::wav
  (:init
   (&key
    ((:data __data) (make-array 0 :initial-element 0 :element-type :integer))
    ((:sync __sync) (make-array 0 :initial-element 0 :element-type :integer))
    ((:num __num) 0)
    ((:sr __sr) 0)
    )
   (send-super :init)
   (setq _data __data)
   (setq _sync __sync)
   (setq _num (round __num))
   (setq _sr (round __sr))
   self)
  (:data
   (&optional __data)
   (if __data (setq _data __data)) _data)
  (:sync
   (&optional __sync)
   (if __sync (setq _sync __sync)) _sync)
  (:num
   (&optional __num)
   (if __num (setq _num __num)) _num)
  (:sr
   (&optional __sr)
   (if __sr (setq _sr __sr)) _sr)
  (:serialization-length
   ()
   (+
    ;; int16[] _data
    (* 2    (length _data)) 4
    ;; int16[] _sync
    (* 2    (length _sync)) 4
    ;; uint64 _num
    8
    ;; uint64 _sr
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16[] _data
     (write-long (length _data) s)
     (dotimes (i (length _data))
       (write-word (elt _data i) s)
       )
     ;; int16[] _sync
     (write-long (length _sync) s)
     (dotimes (i (length _sync))
       (write-word (elt _sync i) s)
       )
     ;; uint64 _num
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _num (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _num) (= (length (_num . bv)) 2)) ;; bignum
              (write-long (ash (elt (_num . bv) 0) 0) s)
              (write-long (ash (elt (_num . bv) 1) -1) s))
             ((and (class _num) (= (length (_num . bv)) 1)) ;; big1
              (write-long (elt (_num . bv) 0) s)
              (write-long (if (>= _num 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _num s)(write-long (if (>= _num 0) 0 #xffffffff) s)))
     ;; uint64 _sr
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _sr (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _sr) (= (length (_sr . bv)) 2)) ;; bignum
              (write-long (ash (elt (_sr . bv) 0) 0) s)
              (write-long (ash (elt (_sr . bv) 1) -1) s))
             ((and (class _sr) (= (length (_sr . bv)) 1)) ;; big1
              (write-long (elt (_sr . bv) 0) s)
              (write-long (if (>= _sr 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _sr s)(write-long (if (>= _sr 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16[] _data
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _data (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _data i) (sys::peek buf ptr- :short)) (incf ptr- 2)
     ))
   ;; int16[] _sync
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _sync (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _sync i) (sys::peek buf ptr- :short)) (incf ptr- 2)
     ))
   ;; uint64 _num
     
#+(or :alpha :irix6 :x86_64)
      (setf _num (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _num (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; uint64 _sr
     
#+(or :alpha :irix6 :x86_64)
      (setf _sr (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _sr (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(setf (get radar::wav :md5sum-) "835c58a78c35188ca9384fba6386b750")
(setf (get radar::wav :datatype-) "radar/wav")
(setf (get radar::wav :definition-)
      "int16[] data
int16[] sync
uint64 num
uint64 sr
")



(provide :radar/wav "835c58a78c35188ca9384fba6386b750")


