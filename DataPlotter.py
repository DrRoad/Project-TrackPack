import time
import ttn

app_id = "trackpack"
access_key = "ttn-account-v2.KK46lPYH8gFKi1noKfc-pU8yCXKD6AJgm_2nCyl3T9Q"

def uplink_callback(msg, client):
  print("Received uplink from ", msg.dev_id)
  print(msg)

handler = ttn.HandlerClient(app_id, access_key)

# using mqtt client
mqtt_client = handler.data()
mqtt_client.set_uplink_callback(uplink_callback)
mqtt_client.connect()
time.sleep(60)
mqtt_client.close()

# using application manager client
app_client =  handler.application()
my_app = app_client.get()
print(my_app)
my_devices = app_client.devices()
print(my_devices)

raw_payload = str(my_app[5])
print(raw_payload)
print(int(b(raw_payload).decode("utf-8")) / 100)