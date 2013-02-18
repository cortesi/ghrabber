import tutils
import ghrabber

def test_extract():
    f = file(tutils.test_data.path("data/search.html")).read()
    ret = list(ghrabber.extract(f))
    for i in ret:
        assert i.endswith(".bash_history")


def test_is_last_page():
    f = file(tutils.test_data.path("data/search.html")).read()
    assert not ghrabber.is_last_page(f)
    f = file(tutils.test_data.path("data/lastpage.html")).read()
    assert ghrabber.is_last_page(f)


def test_to_raw():
    p = "/nonexistent/archlinux/blob/a4f339b71ed6bb703f5f77888272d886f553f99a/.bash_history"
    assert ghrabber.raw_url(p)


def test_make_fname():
    p = "/nonexistent/archlinux/blob/a4f339b71ed6bb703f5f77888272d886f553f99a/.bash_history"
    assert ghrabber.make_fname(p)

