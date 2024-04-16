import time

import ApiConnect

for i in range(1, 10):
    time.sleep(1)
    result = ApiConnect.method()
    print(result)


