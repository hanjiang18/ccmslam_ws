; Auto-generated. Do not edit!


(cl:in-package ccmslam_msgs-msg)


;//! \htmlinclude right.msg.html

(cl:defclass <right> (roslisp-msg-protocol:ros-message)
  ((mvuRight
    :reader mvuRight
    :initarg :mvuRight
    :type cl:float
    :initform 0.0))
)

(cl:defclass right (<right>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <right>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'right)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ccmslam_msgs-msg:<right> is deprecated: use ccmslam_msgs-msg:right instead.")))

(cl:ensure-generic-function 'mvuRight-val :lambda-list '(m))
(cl:defmethod mvuRight-val ((m <right>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ccmslam_msgs-msg:mvuRight-val is deprecated.  Use ccmslam_msgs-msg:mvuRight instead.")
  (mvuRight m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <right>) ostream)
  "Serializes a message object of type '<right>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'mvuRight))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <right>) istream)
  "Deserializes a message object of type '<right>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'mvuRight) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<right>)))
  "Returns string type for a message object of type '<right>"
  "ccmslam_msgs/right")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'right)))
  "Returns string type for a message object of type 'right"
  "ccmslam_msgs/right")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<right>)))
  "Returns md5sum for a message object of type '<right>"
  "18e1f68062c1d4bb45359a23f5776613")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'right)))
  "Returns md5sum for a message object of type 'right"
  "18e1f68062c1d4bb45359a23f5776613")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<right>)))
  "Returns full string definition for message of type '<right>"
  (cl:format cl:nil "float32 mvuRight~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'right)))
  "Returns full string definition for message of type 'right"
  (cl:format cl:nil "float32 mvuRight~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <right>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <right>))
  "Converts a ROS message object to a list"
  (cl:list 'right
    (cl:cons ':mvuRight (mvuRight msg))
))
