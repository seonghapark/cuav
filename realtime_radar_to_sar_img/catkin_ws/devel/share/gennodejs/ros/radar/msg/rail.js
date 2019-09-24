// Auto-generated. Do not edit!

// (in-package radar.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class rail {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.end = null;
    }
    else {
      if (initObj.hasOwnProperty('end')) {
        this.end = initObj.end
      }
      else {
        this.end = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type rail
    // Serialize message field [end]
    bufferOffset = _serializer.bool(obj.end, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type rail
    let len;
    let data = new rail(null);
    // Deserialize message field [end]
    data.end = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a message object
    return 'radar/rail';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'f9ac4e286e7f89fc602116455cd26e68';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool end
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new rail(null);
    if (msg.end !== undefined) {
      resolved.end = msg.end;
    }
    else {
      resolved.end = false
    }

    return resolved;
    }
};

module.exports = rail;
