;; Auto-generated. Do not edit!


(when (boundp 'ccmslam_msgs::PC)
  (if (not (find-package "CCMSLAM_MSGS"))
    (make-package "CCMSLAM_MSGS"))
  (shadow 'PC (find-package "CCMSLAM_MSGS")))
(unless (find-package "CCMSLAM_MSGS::PC")
  (make-package "CCMSLAM_MSGS::PC"))

(in-package "ROS")
;;//! \htmlinclude PC.msg.html


(defclass ccmslam_msgs::PC
  :super ros::object
  :slots (_mDepth _mx _my _mblue _mgreen _mred ))

(defmethod ccmslam_msgs::PC
  (:init
   (&key
    ((:mDepth __mDepth) 0.0)
    ((:mx __mx) 0.0)
    ((:my __my) 0.0)
    ((:mblue __mblue) 0)
    ((:mgreen __mgreen) 0)
    ((:mred __mred) 0)
    )
   (send-super :init)
   (setq _mDepth (float __mDepth))
   (setq _mx (float __mx))
   (setq _my (float __my))
   (setq _mblue (round __mblue))
   (setq _mgreen (round __mgreen))
   (setq _mred (round __mred))
   self)
  (:mDepth
   (&optional __mDepth)
   (if __mDepth (setq _mDepth __mDepth)) _mDepth)
  (:mx
   (&optional __mx)
   (if __mx (setq _mx __mx)) _mx)
  (:my
   (&optional __my)
   (if __my (setq _my __my)) _my)
  (:mblue
   (&optional __mblue)
   (if __mblue (setq _mblue __mblue)) _mblue)
  (:mgreen
   (&optional __mgreen)
   (if __mgreen (setq _mgreen __mgreen)) _mgreen)
  (:mred
   (&optional __mred)
   (if __mred (setq _mred __mred)) _mred)
  (:serialization-length
   ()
   (+
    ;; float64 _mDepth
    8
    ;; float64 _mx
    8
    ;; float64 _my
    8
    ;; uint8 _mblue
    1
    ;; uint8 _mgreen
    1
    ;; uint8 _mred
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _mDepth
       (sys::poke _mDepth (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _mx
       (sys::poke _mx (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _my
       (sys::poke _my (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; uint8 _mblue
       (write-byte _mblue s)
     ;; uint8 _mgreen
       (write-byte _mgreen s)
     ;; uint8 _mred
       (write-byte _mred s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _mDepth
     (setq _mDepth (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _mx
     (setq _mx (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _my
     (setq _my (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; uint8 _mblue
     (setq _mblue (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _mgreen
     (setq _mgreen (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _mred
     (setq _mred (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(setf (get ccmslam_msgs::PC :md5sum-) "bcd02d77df99fd4888c5c5f0c39553bc")
(setf (get ccmslam_msgs::PC :datatype-) "ccmslam_msgs/PC")
(setf (get ccmslam_msgs::PC :definition-)
      "float64 mDepth
float64 mx
float64 my
uint8 mblue
uint8 mgreen
uint8 mred
")



(provide :ccmslam_msgs/PC "bcd02d77df99fd4888c5c5f0c39553bc")


