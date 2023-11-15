# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: p2p.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tp2p.proto\x12\tprotowire\"g\n\x17RequestAddressesMessage\x12\x1d\n\x15includeAllSubnetworks\x18\x01 \x01(\x08\x12-\n\x0csubnetworkId\x18\x02 \x01(\x0b\x32\x17.protowire.SubnetworkId\">\n\x10\x41\x64\x64ressesMessage\x12*\n\x0b\x61\x64\x64ressList\x18\x01 \x03(\x0b\x32\x15.protowire.NetAddress\"9\n\nNetAddress\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\n\n\x02ip\x18\x03 \x01(\x0c\x12\x0c\n\x04port\x18\x04 \x01(\r\"\x1d\n\x0cSubnetworkId\x12\r\n\x05\x62ytes\x18\x01 \x01(\x0c\"\xe0\x01\n\x12TransactionMessage\x12\x0f\n\x07version\x18\x01 \x01(\r\x12+\n\x06inputs\x18\x02 \x03(\x0b\x32\x1b.protowire.TransactionInput\x12-\n\x07outputs\x18\x03 \x03(\x0b\x32\x1c.protowire.TransactionOutput\x12\x10\n\x08lockTime\x18\x04 \x01(\x04\x12-\n\x0csubnetworkId\x18\x05 \x01(\x0b\x32\x17.protowire.SubnetworkId\x12\x0b\n\x03gas\x18\x06 \x01(\x04\x12\x0f\n\x07payload\x18\x08 \x01(\x0c\"\x80\x01\n\x10TransactionInput\x12-\n\x10previousOutpoint\x18\x01 \x01(\x0b\x32\x13.protowire.Outpoint\x12\x17\n\x0fsignatureScript\x18\x02 \x01(\x0c\x12\x10\n\x08sequence\x18\x03 \x01(\x04\x12\x12\n\nsigOpCount\x18\x04 \x01(\r\"J\n\x08Outpoint\x12/\n\rtransactionId\x18\x01 \x01(\x0b\x32\x18.protowire.TransactionId\x12\r\n\x05index\x18\x02 \x01(\r\"\x1e\n\rTransactionId\x12\r\n\x05\x62ytes\x18\x01 \x01(\x0c\"2\n\x0fScriptPublicKey\x12\x0e\n\x06script\x18\x01 \x01(\x0c\x12\x0f\n\x07version\x18\x02 \x01(\r\"W\n\x11TransactionOutput\x12\r\n\x05value\x18\x01 \x01(\x04\x12\x33\n\x0fscriptPublicKey\x18\x02 \x01(\x0b\x32\x1a.protowire.ScriptPublicKey\"k\n\x0c\x42lockMessage\x12&\n\x06header\x18\x01 \x01(\x0b\x32\x16.protowire.BlockHeader\x12\x33\n\x0ctransactions\x18\x02 \x03(\x0b\x32\x1d.protowire.TransactionMessage\"\xdc\x02\n\x0b\x42lockHeader\x12\x0f\n\x07version\x18\x01 \x01(\r\x12-\n\x07parents\x18\x0c \x03(\x0b\x32\x1c.protowire.BlockLevelParents\x12\'\n\x0ehashMerkleRoot\x18\x03 \x01(\x0b\x32\x0f.protowire.Hash\x12-\n\x14\x61\x63\x63\x65ptedIdMerkleRoot\x18\x04 \x01(\x0b\x32\x0f.protowire.Hash\x12\'\n\x0eutxoCommitment\x18\x05 \x01(\x0b\x32\x0f.protowire.Hash\x12\x11\n\ttimestamp\x18\x06 \x01(\x03\x12\x0c\n\x04\x62its\x18\x07 \x01(\r\x12\r\n\x05nonce\x18\x08 \x01(\x04\x12\x10\n\x08\x64\x61\x61Score\x18\t \x01(\x04\x12\x10\n\x08\x62lueWork\x18\n \x01(\x0c\x12%\n\x0cpruningPoint\x18\x0e \x01(\x0b\x32\x0f.protowire.Hash\x12\x11\n\tblueScore\x18\r \x01(\x04\":\n\x11\x42lockLevelParents\x12%\n\x0cparentHashes\x18\x01 \x03(\x0b\x32\x0f.protowire.Hash\"\x15\n\x04Hash\x12\r\n\x05\x62ytes\x18\x01 \x01(\x0c\"N\n\x1aRequestBlockLocatorMessage\x12!\n\x08highHash\x18\x01 \x01(\x0b\x32\x0f.protowire.Hash\x12\r\n\x05limit\x18\x02 \x01(\r\"6\n\x13\x42lockLocatorMessage\x12\x1f\n\x06hashes\x18\x01 \x03(\x0b\x32\x0f.protowire.Hash\"\\\n\x15RequestHeadersMessage\x12 \n\x07lowHash\x18\x01 \x01(\x0b\x32\x0f.protowire.Hash\x12!\n\x08highHash\x18\x02 \x01(\x0b\x32\x0f.protowire.Hash\"\x1b\n\x19RequestNextHeadersMessage\"\x14\n\x12\x44oneHeadersMessage\"<\n\x19RequestRelayBlocksMessage\x12\x1f\n\x06hashes\x18\x01 \x03(\x0b\x32\x0f.protowire.Hash\"C\n\x1aRequestTransactionsMessage\x12%\n\x03ids\x18\x01 \x03(\x0b\x32\x18.protowire.TransactionId\"B\n\x1aTransactionNotFoundMessage\x12$\n\x02id\x18\x01 \x01(\x0b\x32\x18.protowire.TransactionId\"5\n\x14InvRelayBlockMessage\x12\x1d\n\x04hash\x18\x01 \x01(\x0b\x32\x0f.protowire.Hash\"?\n\x16InvTransactionsMessage\x12%\n\x03ids\x18\x01 \x03(\x0b\x32\x18.protowire.TransactionId\"\x1c\n\x0bPingMessage\x12\r\n\x05nonce\x18\x01 \x01(\x04\"\x1c\n\x0bPongMessage\x12\r\n\x05nonce\x18\x01 \x01(\x04\"\x0f\n\rVerackMessage\"\xed\x01\n\x0eVersionMessage\x12\x17\n\x0fprotocolVersion\x18\x01 \x01(\r\x12\x10\n\x08services\x18\x02 \x01(\x04\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\x12&\n\x07\x61\x64\x64ress\x18\x04 \x01(\x0b\x32\x15.protowire.NetAddress\x12\n\n\x02id\x18\x05 \x01(\x0c\x12\x11\n\tuserAgent\x18\x06 \x01(\t\x12\x16\n\x0e\x64isableRelayTx\x18\x08 \x01(\x08\x12-\n\x0csubnetworkId\x18\t \x01(\x0b\x32\x17.protowire.SubnetworkId\x12\x0f\n\x07network\x18\n \x01(\t\"\x1f\n\rRejectMessage\x12\x0e\n\x06reason\x18\x01 \x01(\t\"N\n!RequestPruningPointUTXOSetMessage\x12)\n\x10pruningPointHash\x18\x01 \x01(\x0b\x32\x0f.protowire.Hash\"i\n\x1fPruningPointUtxoSetChunkMessage\x12\x46\n\x19outpointAndUtxoEntryPairs\x18\x01 \x03(\x0b\x32#.protowire.OutpointAndUtxoEntryPair\"j\n\x18OutpointAndUtxoEntryPair\x12%\n\x08outpoint\x18\x01 \x01(\x0b\x32\x13.protowire.Outpoint\x12\'\n\tutxoEntry\x18\x02 \x01(\x0b\x32\x14.protowire.UtxoEntry\"{\n\tUtxoEntry\x12\x0e\n\x06\x61mount\x18\x01 \x01(\x04\x12\x33\n\x0fscriptPublicKey\x18\x02 \x01(\x0b\x32\x1a.protowire.ScriptPublicKey\x12\x15\n\rblockDaaScore\x18\x03 \x01(\x04\x12\x12\n\nisCoinbase\x18\x04 \x01(\x08\",\n*RequestNextPruningPointUtxoSetChunkMessage\"&\n$DonePruningPointUtxoSetChunksMessage\":\n\x17RequestIBDBlocksMessage\x12\x1f\n\x06hashes\x18\x01 \x03(\x0b\x32\x0f.protowire.Hash\"\x1f\n\x1dUnexpectedPruningPointMessage\"j\n\x16IbdBlockLocatorMessage\x12#\n\ntargetHash\x18\x01 \x01(\x0b\x32\x0f.protowire.Hash\x12+\n\x12\x62lockLocatorHashes\x18\x02 \x03(\x0b\x32\x0f.protowire.Hash\"i\n\"RequestIBDChainBlockLocatorMessage\x12 \n\x07lowHash\x18\x01 \x01(\x0b\x32\x0f.protowire.Hash\x12!\n\x08highHash\x18\x02 \x01(\x0b\x32\x0f.protowire.Hash\"J\n\x1bIbdChainBlockLocatorMessage\x12+\n\x12\x62lockLocatorHashes\x18\x01 \x03(\x0b\x32\x0f.protowire.Hash\"b\n\x16RequestAnticoneMessage\x12\"\n\tblockHash\x18\x01 \x01(\x0b\x32\x0f.protowire.Hash\x12$\n\x0b\x63ontextHash\x18\x02 \x01(\x0b\x32\x0f.protowire.Hash\"I\n!IbdBlockLocatorHighestHashMessage\x12$\n\x0bhighestHash\x18\x01 \x01(\x0b\x32\x0f.protowire.Hash\"+\n)IbdBlockLocatorHighestHashNotFoundMessage\"C\n\x13\x42lockHeadersMessage\x12,\n\x0c\x62lockHeaders\x18\x01 \x03(\x0b\x32\x16.protowire.BlockHeader\"*\n(RequestPruningPointAndItsAnticoneMessage\"4\n2RequestNextPruningPointAndItsAnticoneBlocksMessage\"\xbb\x01\n\x1b\x42lockWithTrustedDataMessage\x12&\n\x05\x62lock\x18\x01 \x01(\x0b\x32\x17.protowire.BlockMessage\x12\x10\n\x08\x64\x61\x61Score\x18\x02 \x01(\x04\x12&\n\tdaaWindow\x18\x03 \x03(\x0b\x32\x13.protowire.DaaBlock\x12:\n\x0cghostdagData\x18\x04 \x03(\x0b\x32$.protowire.BlockGhostdagDataHashPair\"a\n\x08\x44\x61\x61\x42lock\x12&\n\x05\x62lock\x18\x03 \x01(\x0b\x32\x17.protowire.BlockMessage\x12-\n\x0cghostdagData\x18\x02 \x01(\x0b\x32\x17.protowire.GhostdagData\"c\n\nDaaBlockV4\x12&\n\x06header\x18\x01 \x01(\x0b\x32\x16.protowire.BlockHeader\x12-\n\x0cghostdagData\x18\x02 \x01(\x0b\x32\x17.protowire.GhostdagData\"i\n\x19\x42lockGhostdagDataHashPair\x12\x1d\n\x04hash\x18\x01 \x01(\x0b\x32\x0f.protowire.Hash\x12-\n\x0cghostdagData\x18\x02 \x01(\x0b\x32\x17.protowire.GhostdagData\"\xe6\x01\n\x0cGhostdagData\x12\x11\n\tblueScore\x18\x01 \x01(\x04\x12\x10\n\x08\x62lueWork\x18\x02 \x01(\x0c\x12\'\n\x0eselectedParent\x18\x03 \x01(\x0b\x32\x0f.protowire.Hash\x12&\n\rmergeSetBlues\x18\x04 \x03(\x0b\x32\x0f.protowire.Hash\x12%\n\x0cmergeSetReds\x18\x05 \x03(\x0b\x32\x0f.protowire.Hash\x12\x39\n\x12\x62luesAnticoneSizes\x18\x06 \x03(\x0b\x32\x1d.protowire.BluesAnticoneSizes\"M\n\x12\x42luesAnticoneSizes\x12!\n\x08\x62lueHash\x18\x01 \x01(\x0b\x32\x0f.protowire.Hash\x12\x14\n\x0c\x61nticoneSize\x18\x02 \x01(\r\"\"\n DoneBlocksWithTrustedDataMessage\"?\n\x14PruningPointsMessage\x12\'\n\x07headers\x18\x01 \x03(\x0b\x32\x16.protowire.BlockHeader\"!\n\x1fRequestPruningPointProofMessage\"T\n\x18PruningPointProofMessage\x12\x38\n\x07headers\x18\x01 \x03(\x0b\x32\'.protowire.PruningPointProofHeaderArray\"G\n\x1cPruningPointProofHeaderArray\x12\'\n\x07headers\x18\x01 \x03(\x0b\x32\x16.protowire.BlockHeader\"\x0e\n\x0cReadyMessage\"~\n\x1d\x42lockWithTrustedDataV4Message\x12&\n\x05\x62lock\x18\x01 \x01(\x0b\x32\x17.protowire.BlockMessage\x12\x18\n\x10\x64\x61\x61WindowIndices\x18\x02 \x03(\x04\x12\x1b\n\x13ghostdagDataIndices\x18\x03 \x03(\x04\"z\n\x12TrustedDataMessage\x12(\n\tdaaWindow\x18\x01 \x03(\x0b\x32\x15.protowire.DaaBlockV4\x12:\n\x0cghostdagData\x18\x02 \x03(\x0b\x32$.protowire.BlockGhostdagDataHashPairB&Z$github.com/karlsen-network/karlsend/protowireb\x06proto3')



