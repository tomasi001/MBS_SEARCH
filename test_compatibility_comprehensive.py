#!/usr/bin/env python3
"""
Comprehensive test suite for MBS compatibility checker.
Generated from real MBS data - 100 test cases.
"""

import pytest
import json
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from mbs_clarity.compatibility_checker import check_mbs_compatibility


# Load test cases
with open('compatibility_test_cases.json', 'r') as f:
    TEST_CASES = json.load(f)


class TestCompatibilityChecker:
    """Comprehensive test suite for compatibility checker."""
    

    # ===== P1 Tests (14 tests) =====

    def test_p1_001_Single_invalid_code(self):
        """Single invalid code (Difficulty: basic)"""
        codes = ['X999']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_002_Multiple_invalid_codes___test_1(self):
        """Multiple invalid codes - test 1 (Difficulty: basic)"""
        codes = ['X999', 'INVALID']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_003_Multiple_invalid_codes___test_2(self):
        """Multiple invalid codes - test 2 (Difficulty: basic)"""
        codes = ['INVALID', '99999']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_004_Multiple_invalid_codes___test_3(self):
        """Multiple invalid codes - test 3 (Difficulty: basic)"""
        codes = ['99999', 'ABCD']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_005_Multiple_invalid_codes___test_4(self):
        """Multiple invalid codes - test 4 (Difficulty: basic)"""
        codes = ['ABCD', 'Z9999']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_006_Multiple_invalid_codes___test_5(self):
        """Multiple invalid codes - test 5 (Difficulty: basic)"""
        codes = ['Z9999', 'X999']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_007_Invalid_code_mixed_with_valid_code(self):
        """Invalid code mixed with valid code (Difficulty: basic)"""
        codes = ['X999', '3']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_008_Empty_codes_array(self):
        """Empty codes array (Difficulty: basic)"""
        codes = []
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_009_Whitespace_only_codes(self):
        """Whitespace-only codes (Difficulty: edge_case)"""
        codes = ['   ', '  ', '']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_010_Invalid_numeric_code_999999(self):
        """Invalid numeric code 999999 (Difficulty: edge_case)"""
        codes = ['999999']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_011_Invalid_numeric_code_1000000(self):
        """Invalid numeric code 1000000 (Difficulty: edge_case)"""
        codes = ['1000000']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_012_Invalid_numeric_code_1000001(self):
        """Invalid numeric code 1000001 (Difficulty: edge_case)"""
        codes = ['1000001']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_013_Invalid_numeric_code_1000002(self):
        """Invalid numeric code 1000002 (Difficulty: edge_case)"""
        codes = ['1000002']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_014_Invalid_numeric_code_1000003(self):
        """Invalid numeric code 1000003 (Difficulty: edge_case)"""
        codes = ['1000003']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        

    # ===== C1 Tests (25 tests) =====

    def test_c1_015_Group_conflict___A1_3_and_4(self):
        """Group conflict - A1 (3 and 4) (Difficulty: moderate)"""
        codes = ['3', '4']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_016_Group_conflict___A10_10905_and_10907(self):
        """Group conflict - A10 (10905 and 10907) (Difficulty: moderate)"""
        codes = ['10905', '10907']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_017_Group_conflict___A11_585_and_588(self):
        """Group conflict - A11 (585 and 588) (Difficulty: moderate)"""
        codes = ['585', '588']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_018_Group_conflict___A12_385_and_386(self):
        """Group conflict - A12 (385 and 386) (Difficulty: moderate)"""
        codes = ['385', '386']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_019_Group_conflict___A13_410_and_411(self):
        """Group conflict - A13 (410 and 411) (Difficulty: moderate)"""
        codes = ['410', '411']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_020_Group_conflict___A14_695_and_699(self):
        """Group conflict - A14 (695 and 699) (Difficulty: moderate)"""
        codes = ['695', '699']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_021_Group_conflict___A15_729_and_731(self):
        """Group conflict - A15 (729 and 731) (Difficulty: moderate)"""
        codes = ['729', '731']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_022_Group_conflict___A17_900_and_903(self):
        """Group conflict - A17 (900 and 903) (Difficulty: moderate)"""
        codes = ['900', '903']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_023_Group_conflict___A2_52_and_53(self):
        """Group conflict - A2 (52 and 53) (Difficulty: moderate)"""
        codes = ['52', '53']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_024_Group_conflict___A20_2700_and_2701(self):
        """Group conflict - A20 (2700 and 2701) (Difficulty: moderate)"""
        codes = ['2700', '2701']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_025_Group_conflict___multiple_codes_in_A1(self):
        """Group conflict - multiple codes in A1 (Difficulty: moderate)"""
        codes = ['3', '4', '23']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_026_Group_conflict___multiple_codes_in_A10(self):
        """Group conflict - multiple codes in A10 (Difficulty: moderate)"""
        codes = ['10905', '10907', '10910']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_027_Group_conflict___multiple_codes_in_A11(self):
        """Group conflict - multiple codes in A11 (Difficulty: moderate)"""
        codes = ['585', '588', '591']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_028_Group_conflict___multiple_codes_in_A12(self):
        """Group conflict - multiple codes in A12 (Difficulty: moderate)"""
        codes = ['385', '386', '387']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_029_Group_conflict___multiple_codes_in_A13(self):
        """Group conflict - multiple codes in A13 (Difficulty: moderate)"""
        codes = ['410', '411', '412']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_030_Direct_exclusion_104_excludes_106(self):
        """Direct exclusion (104 excludes 106) (Difficulty: moderate)"""
        codes = ['104', '106']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_031_Direct_exclusion_104_excludes_109(self):
        """Direct exclusion (104 excludes 109) (Difficulty: moderate)"""
        codes = ['104', '109']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_032_Direct_exclusion_104_excludes_125(self):
        """Direct exclusion (104 excludes 125) (Difficulty: moderate)"""
        codes = ['104', '125']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_033_Direct_exclusion_104_excludes_16401(self):
        """Direct exclusion (104 excludes 16401) (Difficulty: moderate)"""
        codes = ['104', '16401']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_034_Direct_exclusion_105_excludes_126(self):
        """Direct exclusion (105 excludes 126) (Difficulty: moderate)"""
        codes = ['105', '126']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_035_Direct_exclusion_105_excludes_16404(self):
        """Direct exclusion (105 excludes 16404) (Difficulty: moderate)"""
        codes = ['105', '16404']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_036_Direct_exclusion_106_excludes_104(self):
        """Direct exclusion (106 excludes 104) (Difficulty: moderate)"""
        codes = ['106', '104']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_037_Direct_exclusion_106_excludes_109(self):
        """Direct exclusion (106 excludes 109) (Difficulty: moderate)"""
        codes = ['106', '109']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_038_Direct_exclusion_106_excludes_10801(self):
        """Direct exclusion (106 excludes 10801) (Difficulty: moderate)"""
        codes = ['106', '10801']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_039_Direct_exclusion_10809_excludes_10806(self):
        """Direct exclusion (10809 excludes 10806) (Difficulty: moderate)"""
        codes = ['10809', '10806']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        

    # ===== C2 Tests (15 tests) =====

    def test_c2_040_Missing_prerequisite_127_requires_45(self):
        """Missing prerequisite (127 requires 45) (Difficulty: moderate)"""
        codes = ['127']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_041_Missing_prerequisite_129_requires_45(self):
        """Missing prerequisite (129 requires 45) (Difficulty: moderate)"""
        codes = ['129']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_042_Missing_prerequisite_132_requires_2(self):
        """Missing prerequisite (132 requires 2) (Difficulty: moderate)"""
        codes = ['132']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_043_Missing_prerequisite_133_requires_20(self):
        """Missing prerequisite (133 requires 20) (Difficulty: moderate)"""
        codes = ['133']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_044_Missing_prerequisite_133_requires_2(self):
        """Missing prerequisite (133 requires 2) (Difficulty: moderate)"""
        codes = ['133']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_045_Missing_prerequisite_135_requires_45(self):
        """Missing prerequisite (135 requires 45) (Difficulty: moderate)"""
        codes = ['135']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_046_Missing_prerequisite_137_requires_45(self):
        """Missing prerequisite (137 requires 45) (Difficulty: moderate)"""
        codes = ['137']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_047_Missing_prerequisite_289_requires_45(self):
        """Missing prerequisite (289 requires 45) (Difficulty: moderate)"""
        codes = ['289']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_048_Missing_prerequisite_289_requires_2(self):
        """Missing prerequisite (289 requires 2) (Difficulty: moderate)"""
        codes = ['289']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_049_Missing_prerequisite_296_requires_45(self):
        """Missing prerequisite (296 requires 45) (Difficulty: moderate)"""
        codes = ['296']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_050_Missing_prerequisite_297_requires_45(self):
        """Missing prerequisite (297 requires 45) (Difficulty: moderate)"""
        codes = ['297']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_051_Missing_prerequisite_299_requires_45(self):
        """Missing prerequisite (299 requires 45) (Difficulty: moderate)"""
        codes = ['299']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_052_Missing_prerequisite_300_requires_15(self):
        """Missing prerequisite (300 requires 15) (Difficulty: moderate)"""
        codes = ['300']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_053_Missing_prerequisite_302_requires_15(self):
        """Missing prerequisite (302 requires 15) (Difficulty: moderate)"""
        codes = ['302']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_054_Missing_prerequisite_304_requires_30(self):
        """Missing prerequisite (304 requires 30) (Difficulty: moderate)"""
        codes = ['304']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        

    # ===== C3 Tests (10 tests) =====

    def test_c3_055_Solo_only_code_alone_36(self):
        """Solo-only code alone (36) (Difficulty: basic)"""
        codes = ['36']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_056_Solo_only_code_alone_44(self):
        """Solo-only code alone (44) (Difficulty: basic)"""
        codes = ['44']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_057_Solo_only_code_alone_5040(self):
        """Solo-only code alone (5040) (Difficulty: basic)"""
        codes = ['5040']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_058_Solo_only_code_alone_5060(self):
        """Solo-only code alone (5060) (Difficulty: basic)"""
        codes = ['5060']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_059_Solo_only_code_alone_90043(self):
        """Solo-only code alone (90043) (Difficulty: basic)"""
        codes = ['90043']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_060_Solo_only_code_with_other_36_with_104(self):
        """Solo-only code with other (36 with 104) (Difficulty: moderate)"""
        codes = ['36', '104']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_061_Solo_only_code_with_other_44_with_105(self):
        """Solo-only code with other (44 with 105) (Difficulty: moderate)"""
        codes = ['44', '105']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_062_Solo_only_code_with_other_5040_with_106(self):
        """Solo-only code with other (5040 with 106) (Difficulty: moderate)"""
        codes = ['5040', '106']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_063_Solo_only_code_with_other_5060_with_107(self):
        """Solo-only code with other (5060 with 107) (Difficulty: moderate)"""
        codes = ['5060', '107']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_064_Solo_only_code_with_other_90043_with_108(self):
        """Solo-only code with other (90043 with 108) (Difficulty: moderate)"""
        codes = ['90043', '108']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        

    # ===== C4 Tests (15 tests) =====

    def test_c4_065_Duplicate_same_occasion_code_11729_x2(self):
        """Duplicate same_occasion code (11729 x2) (Difficulty: moderate)"""
        codes = ['11729', '11729']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_066_Duplicate_same_occasion_code_11730_x2(self):
        """Duplicate same_occasion code (11730 x2) (Difficulty: moderate)"""
        codes = ['11730', '11730']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_067_Duplicate_same_occasion_code_11732_x2(self):
        """Duplicate same_occasion code (11732 x2) (Difficulty: moderate)"""
        codes = ['11732', '11732']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_068_Duplicate_same_occasion_code_12203_x2(self):
        """Duplicate same_occasion code (12203 x2) (Difficulty: moderate)"""
        codes = ['12203', '12203']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_069_Duplicate_same_occasion_code_12204_x2(self):
        """Duplicate same_occasion code (12204 x2) (Difficulty: moderate)"""
        codes = ['12204', '12204']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_070_Duplicate_same_occasion_code_12205_x2(self):
        """Duplicate same_occasion code (12205 x2) (Difficulty: moderate)"""
        codes = ['12205', '12205']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_071_Duplicate_same_occasion_code_12207_x2(self):
        """Duplicate same_occasion code (12207 x2) (Difficulty: moderate)"""
        codes = ['12207', '12207']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_072_Duplicate_same_occasion_code_12208_x2(self):
        """Duplicate same_occasion code (12208 x2) (Difficulty: moderate)"""
        codes = ['12208', '12208']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_073_Duplicate_same_occasion_code_12210_x2(self):
        """Duplicate same_occasion code (12210 x2) (Difficulty: moderate)"""
        codes = ['12210', '12210']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_074_Duplicate_same_occasion_code_12213_x2(self):
        """Duplicate same_occasion code (12213 x2) (Difficulty: moderate)"""
        codes = ['12213', '12213']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_075_Multiple_duplicates_11729_x3(self):
        """Multiple duplicates (11729 x3) (Difficulty: advanced)"""
        codes = ['11729', '11729', '11729']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_076_Multiple_duplicates_11730_x3(self):
        """Multiple duplicates (11730 x3) (Difficulty: advanced)"""
        codes = ['11730', '11730', '11730']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_077_Multiple_duplicates_11732_x3(self):
        """Multiple duplicates (11732 x3) (Difficulty: advanced)"""
        codes = ['11732', '11732', '11732']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_078_Multiple_duplicates_12203_x3(self):
        """Multiple duplicates (12203 x3) (Difficulty: advanced)"""
        codes = ['12203', '12203', '12203']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_079_Multiple_duplicates_12204_x3(self):
        """Multiple duplicates (12204 x3) (Difficulty: advanced)"""
        codes = ['12204', '12204', '12204']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        

    # ===== YAY Tests (21 tests) =====

    def test_yay_080_Single_valid_code_104(self):
        """Single valid code (104) (Difficulty: basic)"""
        codes = ['104']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_081_Single_valid_code_105(self):
        """Single valid code (105) (Difficulty: basic)"""
        codes = ['105']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_082_Single_valid_code_106(self):
        """Single valid code (106) (Difficulty: basic)"""
        codes = ['106']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_083_Single_valid_code_107(self):
        """Single valid code (107) (Difficulty: basic)"""
        codes = ['107']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_084_Single_valid_code_108(self):
        """Single valid code (108) (Difficulty: basic)"""
        codes = ['108']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_085_Compatible_codes_104_and_10801(self):
        """Compatible codes (104 and 10801) (Difficulty: moderate)"""
        codes = ['104', '10801']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_086_Compatible_codes_104_and_10802(self):
        """Compatible codes (104 and 10802) (Difficulty: moderate)"""
        codes = ['104', '10802']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_087_Compatible_codes_104_and_10803(self):
        """Compatible codes (104 and 10803) (Difficulty: moderate)"""
        codes = ['104', '10803']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_088_Compatible_codes_104_and_10804(self):
        """Compatible codes (104 and 10804) (Difficulty: moderate)"""
        codes = ['104', '10804']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_089_Compatible_codes_104_and_10805(self):
        """Compatible codes (104 and 10805) (Difficulty: moderate)"""
        codes = ['104', '10805']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_090_Compatible_codes_104_and_10806(self):
        """Compatible codes (104 and 10806) (Difficulty: moderate)"""
        codes = ['104', '10806']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_091_Compatible_codes_104_and_10807(self):
        """Compatible codes (104 and 10807) (Difficulty: moderate)"""
        codes = ['104', '10807']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_092_Compatible_codes_104_and_10808(self):
        """Compatible codes (104 and 10808) (Difficulty: moderate)"""
        codes = ['104', '10808']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_093_Compatible_codes_104_and_10809(self):
        """Compatible codes (104 and 10809) (Difficulty: moderate)"""
        codes = ['104', '10809']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_094_Compatible_codes_104_and_10816(self):
        """Compatible codes (104 and 10816) (Difficulty: moderate)"""
        codes = ['104', '10816']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_095_Valid_code_1_10952(self):
        """Valid code 1 (10952) (Difficulty: basic)"""
        codes = ['10952']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_096_Valid_code_2_10953(self):
        """Valid code 2 (10953) (Difficulty: basic)"""
        codes = ['10953']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_097_Valid_code_3_10954(self):
        """Valid code 3 (10954) (Difficulty: basic)"""
        codes = ['10954']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_098_Valid_code_4_10955(self):
        """Valid code 4 (10955) (Difficulty: basic)"""
        codes = ['10955']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_099_Valid_code_5_10956(self):
        """Valid code 5 (10956) (Difficulty: basic)"""
        codes = ['10956']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_100_Valid_code_6_10957(self):
        """Valid code 6 (10957) (Difficulty: basic)"""
        codes = ['10957']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
