// Generated by gencpp from file ccmslam_msgs/CvKeyPoint.msg
// DO NOT EDIT!


#ifndef CCMSLAM_MSGS_MESSAGE_CVKEYPOINT_H
#define CCMSLAM_MSGS_MESSAGE_CVKEYPOINT_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace ccmslam_msgs
{
template <class ContainerAllocator>
struct CvKeyPoint_
{
  typedef CvKeyPoint_<ContainerAllocator> Type;

  CvKeyPoint_()
    : fPoint2f_x(0.0)
    , fPoint2f_y(0.0)
    , size(0)
    , angle(0.0)
    , response(0)
    , octave(0)  {
    }
  CvKeyPoint_(const ContainerAllocator& _alloc)
    : fPoint2f_x(0.0)
    , fPoint2f_y(0.0)
    , size(0)
    , angle(0.0)
    , response(0)
    , octave(0)  {
  (void)_alloc;
    }



   typedef float _fPoint2f_x_type;
  _fPoint2f_x_type fPoint2f_x;

   typedef float _fPoint2f_y_type;
  _fPoint2f_y_type fPoint2f_y;

   typedef uint8_t _size_type;
  _size_type size;

   typedef float _angle_type;
  _angle_type angle;

   typedef uint8_t _response_type;
  _response_type response;

   typedef int8_t _octave_type;
  _octave_type octave;





  typedef boost::shared_ptr< ::ccmslam_msgs::CvKeyPoint_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ccmslam_msgs::CvKeyPoint_<ContainerAllocator> const> ConstPtr;

}; // struct CvKeyPoint_

typedef ::ccmslam_msgs::CvKeyPoint_<std::allocator<void> > CvKeyPoint;

typedef boost::shared_ptr< ::ccmslam_msgs::CvKeyPoint > CvKeyPointPtr;
typedef boost::shared_ptr< ::ccmslam_msgs::CvKeyPoint const> CvKeyPointConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ccmslam_msgs::CvKeyPoint_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ccmslam_msgs::CvKeyPoint_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::ccmslam_msgs::CvKeyPoint_<ContainerAllocator1> & lhs, const ::ccmslam_msgs::CvKeyPoint_<ContainerAllocator2> & rhs)
{
  return lhs.fPoint2f_x == rhs.fPoint2f_x &&
    lhs.fPoint2f_y == rhs.fPoint2f_y &&
    lhs.size == rhs.size &&
    lhs.angle == rhs.angle &&
    lhs.response == rhs.response &&
    lhs.octave == rhs.octave;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::ccmslam_msgs::CvKeyPoint_<ContainerAllocator1> & lhs, const ::ccmslam_msgs::CvKeyPoint_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace ccmslam_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::ccmslam_msgs::CvKeyPoint_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ccmslam_msgs::CvKeyPoint_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ccmslam_msgs::CvKeyPoint_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ccmslam_msgs::CvKeyPoint_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ccmslam_msgs::CvKeyPoint_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ccmslam_msgs::CvKeyPoint_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ccmslam_msgs::CvKeyPoint_<ContainerAllocator> >
{
  static const char* value()
  {
    return "90996e3a2f237f647a484f1ea5d89bea";
  }

  static const char* value(const ::ccmslam_msgs::CvKeyPoint_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x90996e3a2f237f64ULL;
  static const uint64_t static_value2 = 0x7a484f1ea5d89beaULL;
};

template<class ContainerAllocator>
struct DataType< ::ccmslam_msgs::CvKeyPoint_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ccmslam_msgs/CvKeyPoint";
  }

  static const char* value(const ::ccmslam_msgs::CvKeyPoint_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ccmslam_msgs::CvKeyPoint_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 fPoint2f_x\n"
"float32 fPoint2f_y\n"
"#float32 size\n"
"uint8 size\n"
"float32 angle\n"
"#float32 response\n"
"uint8 response\n"
"int8 octave\n"
"#int8 class_id\n"
;
  }

  static const char* value(const ::ccmslam_msgs::CvKeyPoint_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ccmslam_msgs::CvKeyPoint_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.fPoint2f_x);
      stream.next(m.fPoint2f_y);
      stream.next(m.size);
      stream.next(m.angle);
      stream.next(m.response);
      stream.next(m.octave);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct CvKeyPoint_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ccmslam_msgs::CvKeyPoint_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ccmslam_msgs::CvKeyPoint_<ContainerAllocator>& v)
  {
    s << indent << "fPoint2f_x: ";
    Printer<float>::stream(s, indent + "  ", v.fPoint2f_x);
    s << indent << "fPoint2f_y: ";
    Printer<float>::stream(s, indent + "  ", v.fPoint2f_y);
    s << indent << "size: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.size);
    s << indent << "angle: ";
    Printer<float>::stream(s, indent + "  ", v.angle);
    s << indent << "response: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.response);
    s << indent << "octave: ";
    Printer<int8_t>::stream(s, indent + "  ", v.octave);
  }
};

} // namespace message_operations
} // namespace ros

#endif // CCMSLAM_MSGS_MESSAGE_CVKEYPOINT_H