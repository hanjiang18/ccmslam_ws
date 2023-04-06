; Auto-generated. Do not edit!


(cl:in-package ccmslam_msgs-msg)


;//! \htmlinclude PC.msg.html

(cl:defclass <PC> (roslisp-msg-protocol:ros-message)
  ((mDepth
    :reader mDepth
    :initarg :mDepth
    :type cl:float
    :initform 0.0)
   (mx
    :reader mx
    :initarg :mx
    :type cl:float
    :initform 0.0)
   (my
    :reader my
    :initarg :my
    :type cl:float
    :initform 0.0)
   (mblue
    :reader mblue
    :initarg :mblue
    :type cl:fixnum
    :initform 0)
   (mgreen
    :reader mgreen
    :initarg :mgreen
    :type cl:fixnum
    :initform 0)
   (mred
    :reader mred
    :initarg :mred
    :type cl:fixnum
    :initform 0))
)

(cl:defclass PC (<PC>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PC>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PC)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ccmslam_msgs-msg:<PC> is deprecated: use ccmslam_msgs-msg:PC instead.")))

(cl:ensure-generic-function 'mDepth-val :lambda-list '(m))
(cl:defmethod mDepth-val ((m <PC>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ccmslam_msgs-msg:mDepth-val is deprecated.  Use ccmslam_msgs-msg:mDepth instead.")
  (mDepth m))

(cl:ensure-generic-function 'mx-val :lambda-list '(m))
(cl:defmethod mx-val ((m <PC>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ccmslam_msgs-msg:mx-val is deprecated.  Use ccmslam_msgs-msg:mx instead.")
  (mx m))

(cl:ensure-generic-function 'my-val :lambda-list '(m))
(cl:defmethod my-val ((m <PC>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ccmslam_msgs-msg:my-val is deprecated.  Use ccmslam_msgs-msg:my instead.")
  (my m))

(cl:ensure-generic-function 'mblue-val :lambda-list '(m))
(cl:defmethod mblue-val ((m <PC>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ccmslam_msgs-msg:mblue-val is deprecated.  Use ccmslam_msgs-msg:mblue instead.")
  (mblue m))

(cl:ensure-generic-function 'mgreen-val :lambda-list '(m))
(cl:defmethod mgreen-val ((m <PC>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ccmslam_msgs-msg:mgreen-val is deprecated.  Use ccmslam_msgs-msg:mgreen instead.")
  (mgreen m))

(cl:ensure-generic-function 'mred-val :lambda-list '(m))
(cl:defmethod mred-val ((m <PC>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ccmslam_msgs-msg:mred-val is deprecated.  Use ccmslam_msgs-msg:mred instead.")
  (mred m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PC>) ostream)
  "Serializes a message object of type '<PC>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'mDepth))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'mx))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'my))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'mblue)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'mgreen)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'mred)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PC>) istream)
  "Deserializes a message object of type '<PC>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'mDepth) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'mx) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'my) (roslisp-utils:decode-double-float-bits bits)))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'mblue)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'mgreen)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'mred)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PC>)))
  "Returns string type for a message object of type '<PC>"
  "ccmslam_msgs/PC")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PC)))
  "Returns string type for a message object of type 'PC"
  "ccmslam_msgs/PC")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PC>)))
  "Returns md5sum for a message object of type '<PC>"
  "bcd02d77df99fd4888c5c5f0c39553bc")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PC)))
  "Returns md5sum for a message object of type 'PC"
  "bcd02d77df99fd4888c5c5f0c39553bc")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PC>)))
  "Returns full string definition for message of type '<PC>"
  (cl:format cl:nil "float64 mDepth~%float64 mx~%float64 my~%uint8 mblue~%uint8 mgreen~%uint8 mred~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PC)))
  "Returns full string definition for message of type 'PC"
  (cl:format cl:nil "float64 mDepth~%float64 mx~%float64 my~%uint8 mblue~%uint8 mgreen~%uint8 mred~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PC>))
  (cl:+ 0
     8
     8
     8
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PC>))
  "Converts a ROS message object to a list"
  (cl:list 'PC
    (cl:cons ':mDepth (mDepth msg))
    (cl:cons ':mx (mx msg))
    (cl:cons ':my (my msg))
    (cl:cons ':mblue (mblue msg))
    (cl:cons ':mgreen (mgreen msg))
    (cl:cons ':mred (mred msg))
))
