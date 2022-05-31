import base64
from itertools import cycle

message = "L08WNgwPCgESQ09uSEgKAhYOGlR4SEIgAAADFwADGjFPT1dQVAodBzENCCYLS0NSRgEJMgcdGQNU T1RTcwELIB0JCxsDCApzRE9KERAHBxYiDQgmARhIUltESCEGAwITGAoKVHhIQjEODg0bFRdIdFJP SgMSCQtUeEhCJQADSFJbREgjAQFMVw4="

key = bytes("thecoloradothompsons", "utf8")

print(bytes(a ^ b for a, b in zip(base64.b64decode(message), cycle(key))))