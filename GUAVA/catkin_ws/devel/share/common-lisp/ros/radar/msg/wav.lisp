; Auto-generated. Do not edit!


(cl:in-package radar-msg)


;//! \htmlinclude wav.msg.html

(cl:defclass <wav> (roslisp-msg-protocol:ros-message)
  ((data
    :reader data
    :initarg :data
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 0 :element-type 'cl:fixnum :initial-element 0))
   (num
    :reader num
    :initarg :num
    :type cl:integer
    :initform 0))
)

(cl:defclass wav (<wav>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <wav>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'wav)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name radar-msg:<wav> is deprecated: use radar-msg:wav instead.")))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <wav>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader radar-msg:data-val is deprecated.  Use radar-msg:data instead.")
  (data m))

(cl:ensure-generic-function 'num-val :lambda-list '(m))
(cl:defmethod num-val ((m <wav>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader radar-msg:num-val is deprecated.  Use radar-msg:num instead.")
  (num m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <wav>) ostream)
  "Serializes a message object of type '<wav>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'data))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:write-byte (cl:ldb (cl:byte 8 0) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) ele) ostream))
   (cl:slot-value msg 'data))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'num)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'num)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'num)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'num)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 32) (cl:slot-value msg 'num)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 40) (cl:slot-value msg 'num)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 48) (cl:slot-value msg 'num)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 56) (cl:slot-value msg 'num)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <wav>) istream)
  "Deserializes a message object of type '<wav>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'data) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'data)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:aref vals i)) (cl:read-byte istream)))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'num)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'num)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'num)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'num)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 32) (cl:slot-value msg 'num)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 40) (cl:slot-value msg 'num)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 48) (cl:slot-value msg 'num)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 56) (cl:slot-value msg 'num)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<wav>)))
  "Returns string type for a message object of type '<wav>"
  "radar/wav")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'wav)))
  "Returns string type for a message object of type 'wav"
  "radar/wav")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<wav>)))
  "Returns md5sum for a message object of type '<wav>"
  "ee6398427bcac584a415147a410f1beb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'wav)))
  "Returns md5sum for a message object of type 'wav"
  "ee6398427bcac584a415147a410f1beb")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<wav>)))
  "Returns full string definition for message of type '<wav>"
  (cl:format cl:nil "uint16[] data~%uint64 num~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'wav)))
  "Returns full string definition for message of type 'wav"
  (cl:format cl:nil "uint16[] data~%uint64 num~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <wav>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'data) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 2)))
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <wav>))
  "Converts a ROS message object to a list"
  (cl:list 'wav
    (cl:cons ':data (data msg))
    (cl:cons ':num (num msg))
))
