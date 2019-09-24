// Generated by gencpp from file radar/rail.msg
// DO NOT EDIT!


#ifndef RADAR_MESSAGE_RAIL_H
#define RADAR_MESSAGE_RAIL_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace radar
{
template <class ContainerAllocator>
struct rail_
{
  typedef rail_<ContainerAllocator> Type;

  rail_()
    : end(false)  {
    }
  rail_(const ContainerAllocator& _alloc)
    : end(false)  {
  (void)_alloc;
    }



   typedef uint8_t _end_type;
  _end_type end;





  typedef boost::shared_ptr< ::radar::rail_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::radar::rail_<ContainerAllocator> const> ConstPtr;

}; // struct rail_

typedef ::radar::rail_<std::allocator<void> > rail;

typedef boost::shared_ptr< ::radar::rail > railPtr;
typedef boost::shared_ptr< ::radar::rail const> railConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::radar::rail_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::radar::rail_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace radar

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'radar': ['/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::radar::rail_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::radar::rail_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::radar::rail_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::radar::rail_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::radar::rail_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::radar::rail_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::radar::rail_<ContainerAllocator> >
{
  static const char* value()
  {
    return "f9ac4e286e7f89fc602116455cd26e68";
  }

  static const char* value(const ::radar::rail_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xf9ac4e286e7f89fcULL;
  static const uint64_t static_value2 = 0x602116455cd26e68ULL;
};

template<class ContainerAllocator>
struct DataType< ::radar::rail_<ContainerAllocator> >
{
  static const char* value()
  {
    return "radar/rail";
  }

  static const char* value(const ::radar::rail_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::radar::rail_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool end\n\
";
  }

  static const char* value(const ::radar::rail_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::radar::rail_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.end);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct rail_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::radar::rail_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::radar::rail_<ContainerAllocator>& v)
  {
    s << indent << "end: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.end);
  }
};

} // namespace message_operations
} // namespace ros

#endif // RADAR_MESSAGE_RAIL_H
