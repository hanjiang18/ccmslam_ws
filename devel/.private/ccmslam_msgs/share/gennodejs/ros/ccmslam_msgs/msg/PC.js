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

class PC {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.mDepth = null;
      this.mx = null;
      this.my = null;
      this.mblue = null;
      this.mgreen = null;
      this.mred = null;
    }
    else {
      if (initObj.hasOwnProperty('mDepth')) {
        this.mDepth = initObj.mDepth
      }
      else {
        this.mDepth = 0.0;
      }
      if (initObj.hasOwnProperty('mx')) {
        this.mx = initObj.mx
      }
      else {
        this.mx = 0.0;
      }
      if (initObj.hasOwnProperty('my')) {
        this.my = initObj.my
      }
      else {
        this.my = 0.0;
      }
      if (initObj.hasOwnProperty('mblue')) {
        this.mblue = initObj.mblue
      }
      else {
        this.mblue = 0;
      }
      if (initObj.hasOwnProperty('mgreen')) {
        this.mgreen = initObj.mgreen
      }
      else {
        this.mgreen = 0;
      }
      if (initObj.hasOwnProperty('mred')) {
        this.mred = initObj.mred
      }
      else {
        this.mred = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type PC
    // Serialize message field [mDepth]
    bufferOffset = _serializer.float64(obj.mDepth, buffer, bufferOffset);
    // Serialize message field [mx]
    bufferOffset = _serializer.float64(obj.mx, buffer, bufferOffset);
    // Serialize message field [my]
    bufferOffset = _serializer.float64(obj.my, buffer, bufferOffset);
    // Serialize message field [mblue]
    bufferOffset = _serializer.uint8(obj.mblue, buffer, bufferOffset);
    // Serialize message field [mgreen]
    bufferOffset = _serializer.uint8(obj.mgreen, buffer, bufferOffset);
    // Serialize message field [mred]
    bufferOffset = _serializer.uint8(obj.mred, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type PC
    let len;
    let data = new PC(null);
    // Deserialize message field [mDepth]
    data.mDepth = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [mx]
    data.mx = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [my]
    data.my = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [mblue]
    data.mblue = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [mgreen]
    data.mgreen = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [mred]
    data.mred = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 27;
  }

  static datatype() {
    // Returns string type for a message object
    return 'ccmslam_msgs/PC';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'bcd02d77df99fd4888c5c5f0c39553bc';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 mDepth
    float64 mx
    float64 my
    uint8 mblue
    uint8 mgreen
    uint8 mred
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new PC(null);
    if (msg.mDepth !== undefined) {
      resolved.mDepth = msg.mDepth;
    }
    else {
      resolved.mDepth = 0.0
    }

    if (msg.mx !== undefined) {
      resolved.mx = msg.mx;
    }
    else {
      resolved.mx = 0.0
    }

    if (msg.my !== undefined) {
      resolved.my = msg.my;
    }
    else {
      resolved.my = 0.0
    }

    if (msg.mblue !== undefined) {
      resolved.mblue = msg.mblue;
    }
    else {
      resolved.mblue = 0
    }

    if (msg.mgreen !== undefined) {
      resolved.mgreen = msg.mgreen;
    }
    else {
      resolved.mgreen = 0
    }

    if (msg.mred !== undefined) {
      resolved.mred = msg.mred;
    }
    else {
      resolved.mred = 0
    }

    return resolved;
    }
};

module.exports = PC;
