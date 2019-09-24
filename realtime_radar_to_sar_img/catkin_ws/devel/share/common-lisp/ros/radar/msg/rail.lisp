; Auto-generated. Do not edit!


(cl:in-package radar-msg)


;//! \htmlinclude rail.msg.html

(cl:defclass <rail> (roslisp-msg-protocol:ros-message)
  ((end
    :reader end
    :initarg :end
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass rail (<rail>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <rail>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'rail)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name radar-msg:<rail> is deprecated: use radar-msg:rail instead.")))

(cl:ensure-generic-function 'end-val :lambda-list '(m))
(cl:defmethod end-val ((m <rail>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader radar-msg:end-val is deprecated.  Use radar-msg:end instead.")
  (end m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <rail>) ostream)
  "Serializes a message object of type '<rail>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'end) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <rail>) istream)
  "Deserializes a message object of type '<rail>"
    (cl:setf (cl:slot-value msg 'end) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<rail>)))
  "Returns string type for a message object of type '<rail>"
  "radar/rail")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'rail)))
  "Returns string type for a message object of type 'rail"
  "radar/rail")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<rail>)))
  "Returns md5sum for a message object of type '<rail>"
  "f9ac4e286e7f89fc602116455cd26e68")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'rail)))
  "Returns md5sum for a message object of type 'rail"
  "f9ac4e286e7f89fc602116455cd26e68")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<rail>)))
  "Returns full string definition for message of type '<rail>"
  (cl:format cl:nil "bool end~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'rail)))
  "Returns full string definition for message of type 'rail"
  (cl:format cl:nil "bool end~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <rail>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <rail>))
  "Converts a ROS message object to a list"
  (cl:list 'rail
    (cl:cons ':end (end msg))
))
