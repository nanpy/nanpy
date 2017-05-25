

Make sure these boxes are checked before submitting your issue - thank you!

- [ ] Try `examples/blink.py`
- [ ] Try to test the function without Nanpy, using only Arduino code.
- [ ] Check cfg.h. All needed functions are enabled?
- [ ] Run `examples/firmware_check.py` to check cfg.h again. All needed functions are listed?
- [ ] Your program should be as small as possible which demonstrates the bug.
- [ ] Enable logging in program: `import logging;logging.basicConfig(level=logging.DEBUG)`


### Your Python code


```python
import logging
logging.basicConfig(level=logging.DEBUG)

from nanpy import ...
```

### Your log messages

```
DEBUG:nanpy.serialmanager:opening port:/dev/ttyACM0 [115200 baud]
...
```

### Your cfg.h

```c
#define USE_Info                                    1
...
```
### Output of examples/firmware_check.py

```
Firmware classes enabled in cfg.h:
  ...
```

### Your hardware

- Arduino board: `   `
- Additional hardware:  `   `