_REQUESTADDRESSESMESSAGE = DESCRIPTOR.message_types_by_name['RequestAddressesMessage']
_ADDRESSESMESSAGE = DESCRIPTOR.message_types_by_name['AddressesMessage']
_NETADDRESS = DESCRIPTOR.message_types_by_name['NetAddress']
_SUBNETWORKID = DESCRIPTOR.message_types_by_name['SubnetworkId']
_TRANSACTIONMESSAGE = DESCRIPTOR.message_types_by_name['TransactionMessage']
_TRANSACTIONINPUT = DESCRIPTOR.message_types_by_name['TransactionInput']
_OUTPOINT = DESCRIPTOR.message_types_by_name['Outpoint']
_TRANSACTIONID = DESCRIPTOR.message_types_by_name['TransactionId']
_SCRIPTPUBLICKEY = DESCRIPTOR.message_types_by_name['ScriptPublicKey']
_TRANSACTIONOUTPUT = DESCRIPTOR.message_types_by_name['TransactionOutput']
_BLOCKMESSAGE = DESCRIPTOR.message_types_by_name['BlockMessage']
_BLOCKHEADER = DESCRIPTOR.message_types_by_name['BlockHeader']
_BLOCKLEVELPARENTS = DESCRIPTOR.message_types_by_name['BlockLevelParents']
_HASH = DESCRIPTOR.message_types_by_name['Hash']
_REQUESTBLOCKLOCATORMESSAGE = DESCRIPTOR.message_types_by_name['RequestBlockLocatorMessage']
_BLOCKLOCATORMESSAGE = DESCRIPTOR.message_types_by_name['BlockLocatorMessage']
_REQUESTHEADERSMESSAGE = DESCRIPTOR.message_types_by_name['RequestHeadersMessage']
_REQUESTNEXTHEADERSMESSAGE = DESCRIPTOR.message_types_by_name['RequestNextHeadersMessage']
_DONEHEADERSMESSAGE = DESCRIPTOR.message_types_by_name['DoneHeadersMessage']
_REQUESTRELAYBLOCKSMESSAGE = DESCRIPTOR.message_types_by_name['RequestRelayBlocksMessage']
_REQUESTTRANSACTIONSMESSAGE = DESCRIPTOR.message_types_by_name['RequestTransactionsMessage']
_TRANSACTIONNOTFOUNDMESSAGE = DESCRIPTOR.message_types_by_name['TransactionNotFoundMessage']
_INVRELAYBLOCKMESSAGE = DESCRIPTOR.message_types_by_name['InvRelayBlockMessage']
_INVTRANSACTIONSMESSAGE = DESCRIPTOR.message_types_by_name['InvTransactionsMessage']
_PINGMESSAGE = DESCRIPTOR.message_types_by_name['PingMessage']
_PONGMESSAGE = DESCRIPTOR.message_types_by_name['PongMessage']
_VERACKMESSAGE = DESCRIPTOR.message_types_by_name['VerackMessage']
_VERSIONMESSAGE = DESCRIPTOR.message_types_by_name['VersionMessage']
_REJECTMESSAGE = DESCRIPTOR.message_types_by_name['RejectMessage']
_REQUESTPRUNINGPOINTUTXOSETMESSAGE = DESCRIPTOR.message_types_by_name['RequestPruningPointUTXOSetMessage']
_PRUNINGPOINTUTXOSETCHUNKMESSAGE = DESCRIPTOR.message_types_by_name['PruningPointUtxoSetChunkMessage']
_OUTPOINTANDUTXOENTRYPAIR = DESCRIPTOR.message_types_by_name['OutpointAndUtxoEntryPair']
_UTXOENTRY = DESCRIPTOR.message_types_by_name['UtxoEntry']
_REQUESTNEXTPRUNINGPOINTUTXOSETCHUNKMESSAGE = DESCRIPTOR.message_types_by_name['RequestNextPruningPointUtxoSetChunkMessage']
_DONEPRUNINGPOINTUTXOSETCHUNKSMESSAGE = DESCRIPTOR.message_types_by_name['DonePruningPointUtxoSetChunksMessage']
_REQUESTIBDBLOCKSMESSAGE = DESCRIPTOR.message_types_by_name['RequestIBDBlocksMessage']
_UNEXPECTEDPRUNINGPOINTMESSAGE = DESCRIPTOR.message_types_by_name['UnexpectedPruningPointMessage']
_IBDBLOCKLOCATORMESSAGE = DESCRIPTOR.message_types_by_name['IbdBlockLocatorMessage']
_REQUESTIBDCHAINBLOCKLOCATORMESSAGE = DESCRIPTOR.message_types_by_name['RequestIBDChainBlockLocatorMessage']
_IBDCHAINBLOCKLOCATORMESSAGE = DESCRIPTOR.message_types_by_name['IbdChainBlockLocatorMessage']
_REQUESTANTICONEMESSAGE = DESCRIPTOR.message_types_by_name['RequestAnticoneMessage']
_IBDBLOCKLOCATORHIGHESTHASHMESSAGE = DESCRIPTOR.message_types_by_name['IbdBlockLocatorHighestHashMessage']
_IBDBLOCKLOCATORHIGHESTHASHNOTFOUNDMESSAGE = DESCRIPTOR.message_types_by_name['IbdBlockLocatorHighestHashNotFoundMessage']
_BLOCKHEADERSMESSAGE = DESCRIPTOR.message_types_by_name['BlockHeadersMessage']
_REQUESTPRUNINGPOINTANDITSANTICONEMESSAGE = DESCRIPTOR.message_types_by_name['RequestPruningPointAndItsAnticoneMessage']
_REQUESTNEXTPRUNINGPOINTANDITSANTICONEBLOCKSMESSAGE = DESCRIPTOR.message_types_by_name['RequestNextPruningPointAndItsAnticoneBlocksMessage']
_BLOCKWITHTRUSTEDDATAMESSAGE = DESCRIPTOR.message_types_by_name['BlockWithTrustedDataMessage']
_DAABLOCK = DESCRIPTOR.message_types_by_name['DaaBlock']
_DAABLOCKV4 = DESCRIPTOR.message_types_by_name['DaaBlockV4']
_BLOCKGHOSTDAGDATAHASHPAIR = DESCRIPTOR.message_types_by_name['BlockGhostdagDataHashPair']
_GHOSTDAGDATA = DESCRIPTOR.message_types_by_name['GhostdagData']
_BLUESANTICONESIZES = DESCRIPTOR.message_types_by_name['BluesAnticoneSizes']
_DONEBLOCKSWITHTRUSTEDDATAMESSAGE = DESCRIPTOR.message_types_by_name['DoneBlocksWithTrustedDataMessage']
_PRUNINGPOINTSMESSAGE = DESCRIPTOR.message_types_by_name['PruningPointsMessage']
_REQUESTPRUNINGPOINTPROOFMESSAGE = DESCRIPTOR.message_types_by_name['RequestPruningPointProofMessage']
_PRUNINGPOINTPROOFMESSAGE = DESCRIPTOR.message_types_by_name['PruningPointProofMessage']
_PRUNINGPOINTPROOFHEADERARRAY = DESCRIPTOR.message_types_by_name['PruningPointProofHeaderArray']
_READYMESSAGE = DESCRIPTOR.message_types_by_name['ReadyMessage']
_BLOCKWITHTRUSTEDDATAV4MESSAGE = DESCRIPTOR.message_types_by_name['BlockWithTrustedDataV4Message']
_TRUSTEDDATAMESSAGE = DESCRIPTOR.message_types_by_name['TrustedDataMessage']
RequestAddressesMessage = _reflection.GeneratedProtocolMessageType('RequestAddressesMessage', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTADDRESSESMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.RequestAddressesMessage)
  })
