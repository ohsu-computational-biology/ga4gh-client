# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ga4gh_client/sequence_annotation_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ga4gh_client import sequence_annotations_pb2 as ga4gh__client_dot_sequence__annotations__pb2
from elgoog.api import annotations_pb2 as elgoog_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ga4gh_client/sequence_annotation_service.proto',
  package='ga4gh_client',
  syntax='proto3',
  serialized_pb=_b('\n.ga4gh_client/sequence_annotation_service.proto\x12\x0cga4gh_client\x1a\'ga4gh_client/sequence_annotations.proto\x1a\x1c\x65lgoog/api/annotations.proto\"U\n\x18SearchFeatureSetsRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\"d\n\x19SearchFeatureSetsResponse\x12.\n\x0c\x66\x65\x61ture_sets\x18\x01 \x03(\x0b\x32\x18.ga4gh_client.FeatureSet\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\".\n\x14GetFeatureSetRequest\x12\x16\n\x0e\x66\x65\x61ture_set_id\x18\x01 \x01(\t\"\xd7\x01\n\x15SearchFeaturesRequest\x12\x16\n\x0e\x66\x65\x61ture_set_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0bgene_symbol\x18\x03 \x01(\t\x12\x11\n\tparent_id\x18\x04 \x01(\t\x12\x16\n\x0ereference_name\x18\x05 \x01(\t\x12\r\n\x05start\x18\x06 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x07 \x01(\x03\x12\x15\n\rfeature_types\x18\x08 \x03(\t\x12\x11\n\tpage_size\x18\t \x01(\x05\x12\x12\n\npage_token\x18\n \x01(\t\"Z\n\x16SearchFeaturesResponse\x12\'\n\x08\x66\x65\x61tures\x18\x01 \x03(\x0b\x32\x15.ga4gh_client.Feature\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\'\n\x11GetFeatureRequest\x12\x12\n\nfeature_id\x18\x01 \x01(\t2\x9d\x04\n\x19SequenceAnnotationService\x12\x8d\x01\n\x11SearchFeatureSets\x12&.ga4gh_client.SearchFeatureSetsRequest\x1a\'.ga4gh_client.SearchFeatureSetsResponse\"\'\x82\xd3\xe4\x93\x02!\"\x1c/v0.6.0a8/featuresets/search:\x01*\x12}\n\rGetFeatureSet\x12\".ga4gh_client.GetFeatureSetRequest\x1a\x18.ga4gh_client.FeatureSet\".\x82\xd3\xe4\x93\x02(\x12&/v0.6.0a8/featuresets/{feature_set_id}\x12\x81\x01\n\x0eSearchFeatures\x12#.ga4gh_client.SearchFeaturesRequest\x1a$.ga4gh_client.SearchFeaturesResponse\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/v0.6.0a8/features/search:\x01*\x12m\n\nGetFeature\x12\x1f.ga4gh_client.GetFeatureRequest\x1a\x15.ga4gh_client.Feature\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/v0.6.0a8/features/{feature_id}b\x06proto3')
  ,
  dependencies=[ga4gh__client_dot_sequence__annotations__pb2.DESCRIPTOR,elgoog_dot_api_dot_annotations__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SEARCHFEATURESETSREQUEST = _descriptor.Descriptor(
  name='SearchFeatureSetsRequest',
  full_name='ga4gh_client.SearchFeatureSetsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='ga4gh_client.SearchFeatureSetsRequest.dataset_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='ga4gh_client.SearchFeatureSetsRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='ga4gh_client.SearchFeatureSetsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=220,
)


_SEARCHFEATURESETSRESPONSE = _descriptor.Descriptor(
  name='SearchFeatureSetsResponse',
  full_name='ga4gh_client.SearchFeatureSetsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_sets', full_name='ga4gh_client.SearchFeatureSetsResponse.feature_sets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='ga4gh_client.SearchFeatureSetsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=222,
  serialized_end=322,
)


_GETFEATURESETREQUEST = _descriptor.Descriptor(
  name='GetFeatureSetRequest',
  full_name='ga4gh_client.GetFeatureSetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_set_id', full_name='ga4gh_client.GetFeatureSetRequest.feature_set_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=324,
  serialized_end=370,
)


_SEARCHFEATURESREQUEST = _descriptor.Descriptor(
  name='SearchFeaturesRequest',
  full_name='ga4gh_client.SearchFeaturesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_set_id', full_name='ga4gh_client.SearchFeaturesRequest.feature_set_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='ga4gh_client.SearchFeaturesRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gene_symbol', full_name='ga4gh_client.SearchFeaturesRequest.gene_symbol', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent_id', full_name='ga4gh_client.SearchFeaturesRequest.parent_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference_name', full_name='ga4gh_client.SearchFeaturesRequest.reference_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start', full_name='ga4gh_client.SearchFeaturesRequest.start', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='ga4gh_client.SearchFeaturesRequest.end', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feature_types', full_name='ga4gh_client.SearchFeaturesRequest.feature_types', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='ga4gh_client.SearchFeaturesRequest.page_size', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='ga4gh_client.SearchFeaturesRequest.page_token', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=373,
  serialized_end=588,
)


_SEARCHFEATURESRESPONSE = _descriptor.Descriptor(
  name='SearchFeaturesResponse',
  full_name='ga4gh_client.SearchFeaturesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='features', full_name='ga4gh_client.SearchFeaturesResponse.features', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='ga4gh_client.SearchFeaturesResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=590,
  serialized_end=680,
)


_GETFEATUREREQUEST = _descriptor.Descriptor(
  name='GetFeatureRequest',
  full_name='ga4gh_client.GetFeatureRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_id', full_name='ga4gh_client.GetFeatureRequest.feature_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=682,
  serialized_end=721,
)

_SEARCHFEATURESETSRESPONSE.fields_by_name['feature_sets'].message_type = ga4gh__client_dot_sequence__annotations__pb2._FEATURESET
_SEARCHFEATURESRESPONSE.fields_by_name['features'].message_type = ga4gh__client_dot_sequence__annotations__pb2._FEATURE
DESCRIPTOR.message_types_by_name['SearchFeatureSetsRequest'] = _SEARCHFEATURESETSREQUEST
DESCRIPTOR.message_types_by_name['SearchFeatureSetsResponse'] = _SEARCHFEATURESETSRESPONSE
DESCRIPTOR.message_types_by_name['GetFeatureSetRequest'] = _GETFEATURESETREQUEST
DESCRIPTOR.message_types_by_name['SearchFeaturesRequest'] = _SEARCHFEATURESREQUEST
DESCRIPTOR.message_types_by_name['SearchFeaturesResponse'] = _SEARCHFEATURESRESPONSE
DESCRIPTOR.message_types_by_name['GetFeatureRequest'] = _GETFEATUREREQUEST

SearchFeatureSetsRequest = _reflection.GeneratedProtocolMessageType('SearchFeatureSetsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHFEATURESETSREQUEST,
  __module__ = 'ga4gh_client.sequence_annotation_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh_client.SearchFeatureSetsRequest)
  ))
