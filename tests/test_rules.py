from app.rules import is_blank


def test_empty_is_blank():
    assert is_blank("") == True


def test_cam2_is_not_blank():
    assert is_blank("cam2") == False

def test_spaces_is_blank():
    assert is_blank("   ") == True