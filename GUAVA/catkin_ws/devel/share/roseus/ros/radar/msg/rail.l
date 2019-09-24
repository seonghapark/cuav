;; Auto-generated. Do not edit!


(when (boundp 'radar::rail)
  (if (not (find-package "RADAR"))
    (make-package "RADAR"))
  (shadow 'rail (find-package "RADAR")))
(unless (find-package "RADAR::RAIL")
  (make-package "RADAR::RAIL"))

(in-package "ROS")
;;//! \htmlinclude rail.msg.html


(defclass radar::rail
  :super ros::object
  :slots (_end ))

(defmethod radar::rail
  (:init
   (&key
    ((:end __end) nil)
    )
   (send-super :init)
   (setq _end __end)
   self)
  (:end
   (&optional __end)
   (if __end (setq _end __end)) _end)
  (:serialization-length
   ()
   (+
    ;; bool _end
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _end
       (if _end (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _end
     (setq _end (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get radar::rail :md5sum-) "f9ac4e286e7f89fc602116455cd26e68")
(setf (get radar::rail :datatype-) "radar/rail")
(setf (get radar::rail :definition-)
      "bool end
")



(provide :radar/rail "f9ac4e286e7f89fc602116455cd26e68")


