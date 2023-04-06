;; Auto-generated. Do not edit!


(when (boundp 'ccmslam_msgs::right)
  (if (not (find-package "CCMSLAM_MSGS"))
    (make-package "CCMSLAM_MSGS"))
  (shadow 'right (find-package "CCMSLAM_MSGS")))
(unless (find-package "CCMSLAM_MSGS::RIGHT")
  (make-package "CCMSLAM_MSGS::RIGHT"))

(in-package "ROS")
;;//! \htmlinclude right.msg.html


(defclass ccmslam_msgs::right
  :super ros::object
  :slots (_mvuRight ))

(defmethod ccmslam_msgs::right
  (:init
   (&key
    ((:mvuRight __mvuRight) 0.0)
    )
   (send-super :init)
   (setq _mvuRight (float __mvuRight))
   self)
  (:mvuRight
   (&optional __mvuRight)
   (if __mvuRight (setq _mvuRight __mvuRight)) _mvuRight)
  (:serialization-length
   ()
   (+
    ;; float32 _mvuRight
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _mvuRight
       (sys::poke _mvuRight (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _mvuRight
     (setq _mvuRight (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get ccmslam_msgs::right :md5sum-) "18e1f68062c1d4bb45359a23f5776613")
(setf (get ccmslam_msgs::right :datatype-) "ccmslam_msgs/right")
(setf (get ccmslam_msgs::right :definition-)
      "float32 mvuRight
")



(provide :ccmslam_msgs/right "18e1f68062c1d4bb45359a23f5776613")


