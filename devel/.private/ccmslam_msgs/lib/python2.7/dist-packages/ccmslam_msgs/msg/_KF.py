# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ccmslam_msgs/KF.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import ccmslam_msgs.msg

class KF(genpy.Message):
  _md5sum = "a6c3197f3c165f89cfb6d964597ca46c"
  _type = "ccmslam_msgs/KF"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """bool bSentOnce

uint16 mnId # unique KF id
uint8 mClientId # client id
uint32 mUniqueId
float64 dTimestamp
bool mbAck

#Grid (to speed up feature matching)
    int16 mnGridCols
    int16 mnGridRows
    float32 mfGridElementWidthInv
    float32 mfGridElementHeightInv

#Calibration parameters
    float32 fx
    float32 fy
    float32 cx
    float32 cy
    float32 invfx
    float32 invfy
     float32 mbf
    float32 mb

#Number of KeyPoints
    int16 N

#KeyPoints, stereo coordinate and descriptors (all associated by an index)
    CvKeyPoint[] mvKeysUn
    Descriptor[] mDescriptors
    PC[] mPointCloud
    right[] mright

#Pose relative to parent
    float32[16] mTcpred
    float32[16] mTcpar

    bool mbPoseChanged

    bool mbServerBA

    float32[16] mT_SC

#Scale
    int8 mnScaleLevels
    float32 mfScaleFactor
    float32 mfLogScaleFactor
    float32[8] mvScaleFactors
    float32[8] mvLevelSigma2
    float32[8] mvInvLevelSigma2

#Image bounds and calibration
    int16 mnMinX
    int16 mnMinY
    int16 mnMaxX
    int16 mnMaxY
    float32[9] mK

#MapPoints associated to keypoints
    uint32[] mvpMapPoints_Ids
    uint8[] mvpMapPoints_ClientIds
    uint16[] mvpMapPoints_VectId

#Related KFs
    uint16 mpPred_KfId
    uint8 mpPred_KfClientId
    uint16 mpPar_KfId
    uint8 mpPar_KfClientId

#Bad flags
    bool mbBad

================================================================================
MSG: ccmslam_msgs/CvKeyPoint
float32 fPoint2f_x
float32 fPoint2f_y
#float32 size
uint8 size
float32 angle
#float32 response
uint8 response
int8 octave
#int8 class_id

================================================================================
MSG: ccmslam_msgs/Descriptor
uint8[32] mDescriptor

================================================================================
MSG: ccmslam_msgs/PC
float64 mDepth
float64 mx
float64 my
uint8 mblue
uint8 mgreen
uint8 mred
================================================================================
MSG: ccmslam_msgs/right
float32 mvuRight"""
  __slots__ = ['bSentOnce','mnId','mClientId','mUniqueId','dTimestamp','mbAck','mnGridCols','mnGridRows','mfGridElementWidthInv','mfGridElementHeightInv','fx','fy','cx','cy','invfx','invfy','mbf','mb','N','mvKeysUn','mDescriptors','mPointCloud','mright','mTcpred','mTcpar','mbPoseChanged','mbServerBA','mT_SC','mnScaleLevels','mfScaleFactor','mfLogScaleFactor','mvScaleFactors','mvLevelSigma2','mvInvLevelSigma2','mnMinX','mnMinY','mnMaxX','mnMaxY','mK','mvpMapPoints_Ids','mvpMapPoints_ClientIds','mvpMapPoints_VectId','mpPred_KfId','mpPred_KfClientId','mpPar_KfId','mpPar_KfClientId','mbBad']
  _slot_types = ['bool','uint16','uint8','uint32','float64','bool','int16','int16','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','int16','ccmslam_msgs/CvKeyPoint[]','ccmslam_msgs/Descriptor[]','ccmslam_msgs/PC[]','ccmslam_msgs/right[]','float32[16]','float32[16]','bool','bool','float32[16]','int8','float32','float32','float32[8]','float32[8]','float32[8]','int16','int16','int16','int16','float32[9]','uint32[]','uint8[]','uint16[]','uint16','uint8','uint16','uint8','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       bSentOnce,mnId,mClientId,mUniqueId,dTimestamp,mbAck,mnGridCols,mnGridRows,mfGridElementWidthInv,mfGridElementHeightInv,fx,fy,cx,cy,invfx,invfy,mbf,mb,N,mvKeysUn,mDescriptors,mPointCloud,mright,mTcpred,mTcpar,mbPoseChanged,mbServerBA,mT_SC,mnScaleLevels,mfScaleFactor,mfLogScaleFactor,mvScaleFactors,mvLevelSigma2,mvInvLevelSigma2,mnMinX,mnMinY,mnMaxX,mnMaxY,mK,mvpMapPoints_Ids,mvpMapPoints_ClientIds,mvpMapPoints_VectId,mpPred_KfId,mpPred_KfClientId,mpPar_KfId,mpPar_KfClientId,mbBad

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(KF, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.bSentOnce is None:
        self.bSentOnce = False
      if self.mnId is None:
        self.mnId = 0
      if self.mClientId is None:
        self.mClientId = 0
      if self.mUniqueId is None:
        self.mUniqueId = 0
      if self.dTimestamp is None:
        self.dTimestamp = 0.
      if self.mbAck is None:
        self.mbAck = False
      if self.mnGridCols is None:
        self.mnGridCols = 0
      if self.mnGridRows is None:
        self.mnGridRows = 0
      if self.mfGridElementWidthInv is None:
        self.mfGridElementWidthInv = 0.
      if self.mfGridElementHeightInv is None:
        self.mfGridElementHeightInv = 0.
      if self.fx is None:
        self.fx = 0.
      if self.fy is None:
        self.fy = 0.
      if self.cx is None:
        self.cx = 0.
      if self.cy is None:
        self.cy = 0.
      if self.invfx is None:
        self.invfx = 0.
      if self.invfy is None:
        self.invfy = 0.
      if self.mbf is None:
        self.mbf = 0.
      if self.mb is None:
        self.mb = 0.
      if self.N is None:
        self.N = 0
      if self.mvKeysUn is None:
        self.mvKeysUn = []
      if self.mDescriptors is None:
        self.mDescriptors = []
      if self.mPointCloud is None:
        self.mPointCloud = []
      if self.mright is None:
        self.mright = []
      if self.mTcpred is None:
        self.mTcpred = [0.] * 16
      if self.mTcpar is None:
        self.mTcpar = [0.] * 16
      if self.mbPoseChanged is None:
        self.mbPoseChanged = False
      if self.mbServerBA is None:
        self.mbServerBA = False
      if self.mT_SC is None:
        self.mT_SC = [0.] * 16
      if self.mnScaleLevels is None:
        self.mnScaleLevels = 0
      if self.mfScaleFactor is None:
        self.mfScaleFactor = 0.
      if self.mfLogScaleFactor is None:
        self.mfLogScaleFactor = 0.
      if self.mvScaleFactors is None:
        self.mvScaleFactors = [0.] * 8
      if self.mvLevelSigma2 is None:
        self.mvLevelSigma2 = [0.] * 8
      if self.mvInvLevelSigma2 is None:
        self.mvInvLevelSigma2 = [0.] * 8
      if self.mnMinX is None:
        self.mnMinX = 0
      if self.mnMinY is None:
        self.mnMinY = 0
      if self.mnMaxX is None:
        self.mnMaxX = 0
      if self.mnMaxY is None:
        self.mnMaxY = 0
      if self.mK is None:
        self.mK = [0.] * 9
      if self.mvpMapPoints_Ids is None:
        self.mvpMapPoints_Ids = []
      if self.mvpMapPoints_ClientIds is None:
        self.mvpMapPoints_ClientIds = b''
      if self.mvpMapPoints_VectId is None:
        self.mvpMapPoints_VectId = []
      if self.mpPred_KfId is None:
        self.mpPred_KfId = 0
      if self.mpPred_KfClientId is None:
        self.mpPred_KfClientId = 0
      if self.mpPar_KfId is None:
        self.mpPar_KfId = 0
      if self.mpPar_KfClientId is None:
        self.mpPar_KfClientId = 0
      if self.mbBad is None:
        self.mbBad = False
    else:
      self.bSentOnce = False
      self.mnId = 0
      self.mClientId = 0
      self.mUniqueId = 0
      self.dTimestamp = 0.
      self.mbAck = False
      self.mnGridCols = 0
      self.mnGridRows = 0
      self.mfGridElementWidthInv = 0.
      self.mfGridElementHeightInv = 0.
      self.fx = 0.
      self.fy = 0.
      self.cx = 0.
      self.cy = 0.
      self.invfx = 0.
      self.invfy = 0.
      self.mbf = 0.
      self.mb = 0.
      self.N = 0
      self.mvKeysUn = []
      self.mDescriptors = []
      self.mPointCloud = []
      self.mright = []
      self.mTcpred = [0.] * 16
      self.mTcpar = [0.] * 16
      self.mbPoseChanged = False
      self.mbServerBA = False
      self.mT_SC = [0.] * 16
      self.mnScaleLevels = 0
      self.mfScaleFactor = 0.
      self.mfLogScaleFactor = 0.
      self.mvScaleFactors = [0.] * 8
      self.mvLevelSigma2 = [0.] * 8
      self.mvInvLevelSigma2 = [0.] * 8
      self.mnMinX = 0
      self.mnMinY = 0
      self.mnMaxX = 0
      self.mnMaxY = 0
      self.mK = [0.] * 9
      self.mvpMapPoints_Ids = []
      self.mvpMapPoints_ClientIds = b''
      self.mvpMapPoints_VectId = []
      self.mpPred_KfId = 0
      self.mpPred_KfClientId = 0
      self.mpPar_KfId = 0
      self.mpPar_KfClientId = 0
      self.mbBad = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_BHBIdB2h10fh().pack(_x.bSentOnce, _x.mnId, _x.mClientId, _x.mUniqueId, _x.dTimestamp, _x.mbAck, _x.mnGridCols, _x.mnGridRows, _x.mfGridElementWidthInv, _x.mfGridElementHeightInv, _x.fx, _x.fy, _x.cx, _x.cy, _x.invfx, _x.invfy, _x.mbf, _x.mb, _x.N))
      length = len(self.mvKeysUn)
      buff.write(_struct_I.pack(length))
      for val1 in self.mvKeysUn:
        _x = val1
        buff.write(_get_struct_2fBfBb().pack(_x.fPoint2f_x, _x.fPoint2f_y, _x.size, _x.angle, _x.response, _x.octave))
      length = len(self.mDescriptors)
      buff.write(_struct_I.pack(length))
      for val1 in self.mDescriptors:
        _x = val1.mDescriptor
        # - if encoded as a list instead, serialize as bytes instead of string
        if type(_x) in [list, tuple]:
          buff.write(_get_struct_32B().pack(*_x))
        else:
          buff.write(_get_struct_32s().pack(_x))
      length = len(self.mPointCloud)
      buff.write(_struct_I.pack(length))
      for val1 in self.mPointCloud:
        _x = val1
        buff.write(_get_struct_3d3B().pack(_x.mDepth, _x.mx, _x.my, _x.mblue, _x.mgreen, _x.mred))
      length = len(self.mright)
      buff.write(_struct_I.pack(length))
      for val1 in self.mright:
        _x = val1.mvuRight
        buff.write(_get_struct_f().pack(_x))
      buff.write(_get_struct_16f().pack(*self.mTcpred))
      buff.write(_get_struct_16f().pack(*self.mTcpar))
      _x = self
      buff.write(_get_struct_2B().pack(_x.mbPoseChanged, _x.mbServerBA))
      buff.write(_get_struct_16f().pack(*self.mT_SC))
      _x = self
      buff.write(_get_struct_b2f().pack(_x.mnScaleLevels, _x.mfScaleFactor, _x.mfLogScaleFactor))
      buff.write(_get_struct_8f().pack(*self.mvScaleFactors))
      buff.write(_get_struct_8f().pack(*self.mvLevelSigma2))
      buff.write(_get_struct_8f().pack(*self.mvInvLevelSigma2))
      _x = self
      buff.write(_get_struct_4h().pack(_x.mnMinX, _x.mnMinY, _x.mnMaxX, _x.mnMaxY))
      buff.write(_get_struct_9f().pack(*self.mK))
      length = len(self.mvpMapPoints_Ids)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(struct.Struct(pattern).pack(*self.mvpMapPoints_Ids))
      _x = self.mvpMapPoints_ClientIds
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.mvpMapPoints_VectId)
      buff.write(_struct_I.pack(length))
      pattern = '<%sH'%length
      buff.write(struct.Struct(pattern).pack(*self.mvpMapPoints_VectId))
      _x = self
      buff.write(_get_struct_HBH2B().pack(_x.mpPred_KfId, _x.mpPred_KfClientId, _x.mpPar_KfId, _x.mpPar_KfClientId, _x.mbBad))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.mvKeysUn is None:
        self.mvKeysUn = None
      if self.mDescriptors is None:
        self.mDescriptors = None
      if self.mPointCloud is None:
        self.mPointCloud = None
      if self.mright is None:
        self.mright = None
      end = 0
      _x = self
      start = end
      end += 63
      (_x.bSentOnce, _x.mnId, _x.mClientId, _x.mUniqueId, _x.dTimestamp, _x.mbAck, _x.mnGridCols, _x.mnGridRows, _x.mfGridElementWidthInv, _x.mfGridElementHeightInv, _x.fx, _x.fy, _x.cx, _x.cy, _x.invfx, _x.invfy, _x.mbf, _x.mb, _x.N,) = _get_struct_BHBIdB2h10fh().unpack(str[start:end])
      self.bSentOnce = bool(self.bSentOnce)
      self.mbAck = bool(self.mbAck)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.mvKeysUn = []
      for i in range(0, length):
        val1 = ccmslam_msgs.msg.CvKeyPoint()
        _x = val1
        start = end
        end += 15
        (_x.fPoint2f_x, _x.fPoint2f_y, _x.size, _x.angle, _x.response, _x.octave,) = _get_struct_2fBfBb().unpack(str[start:end])
        self.mvKeysUn.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.mDescriptors = []
      for i in range(0, length):
        val1 = ccmslam_msgs.msg.Descriptor()
        start = end
        end += 32
        val1.mDescriptor = str[start:end]
        self.mDescriptors.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.mPointCloud = []
      for i in range(0, length):
        val1 = ccmslam_msgs.msg.PC()
        _x = val1
        start = end
        end += 27
        (_x.mDepth, _x.mx, _x.my, _x.mblue, _x.mgreen, _x.mred,) = _get_struct_3d3B().unpack(str[start:end])
        self.mPointCloud.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.mright = []
      for i in range(0, length):
        val1 = ccmslam_msgs.msg.right()
        start = end
        end += 4
        (val1.mvuRight,) = _get_struct_f().unpack(str[start:end])
        self.mright.append(val1)
      start = end
      end += 64
      self.mTcpred = _get_struct_16f().unpack(str[start:end])
      start = end
      end += 64
      self.mTcpar = _get_struct_16f().unpack(str[start:end])
      _x = self
      start = end
      end += 2
      (_x.mbPoseChanged, _x.mbServerBA,) = _get_struct_2B().unpack(str[start:end])
      self.mbPoseChanged = bool(self.mbPoseChanged)
      self.mbServerBA = bool(self.mbServerBA)
      start = end
      end += 64
      self.mT_SC = _get_struct_16f().unpack(str[start:end])
      _x = self
      start = end
      end += 9
      (_x.mnScaleLevels, _x.mfScaleFactor, _x.mfLogScaleFactor,) = _get_struct_b2f().unpack(str[start:end])
      start = end
      end += 32
      self.mvScaleFactors = _get_struct_8f().unpack(str[start:end])
      start = end
      end += 32
      self.mvLevelSigma2 = _get_struct_8f().unpack(str[start:end])
      start = end
      end += 32
      self.mvInvLevelSigma2 = _get_struct_8f().unpack(str[start:end])
      _x = self
      start = end
      end += 8
      (_x.mnMinX, _x.mnMinY, _x.mnMaxX, _x.mnMaxY,) = _get_struct_4h().unpack(str[start:end])
      start = end
      end += 36
      self.mK = _get_struct_9f().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.mvpMapPoints_Ids = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.mvpMapPoints_ClientIds = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sH'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.mvpMapPoints_VectId = s.unpack(str[start:end])
      _x = self
      start = end
      end += 7
      (_x.mpPred_KfId, _x.mpPred_KfClientId, _x.mpPar_KfId, _x.mpPar_KfClientId, _x.mbBad,) = _get_struct_HBH2B().unpack(str[start:end])
      self.mbBad = bool(self.mbBad)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_BHBIdB2h10fh().pack(_x.bSentOnce, _x.mnId, _x.mClientId, _x.mUniqueId, _x.dTimestamp, _x.mbAck, _x.mnGridCols, _x.mnGridRows, _x.mfGridElementWidthInv, _x.mfGridElementHeightInv, _x.fx, _x.fy, _x.cx, _x.cy, _x.invfx, _x.invfy, _x.mbf, _x.mb, _x.N))
      length = len(self.mvKeysUn)
      buff.write(_struct_I.pack(length))
      for val1 in self.mvKeysUn:
        _x = val1
        buff.write(_get_struct_2fBfBb().pack(_x.fPoint2f_x, _x.fPoint2f_y, _x.size, _x.angle, _x.response, _x.octave))
      length = len(self.mDescriptors)
      buff.write(_struct_I.pack(length))
      for val1 in self.mDescriptors:
        _x = val1.mDescriptor
        # - if encoded as a list instead, serialize as bytes instead of string
        if type(_x) in [list, tuple]:
          buff.write(_get_struct_32B().pack(*_x))
        else:
          buff.write(_get_struct_32s().pack(_x))
      length = len(self.mPointCloud)
      buff.write(_struct_I.pack(length))
      for val1 in self.mPointCloud:
        _x = val1
        buff.write(_get_struct_3d3B().pack(_x.mDepth, _x.mx, _x.my, _x.mblue, _x.mgreen, _x.mred))
      length = len(self.mright)
      buff.write(_struct_I.pack(length))
      for val1 in self.mright:
        _x = val1.mvuRight
        buff.write(_get_struct_f().pack(_x))
      buff.write(self.mTcpred.tostring())
      buff.write(self.mTcpar.tostring())
      _x = self
      buff.write(_get_struct_2B().pack(_x.mbPoseChanged, _x.mbServerBA))
      buff.write(self.mT_SC.tostring())
      _x = self
      buff.write(_get_struct_b2f().pack(_x.mnScaleLevels, _x.mfScaleFactor, _x.mfLogScaleFactor))
      buff.write(self.mvScaleFactors.tostring())
      buff.write(self.mvLevelSigma2.tostring())
      buff.write(self.mvInvLevelSigma2.tostring())
      _x = self
      buff.write(_get_struct_4h().pack(_x.mnMinX, _x.mnMinY, _x.mnMaxX, _x.mnMaxY))
      buff.write(self.mK.tostring())
      length = len(self.mvpMapPoints_Ids)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(self.mvpMapPoints_Ids.tostring())
      _x = self.mvpMapPoints_ClientIds
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.mvpMapPoints_VectId)
      buff.write(_struct_I.pack(length))
      pattern = '<%sH'%length
      buff.write(self.mvpMapPoints_VectId.tostring())
      _x = self
      buff.write(_get_struct_HBH2B().pack(_x.mpPred_KfId, _x.mpPred_KfClientId, _x.mpPar_KfId, _x.mpPar_KfClientId, _x.mbBad))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.mvKeysUn is None:
        self.mvKeysUn = None
      if self.mDescriptors is None:
        self.mDescriptors = None
      if self.mPointCloud is None:
        self.mPointCloud = None
      if self.mright is None:
        self.mright = None
      end = 0
      _x = self
      start = end
      end += 63
      (_x.bSentOnce, _x.mnId, _x.mClientId, _x.mUniqueId, _x.dTimestamp, _x.mbAck, _x.mnGridCols, _x.mnGridRows, _x.mfGridElementWidthInv, _x.mfGridElementHeightInv, _x.fx, _x.fy, _x.cx, _x.cy, _x.invfx, _x.invfy, _x.mbf, _x.mb, _x.N,) = _get_struct_BHBIdB2h10fh().unpack(str[start:end])
      self.bSentOnce = bool(self.bSentOnce)
      self.mbAck = bool(self.mbAck)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.mvKeysUn = []
      for i in range(0, length):
        val1 = ccmslam_msgs.msg.CvKeyPoint()
        _x = val1
        start = end
        end += 15
        (_x.fPoint2f_x, _x.fPoint2f_y, _x.size, _x.angle, _x.response, _x.octave,) = _get_struct_2fBfBb().unpack(str[start:end])
        self.mvKeysUn.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.mDescriptors = []
      for i in range(0, length):
        val1 = ccmslam_msgs.msg.Descriptor()
        start = end
        end += 32
        val1.mDescriptor = str[start:end]
        self.mDescriptors.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.mPointCloud = []
      for i in range(0, length):
        val1 = ccmslam_msgs.msg.PC()
        _x = val1
        start = end
        end += 27
        (_x.mDepth, _x.mx, _x.my, _x.mblue, _x.mgreen, _x.mred,) = _get_struct_3d3B().unpack(str[start:end])
        self.mPointCloud.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.mright = []
      for i in range(0, length):
        val1 = ccmslam_msgs.msg.right()
        start = end
        end += 4
        (val1.mvuRight,) = _get_struct_f().unpack(str[start:end])
        self.mright.append(val1)
      start = end
      end += 64
      self.mTcpred = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=16)
      start = end
      end += 64
      self.mTcpar = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=16)
      _x = self
      start = end
      end += 2
      (_x.mbPoseChanged, _x.mbServerBA,) = _get_struct_2B().unpack(str[start:end])
      self.mbPoseChanged = bool(self.mbPoseChanged)
      self.mbServerBA = bool(self.mbServerBA)
      start = end
      end += 64
      self.mT_SC = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=16)
      _x = self
      start = end
      end += 9
      (_x.mnScaleLevels, _x.mfScaleFactor, _x.mfLogScaleFactor,) = _get_struct_b2f().unpack(str[start:end])
      start = end
      end += 32
      self.mvScaleFactors = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=8)
      start = end
      end += 32
      self.mvLevelSigma2 = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=8)
      start = end
      end += 32
      self.mvInvLevelSigma2 = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=8)
      _x = self
      start = end
      end += 8
      (_x.mnMinX, _x.mnMinY, _x.mnMaxX, _x.mnMaxY,) = _get_struct_4h().unpack(str[start:end])
      start = end
      end += 36
      self.mK = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=9)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.mvpMapPoints_Ids = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.mvpMapPoints_ClientIds = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sH'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.mvpMapPoints_VectId = numpy.frombuffer(str[start:end], dtype=numpy.uint16, count=length)
      _x = self
      start = end
      end += 7
      (_x.mpPred_KfId, _x.mpPred_KfClientId, _x.mpPar_KfId, _x.mpPar_KfClientId, _x.mbBad,) = _get_struct_HBH2B().unpack(str[start:end])
      self.mbBad = bool(self.mbBad)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_16f = None