_sym_db.RegisterMessage(RequestAddressesMessage)

AddressesMessage = _reflection.GeneratedProtocolMessageType('AddressesMessage', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESSESMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.AddressesMessage)
  })
_sym_db.RegisterMessage(AddressesMessage)

NetAddress = _reflection.GeneratedProtocolMessageType('NetAddress', (_message.Message,), {
  'DESCRIPTOR' : _NETADDRESS,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.NetAddress)
  })
_sym_db.RegisterMessage(NetAddress)

SubnetworkId = _reflection.GeneratedProtocolMessageType('SubnetworkId', (_message.Message,), {
  'DESCRIPTOR' : _SUBNETWORKID,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.SubnetworkId)
  })
_sym_db.RegisterMessage(SubnetworkId)

TransactionMessage = _reflection.GeneratedProtocolMessageType('TransactionMessage', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.TransactionMessage)
  })
_sym_db.RegisterMessage(TransactionMessage)

TransactionInput = _reflection.GeneratedProtocolMessageType('TransactionInput', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONINPUT,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.TransactionInput)
  })
_sym_db.RegisterMessage(TransactionInput)

Outpoint = _reflection.GeneratedProtocolMessageType('Outpoint', (_message.Message,), {
  'DESCRIPTOR' : _OUTPOINT,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.Outpoint)
  })
