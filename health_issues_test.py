"""
File: health_issues_test.py
Description: test module for testing health issues module for advanced programming assignment
Author: Natasha Hunter
ID: 110439590
Username: hunny006
This is my own work as defined by the University's Academic Integrity Policy.
"""

import health_issues
import pytest

@pytest.fixture
def health_issue1():
    return health_issues.Illness('Tail Fungus','Fungus present on animal\'s tail',10/11/2025,'minor')

@pytest.fixture
def health_issue2():
    return health_issues.Injury('Broken Leg','Animal\'s leg is broken in 3 places', 1/6/2025,'severe')

@pytest.fixture
def health_issue3():
    return health_issues.Behavioural_Issue('Depression','Animal is depressed and sad',1/1/2024,'moderate')