_sym_db.RegisterMessage(SearchFeatureSetsRequest)

SearchFeatureSetsResponse = _reflection.GeneratedProtocolMessageType('SearchFeatureSetsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHFEATURESETSRESPONSE,
  __module__ = 'ga4gh_client.sequence_annotation_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh_client.SearchFeatureSetsResponse)
  ))
_sym_db.RegisterMessage(SearchFeatureSetsResponse)

GetFeatureSetRequest = _reflection.GeneratedProtocolMessageType('GetFeatureSetRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETFEATURESETREQUEST,
  __module__ = 'ga4gh_client.sequence_annotation_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh_client.GetFeatureSetRequest)
  ))
_sym_db.RegisterMessage(GetFeatureSetRequest)

SearchFeaturesRequest = _reflection.GeneratedProtocolMessageType('SearchFeaturesRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHFEATURESREQUEST,
  __module__ = 'ga4gh_client.sequence_annotation_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh_client.SearchFeaturesRequest)
  ))
_sym_db.RegisterMessage(SearchFeaturesRequest)

SearchFeaturesResponse = _reflection.GeneratedProtocolMessageType('SearchFeaturesResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHFEATURESRESPONSE,
  __module__ = 'ga4gh_client.sequence_annotation_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh_client.SearchFeaturesResponse)
  ))
_sym_db.RegisterMessage(SearchFeaturesResponse)

GetFeatureRequest = _reflection.GeneratedProtocolMessageType('GetFeatureRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETFEATUREREQUEST,
  __module__ = 'ga4gh_client.sequence_annotation_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh_client.GetFeatureRequest)
  ))
_sym_db.RegisterMessage(GetFeatureRequest)


# @@protoc_insertion_point(module_scope)