_sym_db.RegisterMessage(Outpoint)

TransactionId = _reflection.GeneratedProtocolMessageType('TransactionId', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONID,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.TransactionId)
  })
_sym_db.RegisterMessage(TransactionId)

ScriptPublicKey = _reflection.GeneratedProtocolMessageType('ScriptPublicKey', (_message.Message,), {
  'DESCRIPTOR' : _SCRIPTPUBLICKEY,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.ScriptPublicKey)
  })
_sym_db.RegisterMessage(ScriptPublicKey)

TransactionOutput = _reflection.GeneratedProtocolMessageType('TransactionOutput', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONOUTPUT,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.TransactionOutput)
  })
_sym_db.RegisterMessage(TransactionOutput)

BlockMessage = _reflection.GeneratedProtocolMessageType('BlockMessage', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.BlockMessage)
  })
_sym_db.RegisterMessage(BlockMessage)

BlockHeader = _reflection.GeneratedProtocolMessageType('BlockHeader', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKHEADER,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.BlockHeader)
  })
_sym_db.RegisterMessage(BlockHeader)

BlockLevelParents = _reflection.GeneratedProtocolMessageType('BlockLevelParents', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKLEVELPARENTS,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.BlockLevelParents)
  })
_sym_db.RegisterMessage(BlockLevelParents)

