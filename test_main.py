from main import add_task

def test_add_task():
    ukoly = {}
    result = add_task(ukoly, "Zorat pole", "Zitra")
    assert result == {"Zorat pole", "Zitra"}