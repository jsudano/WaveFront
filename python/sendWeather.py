from OSC import OSCClient, OSCBundle
from owmAPI import owmAPI

client = OSCClient()
client.connect(("localhost", 54345))

# Connect to a node
ucb = owmAPI("5327684")
sunrise = ucb.fetch('sys')['sunrise']

# Parse node data
melody = []
while sunrise:
    melody.insert(0, (sunrise % 10))
    sunrise //= 10

# Create and send a bundle
bundle = OSCBundle()
bundle.append({'addr': "/melody", 'args': str(melody)})
client.send(bundle)