Hash = _reflection.GeneratedProtocolMessageType('Hash', (_message.Message,), {
  'DESCRIPTOR' : _HASH,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.Hash)
  })
_sym_db.RegisterMessage(Hash)

RequestBlockLocatorMessage = _reflection.GeneratedProtocolMessageType('RequestBlockLocatorMessage', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTBLOCKLOCATORMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.RequestBlockLocatorMessage)
  })
_sym_db.RegisterMessage(RequestBlockLocatorMessage)

BlockLocatorMessage = _reflection.GeneratedProtocolMessageType('BlockLocatorMessage', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKLOCATORMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.BlockLocatorMessage)
  })
_sym_db.RegisterMessage(BlockLocatorMessage)

RequestHeadersMessage = _reflection.GeneratedProtocolMessageType('RequestHeadersMessage', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTHEADERSMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.RequestHeadersMessage)
  })
_sym_db.RegisterMessage(RequestHeadersMessage)

RequestNextHeadersMessage = _reflection.GeneratedProtocolMessageType('RequestNextHeadersMessage', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTNEXTHEADERSMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.RequestNextHeadersMessage)
  })
_sym_db.RegisterMessage(RequestNextHeadersMessage)

DoneHeadersMessage = _reflection.GeneratedProtocolMessageType('DoneHeadersMessage', (_message.Message,), {
  'DESCRIPTOR' : _DONEHEADERSMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.DoneHeadersMessage)
  })
_sym_db.RegisterMessage(DoneHeadersMessage)

RequestRelayBlocksMessage = _reflection.GeneratedProtocolMessageType('RequestRelayBlocksMessage', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTRELAYBLOCKSMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.RequestRelayBlocksMessage)
  })
_sym_db.RegisterMessage(RequestRelayBlocksMessage)

RequestTransactionsMessage = _reflection.GeneratedProtocolMessageType('RequestTransactionsMessage', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTTRANSACTIONSMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.RequestTransactionsMessage)
  })
_sym_db.RegisterMessage(RequestTransactionsMessage)

TransactionNotFoundMessage = _reflection.GeneratedProtocolMessageType('TransactionNotFoundMessage', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONNOTFOUNDMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.TransactionNotFoundMessage)
  })
_sym_db.RegisterMessage(TransactionNotFoundMessage)

InvRelayBlockMessage = _reflection.GeneratedProtocolMessageType('InvRelayBlockMessage', (_message.Message,), {
  'DESCRIPTOR' : _INVRELAYBLOCKMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.InvRelayBlockMessage)
  })
_sym_db.RegisterMessage(InvRelayBlockMessage)

InvTransactionsMessage = _reflection.GeneratedProtocolMessageType('InvTransactionsMessage', (_message.Message,), {
  'DESCRIPTOR' : _INVTRANSACTIONSMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.InvTransactionsMessage)
  })
_sym_db.RegisterMessage(InvTransactionsMessage)

PingMessage = _reflection.GeneratedProtocolMessageType('PingMessage', (_message.Message,), {
  'DESCRIPTOR' : _PINGMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.PingMessage)
  })
_sym_db.RegisterMessage(PingMessage)

PongMessage = _reflection.GeneratedProtocolMessageType('PongMessage', (_message.Message,), {
  'DESCRIPTOR' : _PONGMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.PongMessage)
  })
_sym_db.RegisterMessage(PongMessage)

VerackMessage = _reflection.GeneratedProtocolMessageType('VerackMessage', (_message.Message,), {
  'DESCRIPTOR' : _VERACKMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.VerackMessage)
  })
_sym_db.RegisterMessage(VerackMessage)

VersionMessage = _reflection.GeneratedProtocolMessageType('VersionMessage', (_message.Message,), {
  'DESCRIPTOR' : _VERSIONMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.VersionMessage)
  })
_sym_db.RegisterMessage(VersionMessage)

RejectMessage = _reflection.GeneratedProtocolMessageType('RejectMessage', (_message.Message,), {
  'DESCRIPTOR' : _REJECTMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.RejectMessage)
  })
_sym_db.RegisterMessage(RejectMessage)

RequestPruningPointUTXOSetMessage = _reflection.GeneratedProtocolMessageType('RequestPruningPointUTXOSetMessage', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTPRUNINGPOINTUTXOSETMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.RequestPruningPointUTXOSetMessage)
  })
_sym_db.RegisterMessage(RequestPruningPointUTXOSetMessage)

PruningPointUtxoSetChunkMessage = _reflection.GeneratedProtocolMessageType('PruningPointUtxoSetChunkMessage', (_message.Message,), {
  'DESCRIPTOR' : _PRUNINGPOINTUTXOSETCHUNKMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.PruningPointUtxoSetChunkMessage)
  })
_sym_db.RegisterMessage(PruningPointUtxoSetChunkMessage)

OutpointAndUtxoEntryPair = _reflection.GeneratedProtocolMessageType('OutpointAndUtxoEntryPair', (_message.Message,), {
  'DESCRIPTOR' : _OUTPOINTANDUTXOENTRYPAIR,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.OutpointAndUtxoEntryPair)
  })
_sym_db.RegisterMessage(OutpointAndUtxoEntryPair)

UtxoEntry = _reflection.GeneratedProtocolMessageType('UtxoEntry', (_message.Message,), {
  'DESCRIPTOR' : _UTXOENTRY,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.UtxoEntry)
  })
_sym_db.RegisterMessage(UtxoEntry)

