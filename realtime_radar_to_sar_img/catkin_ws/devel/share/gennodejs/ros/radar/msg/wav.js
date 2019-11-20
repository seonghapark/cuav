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

class wav {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.data = null;
      this.sync = null;
      this.num = null;
      this.sr = null;
    }
    else {
      if (initObj.hasOwnProperty('data')) {
        this.data = initObj.data
      }
      else {
        this.data = [];
      }
      if (initObj.hasOwnProperty('sync')) {
        this.sync = initObj.sync
      }
      else {
        this.sync = [];
      }
      if (initObj.hasOwnProperty('num')) {
        this.num = initObj.num
      }
      else {
        this.num = 0;
      }
      if (initObj.hasOwnProperty('sr')) {
        this.sr = initObj.sr
      }
      else {
        this.sr = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type wav
    // Serialize message field [data]
    bufferOffset = _arraySerializer.int16(obj.data, buffer, bufferOffset, null);
    // Serialize message field [sync]
    bufferOffset = _arraySerializer.int16(obj.sync, buffer, bufferOffset, null);
    // Serialize message field [num]
    bufferOffset = _serializer.uint64(obj.num, buffer, bufferOffset);
    // Serialize message field [sr]
    bufferOffset = _serializer.uint64(obj.sr, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type wav
    let len;
    let data = new wav(null);
    // Deserialize message field [data]
    data.data = _arrayDeserializer.int16(buffer, bufferOffset, null)
    // Deserialize message field [sync]
    data.sync = _arrayDeserializer.int16(buffer, bufferOffset, null)
    // Deserialize message field [num]
    data.num = _deserializer.uint64(buffer, bufferOffset);
    // Deserialize message field [sr]
    data.sr = _deserializer.uint64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 2 * object.data.length;
    length += 2 * object.sync.length;
    return length + 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'radar/wav';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '835c58a78c35188ca9384fba6386b750';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int16[] data
    int16[] sync
    uint64 num
    uint64 sr
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new wav(null);
    if (msg.data !== undefined) {
      resolved.data = msg.data;
    }
    else {
      resolved.data = []
    }

    if (msg.sync !== undefined) {
      resolved.sync = msg.sync;
    }
    else {
      resolved.sync = []
    }

    if (msg.num !== undefined) {
      resolved.num = msg.num;
    }
    else {
      resolved.num = 0
    }

    if (msg.sr !== undefined) {
      resolved.sr = msg.sr;
    }
    else {
      resolved.sr = 0
    }

    return resolved;
    }
};

module.exports = wav;