def _get_struct_16f():
    global _struct_16f
    if _struct_16f is None:
        _struct_16f = struct.Struct("<16f")
    return _struct_16f
_struct_2B = None
def _get_struct_2B():
    global _struct_2B
    if _struct_2B is None:
        _struct_2B = struct.Struct("<2B")
    return _struct_2B
_struct_2fBfBb = None
def _get_struct_2fBfBb():
    global _struct_2fBfBb
    if _struct_2fBfBb is None:
        _struct_2fBfBb = struct.Struct("<2fBfBb")
    return _struct_2fBfBb
_struct_32B = None
def _get_struct_32B():
    global _struct_32B
    if _struct_32B is None:
        _struct_32B = struct.Struct("<32B")
    return _struct_32B
_struct_32s = None
def _get_struct_32s():
    global _struct_32s
    if _struct_32s is None:
        _struct_32s = struct.Struct("<32s")
    return _struct_32s
_struct_3d3B = None
def _get_struct_3d3B():
    global _struct_3d3B
    if _struct_3d3B is None:
        _struct_3d3B = struct.Struct("<3d3B")
    return _struct_3d3B
_struct_4h = None
def _get_struct_4h():
    global _struct_4h
    if _struct_4h is None:
        _struct_4h = struct.Struct("<4h")
    return _struct_4h
_struct_8f = None
def _get_struct_8f():
    global _struct_8f
    if _struct_8f is None:
        _struct_8f = struct.Struct("<8f")
    return _struct_8f
_struct_9f = None
def _get_struct_9f():
    global _struct_9f
    if _struct_9f is None:
        _struct_9f = struct.Struct("<9f")
    return _struct_9f
_struct_BHBIdB2h10fh = None
def _get_struct_BHBIdB2h10fh():
    global _struct_BHBIdB2h10fh
    if _struct_BHBIdB2h10fh is None:
        _struct_BHBIdB2h10fh = struct.Struct("<BHBIdB2h10fh")
    return _struct_BHBIdB2h10fh
_struct_HBH2B = None
def _get_struct_HBH2B():
    global _struct_HBH2B
    if _struct_HBH2B is None:
        _struct_HBH2B = struct.Struct("<HBH2B")
    return _struct_HBH2B
_struct_b2f = None
def _get_struct_b2f():
    global _struct_b2f
    if _struct_b2f is None:
        _struct_b2f = struct.Struct("<b2f")
    return _struct_b2f
_struct_f = None
def _get_struct_f():
    global _struct_f
    if _struct_f is None:
        _struct_f = struct.Struct("<f")
    return _struct_f