RequestNextPruningPointUtxoSetChunkMessage = _reflection.GeneratedProtocolMessageType('RequestNextPruningPointUtxoSetChunkMessage', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTNEXTPRUNINGPOINTUTXOSETCHUNKMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.RequestNextPruningPointUtxoSetChunkMessage)
  })
_sym_db.RegisterMessage(RequestNextPruningPointUtxoSetChunkMessage)

DonePruningPointUtxoSetChunksMessage = _reflection.GeneratedProtocolMessageType('DonePruningPointUtxoSetChunksMessage', (_message.Message,), {
  'DESCRIPTOR' : _DONEPRUNINGPOINTUTXOSETCHUNKSMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.DonePruningPointUtxoSetChunksMessage)
  })
_sym_db.RegisterMessage(DonePruningPointUtxoSetChunksMessage)

RequestIBDBlocksMessage = _reflection.GeneratedProtocolMessageType('RequestIBDBlocksMessage', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTIBDBLOCKSMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.RequestIBDBlocksMessage)
  })
_sym_db.RegisterMessage(RequestIBDBlocksMessage)

UnexpectedPruningPointMessage = _reflection.GeneratedProtocolMessageType('UnexpectedPruningPointMessage', (_message.Message,), {
  'DESCRIPTOR' : _UNEXPECTEDPRUNINGPOINTMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.UnexpectedPruningPointMessage)
  })
_sym_db.RegisterMessage(UnexpectedPruningPointMessage)

IbdBlockLocatorMessage = _reflection.GeneratedProtocolMessageType('IbdBlockLocatorMessage', (_message.Message,), {
  'DESCRIPTOR' : _IBDBLOCKLOCATORMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.IbdBlockLocatorMessage)
  })
_sym_db.RegisterMessage(IbdBlockLocatorMessage)

RequestIBDChainBlockLocatorMessage = _reflection.GeneratedProtocolMessageType('RequestIBDChainBlockLocatorMessage', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTIBDCHAINBLOCKLOCATORMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.RequestIBDChainBlockLocatorMessage)
  })
_sym_db.RegisterMessage(RequestIBDChainBlockLocatorMessage)

IbdChainBlockLocatorMessage = _reflection.GeneratedProtocolMessageType('IbdChainBlockLocatorMessage', (_message.Message,), {
  'DESCRIPTOR' : _IBDCHAINBLOCKLOCATORMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.IbdChainBlockLocatorMessage)
  })
_sym_db.RegisterMessage(IbdChainBlockLocatorMessage)

RequestAnticoneMessage = _reflection.GeneratedProtocolMessageType('RequestAnticoneMessage', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTANTICONEMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.RequestAnticoneMessage)
  })
_sym_db.RegisterMessage(RequestAnticoneMessage)

IbdBlockLocatorHighestHashMessage = _reflection.GeneratedProtocolMessageType('IbdBlockLocatorHighestHashMessage', (_message.Message,), {
  'DESCRIPTOR' : _IBDBLOCKLOCATORHIGHESTHASHMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.IbdBlockLocatorHighestHashMessage)
  })
_sym_db.RegisterMessage(IbdBlockLocatorHighestHashMessage)

IbdBlockLocatorHighestHashNotFoundMessage = _reflection.GeneratedProtocolMessageType('IbdBlockLocatorHighestHashNotFoundMessage', (_message.Message,), {
  'DESCRIPTOR' : _IBDBLOCKLOCATORHIGHESTHASHNOTFOUNDMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.IbdBlockLocatorHighestHashNotFoundMessage)
  })
_sym_db.RegisterMessage(IbdBlockLocatorHighestHashNotFoundMessage)

BlockHeadersMessage = _reflection.GeneratedProtocolMessageType('BlockHeadersMessage', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKHEADERSMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.BlockHeadersMessage)
  })
_sym_db.RegisterMessage(BlockHeadersMessage)

RequestPruningPointAndItsAnticoneMessage = _reflection.GeneratedProtocolMessageType('RequestPruningPointAndItsAnticoneMessage', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTPRUNINGPOINTANDITSANTICONEMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.RequestPruningPointAndItsAnticoneMessage)
  })
_sym_db.RegisterMessage(RequestPruningPointAndItsAnticoneMessage)

RequestNextPruningPointAndItsAnticoneBlocksMessage = _reflection.GeneratedProtocolMessageType('RequestNextPruningPointAndItsAnticoneBlocksMessage', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTNEXTPRUNINGPOINTANDITSANTICONEBLOCKSMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.RequestNextPruningPointAndItsAnticoneBlocksMessage)
  })
_sym_db.RegisterMessage(RequestNextPruningPointAndItsAnticoneBlocksMessage)

BlockWithTrustedDataMessage = _reflection.GeneratedProtocolMessageType('BlockWithTrustedDataMessage', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKWITHTRUSTEDDATAMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.BlockWithTrustedDataMessage)
  })
_sym_db.RegisterMessage(BlockWithTrustedDataMessage)

DaaBlock = _reflection.GeneratedProtocolMessageType('DaaBlock', (_message.Message,), {
  'DESCRIPTOR' : _DAABLOCK,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.DaaBlock)
  })
_sym_db.RegisterMessage(DaaBlock)

DaaBlockV4 = _reflection.GeneratedProtocolMessageType('DaaBlockV4', (_message.Message,), {
  'DESCRIPTOR' : _DAABLOCKV4,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.DaaBlockV4)
  })
_sym_db.RegisterMessage(DaaBlockV4)

BlockGhostdagDataHashPair = _reflection.GeneratedProtocolMessageType('BlockGhostdagDataHashPair', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKGHOSTDAGDATAHASHPAIR,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.BlockGhostdagDataHashPair)
  })
_sym_db.RegisterMessage(BlockGhostdagDataHashPair)

GhostdagData = _reflection.GeneratedProtocolMessageType('GhostdagData', (_message.Message,), {
  'DESCRIPTOR' : _GHOSTDAGDATA,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.GhostdagData)
  })
_sym_db.RegisterMessage(GhostdagData)

