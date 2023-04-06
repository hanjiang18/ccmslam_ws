// Auto-generated. Do not edit!

// (in-package ccmslam_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class right {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.mvuRight = null;
    }
    else {
      if (initObj.hasOwnProperty('mvuRight')) {
        this.mvuRight = initObj.mvuRight
      }
      else {
        this.mvuRight = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type right
    // Serialize message field [mvuRight]
    bufferOffset = _serializer.float32(obj.mvuRight, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type right
    let len;
    let data = new right(null);
    // Deserialize message field [mvuRight]
    data.mvuRight = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'ccmslam_msgs/right';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '18e1f68062c1d4bb45359a23f5776613';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 mvuRight
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new right(null);
    if (msg.mvuRight !== undefined) {
      resolved.mvuRight = msg.mvuRight;
    }
    else {
      resolved.mvuRight = 0.0
    }

    return resolved;
    }
};

module.exports = right;
