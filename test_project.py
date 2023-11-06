import pytest
from project import IsStandardTuning, Replace, CountBars

def test_IsStandardTuning():
    # Test a tab file in standard tuning
    result = IsStandardTuning("standard_tuning.txt")
    assert result == True

    # Test a tab file not in standard tuning
    result = IsStandardTuning("non_standard_tuning.txt")
    assert result == False


def test_Replace():
    # Test the Replace function with a standard tuning tab file
    Replace("standard_tuning.txt", "The tabs are in standard tuning.", "There is 1 bar.")

    # Read the output file produced by the Replace function
    with open("modified_tab.txt", "r") as f:
        output = f.read()

    # Read the expected output file
    with open("expected_output1.txt", "r") as f:
        expected_output = f.read()

    # Compare the output and expected output
    assert output == expected_output


def test_CountBars():
    # Test a tab file with 8 bars
    result = CountBars("tab_with_8_bars.txt")
    assert result == "There are 8 bars."


    # Test a tab file with 16 bars
    result = CountBars("tab_with_16_bars.txt")
    assert result == "There are 16 bars."

    # Test a tab file with 1 bar
    result = CountBars("standard_tuning.txt")
    assert result == "There is 1 bar."
