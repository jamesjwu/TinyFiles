# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: filerequest.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='filerequest.proto',
  package='',
  serialized_pb='\n\x11\x66ilerequest.proto\"\x9d\x01\n\x0b\x46ileRequest\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\x12\x10\n\x08\x63ontents\x18\x02 \x01(\t\x12.\n\x0crequest_type\x18\x03 \x02(\x0e\x32\x18.FileRequest.RequestType\":\n\x0bRequestType\x12\x08\n\x04READ\x10\x00\x12\t\n\x05WRITE\x10\x01\x12\n\n\x06\x41PPEND\x10\x02\x12\n\n\x06\x44\x45LETE\x10\x03\"1\n\x0c\x46ileResponse\x12\x0f\n\x07success\x18\x01 \x02(\x08\x12\x10\n\x08\x63ontents\x18\x02 \x01(\t')



_FILEREQUEST_REQUESTTYPE = _descriptor.EnumDescriptor(
  name='RequestType',
  full_name='FileRequest.RequestType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='READ', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WRITE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APPEND', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=121,
  serialized_end=179,
)


_FILEREQUEST = _descriptor.Descriptor(
  name='FileRequest',
  full_name='FileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='FileRequest.filename', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='contents', full_name='FileRequest.contents', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='request_type', full_name='FileRequest.request_type', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FILEREQUEST_REQUESTTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=22,
  serialized_end=179,
)


_FILERESPONSE = _descriptor.Descriptor(
  name='FileResponse',
  full_name='FileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='FileResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='contents', full_name='FileResponse.contents', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=181,
  serialized_end=230,
)

_FILEREQUEST.fields_by_name['request_type'].enum_type = _FILEREQUEST_REQUESTTYPE
_FILEREQUEST_REQUESTTYPE.containing_type = _FILEREQUEST;
DESCRIPTOR.message_types_by_name['FileRequest'] = _FILEREQUEST
DESCRIPTOR.message_types_by_name['FileResponse'] = _FILERESPONSE

class FileRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FILEREQUEST

  # @@protoc_insertion_point(class_scope:FileRequest)

class FileResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FILERESPONSE

  # @@protoc_insertion_point(class_scope:FileResponse)


# @@protoc_insertion_point(module_scope)
