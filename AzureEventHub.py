ADDRESS = 'sb://####.servicebus.windows.net/#####'
USER = '##########'
KEY = '##################################'
CONSUMER_GROUP = "$default"
OFFSET = Offset("-1")
PARTITION = "1"


total = 0
last_sn = -1
last_offset = "-1"

try:
  if not ADDRESS:
      raise ValueError("No EventHubs URL supplied.")
  client = EventHubClient(ADDRESS, debug=False, username=USER, password=KEY)
  receiver = client.add_receiver(CONSUMER_GROUP, PARTITION, prefetch=5000, 
  offset=OFFSET)
  client.run()
  try:
      batched_events = receiver.receive(timeout=20)
  except:
      raise
  finally:
      client.stop()
  for event_data in batched_events:
      last_offset = event_data.offset.value
      last_sn = event_data.sequence_number
      total += 1
      print("Partition {}, Received {}, sn={} offset={}".format(
         PARTITION,
         total,
         last_sn,
         last_offset))

except KeyboardInterrupt:
   pass