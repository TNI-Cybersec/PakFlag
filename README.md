# PakFlag
**PakFlag** (ปักธง) is a simple CTF flags generator, written in Python.

## Usage

### Runs
```cmd
$ python pakflag.py
```

### Inputs
```cmd
Flags' name	: <FLAG_NAME: str>
Length		: <KEY_LENGTH: int>  // Default is 32 (MD5 hex digit)
Number		: <NUMBER_OF_FLAG: int>  // Default is 100
```
> List of flags will be saved as `<FLAG_NAME>_flags.txt`

### Example
```cmd
Flags' name	: TNICYBER
Length		: 16
Number		: 10
--------------------------------------------------
TNICYBER{240b5d73e2e8ab4a41075c972de3ea5b}
TNICYBER{e41684347e5aa1edd3b38a03c78aa5b3}
TNICYBER{68c0a2407f9b996375afce5ad95a8c00}
TNICYBER{48ec39083a21a772356c3a7cc53ff356}
TNICYBER{0f05bcb605e07079ddc022310ab1d89c}
TNICYBER{0c8b0e2a8e86a391e92718fbc48dc369}
TNICYBER{b58a69be301d176188f2bd890f556116}
TNICYBER{b4804d6ede3b317f37994215f6b15ea9}
TNICYBER{15905ff297dfacc38cc097712a14a707}
TNICYBER{362ca9ca90f302ce6b762b9bc2e04fe2}
--------------------------------------------------
All flags have been saved as "TNICYBER_flags.txt"
```

---
[![License: MIT](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)
