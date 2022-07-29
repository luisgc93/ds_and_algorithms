from algorithms.can_generate_doc import can_generate_document


def test_can_generate_doc():
    assert can_generate_document("abcabc", "aabbccc") is False
    assert can_generate_document("abcabc", "aabbcc") is True

