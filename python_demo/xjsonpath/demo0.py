from jsonpath import jsonpath


data = {
  "store": {
    "book": [
      {
        "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      {
        "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      },
      {
        "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-3",
        "price": 8.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  }
}


a = jsonpath(data, '$.store')
print(a)


data = {
    'request': {
        'pubInfo': {
            'sdkVersion': 'Union',
        },
        'busiData': {
            'sdkVersion1': 'Union1',
            'sdkVersion2': 'Union2',
            'payPassword': 'test',
        },
    }
}

b = jsonpath(data, '$.request.busiData')
if b:
    print(b[0])