# %%
import os
import pytest
import temperature_plotting as tpl

@pytest.mark.skip(reason="Test is bad")
def test_compute_mean_bad():
    calc = tpl.compute_mean([1,2,3])
    assert calc == 5

def test_compute_mean():
    calc = tpl.compute_mean([0, 10, 20])
    assert calc == 10
    assert type(calc) == float

    calc = tpl.compute_mean([-10, 10])
    assert calc == 0

    calc = tpl.compute_mean([0, 10, 0])
    assert round(calc, 4) == 3.3333, "Check that the average is roughly correct"

    with pytest.raises(TypeError):
        calc = tpl.compute_mean(["a", "b", "c"])
    
    calc = tpl.compute_mean([])
    assert calc == None

# Integration test
def test_main():
    tpl.main()
    assert os.path.exists("plot_25.png")



