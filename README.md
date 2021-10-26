# PakFlag
**PakFlag** (🇹🇭: ปักธง, 🇯🇵: パクフラグ) is a simple CTF flags generator, written in Python.

## Usage

### Runs
```cmd
$ python pakflag.py
```

### Inputs
```cmd
Flags' name	: <FLAG_NAME: str>
Length		: <KEY_LENGTH: int>	// Default is 32 (MD5 hex digit), only even numbers
Number		: <NUMBER_OF_FLAG: int>	// Default is 100
```
> List of flags will be saved as `<FLAG_NAME>_flags.txt`

### Example
```cmd
Flags' name	: TNICYBER
Length		: 24
Number		: 10
--------------------------------------------------
TNICYBER{d83469c88e383ffcf900fb96}
TNICYBER{2004ea78c447075de2a2dfcc}
TNICYBER{48e60f6c0bb2e01e01897a6b}
TNICYBER{c440415f5f35169cc03987b3}
TNICYBER{1f1d8a1a8e4faa6eb8995e75}
TNICYBER{3420a2ac5a1928927832eae8}
TNICYBER{39c31f5507a6394cbde7c3f5}
TNICYBER{f1133a2ba1f87667edb76d68}
TNICYBER{b4feae745fd8a3b78694eb85}
TNICYBER{ad97aea22644289f08639777}
--------------------------------------------------
All flags have been saved as "TNICYBER_flags.txt"
```

---
[![License: MIT](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)
