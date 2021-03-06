# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gRPC/indeedclone.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='gRPC/indeedclone.proto',
  package='scrapper',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x16gRPC/indeedclone.proto\x12\x08scrapper\"\x1d\n\rsearchRequest\x12\x0c\n\x04term\x18\x01 \x01(\t\"Y\n\tjobObject\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x0e\n\x06salary\x18\x04 \x01(\t\x12\x0f\n\x07summary\x18\x05 \x01(\t\"3\n\x0esearchResponse\x12!\n\x04jobs\x18\x01 \x03(\x0b\x32\x13.scrapper.jobObject2K\n\njobService\x12=\n\x06Search\x12\x17.scrapper.searchRequest\x1a\x18.scrapper.searchResponse\"\x00\x62\x06proto3'
)




_SEARCHREQUEST = _descriptor.Descriptor(
  name='searchRequest',
  full_name='scrapper.searchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='term', full_name='scrapper.searchRequest.term', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=65,
)


_JOBOBJECT = _descriptor.Descriptor(
  name='jobObject',
  full_name='scrapper.jobObject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='scrapper.jobObject.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='scrapper.jobObject.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='scrapper.jobObject.location', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='salary', full_name='scrapper.jobObject.salary', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='summary', full_name='scrapper.jobObject.summary', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=156,
)


_SEARCHRESPONSE = _descriptor.Descriptor(
  name='searchResponse',
  full_name='scrapper.searchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jobs', full_name='scrapper.searchResponse.jobs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=158,
  serialized_end=209,
)

_SEARCHRESPONSE.fields_by_name['jobs'].message_type = _JOBOBJECT
DESCRIPTOR.message_types_by_name['searchRequest'] = _SEARCHREQUEST
DESCRIPTOR.message_types_by_name['jobObject'] = _JOBOBJECT
DESCRIPTOR.message_types_by_name['searchResponse'] = _SEARCHRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

searchRequest = _reflection.GeneratedProtocolMessageType('searchRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHREQUEST,
  '__module__' : 'gRPC.indeedclone_pb2'
  # @@protoc_insertion_point(class_scope:scrapper.searchRequest)
  })
_sym_db.RegisterMessage(searchRequest)

jobObject = _reflection.GeneratedProtocolMessageType('jobObject', (_message.Message,), {
  'DESCRIPTOR' : _JOBOBJECT,
  '__module__' : 'gRPC.indeedclone_pb2'
  # @@protoc_insertion_point(class_scope:scrapper.jobObject)
  })
_sym_db.RegisterMessage(jobObject)

searchResponse = _reflection.GeneratedProtocolMessageType('searchResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHRESPONSE,
  '__module__' : 'gRPC.indeedclone_pb2'
  # @@protoc_insertion_point(class_scope:scrapper.searchResponse)
  })
_sym_db.RegisterMessage(searchResponse)



_JOBSERVICE = _descriptor.ServiceDescriptor(
  name='jobService',
  full_name='scrapper.jobService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=211,
  serialized_end=286,
  methods=[
  _descriptor.MethodDescriptor(
    name='Search',
    full_name='scrapper.jobService.Search',
    index=0,
    containing_service=None,
    input_type=_SEARCHREQUEST,
    output_type=_SEARCHRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_JOBSERVICE)

DESCRIPTOR.services_by_name['jobService'] = _JOBSERVICE

# @@protoc_insertion_point(module_scope)
