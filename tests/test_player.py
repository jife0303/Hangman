from src.player import set_name

def test_set_name():
    """Test set_name()."""
    assert set_name("Jialin", 1) == "Jialin"
    assert set_name(None, 1) == "Player 1"
    assert set_name(None, 2) == "Player 2"