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

class TestHealthIssues:
    '''
    Test class for health_issues module
    '''
    @pytest.fixture
    def health_issue1(self):
        return health_issues.Illness('Tail Fungus','Fungus present on animal\'s tail',10/11/2025,'minor')

    @pytest.fixture
    def health_issue2(self):
        return health_issues.Injury('Broken Leg','Animal\'s leg is broken in 3 places', 1/6/2025,'severe')

    @pytest.fixture
    def health_issue3(self):
        return health_issues.Behavioural_Issue('Depression','Animal is depressed and sad',1/1/2024,'moderate')

    def test_illness(self,health_issue1):
        # test illness created correctly
        assert health_issue1.name == 'Tail Fungus'
        assert health_issue1.treatment_plan in ['Wait and see', 'Medication', 'Surgery']

    def test_injury(self,health_issue2):
        # test injury created correctly
        assert health_issue2.severity == 'severe'
        assert health_issue2.treatment_plan in ['Wait and see', 'First Aid', 'Surgery']

    def test_behavioural_issue(self,health_issue3):
        # test behavioural issue created correctly
        assert health_issue3.date_reported == 1/1/2024
        assert health_issue3.treatment_plan in ['Wait and see', 'Therapy','Medication']