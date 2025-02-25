import myencryption.encryption as enc

encoder_str = enc.encoder_str


def testTextEncoding():
    message = "HALLO123_"
    assert enc.textEncoding(message, encoder_str) == [
        17,
        10,
        21,
        21,
        24,
        1,
        2,
        3,
        40,
    ]


def testCreateKeys():
    encoded_message = [
        17,
        10,
        21,
        21,
        24,
        1,
        2,
        3,
        40,
    ]

    result = enc.createKeys(encoded_message)

    print(result is tuple)

    assert isinstance(result, tuple)
    assert isinstance(result[0], list)
    assert isinstance(result[1], list)
    assert len(result[0]) == 9
    assert len(result[1]) == 9


def testDecryptmessage():
    key1 = [13, 4, 15, 10, 8, 0, 2, 3, 14]
    key2 = [4, 6, 6, 11, 16, 1, 0, 0, 26]

    assert enc.decryptMessage(encoder_str, key1, key2) == "HALLO123_"
