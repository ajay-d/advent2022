import numpy as np
import re
from collections import Counter

with open("day7.txt") as f:
    txt = f.read().splitlines()

len(txt)
len([cmd for cmd in txt if cmd.startswith("$")])
[cmd for cmd in txt if cmd.startswith("$")]
[cmd for cmd in txt if re.search(r'^[^\$]', cmd)]

len([cmd for cmd in txt if cmd.startswith("$")])
len([cmd for cmd in txt if re.search(r'^[^\$]', cmd)])

[re.sub(r'\$ ', '', cmd) for cmd in txt if cmd.startswith("$")]
cnt = Counter([re.sub(r'\$ ', '', cmd) for cmd in txt if cmd.startswith("$")])
cnt.most_common(3)