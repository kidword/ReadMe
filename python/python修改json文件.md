```python
# coding=utf-8
import os, sys
import json


def get_new_json(filepath, key, value):
    key_ = key.split(".")
    key_length = len(key_)
    with open(filepath, 'rb') as f:
        json_data = json.load(f)
        i = 0
        a = json_data
        while i < key_length:
            if i + 1 == key_length:
                a[key_[i]] = value
                i = i + 1
            else:
                a = a[key_[i]]
                i = i + 1
    f.close()
    return json_data


def rewrite_json_file(filepath, json_data):
    with open(filepath, 'w') as f:
        json.dump(json_data, f)
    f.close()


if __name__ == '__main__':
    key = "status"
    value = "YES"
    json_path = "status.json"

    m_json_data = get_new_json(json_path, key, value)
    rewrite_json_file(json_path, m_json_data)

```

