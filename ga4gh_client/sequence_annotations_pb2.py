# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ga4gh_client/sequence_annotations.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ga4gh_client import common_pb2 as ga4gh__client_dot_common__pb2
from ga4gh_client import metadata_pb2 as ga4gh__client_dot_metadata__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ga4gh_client/sequence_annotations.proto',
  package='ga4gh_client',
  syntax='proto3',
  serialized_pb=_b('\n\'ga4gh_client/sequence_annotations.proto\x12\x0cga4gh_client\x1a\x19ga4gh_client/common.proto\x1a\x1bga4gh_client/metadata.proto\x1a\x1cgoogle/protobuf/struct.proto\"\x91\x03\n\nAttributes\x12\x30\n\x04vals\x18\x01 \x03(\x0b\x32\".ga4gh_client.Attributes.ValsEntry\x1a\xa7\x01\n\x0e\x41ttributeValue\x12\x16\n\x0cstring_value\x18\x01 \x01(\tH\x00\x12?\n\x13\x65xternal_identifier\x18\x02 \x01(\x0b\x32 .ga4gh_client.ExternalIdentifierH\x00\x12\x33\n\rontology_term\x18\x03 \x01(\x0b\x32\x1a.ga4gh_client.OntologyTermH\x00\x42\x07\n\x05value\x1aM\n\x12\x41ttributeValueList\x12\x37\n\x06values\x18\x01 \x03(\x0b\x32\'.ga4gh_client.Attributes.AttributeValue\x1aX\n\tValsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\x05value\x18\x02 \x01(\x0b\x32+.ga4gh_client.Attributes.AttributeValueList:\x02\x38\x01\"\xb0\x02\n\x07\x46\x65\x61ture\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0bgene_symbol\x18\x03 \x01(\t\x12\x11\n\tparent_id\x18\x04 \x01(\t\x12\x11\n\tchild_ids\x18\x05 \x03(\t\x12\x16\n\x0e\x66\x65\x61ture_set_id\x18\x06 \x01(\t\x12\x16\n\x0ereference_name\x18\x07 \x01(\t\x12\r\n\x05start\x18\x08 \x01(\x03\x12\x0b\n\x03\x65nd\x18\t \x01(\x03\x12$\n\x06strand\x18\n \x01(\x0e\x32\x14.ga4gh_client.Strand\x12\x30\n\x0c\x66\x65\x61ture_type\x18\x0b \x01(\x0b\x32\x1a.ga4gh_client.OntologyTerm\x12,\n\nattributes\x18\x0c \x01(\x0b\x32\x18.ga4gh_client.Attributes\"\xe3\x01\n\nFeatureSet\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ndataset_id\x18\x02 \x01(\t\x12\x18\n\x10reference_set_id\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x12\n\nsource_uri\x18\x05 \x01(\t\x12\x30\n\x04info\x18\x06 \x03(\x0b\x32\".ga4gh_client.FeatureSet.InfoEntry\x1aG\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.ListValue:\x02\x38\x01\x62\x06proto3')
  ,
  dependencies=[ga4gh__client_dot_common__pb2.DESCRIPTOR,ga4gh__client_dot_metadata__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ATTRIBUTES_ATTRIBUTEVALUE = _descriptor.Descriptor(
  name='AttributeValue',
  full_name='ga4gh_client.Attributes.AttributeValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='string_value', full_name='ga4gh_client.Attributes.AttributeValue.string_value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='external_identifier', full_name='ga4gh_client.Attributes.AttributeValue.external_identifier', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ontology_term', full_name='ga4gh_client.Attributes.AttributeValue.ontology_term', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='value', full_name='ga4gh_client.Attributes.AttributeValue.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=209,
  serialized_end=376,
)

_ATTRIBUTES_ATTRIBUTEVALUELIST = _descriptor.Descriptor(
  name='AttributeValueList',
  full_name='ga4gh_client.Attributes.AttributeValueList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='ga4gh_client.Attributes.AttributeValueList.values', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=378,
  serialized_end=455,
)

_ATTRIBUTES_VALSENTRY = _descriptor.Descriptor(
  name='ValsEntry',
  full_name='ga4gh_client.Attributes.ValsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ga4gh_client.Attributes.ValsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='ga4gh_client.Attributes.ValsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=457,
  serialized_end=545,
)

_ATTRIBUTES = _descriptor.Descriptor(
  name='Attributes',
  full_name='ga4gh_client.Attributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vals', full_name='ga4gh_client.Attributes.vals', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ATTRIBUTES_ATTRIBUTEVALUE, _ATTRIBUTES_ATTRIBUTEVALUELIST, _ATTRIBUTES_VALSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=144,
  serialized_end=545,
)


_FEATURE = _descriptor.Descriptor(
  name='Feature',
  full_name='ga4gh_client.Feature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ga4gh_client.Feature.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='ga4gh_client.Feature.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gene_symbol', full_name='ga4gh_client.Feature.gene_symbol', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent_id', full_name='ga4gh_client.Feature.parent_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='child_ids', full_name='ga4gh_client.Feature.child_ids', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feature_set_id', full_name='ga4gh_client.Feature.feature_set_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference_name', full_name='ga4gh_client.Feature.reference_name', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start', full_name='ga4gh_client.Feature.start', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='ga4gh_client.Feature.end', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='strand', full_name='ga4gh_client.Feature.strand', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feature_type', full_name='ga4gh_client.Feature.feature_type', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='ga4gh_client.Feature.attributes', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=548,
  serialized_end=852,
)


_FEATURESET_INFOENTRY = _descriptor.Descriptor(
  name='InfoEntry',
  full_name='ga4gh_client.FeatureSet.InfoEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ga4gh_client.FeatureSet.InfoEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='ga4gh_client.FeatureSet.InfoEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1011,
  serialized_end=1082,
)

_FEATURESET = _descriptor.Descriptor(
  name='FeatureSet',
  full_name='ga4gh_client.FeatureSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ga4gh_client.FeatureSet.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='ga4gh_client.FeatureSet.dataset_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference_set_id', full_name='ga4gh_client.FeatureSet.reference_set_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='ga4gh_client.FeatureSet.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_uri', full_name='ga4gh_client.FeatureSet.source_uri', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='info', full_name='ga4gh_client.FeatureSet.info', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_FEATURESET_INFOENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=855,
  serialized_end=1082,
)

_ATTRIBUTES_ATTRIBUTEVALUE.fields_by_name['external_identifier'].message_type = ga4gh__client_dot_common__pb2._EXTERNALIDENTIFIER
_ATTRIBUTES_ATTRIBUTEVALUE.fields_by_name['ontology_term'].message_type = ga4gh__client_dot_metadata__pb2._ONTOLOGYTERM
_ATTRIBUTES_ATTRIBUTEVALUE.containing_type = _ATTRIBUTES
_ATTRIBUTES_ATTRIBUTEVALUE.oneofs_by_name['value'].fields.append(
  _ATTRIBUTES_ATTRIBUTEVALUE.fields_by_name['string_value'])
_ATTRIBUTES_ATTRIBUTEVALUE.fields_by_name['string_value'].containing_oneof = _ATTRIBUTES_ATTRIBUTEVALUE.oneofs_by_name['value']
_ATTRIBUTES_ATTRIBUTEVALUE.oneofs_by_name['value'].fields.append(
  _ATTRIBUTES_ATTRIBUTEVALUE.fields_by_name['external_identifier'])
_ATTRIBUTES_ATTRIBUTEVALUE.fields_by_name['external_identifier'].containing_oneof = _ATTRIBUTES_ATTRIBUTEVALUE.oneofs_by_name['value']
_ATTRIBUTES_ATTRIBUTEVALUE.oneofs_by_name['value'].fields.append(
  _ATTRIBUTES_ATTRIBUTEVALUE.fields_by_name['ontology_term'])
_ATTRIBUTES_ATTRIBUTEVALUE.fields_by_name['ontology_term'].containing_oneof = _ATTRIBUTES_ATTRIBUTEVALUE.oneofs_by_name['value']
_ATTRIBUTES_ATTRIBUTEVALUELIST.fields_by_name['values'].message_type = _ATTRIBUTES_ATTRIBUTEVALUE
_ATTRIBUTES_ATTRIBUTEVALUELIST.containing_type = _ATTRIBUTES
_ATTRIBUTES_VALSENTRY.fields_by_name['value'].message_type = _ATTRIBUTES_ATTRIBUTEVALUELIST
_ATTRIBUTES_VALSENTRY.containing_type = _ATTRIBUTES
_ATTRIBUTES.fields_by_name['vals'].message_type = _ATTRIBUTES_VALSENTRY
_FEATURE.fields_by_name['strand'].enum_type = ga4gh__client_dot_common__pb2._STRAND
_FEATURE.fields_by_name['feature_type'].message_type = ga4gh__client_dot_metadata__pb2._ONTOLOGYTERM
_FEATURE.fields_by_name['attributes'].message_type = _ATTRIBUTES
_FEATURESET_INFOENTRY.fields_by_name['value'].message_type = google_dot_protobuf_dot_struct__pb2._LISTVALUE
_FEATURESET_INFOENTRY.containing_type = _FEATURESET
_FEATURESET.fields_by_name['info'].message_type = _FEATURESET_INFOENTRY
DESCRIPTOR.message_types_by_name['Attributes'] = _ATTRIBUTES
DESCRIPTOR.message_types_by_name['Feature'] = _FEATURE
DESCRIPTOR.message_types_by_name['FeatureSet'] = _FEATURESET

Attributes = _reflection.GeneratedProtocolMessageType('Attributes', (_message.Message,), dict(

  AttributeValue = _reflection.GeneratedProtocolMessageType('AttributeValue', (_message.Message,), dict(
    DESCRIPTOR = _ATTRIBUTES_ATTRIBUTEVALUE,
    __module__ = 'ga4gh_client.sequence_annotations_pb2'
    # @@protoc_insertion_point(class_scope:ga4gh_client.Attributes.AttributeValue)
    ))
  ,

  AttributeValueList = _reflection.GeneratedProtocolMessageType('AttributeValueList', (_message.Message,), dict(
    DESCRIPTOR = _ATTRIBUTES_ATTRIBUTEVALUELIST,
    __module__ = 'ga4gh_client.sequence_annotations_pb2'
    # @@protoc_insertion_point(class_scope:ga4gh_client.Attributes.AttributeValueList)
    ))
  ,

  ValsEntry = _reflection.GeneratedProtocolMessageType('ValsEntry', (_message.Message,), dict(
    DESCRIPTOR = _ATTRIBUTES_VALSENTRY,
    __module__ = 'ga4gh_client.sequence_annotations_pb2'
    # @@protoc_insertion_point(class_scope:ga4gh_client.Attributes.ValsEntry)
    ))
  ,
  DESCRIPTOR = _ATTRIBUTES,
  __module__ = 'ga4gh_client.sequence_annotations_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh_client.Attributes)
  ))
_sym_db.RegisterMessage(Attributes)
_sym_db.RegisterMessage(Attributes.AttributeValue)
_sym_db.RegisterMessage(Attributes.AttributeValueList)
_sym_db.RegisterMessage(Attributes.ValsEntry)

Feature = _reflection.GeneratedProtocolMessageType('Feature', (_message.Message,), dict(
  DESCRIPTOR = _FEATURE,
  __module__ = 'ga4gh_client.sequence_annotations_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh_client.Feature)
  ))
_sym_db.RegisterMessage(Feature)

FeatureSet = _reflection.GeneratedProtocolMessageType('FeatureSet', (_message.Message,), dict(

  InfoEntry = _reflection.GeneratedProtocolMessageType('InfoEntry', (_message.Message,), dict(
    DESCRIPTOR = _FEATURESET_INFOENTRY,
    __module__ = 'ga4gh_client.sequence_annotations_pb2'
    # @@protoc_insertion_point(class_scope:ga4gh_client.FeatureSet.InfoEntry)
    ))
  ,
  DESCRIPTOR = _FEATURESET,
  __module__ = 'ga4gh_client.sequence_annotations_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh_client.FeatureSet)
  ))
_sym_db.RegisterMessage(FeatureSet)
_sym_db.RegisterMessage(FeatureSet.InfoEntry)


_ATTRIBUTES_VALSENTRY.has_options = True
_ATTRIBUTES_VALSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_FEATURESET_INFOENTRY.has_options = True
_FEATURESET_INFOENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