BluesAnticoneSizes = _reflection.GeneratedProtocolMessageType('BluesAnticoneSizes', (_message.Message,), {
  'DESCRIPTOR' : _BLUESANTICONESIZES,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.BluesAnticoneSizes)
  })
_sym_db.RegisterMessage(BluesAnticoneSizes)

DoneBlocksWithTrustedDataMessage = _reflection.GeneratedProtocolMessageType('DoneBlocksWithTrustedDataMessage', (_message.Message,), {
  'DESCRIPTOR' : _DONEBLOCKSWITHTRUSTEDDATAMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.DoneBlocksWithTrustedDataMessage)
  })
_sym_db.RegisterMessage(DoneBlocksWithTrustedDataMessage)

PruningPointsMessage = _reflection.GeneratedProtocolMessageType('PruningPointsMessage', (_message.Message,), {
  'DESCRIPTOR' : _PRUNINGPOINTSMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.PruningPointsMessage)
  })
_sym_db.RegisterMessage(PruningPointsMessage)

RequestPruningPointProofMessage = _reflection.GeneratedProtocolMessageType('RequestPruningPointProofMessage', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTPRUNINGPOINTPROOFMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.RequestPruningPointProofMessage)
  })
_sym_db.RegisterMessage(RequestPruningPointProofMessage)

PruningPointProofMessage = _reflection.GeneratedProtocolMessageType('PruningPointProofMessage', (_message.Message,), {
  'DESCRIPTOR' : _PRUNINGPOINTPROOFMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.PruningPointProofMessage)
  })
_sym_db.RegisterMessage(PruningPointProofMessage)

PruningPointProofHeaderArray = _reflection.GeneratedProtocolMessageType('PruningPointProofHeaderArray', (_message.Message,), {
  'DESCRIPTOR' : _PRUNINGPOINTPROOFHEADERARRAY,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.PruningPointProofHeaderArray)
  })
_sym_db.RegisterMessage(PruningPointProofHeaderArray)

ReadyMessage = _reflection.GeneratedProtocolMessageType('ReadyMessage', (_message.Message,), {
  'DESCRIPTOR' : _READYMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.ReadyMessage)
  })
_sym_db.RegisterMessage(ReadyMessage)

BlockWithTrustedDataV4Message = _reflection.GeneratedProtocolMessageType('BlockWithTrustedDataV4Message', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKWITHTRUSTEDDATAV4MESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.BlockWithTrustedDataV4Message)
  })
_sym_db.RegisterMessage(BlockWithTrustedDataV4Message)

TrustedDataMessage = _reflection.GeneratedProtocolMessageType('TrustedDataMessage', (_message.Message,), {
  'DESCRIPTOR' : _TRUSTEDDATAMESSAGE,
  '__module__' : 'p2p_pb2'
  # @@protoc_insertion_point(class_scope:protowire.TrustedDataMessage)
  })
