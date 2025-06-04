import pcl


def test_add():
    assert pcl.add(1, 2) == 3
    assert pcl.add(4, 5, 6) == 15


def test_version():
    assert pcl.__version__ == "0.0.1"
