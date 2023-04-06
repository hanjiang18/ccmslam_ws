// Generated by gencpp from file ccmslam_msgs/UIntVec.msg
// DO NOT EDIT!


#ifndef CCMSLAM_MSGS_MESSAGE_UINTVEC_H
#define CCMSLAM_MSGS_MESSAGE_UINTVEC_H


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
struct UIntVec_
{
  typedef UIntVec_<ContainerAllocator> Type;

  UIntVec_()
    : uintvec()  {
    }
  UIntVec_(const ContainerAllocator& _alloc)
    : uintvec(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector<uint32_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<uint32_t>> _uintvec_type;
  _uintvec_type uintvec;





  typedef boost::shared_ptr< ::ccmslam_msgs::UIntVec_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ccmslam_msgs::UIntVec_<ContainerAllocator> const> ConstPtr;

}; // struct UIntVec_

typedef ::ccmslam_msgs::UIntVec_<std::allocator<void> > UIntVec;

typedef boost::shared_ptr< ::ccmslam_msgs::UIntVec > UIntVecPtr;
typedef boost::shared_ptr< ::ccmslam_msgs::UIntVec const> UIntVecConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ccmslam_msgs::UIntVec_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ccmslam_msgs::UIntVec_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::ccmslam_msgs::UIntVec_<ContainerAllocator1> & lhs, const ::ccmslam_msgs::UIntVec_<ContainerAllocator2> & rhs)
{
  return lhs.uintvec == rhs.uintvec;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::ccmslam_msgs::UIntVec_<ContainerAllocator1> & lhs, const ::ccmslam_msgs::UIntVec_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace ccmslam_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::ccmslam_msgs::UIntVec_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ccmslam_msgs::UIntVec_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ccmslam_msgs::UIntVec_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ccmslam_msgs::UIntVec_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ccmslam_msgs::UIntVec_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ccmslam_msgs::UIntVec_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ccmslam_msgs::UIntVec_<ContainerAllocator> >
{
  static const char* value()
  {
    return "4639613f2da593b427bc5b53e131a909";
  }

  static const char* value(const ::ccmslam_msgs::UIntVec_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x4639613f2da593b4ULL;
  static const uint64_t static_value2 = 0x27bc5b53e131a909ULL;
};

template<class ContainerAllocator>
struct DataType< ::ccmslam_msgs::UIntVec_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ccmslam_msgs/UIntVec";
  }

  static const char* value(const ::ccmslam_msgs::UIntVec_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ccmslam_msgs::UIntVec_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uint32[] uintvec\n"
;
  }

  static const char* value(const ::ccmslam_msgs::UIntVec_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ccmslam_msgs::UIntVec_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.uintvec);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct UIntVec_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ccmslam_msgs::UIntVec_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ccmslam_msgs::UIntVec_<ContainerAllocator>& v)
  {
    s << indent << "uintvec[]" << std::endl;
    for (size_t i = 0; i < v.uintvec.size(); ++i)
    {
      s << indent << "  uintvec[" << i << "]: ";
      Printer<uint32_t>::stream(s, indent + "  ", v.uintvec[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // CCMSLAM_MSGS_MESSAGE_UINTVEC_H