_sym_db.RegisterMessage(TrustedDataMessage)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z$github.com/karlsen-network/karlsend/protowire'
  _REQUESTADDRESSESMESSAGE._serialized_start=24
  _REQUESTADDRESSESMESSAGE._serialized_end=127
  _ADDRESSESMESSAGE._serialized_start=129
  _ADDRESSESMESSAGE._serialized_end=191
  _NETADDRESS._serialized_start=193
  _NETADDRESS._serialized_end=250
  _SUBNETWORKID._serialized_start=252
  _SUBNETWORKID._serialized_end=281
  _TRANSACTIONMESSAGE._serialized_start=284
  _TRANSACTIONMESSAGE._serialized_end=508
  _TRANSACTIONINPUT._serialized_start=511
  _TRANSACTIONINPUT._serialized_end=639
  _OUTPOINT._serialized_start=641
  _OUTPOINT._serialized_end=715
  _TRANSACTIONID._serialized_start=717
  _TRANSACTIONID._serialized_end=747
  _SCRIPTPUBLICKEY._serialized_start=749
  _SCRIPTPUBLICKEY._serialized_end=799
  _TRANSACTIONOUTPUT._serialized_start=801
  _TRANSACTIONOUTPUT._serialized_end=888
  _BLOCKMESSAGE._serialized_start=890
  _BLOCKMESSAGE._serialized_end=997
  _BLOCKHEADER._serialized_start=1000
  _BLOCKHEADER._serialized_end=1348
  _BLOCKLEVELPARENTS._serialized_start=1350
  _BLOCKLEVELPARENTS._serialized_end=1408
  _HASH._serialized_start=1410
  _HASH._serialized_end=1431
  _REQUESTBLOCKLOCATORMESSAGE._serialized_start=1433
  _REQUESTBLOCKLOCATORMESSAGE._serialized_end=1511
  _BLOCKLOCATORMESSAGE._serialized_start=1513
  _BLOCKLOCATORMESSAGE._serialized_end=1567
  _REQUESTHEADERSMESSAGE._serialized_start=1569
  _REQUESTHEADERSMESSAGE._serialized_end=1661
  _REQUESTNEXTHEADERSMESSAGE._serialized_start=1663
  _REQUESTNEXTHEADERSMESSAGE._serialized_end=1690
  _DONEHEADERSMESSAGE._serialized_start=1692
  _DONEHEADERSMESSAGE._serialized_end=1712
  _REQUESTRELAYBLOCKSMESSAGE._serialized_start=1714
  _REQUESTRELAYBLOCKSMESSAGE._serialized_end=1774
  _REQUESTTRANSACTIONSMESSAGE._serialized_start=1776
  _REQUESTTRANSACTIONSMESSAGE._serialized_end=1843
  _TRANSACTIONNOTFOUNDMESSAGE._serialized_start=1845
  _TRANSACTIONNOTFOUNDMESSAGE._serialized_end=1911
  _INVRELAYBLOCKMESSAGE._serialized_start=1913
  _INVRELAYBLOCKMESSAGE._serialized_end=1966
  _INVTRANSACTIONSMESSAGE._serialized_start=1968
  _INVTRANSACTIONSMESSAGE._serialized_end=2031
  _PINGMESSAGE._serialized_start=2033
  _PINGMESSAGE._serialized_end=2061
  _PONGMESSAGE._serialized_start=2063
  _PONGMESSAGE._serialized_end=2091
  _VERACKMESSAGE._serialized_start=2093
  _VERACKMESSAGE._serialized_end=2108
  _VERSIONMESSAGE._serialized_start=2111
  _VERSIONMESSAGE._serialized_end=2348
  _REJECTMESSAGE._serialized_start=2350
  _REJECTMESSAGE._serialized_end=2381
  _REQUESTPRUNINGPOINTUTXOSETMESSAGE._serialized_start=2383
  _REQUESTPRUNINGPOINTUTXOSETMESSAGE._serialized_end=2461
  _PRUNINGPOINTUTXOSETCHUNKMESSAGE._serialized_start=2463
  _PRUNINGPOINTUTXOSETCHUNKMESSAGE._serialized_end=2568
  _OUTPOINTANDUTXOENTRYPAIR._serialized_start=2570
  _OUTPOINTANDUTXOENTRYPAIR._serialized_end=2676
  _UTXOENTRY._serialized_start=2678
  _UTXOENTRY._serialized_end=2801
  _REQUESTNEXTPRUNINGPOINTUTXOSETCHUNKMESSAGE._serialized_start=2803
  _REQUESTNEXTPRUNINGPOINTUTXOSETCHUNKMESSAGE._serialized_end=2847
  _DONEPRUNINGPOINTUTXOSETCHUNKSMESSAGE._serialized_start=2849
  _DONEPRUNINGPOINTUTXOSETCHUNKSMESSAGE._serialized_end=2887
  _REQUESTIBDBLOCKSMESSAGE._serialized_start=2889
  _REQUESTIBDBLOCKSMESSAGE._serialized_end=2947
  _UNEXPECTEDPRUNINGPOINTMESSAGE._serialized_start=2949
  _UNEXPECTEDPRUNINGPOINTMESSAGE._serialized_end=2980
  _IBDBLOCKLOCATORMESSAGE._serialized_start=2982
  _IBDBLOCKLOCATORMESSAGE._serialized_end=3088
  _REQUESTIBDCHAINBLOCKLOCATORMESSAGE._serialized_start=3090
  _REQUESTIBDCHAINBLOCKLOCATORMESSAGE._serialized_end=3195
  _IBDCHAINBLOCKLOCATORMESSAGE._serialized_start=3197
  _IBDCHAINBLOCKLOCATORMESSAGE._serialized_end=3271
  _REQUESTANTICONEMESSAGE._serialized_start=3273
  _REQUESTANTICONEMESSAGE._serialized_end=3371
  _IBDBLOCKLOCATORHIGHESTHASHMESSAGE._serialized_start=3373
  _IBDBLOCKLOCATORHIGHESTHASHMESSAGE._serialized_end=3446
  _IBDBLOCKLOCATORHIGHESTHASHNOTFOUNDMESSAGE._serialized_start=3448
  _IBDBLOCKLOCATORHIGHESTHASHNOTFOUNDMESSAGE._serialized_end=3491
  _BLOCKHEADERSMESSAGE._serialized_start=3493
  _BLOCKHEADERSMESSAGE._serialized_end=3560
  _REQUESTPRUNINGPOINTANDITSANTICONEMESSAGE._serialized_start=3562
  _REQUESTPRUNINGPOINTANDITSANTICONEMESSAGE._serialized_end=3604
  _REQUESTNEXTPRUNINGPOINTANDITSANTICONEBLOCKSMESSAGE._serialized_start=3606
  _REQUESTNEXTPRUNINGPOINTANDITSANTICONEBLOCKSMESSAGE._serialized_end=3658
  _BLOCKWITHTRUSTEDDATAMESSAGE._serialized_start=3661
  _BLOCKWITHTRUSTEDDATAMESSAGE._serialized_end=3848
  _DAABLOCK._serialized_start=3850
  _DAABLOCK._serialized_end=3947
  _DAABLOCKV4._serialized_start=3949
  _DAABLOCKV4._serialized_end=4048
  _BLOCKGHOSTDAGDATAHASHPAIR._serialized_start=4050
  _BLOCKGHOSTDAGDATAHASHPAIR._serialized_end=4155
  _GHOSTDAGDATA._serialized_start=4158
  _GHOSTDAGDATA._serialized_end=4388
  _BLUESANTICONESIZES._serialized_start=4390
  _BLUESANTICONESIZES._serialized_end=4467
  _DONEBLOCKSWITHTRUSTEDDATAMESSAGE._serialized_start=4469
  _DONEBLOCKSWITHTRUSTEDDATAMESSAGE._serialized_end=4503
  _PRUNINGPOINTSMESSAGE._serialized_start=4505
  _PRUNINGPOINTSMESSAGE._serialized_end=4568
  _REQUESTPRUNINGPOINTPROOFMESSAGE._serialized_start=4570
  _REQUESTPRUNINGPOINTPROOFMESSAGE._serialized_end=4603
  _PRUNINGPOINTPROOFMESSAGE._serialized_start=4605
  _PRUNINGPOINTPROOFMESSAGE._serialized_end=4689
  _PRUNINGPOINTPROOFHEADERARRAY._serialized_start=4691
  _PRUNINGPOINTPROOFHEADERARRAY._serialized_end=4762
  _READYMESSAGE._serialized_start=4764
  _READYMESSAGE._serialized_end=4778
  _BLOCKWITHTRUSTEDDATAV4MESSAGE._serialized_start=4780
  _BLOCKWITHTRUSTEDDATAV4MESSAGE._serialized_end=4906
  _TRUSTEDDATAMESSAGE._serialized_start=4908
  _TRUSTEDDATAMESSAGE._serialized_end=5030
# @@protoc_insertion_point(module_scope)
