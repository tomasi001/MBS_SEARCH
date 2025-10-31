#!/usr/bin/env python3
"""
Comprehensive test suite for MBS compatibility checker - 1000 test cases.
Generated from real MBS data with actual code combinations.
"""

import pytest
import json
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from mbs_clarity.compatibility_checker import check_mbs_compatibility


# Load test cases
with open("compatibility_test_cases_1000.json", "r") as f:
    TEST_CASES = json.load(f)


class TestCompatibilityChecker1000:
    """Comprehensive test suite - 1000 test cases."""
    

    # ===== P1 Tests (100 tests) =====

    def test_p1_0001_Single_invalid_code_X999(self):
        """Single invalid code (X999) (Difficulty: basic)"""
        codes = ['X999']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0002_Single_invalid_code_INVALID(self):
        """Single invalid code (INVALID) (Difficulty: basic)"""
        codes = ['INVALID']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0003_Single_invalid_code_99999(self):
        """Single invalid code (99999) (Difficulty: basic)"""
        codes = ['99999']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0004_Single_invalid_code_ABCD(self):
        """Single invalid code (ABCD) (Difficulty: basic)"""
        codes = ['ABCD']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0005_Single_invalid_code_Z9999(self):
        """Single invalid code (Z9999) (Difficulty: basic)"""
        codes = ['Z9999']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0006_Multiple_invalid_codes_X999_INVALID(self):
        """Multiple invalid codes (X999, INVALID) (Difficulty: basic)"""
        codes = ['X999', 'INVALID']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0007_Multiple_invalid_codes_INVALID_99999(self):
        """Multiple invalid codes (INVALID, 99999) (Difficulty: basic)"""
        codes = ['INVALID', '99999']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0008_Multiple_invalid_codes_99999_ABCD(self):
        """Multiple invalid codes (99999, ABCD) (Difficulty: basic)"""
        codes = ['99999', 'ABCD']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0009_Multiple_invalid_codes_ABCD_Z9999(self):
        """Multiple invalid codes (ABCD, Z9999) (Difficulty: basic)"""
        codes = ['ABCD', 'Z9999']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0010_Multiple_invalid_codes_Z9999_X999(self):
        """Multiple invalid codes (Z9999, X999) (Difficulty: basic)"""
        codes = ['Z9999', 'X999']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0011_Multiple_invalid_codes_X999_INVALID(self):
        """Multiple invalid codes (X999, INVALID) (Difficulty: basic)"""
        codes = ['X999', 'INVALID']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0012_Multiple_invalid_codes_INVALID_99999(self):
        """Multiple invalid codes (INVALID, 99999) (Difficulty: basic)"""
        codes = ['INVALID', '99999']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0013_Multiple_invalid_codes_99999_ABCD(self):
        """Multiple invalid codes (99999, ABCD) (Difficulty: basic)"""
        codes = ['99999', 'ABCD']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0014_Multiple_invalid_codes_ABCD_Z9999(self):
        """Multiple invalid codes (ABCD, Z9999) (Difficulty: basic)"""
        codes = ['ABCD', 'Z9999']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0015_Multiple_invalid_codes_Z9999_X999(self):
        """Multiple invalid codes (Z9999, X999) (Difficulty: basic)"""
        codes = ['Z9999', 'X999']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0016_Multiple_invalid_codes_X999_INVALID(self):
        """Multiple invalid codes (X999, INVALID) (Difficulty: basic)"""
        codes = ['X999', 'INVALID']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0017_Multiple_invalid_codes_INVALID_99999(self):
        """Multiple invalid codes (INVALID, 99999) (Difficulty: basic)"""
        codes = ['INVALID', '99999']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0018_Multiple_invalid_codes_99999_ABCD(self):
        """Multiple invalid codes (99999, ABCD) (Difficulty: basic)"""
        codes = ['99999', 'ABCD']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0019_Multiple_invalid_codes_ABCD_Z9999(self):
        """Multiple invalid codes (ABCD, Z9999) (Difficulty: basic)"""
        codes = ['ABCD', 'Z9999']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0020_Multiple_invalid_codes_Z9999_X999(self):
        """Multiple invalid codes (Z9999, X999) (Difficulty: basic)"""
        codes = ['Z9999', 'X999']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0021_Multiple_invalid_codes_X999_INVALID(self):
        """Multiple invalid codes (X999, INVALID) (Difficulty: basic)"""
        codes = ['X999', 'INVALID']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0022_Multiple_invalid_codes_INVALID_99999(self):
        """Multiple invalid codes (INVALID, 99999) (Difficulty: basic)"""
        codes = ['INVALID', '99999']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0023_Multiple_invalid_codes_99999_ABCD(self):
        """Multiple invalid codes (99999, ABCD) (Difficulty: basic)"""
        codes = ['99999', 'ABCD']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0024_Multiple_invalid_codes_ABCD_Z9999(self):
        """Multiple invalid codes (ABCD, Z9999) (Difficulty: basic)"""
        codes = ['ABCD', 'Z9999']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0025_Multiple_invalid_codes_Z9999_X999(self):
        """Multiple invalid codes (Z9999, X999) (Difficulty: basic)"""
        codes = ['Z9999', 'X999']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0026_Multiple_invalid_codes_X999_INVALID(self):
        """Multiple invalid codes (X999, INVALID) (Difficulty: basic)"""
        codes = ['X999', 'INVALID']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0027_Multiple_invalid_codes_INVALID_99999(self):
        """Multiple invalid codes (INVALID, 99999) (Difficulty: basic)"""
        codes = ['INVALID', '99999']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0028_Multiple_invalid_codes_99999_ABCD(self):
        """Multiple invalid codes (99999, ABCD) (Difficulty: basic)"""
        codes = ['99999', 'ABCD']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0029_Multiple_invalid_codes_ABCD_Z9999(self):
        """Multiple invalid codes (ABCD, Z9999) (Difficulty: basic)"""
        codes = ['ABCD', 'Z9999']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0030_Multiple_invalid_codes_Z9999_X999(self):
        """Multiple invalid codes (Z9999, X999) (Difficulty: basic)"""
        codes = ['Z9999', 'X999']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0031_Multiple_invalid_codes_X999_INVALID(self):
        """Multiple invalid codes (X999, INVALID) (Difficulty: basic)"""
        codes = ['X999', 'INVALID']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0032_Multiple_invalid_codes_INVALID_99999(self):
        """Multiple invalid codes (INVALID, 99999) (Difficulty: basic)"""
        codes = ['INVALID', '99999']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0033_Multiple_invalid_codes_99999_ABCD(self):
        """Multiple invalid codes (99999, ABCD) (Difficulty: basic)"""
        codes = ['99999', 'ABCD']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0034_Multiple_invalid_codes_ABCD_Z9999(self):
        """Multiple invalid codes (ABCD, Z9999) (Difficulty: basic)"""
        codes = ['ABCD', 'Z9999']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0035_Multiple_invalid_codes_Z9999_X999(self):
        """Multiple invalid codes (Z9999, X999) (Difficulty: basic)"""
        codes = ['Z9999', 'X999']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0036_Invalid_mixed_with_valid_X999_104(self):
        """Invalid mixed with valid (X999, 104) (Difficulty: basic)"""
        codes = ['X999', '104']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0037_Invalid_mixed_with_valid_INVALID_105(self):
        """Invalid mixed with valid (INVALID, 105) (Difficulty: basic)"""
        codes = ['INVALID', '105']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0038_Invalid_mixed_with_valid_99999_106(self):
        """Invalid mixed with valid (99999, 106) (Difficulty: basic)"""
        codes = ['99999', '106']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0039_Invalid_mixed_with_valid_ABCD_107(self):
        """Invalid mixed with valid (ABCD, 107) (Difficulty: basic)"""
        codes = ['ABCD', '107']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0040_Invalid_mixed_with_valid_Z9999_108(self):
        """Invalid mixed with valid (Z9999, 108) (Difficulty: basic)"""
        codes = ['Z9999', '108']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0041_Invalid_mixed_with_valid_X999_10801(self):
        """Invalid mixed with valid (X999, 10801) (Difficulty: basic)"""
        codes = ['X999', '10801']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0042_Invalid_mixed_with_valid_INVALID_10802(self):
        """Invalid mixed with valid (INVALID, 10802) (Difficulty: basic)"""
        codes = ['INVALID', '10802']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0043_Invalid_mixed_with_valid_99999_10803(self):
        """Invalid mixed with valid (99999, 10803) (Difficulty: basic)"""
        codes = ['99999', '10803']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0044_Invalid_mixed_with_valid_ABCD_10804(self):
        """Invalid mixed with valid (ABCD, 10804) (Difficulty: basic)"""
        codes = ['ABCD', '10804']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0045_Invalid_mixed_with_valid_Z9999_10805(self):
        """Invalid mixed with valid (Z9999, 10805) (Difficulty: basic)"""
        codes = ['Z9999', '10805']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0046_Invalid_mixed_with_valid_X999_10806(self):
        """Invalid mixed with valid (X999, 10806) (Difficulty: basic)"""
        codes = ['X999', '10806']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0047_Invalid_mixed_with_valid_INVALID_10807(self):
        """Invalid mixed with valid (INVALID, 10807) (Difficulty: basic)"""
        codes = ['INVALID', '10807']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0048_Invalid_mixed_with_valid_99999_10808(self):
        """Invalid mixed with valid (99999, 10808) (Difficulty: basic)"""
        codes = ['99999', '10808']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0049_Invalid_mixed_with_valid_ABCD_10809(self):
        """Invalid mixed with valid (ABCD, 10809) (Difficulty: basic)"""
        codes = ['ABCD', '10809']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0050_Invalid_mixed_with_valid_Z9999_10816(self):
        """Invalid mixed with valid (Z9999, 10816) (Difficulty: basic)"""
        codes = ['Z9999', '10816']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0051_Invalid_mixed_with_valid_X999_109(self):
        """Invalid mixed with valid (X999, 109) (Difficulty: basic)"""
        codes = ['X999', '109']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0052_Invalid_mixed_with_valid_INVALID_10905(self):
        """Invalid mixed with valid (INVALID, 10905) (Difficulty: basic)"""
        codes = ['INVALID', '10905']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0053_Invalid_mixed_with_valid_99999_10907(self):
        """Invalid mixed with valid (99999, 10907) (Difficulty: basic)"""
        codes = ['99999', '10907']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0054_Invalid_mixed_with_valid_ABCD_10910(self):
        """Invalid mixed with valid (ABCD, 10910) (Difficulty: basic)"""
        codes = ['ABCD', '10910']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0055_Invalid_mixed_with_valid_Z9999_10911(self):
        """Invalid mixed with valid (Z9999, 10911) (Difficulty: basic)"""
        codes = ['Z9999', '10911']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0056_Empty_codes_array(self):
        """Empty codes array (Difficulty: basic)"""
        codes = []
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0057_Whitespace_only_codes(self):
        """Whitespace-only codes (Difficulty: edge_case)"""
        codes = ['   ', '  ', '']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0058_Invalid_numeric_code_999999(self):
        """Invalid numeric code 999999 (Difficulty: edge_case)"""
        codes = ['999999']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0059_Invalid_numeric_code_1000000(self):
        """Invalid numeric code 1000000 (Difficulty: edge_case)"""
        codes = ['1000000']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0060_Invalid_numeric_code_1000001(self):
        """Invalid numeric code 1000001 (Difficulty: edge_case)"""
        codes = ['1000001']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0061_Invalid_numeric_code_1000002(self):
        """Invalid numeric code 1000002 (Difficulty: edge_case)"""
        codes = ['1000002']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0062_Invalid_numeric_code_1000003(self):
        """Invalid numeric code 1000003 (Difficulty: edge_case)"""
        codes = ['1000003']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0063_Invalid_numeric_code_1000004(self):
        """Invalid numeric code 1000004 (Difficulty: edge_case)"""
        codes = ['1000004']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0064_Invalid_numeric_code_1000005(self):
        """Invalid numeric code 1000005 (Difficulty: edge_case)"""
        codes = ['1000005']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0065_Invalid_numeric_code_1000006(self):
        """Invalid numeric code 1000006 (Difficulty: edge_case)"""
        codes = ['1000006']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0066_Invalid_numeric_code_1000007(self):
        """Invalid numeric code 1000007 (Difficulty: edge_case)"""
        codes = ['1000007']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0067_Invalid_numeric_code_1000008(self):
        """Invalid numeric code 1000008 (Difficulty: edge_case)"""
        codes = ['1000008']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0068_Invalid_numeric_code_1000009(self):
        """Invalid numeric code 1000009 (Difficulty: edge_case)"""
        codes = ['1000009']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0069_Invalid_numeric_code_1000010(self):
        """Invalid numeric code 1000010 (Difficulty: edge_case)"""
        codes = ['1000010']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0070_Invalid_numeric_code_1000011(self):
        """Invalid numeric code 1000011 (Difficulty: edge_case)"""
        codes = ['1000011']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0071_Invalid_numeric_code_1000012(self):
        """Invalid numeric code 1000012 (Difficulty: edge_case)"""
        codes = ['1000012']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0072_Invalid_numeric_code_1000013(self):
        """Invalid numeric code 1000013 (Difficulty: edge_case)"""
        codes = ['1000013']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0073_Invalid_numeric_code_1000014(self):
        """Invalid numeric code 1000014 (Difficulty: edge_case)"""
        codes = ['1000014']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0074_Invalid_numeric_code_1000015(self):
        """Invalid numeric code 1000015 (Difficulty: edge_case)"""
        codes = ['1000015']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0075_Invalid_numeric_code_1000016(self):
        """Invalid numeric code 1000016 (Difficulty: edge_case)"""
        codes = ['1000016']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0076_Invalid_numeric_code_1000017(self):
        """Invalid numeric code 1000017 (Difficulty: edge_case)"""
        codes = ['1000017']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0077_Invalid_numeric_code_1000018(self):
        """Invalid numeric code 1000018 (Difficulty: edge_case)"""
        codes = ['1000018']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0078_Invalid_numeric_code_1000019(self):
        """Invalid numeric code 1000019 (Difficulty: edge_case)"""
        codes = ['1000019']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0079_Invalid_numeric_code_1000020(self):
        """Invalid numeric code 1000020 (Difficulty: edge_case)"""
        codes = ['1000020']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0080_Invalid_numeric_code_1000021(self):
        """Invalid numeric code 1000021 (Difficulty: edge_case)"""
        codes = ['1000021']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0081_Invalid_numeric_code_1000022(self):
        """Invalid numeric code 1000022 (Difficulty: edge_case)"""
        codes = ['1000022']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0082_Invalid_numeric_code_1000023(self):
        """Invalid numeric code 1000023 (Difficulty: edge_case)"""
        codes = ['1000023']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0083_Invalid_numeric_code_1000024(self):
        """Invalid numeric code 1000024 (Difficulty: edge_case)"""
        codes = ['1000024']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0084_Invalid_numeric_code_1000025(self):
        """Invalid numeric code 1000025 (Difficulty: edge_case)"""
        codes = ['1000025']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0085_Invalid_numeric_code_1000026(self):
        """Invalid numeric code 1000026 (Difficulty: edge_case)"""
        codes = ['1000026']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0086_Invalid_numeric_code_1000027(self):
        """Invalid numeric code 1000027 (Difficulty: edge_case)"""
        codes = ['1000027']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0087_Invalid_numeric_code_1000028(self):
        """Invalid numeric code 1000028 (Difficulty: edge_case)"""
        codes = ['1000028']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0088_Invalid_numeric_code_1000029(self):
        """Invalid numeric code 1000029 (Difficulty: edge_case)"""
        codes = ['1000029']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0089_Invalid_numeric_code_1000030(self):
        """Invalid numeric code 1000030 (Difficulty: edge_case)"""
        codes = ['1000030']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0090_Invalid_numeric_code_1000031(self):
        """Invalid numeric code 1000031 (Difficulty: edge_case)"""
        codes = ['1000031']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0091_Invalid_numeric_code_1000032(self):
        """Invalid numeric code 1000032 (Difficulty: edge_case)"""
        codes = ['1000032']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0092_Invalid_numeric_code_1000033(self):
        """Invalid numeric code 1000033 (Difficulty: edge_case)"""
        codes = ['1000033']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0093_Invalid_numeric_code_1000034(self):
        """Invalid numeric code 1000034 (Difficulty: edge_case)"""
        codes = ['1000034']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0094_Invalid_numeric_code_1000035(self):
        """Invalid numeric code 1000035 (Difficulty: edge_case)"""
        codes = ['1000035']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0095_Invalid_numeric_code_1000036(self):
        """Invalid numeric code 1000036 (Difficulty: edge_case)"""
        codes = ['1000036']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0096_Invalid_numeric_code_1000037(self):
        """Invalid numeric code 1000037 (Difficulty: edge_case)"""
        codes = ['1000037']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0097_Invalid_numeric_code_1000038(self):
        """Invalid numeric code 1000038 (Difficulty: edge_case)"""
        codes = ['1000038']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0098_Invalid_numeric_code_1000039(self):
        """Invalid numeric code 1000039 (Difficulty: edge_case)"""
        codes = ['1000039']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0099_Invalid_numeric_code_1000040(self):
        """Invalid numeric code 1000040 (Difficulty: edge_case)"""
        codes = ['1000040']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        
    def test_p1_0100_Invalid_numeric_code_1000041(self):
        """Invalid numeric code 1000041 (Difficulty: edge_case)"""
        codes = ['1000041']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'P1', \
            f"Expected failed_check 'P1', got {result['failed_check']}"
        

    # ===== C1 Tests (300 tests) =====

    def test_c1_0101_Group_conflict___A1_3_and_4(self):
        """Group conflict - A1 (3 and 4) (Difficulty: moderate)"""
        codes = ['3', '4']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0102_Group_conflict___A1_3_and_23(self):
        """Group conflict - A1 (3 and 23) (Difficulty: moderate)"""
        codes = ['3', '23']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0103_Group_conflict___A1_3_and_24(self):
        """Group conflict - A1 (3 and 24) (Difficulty: moderate)"""
        codes = ['3', '24']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0104_Group_conflict___A1_3_and_37(self):
        """Group conflict - A1 (3 and 37) (Difficulty: moderate)"""
        codes = ['3', '37']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0105_Group_conflict___A1_3_and_47(self):
        """Group conflict - A1 (3 and 47) (Difficulty: moderate)"""
        codes = ['3', '47']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0106_Group_conflict___A1_3_and_123(self):
        """Group conflict - A1 (3 and 123) (Difficulty: moderate)"""
        codes = ['3', '123']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0107_Group_conflict___A1_3_and_124(self):
        """Group conflict - A1 (3 and 124) (Difficulty: moderate)"""
        codes = ['3', '124']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0108_Group_conflict___A1_4_and_23(self):
        """Group conflict - A1 (4 and 23) (Difficulty: moderate)"""
        codes = ['4', '23']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0109_Group_conflict___A1_4_and_24(self):
        """Group conflict - A1 (4 and 24) (Difficulty: moderate)"""
        codes = ['4', '24']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0110_Group_conflict___A1_4_and_37(self):
        """Group conflict - A1 (4 and 37) (Difficulty: moderate)"""
        codes = ['4', '37']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0111_Group_conflict___A1_4_and_47(self):
        """Group conflict - A1 (4 and 47) (Difficulty: moderate)"""
        codes = ['4', '47']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0112_Group_conflict___A1_4_and_123(self):
        """Group conflict - A1 (4 and 123) (Difficulty: moderate)"""
        codes = ['4', '123']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0113_Group_conflict___A1_4_and_124(self):
        """Group conflict - A1 (4 and 124) (Difficulty: moderate)"""
        codes = ['4', '124']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0114_Group_conflict___A1_23_and_24(self):
        """Group conflict - A1 (23 and 24) (Difficulty: moderate)"""
        codes = ['23', '24']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0115_Group_conflict___A1_23_and_37(self):
        """Group conflict - A1 (23 and 37) (Difficulty: moderate)"""
        codes = ['23', '37']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0116_Group_conflict___A1_23_and_47(self):
        """Group conflict - A1 (23 and 47) (Difficulty: moderate)"""
        codes = ['23', '47']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0117_Group_conflict___A1_23_and_123(self):
        """Group conflict - A1 (23 and 123) (Difficulty: moderate)"""
        codes = ['23', '123']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0118_Group_conflict___A1_23_and_124(self):
        """Group conflict - A1 (23 and 124) (Difficulty: moderate)"""
        codes = ['23', '124']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0119_Group_conflict___A1_24_and_37(self):
        """Group conflict - A1 (24 and 37) (Difficulty: moderate)"""
        codes = ['24', '37']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0120_Group_conflict___A1_24_and_47(self):
        """Group conflict - A1 (24 and 47) (Difficulty: moderate)"""
        codes = ['24', '47']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0121_Group_conflict___A1_24_and_123(self):
        """Group conflict - A1 (24 and 123) (Difficulty: moderate)"""
        codes = ['24', '123']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0122_Group_conflict___A1_24_and_124(self):
        """Group conflict - A1 (24 and 124) (Difficulty: moderate)"""
        codes = ['24', '124']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0123_Group_conflict___A1_37_and_47(self):
        """Group conflict - A1 (37 and 47) (Difficulty: moderate)"""
        codes = ['37', '47']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0124_Group_conflict___A1_37_and_123(self):
        """Group conflict - A1 (37 and 123) (Difficulty: moderate)"""
        codes = ['37', '123']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0125_Group_conflict___A1_37_and_124(self):
        """Group conflict - A1 (37 and 124) (Difficulty: moderate)"""
        codes = ['37', '124']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0126_Group_conflict___A1_47_and_123(self):
        """Group conflict - A1 (47 and 123) (Difficulty: moderate)"""
        codes = ['47', '123']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0127_Group_conflict___A1_47_and_124(self):
        """Group conflict - A1 (47 and 124) (Difficulty: moderate)"""
        codes = ['47', '124']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0128_Group_conflict___A1_123_and_124(self):
        """Group conflict - A1 (123 and 124) (Difficulty: moderate)"""
        codes = ['123', '124']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0129_Group_conflict___A10_10905_and_10907(self):
        """Group conflict - A10 (10905 and 10907) (Difficulty: moderate)"""
        codes = ['10905', '10907']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0130_Group_conflict___A10_10905_and_10910(self):
        """Group conflict - A10 (10905 and 10910) (Difficulty: moderate)"""
        codes = ['10905', '10910']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0131_Group_conflict___A10_10905_and_10911(self):
        """Group conflict - A10 (10905 and 10911) (Difficulty: moderate)"""
        codes = ['10905', '10911']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0132_Group_conflict___A10_10905_and_10913(self):
        """Group conflict - A10 (10905 and 10913) (Difficulty: moderate)"""
        codes = ['10905', '10913']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0133_Group_conflict___A10_10905_and_10914(self):
        """Group conflict - A10 (10905 and 10914) (Difficulty: moderate)"""
        codes = ['10905', '10914']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0134_Group_conflict___A10_10905_and_10915(self):
        """Group conflict - A10 (10905 and 10915) (Difficulty: moderate)"""
        codes = ['10905', '10915']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0135_Group_conflict___A10_10905_and_10916(self):
        """Group conflict - A10 (10905 and 10916) (Difficulty: moderate)"""
        codes = ['10905', '10916']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0136_Group_conflict___A10_10905_and_10918(self):
        """Group conflict - A10 (10905 and 10918) (Difficulty: moderate)"""
        codes = ['10905', '10918']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0137_Group_conflict___A10_10905_and_10921(self):
        """Group conflict - A10 (10905 and 10921) (Difficulty: moderate)"""
        codes = ['10905', '10921']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0138_Group_conflict___A10_10905_and_10924(self):
        """Group conflict - A10 (10905 and 10924) (Difficulty: moderate)"""
        codes = ['10905', '10924']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0139_Group_conflict___A10_10905_and_10926(self):
        """Group conflict - A10 (10905 and 10926) (Difficulty: moderate)"""
        codes = ['10905', '10926']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0140_Group_conflict___A10_10905_and_10927(self):
        """Group conflict - A10 (10905 and 10927) (Difficulty: moderate)"""
        codes = ['10905', '10927']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0141_Group_conflict___A10_10905_and_10928(self):
        """Group conflict - A10 (10905 and 10928) (Difficulty: moderate)"""
        codes = ['10905', '10928']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0142_Group_conflict___A10_10905_and_10929(self):
        """Group conflict - A10 (10905 and 10929) (Difficulty: moderate)"""
        codes = ['10905', '10929']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0143_Group_conflict___A10_10905_and_10930(self):
        """Group conflict - A10 (10905 and 10930) (Difficulty: moderate)"""
        codes = ['10905', '10930']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0144_Group_conflict___A10_10905_and_10931(self):
        """Group conflict - A10 (10905 and 10931) (Difficulty: moderate)"""
        codes = ['10905', '10931']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0145_Group_conflict___A10_10905_and_10938(self):
        """Group conflict - A10 (10905 and 10938) (Difficulty: moderate)"""
        codes = ['10905', '10938']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0146_Group_conflict___A10_10905_and_10939(self):
        """Group conflict - A10 (10905 and 10939) (Difficulty: moderate)"""
        codes = ['10905', '10939']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0147_Group_conflict___A10_10905_and_10940(self):
        """Group conflict - A10 (10905 and 10940) (Difficulty: moderate)"""
        codes = ['10905', '10940']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0148_Group_conflict___A10_10905_and_10941(self):
        """Group conflict - A10 (10905 and 10941) (Difficulty: moderate)"""
        codes = ['10905', '10941']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0149_Group_conflict___A10_10905_and_10942(self):
        """Group conflict - A10 (10905 and 10942) (Difficulty: moderate)"""
        codes = ['10905', '10942']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0150_Group_conflict___A10_10905_and_10943(self):
        """Group conflict - A10 (10905 and 10943) (Difficulty: moderate)"""
        codes = ['10905', '10943']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0151_Group_conflict___A10_10905_and_10944(self):
        """Group conflict - A10 (10905 and 10944) (Difficulty: moderate)"""
        codes = ['10905', '10944']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0152_Group_conflict___A10_10905_and_10945(self):
        """Group conflict - A10 (10905 and 10945) (Difficulty: moderate)"""
        codes = ['10905', '10945']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0153_Group_conflict___A10_10905_and_10946(self):
        """Group conflict - A10 (10905 and 10946) (Difficulty: moderate)"""
        codes = ['10905', '10946']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0154_Group_conflict___A10_10907_and_10910(self):
        """Group conflict - A10 (10907 and 10910) (Difficulty: moderate)"""
        codes = ['10907', '10910']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0155_Group_conflict___A10_10907_and_10911(self):
        """Group conflict - A10 (10907 and 10911) (Difficulty: moderate)"""
        codes = ['10907', '10911']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0156_Group_conflict___A10_10907_and_10913(self):
        """Group conflict - A10 (10907 and 10913) (Difficulty: moderate)"""
        codes = ['10907', '10913']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0157_Group_conflict___A10_10907_and_10914(self):
        """Group conflict - A10 (10907 and 10914) (Difficulty: moderate)"""
        codes = ['10907', '10914']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0158_Group_conflict___A10_10907_and_10915(self):
        """Group conflict - A10 (10907 and 10915) (Difficulty: moderate)"""
        codes = ['10907', '10915']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0159_Group_conflict___A10_10907_and_10916(self):
        """Group conflict - A10 (10907 and 10916) (Difficulty: moderate)"""
        codes = ['10907', '10916']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0160_Group_conflict___A10_10907_and_10918(self):
        """Group conflict - A10 (10907 and 10918) (Difficulty: moderate)"""
        codes = ['10907', '10918']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0161_Group_conflict___A10_10907_and_10921(self):
        """Group conflict - A10 (10907 and 10921) (Difficulty: moderate)"""
        codes = ['10907', '10921']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0162_Group_conflict___A10_10907_and_10924(self):
        """Group conflict - A10 (10907 and 10924) (Difficulty: moderate)"""
        codes = ['10907', '10924']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0163_Group_conflict___A10_10907_and_10926(self):
        """Group conflict - A10 (10907 and 10926) (Difficulty: moderate)"""
        codes = ['10907', '10926']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0164_Group_conflict___A10_10907_and_10927(self):
        """Group conflict - A10 (10907 and 10927) (Difficulty: moderate)"""
        codes = ['10907', '10927']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0165_Group_conflict___A10_10907_and_10928(self):
        """Group conflict - A10 (10907 and 10928) (Difficulty: moderate)"""
        codes = ['10907', '10928']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0166_Group_conflict___A10_10907_and_10929(self):
        """Group conflict - A10 (10907 and 10929) (Difficulty: moderate)"""
        codes = ['10907', '10929']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0167_Group_conflict___A10_10907_and_10930(self):
        """Group conflict - A10 (10907 and 10930) (Difficulty: moderate)"""
        codes = ['10907', '10930']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0168_Group_conflict___A10_10907_and_10931(self):
        """Group conflict - A10 (10907 and 10931) (Difficulty: moderate)"""
        codes = ['10907', '10931']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0169_Group_conflict___A10_10907_and_10938(self):
        """Group conflict - A10 (10907 and 10938) (Difficulty: moderate)"""
        codes = ['10907', '10938']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0170_Group_conflict___A10_10907_and_10939(self):
        """Group conflict - A10 (10907 and 10939) (Difficulty: moderate)"""
        codes = ['10907', '10939']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0171_Group_conflict___A10_10907_and_10940(self):
        """Group conflict - A10 (10907 and 10940) (Difficulty: moderate)"""
        codes = ['10907', '10940']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0172_Group_conflict___A10_10907_and_10941(self):
        """Group conflict - A10 (10907 and 10941) (Difficulty: moderate)"""
        codes = ['10907', '10941']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0173_Group_conflict___A10_10907_and_10942(self):
        """Group conflict - A10 (10907 and 10942) (Difficulty: moderate)"""
        codes = ['10907', '10942']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0174_Group_conflict___A10_10907_and_10943(self):
        """Group conflict - A10 (10907 and 10943) (Difficulty: moderate)"""
        codes = ['10907', '10943']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0175_Group_conflict___A10_10907_and_10944(self):
        """Group conflict - A10 (10907 and 10944) (Difficulty: moderate)"""
        codes = ['10907', '10944']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0176_Group_conflict___A10_10907_and_10945(self):
        """Group conflict - A10 (10907 and 10945) (Difficulty: moderate)"""
        codes = ['10907', '10945']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0177_Group_conflict___A10_10907_and_10946(self):
        """Group conflict - A10 (10907 and 10946) (Difficulty: moderate)"""
        codes = ['10907', '10946']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0178_Group_conflict___A10_10910_and_10911(self):
        """Group conflict - A10 (10910 and 10911) (Difficulty: moderate)"""
        codes = ['10910', '10911']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0179_Group_conflict___A10_10910_and_10913(self):
        """Group conflict - A10 (10910 and 10913) (Difficulty: moderate)"""
        codes = ['10910', '10913']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0180_Group_conflict___A10_10910_and_10914(self):
        """Group conflict - A10 (10910 and 10914) (Difficulty: moderate)"""
        codes = ['10910', '10914']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0181_Group_conflict___A10_10910_and_10915(self):
        """Group conflict - A10 (10910 and 10915) (Difficulty: moderate)"""
        codes = ['10910', '10915']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0182_Group_conflict___A10_10910_and_10916(self):
        """Group conflict - A10 (10910 and 10916) (Difficulty: moderate)"""
        codes = ['10910', '10916']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0183_Group_conflict___A10_10910_and_10918(self):
        """Group conflict - A10 (10910 and 10918) (Difficulty: moderate)"""
        codes = ['10910', '10918']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0184_Group_conflict___A10_10910_and_10921(self):
        """Group conflict - A10 (10910 and 10921) (Difficulty: moderate)"""
        codes = ['10910', '10921']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0185_Group_conflict___A10_10910_and_10924(self):
        """Group conflict - A10 (10910 and 10924) (Difficulty: moderate)"""
        codes = ['10910', '10924']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0186_Group_conflict___A10_10910_and_10926(self):
        """Group conflict - A10 (10910 and 10926) (Difficulty: moderate)"""
        codes = ['10910', '10926']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0187_Group_conflict___A10_10910_and_10927(self):
        """Group conflict - A10 (10910 and 10927) (Difficulty: moderate)"""
        codes = ['10910', '10927']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0188_Group_conflict___A10_10910_and_10928(self):
        """Group conflict - A10 (10910 and 10928) (Difficulty: moderate)"""
        codes = ['10910', '10928']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0189_Group_conflict___A10_10910_and_10929(self):
        """Group conflict - A10 (10910 and 10929) (Difficulty: moderate)"""
        codes = ['10910', '10929']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0190_Group_conflict___A10_10910_and_10930(self):
        """Group conflict - A10 (10910 and 10930) (Difficulty: moderate)"""
        codes = ['10910', '10930']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0191_Group_conflict___A10_10910_and_10931(self):
        """Group conflict - A10 (10910 and 10931) (Difficulty: moderate)"""
        codes = ['10910', '10931']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0192_Group_conflict___A10_10910_and_10938(self):
        """Group conflict - A10 (10910 and 10938) (Difficulty: moderate)"""
        codes = ['10910', '10938']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0193_Group_conflict___A10_10910_and_10939(self):
        """Group conflict - A10 (10910 and 10939) (Difficulty: moderate)"""
        codes = ['10910', '10939']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0194_Group_conflict___A10_10910_and_10940(self):
        """Group conflict - A10 (10910 and 10940) (Difficulty: moderate)"""
        codes = ['10910', '10940']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0195_Group_conflict___A10_10910_and_10941(self):
        """Group conflict - A10 (10910 and 10941) (Difficulty: moderate)"""
        codes = ['10910', '10941']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0196_Group_conflict___A10_10910_and_10942(self):
        """Group conflict - A10 (10910 and 10942) (Difficulty: moderate)"""
        codes = ['10910', '10942']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0197_Group_conflict___A10_10910_and_10943(self):
        """Group conflict - A10 (10910 and 10943) (Difficulty: moderate)"""
        codes = ['10910', '10943']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0198_Group_conflict___A10_10910_and_10944(self):
        """Group conflict - A10 (10910 and 10944) (Difficulty: moderate)"""
        codes = ['10910', '10944']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0199_Group_conflict___A10_10910_and_10945(self):
        """Group conflict - A10 (10910 and 10945) (Difficulty: moderate)"""
        codes = ['10910', '10945']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0200_Group_conflict___A10_10910_and_10946(self):
        """Group conflict - A10 (10910 and 10946) (Difficulty: moderate)"""
        codes = ['10910', '10946']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0201_Group_conflict___A10_10911_and_10913(self):
        """Group conflict - A10 (10911 and 10913) (Difficulty: moderate)"""
        codes = ['10911', '10913']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0202_Group_conflict___A10_10911_and_10914(self):
        """Group conflict - A10 (10911 and 10914) (Difficulty: moderate)"""
        codes = ['10911', '10914']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0203_Group_conflict___A10_10911_and_10915(self):
        """Group conflict - A10 (10911 and 10915) (Difficulty: moderate)"""
        codes = ['10911', '10915']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0204_Group_conflict___A10_10911_and_10916(self):
        """Group conflict - A10 (10911 and 10916) (Difficulty: moderate)"""
        codes = ['10911', '10916']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0205_Group_conflict___A10_10911_and_10918(self):
        """Group conflict - A10 (10911 and 10918) (Difficulty: moderate)"""
        codes = ['10911', '10918']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0206_Group_conflict___A10_10911_and_10921(self):
        """Group conflict - A10 (10911 and 10921) (Difficulty: moderate)"""
        codes = ['10911', '10921']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0207_Group_conflict___A10_10911_and_10924(self):
        """Group conflict - A10 (10911 and 10924) (Difficulty: moderate)"""
        codes = ['10911', '10924']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0208_Group_conflict___A10_10911_and_10926(self):
        """Group conflict - A10 (10911 and 10926) (Difficulty: moderate)"""
        codes = ['10911', '10926']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0209_Group_conflict___A10_10911_and_10927(self):
        """Group conflict - A10 (10911 and 10927) (Difficulty: moderate)"""
        codes = ['10911', '10927']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0210_Group_conflict___A10_10911_and_10928(self):
        """Group conflict - A10 (10911 and 10928) (Difficulty: moderate)"""
        codes = ['10911', '10928']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0211_Group_conflict___A10_10911_and_10929(self):
        """Group conflict - A10 (10911 and 10929) (Difficulty: moderate)"""
        codes = ['10911', '10929']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0212_Group_conflict___A10_10911_and_10930(self):
        """Group conflict - A10 (10911 and 10930) (Difficulty: moderate)"""
        codes = ['10911', '10930']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0213_Group_conflict___A10_10911_and_10931(self):
        """Group conflict - A10 (10911 and 10931) (Difficulty: moderate)"""
        codes = ['10911', '10931']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0214_Group_conflict___A10_10911_and_10938(self):
        """Group conflict - A10 (10911 and 10938) (Difficulty: moderate)"""
        codes = ['10911', '10938']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0215_Group_conflict___A10_10911_and_10939(self):
        """Group conflict - A10 (10911 and 10939) (Difficulty: moderate)"""
        codes = ['10911', '10939']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0216_Group_conflict___A10_10911_and_10940(self):
        """Group conflict - A10 (10911 and 10940) (Difficulty: moderate)"""
        codes = ['10911', '10940']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0217_Group_conflict___A10_10911_and_10941(self):
        """Group conflict - A10 (10911 and 10941) (Difficulty: moderate)"""
        codes = ['10911', '10941']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0218_Group_conflict___A10_10911_and_10942(self):
        """Group conflict - A10 (10911 and 10942) (Difficulty: moderate)"""
        codes = ['10911', '10942']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0219_Group_conflict___A10_10911_and_10943(self):
        """Group conflict - A10 (10911 and 10943) (Difficulty: moderate)"""
        codes = ['10911', '10943']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0220_Group_conflict___A10_10911_and_10944(self):
        """Group conflict - A10 (10911 and 10944) (Difficulty: moderate)"""
        codes = ['10911', '10944']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0221_Group_conflict___A10_10911_and_10945(self):
        """Group conflict - A10 (10911 and 10945) (Difficulty: moderate)"""
        codes = ['10911', '10945']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0222_Group_conflict___A10_10911_and_10946(self):
        """Group conflict - A10 (10911 and 10946) (Difficulty: moderate)"""
        codes = ['10911', '10946']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0223_Group_conflict___A10_10913_and_10914(self):
        """Group conflict - A10 (10913 and 10914) (Difficulty: moderate)"""
        codes = ['10913', '10914']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0224_Group_conflict___A10_10913_and_10915(self):
        """Group conflict - A10 (10913 and 10915) (Difficulty: moderate)"""
        codes = ['10913', '10915']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0225_Group_conflict___A10_10913_and_10916(self):
        """Group conflict - A10 (10913 and 10916) (Difficulty: moderate)"""
        codes = ['10913', '10916']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0226_Group_conflict___A10_10913_and_10918(self):
        """Group conflict - A10 (10913 and 10918) (Difficulty: moderate)"""
        codes = ['10913', '10918']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0227_Group_conflict___A10_10913_and_10921(self):
        """Group conflict - A10 (10913 and 10921) (Difficulty: moderate)"""
        codes = ['10913', '10921']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0228_Group_conflict___A10_10913_and_10924(self):
        """Group conflict - A10 (10913 and 10924) (Difficulty: moderate)"""
        codes = ['10913', '10924']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0229_Group_conflict___A10_10913_and_10926(self):
        """Group conflict - A10 (10913 and 10926) (Difficulty: moderate)"""
        codes = ['10913', '10926']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0230_Group_conflict___A10_10913_and_10927(self):
        """Group conflict - A10 (10913 and 10927) (Difficulty: moderate)"""
        codes = ['10913', '10927']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0231_Group_conflict___A10_10913_and_10928(self):
        """Group conflict - A10 (10913 and 10928) (Difficulty: moderate)"""
        codes = ['10913', '10928']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0232_Group_conflict___A10_10913_and_10929(self):
        """Group conflict - A10 (10913 and 10929) (Difficulty: moderate)"""
        codes = ['10913', '10929']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0233_Group_conflict___A10_10913_and_10930(self):
        """Group conflict - A10 (10913 and 10930) (Difficulty: moderate)"""
        codes = ['10913', '10930']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0234_Group_conflict___A10_10913_and_10931(self):
        """Group conflict - A10 (10913 and 10931) (Difficulty: moderate)"""
        codes = ['10913', '10931']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0235_Group_conflict___A10_10913_and_10938(self):
        """Group conflict - A10 (10913 and 10938) (Difficulty: moderate)"""
        codes = ['10913', '10938']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0236_Group_conflict___A10_10913_and_10939(self):
        """Group conflict - A10 (10913 and 10939) (Difficulty: moderate)"""
        codes = ['10913', '10939']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0237_Group_conflict___A10_10913_and_10940(self):
        """Group conflict - A10 (10913 and 10940) (Difficulty: moderate)"""
        codes = ['10913', '10940']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0238_Group_conflict___A10_10913_and_10941(self):
        """Group conflict - A10 (10913 and 10941) (Difficulty: moderate)"""
        codes = ['10913', '10941']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0239_Group_conflict___A10_10913_and_10942(self):
        """Group conflict - A10 (10913 and 10942) (Difficulty: moderate)"""
        codes = ['10913', '10942']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0240_Group_conflict___A10_10913_and_10943(self):
        """Group conflict - A10 (10913 and 10943) (Difficulty: moderate)"""
        codes = ['10913', '10943']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0241_Group_conflict___A10_10913_and_10944(self):
        """Group conflict - A10 (10913 and 10944) (Difficulty: moderate)"""
        codes = ['10913', '10944']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0242_Group_conflict___A10_10913_and_10945(self):
        """Group conflict - A10 (10913 and 10945) (Difficulty: moderate)"""
        codes = ['10913', '10945']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0243_Group_conflict___A10_10913_and_10946(self):
        """Group conflict - A10 (10913 and 10946) (Difficulty: moderate)"""
        codes = ['10913', '10946']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0244_Group_conflict___A10_10914_and_10915(self):
        """Group conflict - A10 (10914 and 10915) (Difficulty: moderate)"""
        codes = ['10914', '10915']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0245_Group_conflict___A10_10914_and_10916(self):
        """Group conflict - A10 (10914 and 10916) (Difficulty: moderate)"""
        codes = ['10914', '10916']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0246_Group_conflict___A10_10914_and_10918(self):
        """Group conflict - A10 (10914 and 10918) (Difficulty: moderate)"""
        codes = ['10914', '10918']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0247_Group_conflict___A10_10914_and_10921(self):
        """Group conflict - A10 (10914 and 10921) (Difficulty: moderate)"""
        codes = ['10914', '10921']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0248_Group_conflict___A10_10914_and_10924(self):
        """Group conflict - A10 (10914 and 10924) (Difficulty: moderate)"""
        codes = ['10914', '10924']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0249_Group_conflict___A10_10914_and_10926(self):
        """Group conflict - A10 (10914 and 10926) (Difficulty: moderate)"""
        codes = ['10914', '10926']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0250_Group_conflict___A10_10914_and_10927(self):
        """Group conflict - A10 (10914 and 10927) (Difficulty: moderate)"""
        codes = ['10914', '10927']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0251_Group_conflict___A1_3_codes(self):
        """Group conflict - A1 (3 codes) (Difficulty: moderate)"""
        codes = ['3', '4', '23']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0252_Group_conflict___A1_4_codes(self):
        """Group conflict - A1 (4 codes) (Difficulty: moderate)"""
        codes = ['3', '4', '23', '24']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0253_Group_conflict___A1_5_codes(self):
        """Group conflict - A1 (5 codes) (Difficulty: moderate)"""
        codes = ['3', '4', '23', '24', '37']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0254_Group_conflict___A10_3_codes(self):
        """Group conflict - A10 (3 codes) (Difficulty: moderate)"""
        codes = ['10905', '10907', '10910']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0255_Group_conflict___A10_4_codes(self):
        """Group conflict - A10 (4 codes) (Difficulty: moderate)"""
        codes = ['10905', '10907', '10910', '10911']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0256_Group_conflict___A10_5_codes(self):
        """Group conflict - A10 (5 codes) (Difficulty: moderate)"""
        codes = ['10905', '10907', '10910', '10911', '10913']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0257_Group_conflict___A11_3_codes(self):
        """Group conflict - A11 (3 codes) (Difficulty: moderate)"""
        codes = ['585', '588', '591']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0258_Group_conflict___A11_4_codes(self):
        """Group conflict - A11 (4 codes) (Difficulty: moderate)"""
        codes = ['585', '588', '591', '594']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0259_Group_conflict___A11_5_codes(self):
        """Group conflict - A11 (5 codes) (Difficulty: moderate)"""
        codes = ['585', '588', '591', '594', '599']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0260_Group_conflict___A12_3_codes(self):
        """Group conflict - A12 (3 codes) (Difficulty: moderate)"""
        codes = ['385', '386', '387']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0261_Group_conflict___A12_4_codes(self):
        """Group conflict - A12 (4 codes) (Difficulty: moderate)"""
        codes = ['385', '386', '387', '388']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0262_Group_conflict___A13_3_codes(self):
        """Group conflict - A13 (3 codes) (Difficulty: moderate)"""
        codes = ['410', '411', '412']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0263_Group_conflict___A13_4_codes(self):
        """Group conflict - A13 (4 codes) (Difficulty: moderate)"""
        codes = ['410', '411', '412', '413']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0264_Group_conflict___A13_5_codes(self):
        """Group conflict - A13 (5 codes) (Difficulty: moderate)"""
        codes = ['410', '411', '412', '413', '414']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0265_Group_conflict___A14_3_codes(self):
        """Group conflict - A14 (3 codes) (Difficulty: moderate)"""
        codes = ['695', '699', '701']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0266_Group_conflict___A14_4_codes(self):
        """Group conflict - A14 (4 codes) (Difficulty: moderate)"""
        codes = ['695', '699', '701', '703']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0267_Group_conflict___A14_5_codes(self):
        """Group conflict - A14 (5 codes) (Difficulty: moderate)"""
        codes = ['695', '699', '701', '703', '705']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0268_Group_conflict___A15_3_codes(self):
        """Group conflict - A15 (3 codes) (Difficulty: moderate)"""
        codes = ['729', '731', '735']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0269_Group_conflict___A15_4_codes(self):
        """Group conflict - A15 (4 codes) (Difficulty: moderate)"""
        codes = ['729', '731', '735', '739']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0270_Group_conflict___A15_5_codes(self):
        """Group conflict - A15 (5 codes) (Difficulty: moderate)"""
        codes = ['729', '731', '735', '739', '743']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0271_Group_conflict___A2_3_codes(self):
        """Group conflict - A2 (3 codes) (Difficulty: moderate)"""
        codes = ['52', '53', '54']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0272_Group_conflict___A2_4_codes(self):
        """Group conflict - A2 (4 codes) (Difficulty: moderate)"""
        codes = ['52', '53', '54', '57']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0273_Group_conflict___A2_5_codes(self):
        """Group conflict - A2 (5 codes) (Difficulty: moderate)"""
        codes = ['52', '53', '54', '57', '58']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0274_Group_conflict___A20_3_codes(self):
        """Group conflict - A20 (3 codes) (Difficulty: moderate)"""
        codes = ['2700', '2701', '2712']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0275_Group_conflict___A20_4_codes(self):
        """Group conflict - A20 (4 codes) (Difficulty: moderate)"""
        codes = ['2700', '2701', '2712', '2713']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0276_Group_conflict___A20_5_codes(self):
        """Group conflict - A20 (5 codes) (Difficulty: moderate)"""
        codes = ['2700', '2701', '2712', '2713', '2715']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0277_Group_conflict___A21_3_codes(self):
        """Group conflict - A21 (3 codes) (Difficulty: moderate)"""
        codes = ['5001', '5004', '5011']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0278_Group_conflict___A21_4_codes(self):
        """Group conflict - A21 (4 codes) (Difficulty: moderate)"""
        codes = ['5001', '5004', '5011', '5012']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0279_Group_conflict___A21_5_codes(self):
        """Group conflict - A21 (5 codes) (Difficulty: moderate)"""
        codes = ['5001', '5004', '5011', '5012', '5013']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0280_Group_conflict___A22_3_codes(self):
        """Group conflict - A22 (3 codes) (Difficulty: moderate)"""
        codes = ['5000', '5003', '5010']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0281_Group_conflict___A22_4_codes(self):
        """Group conflict - A22 (4 codes) (Difficulty: moderate)"""
        codes = ['5000', '5003', '5010', '5020']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0282_Group_conflict___A22_5_codes(self):
        """Group conflict - A22 (5 codes) (Difficulty: moderate)"""
        codes = ['5000', '5003', '5010', '5020', '5023']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0283_Group_conflict___A23_3_codes(self):
        """Group conflict - A23 (3 codes) (Difficulty: moderate)"""
        codes = ['5200', '5203', '5207']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0284_Group_conflict___A23_4_codes(self):
        """Group conflict - A23 (4 codes) (Difficulty: moderate)"""
        codes = ['5200', '5203', '5207', '5208']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0285_Group_conflict___A23_5_codes(self):
        """Group conflict - A23 (5 codes) (Difficulty: moderate)"""
        codes = ['5200', '5203', '5207', '5208', '5209']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0286_Group_conflict___A24_3_codes(self):
        """Group conflict - A24 (3 codes) (Difficulty: moderate)"""
        codes = ['2801', '2806', '2814']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0287_Group_conflict___A24_4_codes(self):
        """Group conflict - A24 (4 codes) (Difficulty: moderate)"""
        codes = ['2801', '2806', '2814', '2824']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0288_Group_conflict___A24_5_codes(self):
        """Group conflict - A24 (5 codes) (Difficulty: moderate)"""
        codes = ['2801', '2806', '2814', '2824', '2832']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0289_Group_conflict___A26_3_codes(self):
        """Group conflict - A26 (3 codes) (Difficulty: moderate)"""
        codes = ['6007', '6009', '6011']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0290_Group_conflict___A26_4_codes(self):
        """Group conflict - A26 (4 codes) (Difficulty: moderate)"""
        codes = ['6007', '6009', '6011', '6013']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0291_Group_conflict___A26_5_codes(self):
        """Group conflict - A26 (5 codes) (Difficulty: moderate)"""
        codes = ['6007', '6009', '6011', '6013', '6015']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0292_Group_conflict___A28_3_codes(self):
        """Group conflict - A28 (3 codes) (Difficulty: moderate)"""
        codes = ['141', '143', '145']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0293_Group_conflict___A28_4_codes(self):
        """Group conflict - A28 (4 codes) (Difficulty: moderate)"""
        codes = ['141', '143', '145', '147']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0294_Group_conflict___A29_3_codes(self):
        """Group conflict - A29 (3 codes) (Difficulty: moderate)"""
        codes = ['135', '137', '139']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0295_Group_conflict___A3_3_codes(self):
        """Group conflict - A3 (3 codes) (Difficulty: moderate)"""
        codes = ['104', '105', '106']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0296_Group_conflict___A3_4_codes(self):
        """Group conflict - A3 (4 codes) (Difficulty: moderate)"""
        codes = ['104', '105', '106', '107']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0297_Group_conflict___A3_5_codes(self):
        """Group conflict - A3 (5 codes) (Difficulty: moderate)"""
        codes = ['104', '105', '106', '107', '108']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0298_Group_conflict___A31_3_codes(self):
        """Group conflict - A31 (3 codes) (Difficulty: moderate)"""
        codes = ['6018', '6019', '6023']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0299_Group_conflict___A31_4_codes(self):
        """Group conflict - A31 (4 codes) (Difficulty: moderate)"""
        codes = ['6018', '6019', '6023', '6024']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0300_Group_conflict___A31_5_codes(self):
        """Group conflict - A31 (5 codes) (Difficulty: moderate)"""
        codes = ['6018', '6019', '6023', '6024', '6028']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0301_Direct_exclusion_104_excludes_106(self):
        """Direct exclusion (104 excludes 106) (Difficulty: moderate)"""
        codes = ['104', '106']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0302_Direct_exclusion_104_excludes_109(self):
        """Direct exclusion (104 excludes 109) (Difficulty: moderate)"""
        codes = ['104', '109']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0303_Direct_exclusion_104_excludes_125(self):
        """Direct exclusion (104 excludes 125) (Difficulty: moderate)"""
        codes = ['104', '125']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0304_Direct_exclusion_104_excludes_16401(self):
        """Direct exclusion (104 excludes 16401) (Difficulty: moderate)"""
        codes = ['104', '16401']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0305_Direct_exclusion_105_excludes_126(self):
        """Direct exclusion (105 excludes 126) (Difficulty: moderate)"""
        codes = ['105', '126']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0306_Direct_exclusion_105_excludes_16404(self):
        """Direct exclusion (105 excludes 16404) (Difficulty: moderate)"""
        codes = ['105', '16404']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0307_Direct_exclusion_106_excludes_104(self):
        """Direct exclusion (106 excludes 104) (Difficulty: moderate)"""
        codes = ['106', '104']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0308_Direct_exclusion_106_excludes_109(self):
        """Direct exclusion (106 excludes 109) (Difficulty: moderate)"""
        codes = ['106', '109']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0309_Direct_exclusion_106_excludes_10801(self):
        """Direct exclusion (106 excludes 10801) (Difficulty: moderate)"""
        codes = ['106', '10801']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0310_Direct_exclusion_10809_excludes_10806(self):
        """Direct exclusion (10809 excludes 10806) (Difficulty: moderate)"""
        codes = ['10809', '10806']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0311_Direct_exclusion_10809_excludes_10807(self):
        """Direct exclusion (10809 excludes 10807) (Difficulty: moderate)"""
        codes = ['10809', '10807']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0312_Direct_exclusion_10809_excludes_10808(self):
        """Direct exclusion (10809 excludes 10808) (Difficulty: moderate)"""
        codes = ['10809', '10808']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0313_Direct_exclusion_10816_excludes_10801(self):
        """Direct exclusion (10816 excludes 10801) (Difficulty: moderate)"""
        codes = ['10816', '10801']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0314_Direct_exclusion_109_excludes_104(self):
        """Direct exclusion (109 excludes 104) (Difficulty: moderate)"""
        codes = ['109', '104']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0315_Direct_exclusion_109_excludes_106(self):
        """Direct exclusion (109 excludes 106) (Difficulty: moderate)"""
        codes = ['109', '106']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0316_Direct_exclusion_109_excludes_10801(self):
        """Direct exclusion (109 excludes 10801) (Difficulty: moderate)"""
        codes = ['109', '10801']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0317_Direct_exclusion_10907_excludes_10905(self):
        """Direct exclusion (10907 excludes 10905) (Difficulty: moderate)"""
        codes = ['10907', '10905']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0318_Direct_exclusion_10907_excludes_10910(self):
        """Direct exclusion (10907 excludes 10910) (Difficulty: moderate)"""
        codes = ['10907', '10910']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0319_Direct_exclusion_10907_excludes_10911(self):
        """Direct exclusion (10907 excludes 10911) (Difficulty: moderate)"""
        codes = ['10907', '10911']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0320_Direct_exclusion_10907_excludes_10913(self):
        """Direct exclusion (10907 excludes 10913) (Difficulty: moderate)"""
        codes = ['10907', '10913']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0321_Direct_exclusion_10907_excludes_10914(self):
        """Direct exclusion (10907 excludes 10914) (Difficulty: moderate)"""
        codes = ['10907', '10914']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0322_Direct_exclusion_10907_excludes_10915(self):
        """Direct exclusion (10907 excludes 10915) (Difficulty: moderate)"""
        codes = ['10907', '10915']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0323_Direct_exclusion_10910_excludes_10905(self):
        """Direct exclusion (10910 excludes 10905) (Difficulty: moderate)"""
        codes = ['10910', '10905']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0324_Direct_exclusion_10910_excludes_10907(self):
        """Direct exclusion (10910 excludes 10907) (Difficulty: moderate)"""
        codes = ['10910', '10907']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0325_Direct_exclusion_10910_excludes_10913(self):
        """Direct exclusion (10910 excludes 10913) (Difficulty: moderate)"""
        codes = ['10910', '10913']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0326_Direct_exclusion_10910_excludes_10914(self):
        """Direct exclusion (10910 excludes 10914) (Difficulty: moderate)"""
        codes = ['10910', '10914']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0327_Direct_exclusion_10910_excludes_10915(self):
        """Direct exclusion (10910 excludes 10915) (Difficulty: moderate)"""
        codes = ['10910', '10915']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0328_Direct_exclusion_10911_excludes_10905(self):
        """Direct exclusion (10911 excludes 10905) (Difficulty: moderate)"""
        codes = ['10911', '10905']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0329_Direct_exclusion_10911_excludes_10907(self):
        """Direct exclusion (10911 excludes 10907) (Difficulty: moderate)"""
        codes = ['10911', '10907']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0330_Direct_exclusion_10911_excludes_10910(self):
        """Direct exclusion (10911 excludes 10910) (Difficulty: moderate)"""
        codes = ['10911', '10910']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0331_Direct_exclusion_10911_excludes_10913(self):
        """Direct exclusion (10911 excludes 10913) (Difficulty: moderate)"""
        codes = ['10911', '10913']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0332_Direct_exclusion_10911_excludes_10914(self):
        """Direct exclusion (10911 excludes 10914) (Difficulty: moderate)"""
        codes = ['10911', '10914']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0333_Direct_exclusion_10911_excludes_10915(self):
        """Direct exclusion (10911 excludes 10915) (Difficulty: moderate)"""
        codes = ['10911', '10915']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0334_Direct_exclusion_10913_excludes_10905(self):
        """Direct exclusion (10913 excludes 10905) (Difficulty: moderate)"""
        codes = ['10913', '10905']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0335_Direct_exclusion_10913_excludes_10907(self):
        """Direct exclusion (10913 excludes 10907) (Difficulty: moderate)"""
        codes = ['10913', '10907']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0336_Direct_exclusion_10913_excludes_10910(self):
        """Direct exclusion (10913 excludes 10910) (Difficulty: moderate)"""
        codes = ['10913', '10910']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0337_Direct_exclusion_10913_excludes_10914(self):
        """Direct exclusion (10913 excludes 10914) (Difficulty: moderate)"""
        codes = ['10913', '10914']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0338_Direct_exclusion_10913_excludes_10915(self):
        """Direct exclusion (10913 excludes 10915) (Difficulty: moderate)"""
        codes = ['10913', '10915']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0339_Direct_exclusion_10913_excludes_10911(self):
        """Direct exclusion (10913 excludes 10911) (Difficulty: moderate)"""
        codes = ['10913', '10911']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0340_Direct_exclusion_10914_excludes_10905(self):
        """Direct exclusion (10914 excludes 10905) (Difficulty: moderate)"""
        codes = ['10914', '10905']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0341_Direct_exclusion_10914_excludes_10907(self):
        """Direct exclusion (10914 excludes 10907) (Difficulty: moderate)"""
        codes = ['10914', '10907']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0342_Direct_exclusion_10914_excludes_10910(self):
        """Direct exclusion (10914 excludes 10910) (Difficulty: moderate)"""
        codes = ['10914', '10910']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0343_Direct_exclusion_10914_excludes_10913(self):
        """Direct exclusion (10914 excludes 10913) (Difficulty: moderate)"""
        codes = ['10914', '10913']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0344_Direct_exclusion_10914_excludes_10915(self):
        """Direct exclusion (10914 excludes 10915) (Difficulty: moderate)"""
        codes = ['10914', '10915']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0345_Direct_exclusion_10914_excludes_10911(self):
        """Direct exclusion (10914 excludes 10911) (Difficulty: moderate)"""
        codes = ['10914', '10911']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0346_Direct_exclusion_10916_excludes_10938(self):
        """Direct exclusion (10916 excludes 10938) (Difficulty: moderate)"""
        codes = ['10916', '10938']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0347_Direct_exclusion_10916_excludes_10939(self):
        """Direct exclusion (10916 excludes 10939) (Difficulty: moderate)"""
        codes = ['10916', '10939']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0348_Direct_exclusion_10916_excludes_10940(self):
        """Direct exclusion (10916 excludes 10940) (Difficulty: moderate)"""
        codes = ['10916', '10940']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0349_Direct_exclusion_10916_excludes_10941(self):
        """Direct exclusion (10916 excludes 10941) (Difficulty: moderate)"""
        codes = ['10916', '10941']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0350_Direct_exclusion_10916_excludes_10942(self):
        """Direct exclusion (10916 excludes 10942) (Difficulty: moderate)"""
        codes = ['10916', '10942']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0351_Direct_exclusion_10916_excludes_10943(self):
        """Direct exclusion (10916 excludes 10943) (Difficulty: moderate)"""
        codes = ['10916', '10943']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0352_Direct_exclusion_10918_excludes_10938(self):
        """Direct exclusion (10918 excludes 10938) (Difficulty: moderate)"""
        codes = ['10918', '10938']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0353_Direct_exclusion_10918_excludes_10939(self):
        """Direct exclusion (10918 excludes 10939) (Difficulty: moderate)"""
        codes = ['10918', '10939']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0354_Direct_exclusion_10918_excludes_10940(self):
        """Direct exclusion (10918 excludes 10940) (Difficulty: moderate)"""
        codes = ['10918', '10940']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0355_Direct_exclusion_10918_excludes_10941(self):
        """Direct exclusion (10918 excludes 10941) (Difficulty: moderate)"""
        codes = ['10918', '10941']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0356_Direct_exclusion_10921_excludes_10905(self):
        """Direct exclusion (10921 excludes 10905) (Difficulty: moderate)"""
        codes = ['10921', '10905']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0357_Direct_exclusion_10921_excludes_10907(self):
        """Direct exclusion (10921 excludes 10907) (Difficulty: moderate)"""
        codes = ['10921', '10907']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0358_Direct_exclusion_10921_excludes_10910(self):
        """Direct exclusion (10921 excludes 10910) (Difficulty: moderate)"""
        codes = ['10921', '10910']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0359_Direct_exclusion_10921_excludes_10911(self):
        """Direct exclusion (10921 excludes 10911) (Difficulty: moderate)"""
        codes = ['10921', '10911']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0360_Direct_exclusion_10921_excludes_10913(self):
        """Direct exclusion (10921 excludes 10913) (Difficulty: moderate)"""
        codes = ['10921', '10913']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0361_Direct_exclusion_10921_excludes_10914(self):
        """Direct exclusion (10921 excludes 10914) (Difficulty: moderate)"""
        codes = ['10921', '10914']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0362_Direct_exclusion_10921_excludes_10915(self):
        """Direct exclusion (10921 excludes 10915) (Difficulty: moderate)"""
        codes = ['10921', '10915']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0363_Direct_exclusion_10921_excludes_10916(self):
        """Direct exclusion (10921 excludes 10916) (Difficulty: moderate)"""
        codes = ['10921', '10916']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0364_Direct_exclusion_10924_excludes_10905(self):
        """Direct exclusion (10924 excludes 10905) (Difficulty: moderate)"""
        codes = ['10924', '10905']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0365_Direct_exclusion_10924_excludes_10907(self):
        """Direct exclusion (10924 excludes 10907) (Difficulty: moderate)"""
        codes = ['10924', '10907']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0366_Direct_exclusion_10924_excludes_10910(self):
        """Direct exclusion (10924 excludes 10910) (Difficulty: moderate)"""
        codes = ['10924', '10910']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0367_Direct_exclusion_10924_excludes_10911(self):
        """Direct exclusion (10924 excludes 10911) (Difficulty: moderate)"""
        codes = ['10924', '10911']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0368_Direct_exclusion_10924_excludes_10913(self):
        """Direct exclusion (10924 excludes 10913) (Difficulty: moderate)"""
        codes = ['10924', '10913']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0369_Direct_exclusion_10924_excludes_10914(self):
        """Direct exclusion (10924 excludes 10914) (Difficulty: moderate)"""
        codes = ['10924', '10914']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0370_Direct_exclusion_10924_excludes_10915(self):
        """Direct exclusion (10924 excludes 10915) (Difficulty: moderate)"""
        codes = ['10924', '10915']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0371_Direct_exclusion_10924_excludes_10916(self):
        """Direct exclusion (10924 excludes 10916) (Difficulty: moderate)"""
        codes = ['10924', '10916']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0372_Direct_exclusion_10926_excludes_10905(self):
        """Direct exclusion (10926 excludes 10905) (Difficulty: moderate)"""
        codes = ['10926', '10905']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0373_Direct_exclusion_10926_excludes_10907(self):
        """Direct exclusion (10926 excludes 10907) (Difficulty: moderate)"""
        codes = ['10926', '10907']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0374_Direct_exclusion_10926_excludes_10910(self):
        """Direct exclusion (10926 excludes 10910) (Difficulty: moderate)"""
        codes = ['10926', '10910']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0375_Direct_exclusion_10926_excludes_10911(self):
        """Direct exclusion (10926 excludes 10911) (Difficulty: moderate)"""
        codes = ['10926', '10911']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0376_Direct_exclusion_10926_excludes_10913(self):
        """Direct exclusion (10926 excludes 10913) (Difficulty: moderate)"""
        codes = ['10926', '10913']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0377_Direct_exclusion_10926_excludes_10914(self):
        """Direct exclusion (10926 excludes 10914) (Difficulty: moderate)"""
        codes = ['10926', '10914']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0378_Direct_exclusion_10926_excludes_10915(self):
        """Direct exclusion (10926 excludes 10915) (Difficulty: moderate)"""
        codes = ['10926', '10915']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0379_Direct_exclusion_10926_excludes_10916(self):
        """Direct exclusion (10926 excludes 10916) (Difficulty: moderate)"""
        codes = ['10926', '10916']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0380_Direct_exclusion_10927_excludes_10905(self):
        """Direct exclusion (10927 excludes 10905) (Difficulty: moderate)"""
        codes = ['10927', '10905']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0381_Direct_exclusion_10927_excludes_10907(self):
        """Direct exclusion (10927 excludes 10907) (Difficulty: moderate)"""
        codes = ['10927', '10907']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0382_Direct_exclusion_10927_excludes_10910(self):
        """Direct exclusion (10927 excludes 10910) (Difficulty: moderate)"""
        codes = ['10927', '10910']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0383_Direct_exclusion_10927_excludes_10911(self):
        """Direct exclusion (10927 excludes 10911) (Difficulty: moderate)"""
        codes = ['10927', '10911']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0384_Direct_exclusion_10927_excludes_10913(self):
        """Direct exclusion (10927 excludes 10913) (Difficulty: moderate)"""
        codes = ['10927', '10913']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0385_Direct_exclusion_10927_excludes_10914(self):
        """Direct exclusion (10927 excludes 10914) (Difficulty: moderate)"""
        codes = ['10927', '10914']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0386_Direct_exclusion_10927_excludes_10915(self):
        """Direct exclusion (10927 excludes 10915) (Difficulty: moderate)"""
        codes = ['10927', '10915']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0387_Direct_exclusion_10927_excludes_10916(self):
        """Direct exclusion (10927 excludes 10916) (Difficulty: moderate)"""
        codes = ['10927', '10916']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0388_Direct_exclusion_10928_excludes_10905(self):
        """Direct exclusion (10928 excludes 10905) (Difficulty: moderate)"""
        codes = ['10928', '10905']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0389_Direct_exclusion_10928_excludes_10907(self):
        """Direct exclusion (10928 excludes 10907) (Difficulty: moderate)"""
        codes = ['10928', '10907']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0390_Direct_exclusion_10928_excludes_10910(self):
        """Direct exclusion (10928 excludes 10910) (Difficulty: moderate)"""
        codes = ['10928', '10910']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0391_Direct_exclusion_10928_excludes_10911(self):
        """Direct exclusion (10928 excludes 10911) (Difficulty: moderate)"""
        codes = ['10928', '10911']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0392_Direct_exclusion_10928_excludes_10913(self):
        """Direct exclusion (10928 excludes 10913) (Difficulty: moderate)"""
        codes = ['10928', '10913']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0393_Direct_exclusion_10928_excludes_10914(self):
        """Direct exclusion (10928 excludes 10914) (Difficulty: moderate)"""
        codes = ['10928', '10914']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0394_Direct_exclusion_10928_excludes_10915(self):
        """Direct exclusion (10928 excludes 10915) (Difficulty: moderate)"""
        codes = ['10928', '10915']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0395_Direct_exclusion_10928_excludes_10916(self):
        """Direct exclusion (10928 excludes 10916) (Difficulty: moderate)"""
        codes = ['10928', '10916']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0396_Direct_exclusion_10929_excludes_10926(self):
        """Direct exclusion (10929 excludes 10926) (Difficulty: moderate)"""
        codes = ['10929', '10926']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0397_Direct_exclusion_10929_excludes_10927(self):
        """Direct exclusion (10929 excludes 10927) (Difficulty: moderate)"""
        codes = ['10929', '10927']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0398_Direct_exclusion_10929_excludes_10928(self):
        """Direct exclusion (10929 excludes 10928) (Difficulty: moderate)"""
        codes = ['10929', '10928']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0399_Direct_exclusion_10929_excludes_10905(self):
        """Direct exclusion (10929 excludes 10905) (Difficulty: moderate)"""
        codes = ['10929', '10905']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        
    def test_c1_0400_Direct_exclusion_10929_excludes_10907(self):
        """Direct exclusion (10929 excludes 10907) (Difficulty: moderate)"""
        codes = ['10929', '10907']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C1', \
            f"Expected failed_check 'C1', got {result['failed_check']}"
        

    # ===== C2 Tests (150 tests) =====

    def test_c2_0401_Missing_prerequisite_127_requires_45___test_1(self):
        """Missing prerequisite (127 requires 45) - test 1 (Difficulty: moderate)"""
        codes = ['127']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0402_Missing_prerequisite_129_requires_45___test_2(self):
        """Missing prerequisite (129 requires 45) - test 2 (Difficulty: moderate)"""
        codes = ['129']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0403_Missing_prerequisite_132_requires_2___test_3(self):
        """Missing prerequisite (132 requires 2) - test 3 (Difficulty: moderate)"""
        codes = ['132']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0404_Missing_prerequisite_133_requires_20___test_4(self):
        """Missing prerequisite (133 requires 20) - test 4 (Difficulty: moderate)"""
        codes = ['133']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0405_Missing_prerequisite_133_requires_2___test_5(self):
        """Missing prerequisite (133 requires 2) - test 5 (Difficulty: moderate)"""
        codes = ['133']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0406_Missing_prerequisite_135_requires_45___test_6(self):
        """Missing prerequisite (135 requires 45) - test 6 (Difficulty: moderate)"""
        codes = ['135']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0407_Missing_prerequisite_137_requires_45___test_7(self):
        """Missing prerequisite (137 requires 45) - test 7 (Difficulty: moderate)"""
        codes = ['137']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0408_Missing_prerequisite_289_requires_45___test_8(self):
        """Missing prerequisite (289 requires 45) - test 8 (Difficulty: moderate)"""
        codes = ['289']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0409_Missing_prerequisite_289_requires_2___test_9(self):
        """Missing prerequisite (289 requires 2) - test 9 (Difficulty: moderate)"""
        codes = ['289']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0410_Missing_prerequisite_296_requires_45___test_10(self):
        """Missing prerequisite (296 requires 45) - test 10 (Difficulty: moderate)"""
        codes = ['296']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0411_Missing_prerequisite_297_requires_45___test_11(self):
        """Missing prerequisite (297 requires 45) - test 11 (Difficulty: moderate)"""
        codes = ['297']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0412_Missing_prerequisite_299_requires_45___test_12(self):
        """Missing prerequisite (299 requires 45) - test 12 (Difficulty: moderate)"""
        codes = ['299']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0413_Missing_prerequisite_300_requires_15___test_13(self):
        """Missing prerequisite (300 requires 15) - test 13 (Difficulty: moderate)"""
        codes = ['300']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0414_Missing_prerequisite_302_requires_15___test_14(self):
        """Missing prerequisite (302 requires 15) - test 14 (Difficulty: moderate)"""
        codes = ['302']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0415_Missing_prerequisite_304_requires_30___test_15(self):
        """Missing prerequisite (304 requires 30) - test 15 (Difficulty: moderate)"""
        codes = ['304']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0416_Missing_prerequisite_306_requires_45___test_16(self):
        """Missing prerequisite (306 requires 45) - test 16 (Difficulty: moderate)"""
        codes = ['306']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0417_Missing_prerequisite_308_requires_75___test_17(self):
        """Missing prerequisite (308 requires 75) - test 17 (Difficulty: moderate)"""
        codes = ['308']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0418_Missing_prerequisite_312_requires_15___test_18(self):
        """Missing prerequisite (312 requires 15) - test 18 (Difficulty: moderate)"""
        codes = ['312']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0419_Missing_prerequisite_314_requires_30___test_19(self):
        """Missing prerequisite (314 requires 30) - test 19 (Difficulty: moderate)"""
        codes = ['314']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0420_Missing_prerequisite_316_requires_45___test_20(self):
        """Missing prerequisite (316 requires 45) - test 20 (Difficulty: moderate)"""
        codes = ['316']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0421_Missing_prerequisite_318_requires_75___test_21(self):
        """Missing prerequisite (318 requires 75) - test 21 (Difficulty: moderate)"""
        codes = ['318']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0422_Missing_prerequisite_322_requires_15___test_22(self):
        """Missing prerequisite (322 requires 15) - test 22 (Difficulty: moderate)"""
        codes = ['322']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0423_Missing_prerequisite_324_requires_30___test_23(self):
        """Missing prerequisite (324 requires 30) - test 23 (Difficulty: moderate)"""
        codes = ['324']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0424_Missing_prerequisite_326_requires_45___test_24(self):
        """Missing prerequisite (326 requires 45) - test 24 (Difficulty: moderate)"""
        codes = ['326']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0425_Missing_prerequisite_328_requires_75___test_25(self):
        """Missing prerequisite (328 requires 75) - test 25 (Difficulty: moderate)"""
        codes = ['328']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0426_Missing_prerequisite_332_requires_15___test_26(self):
        """Missing prerequisite (332 requires 15) - test 26 (Difficulty: moderate)"""
        codes = ['332']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0427_Missing_prerequisite_334_requires_30___test_27(self):
        """Missing prerequisite (334 requires 30) - test 27 (Difficulty: moderate)"""
        codes = ['334']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0428_Missing_prerequisite_336_requires_45___test_28(self):
        """Missing prerequisite (336 requires 45) - test 28 (Difficulty: moderate)"""
        codes = ['336']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0429_Missing_prerequisite_338_requires_75___test_29(self):
        """Missing prerequisite (338 requires 75) - test 29 (Difficulty: moderate)"""
        codes = ['338']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0430_Missing_prerequisite_6023_requires_45___test_30(self):
        """Missing prerequisite (6023 requires 45) - test 30 (Difficulty: moderate)"""
        codes = ['6023']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0431_Missing_prerequisite_6023_requires_2___test_31(self):
        """Missing prerequisite (6023 requires 2) - test 31 (Difficulty: moderate)"""
        codes = ['6023']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0432_Missing_prerequisite_6057_requires_45___test_32(self):
        """Missing prerequisite (6057 requires 45) - test 32 (Difficulty: moderate)"""
        codes = ['6057']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0433_Missing_prerequisite_6057_requires_2___test_33(self):
        """Missing prerequisite (6057 requires 2) - test 33 (Difficulty: moderate)"""
        codes = ['6057']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0434_Missing_prerequisite_91869_requires_15___test_34(self):
        """Missing prerequisite (91869 requires 15) - test 34 (Difficulty: moderate)"""
        codes = ['91869']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0435_Missing_prerequisite_91870_requires_30___test_35(self):
        """Missing prerequisite (91870 requires 30) - test 35 (Difficulty: moderate)"""
        codes = ['91870']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0436_Missing_prerequisite_91871_requires_45___test_36(self):
        """Missing prerequisite (91871 requires 45) - test 36 (Difficulty: moderate)"""
        codes = ['91871']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0437_Missing_prerequisite_91872_requires_75___test_37(self):
        """Missing prerequisite (91872 requires 75) - test 37 (Difficulty: moderate)"""
        codes = ['91872']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0438_Missing_prerequisite_91873_requires_45___test_38(self):
        """Missing prerequisite (91873 requires 45) - test 38 (Difficulty: moderate)"""
        codes = ['91873']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0439_Missing_prerequisite_91880_requires_15___test_39(self):
        """Missing prerequisite (91880 requires 15) - test 39 (Difficulty: moderate)"""
        codes = ['91880']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0440_Missing_prerequisite_91881_requires_30___test_40(self):
        """Missing prerequisite (91881 requires 30) - test 40 (Difficulty: moderate)"""
        codes = ['91881']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0441_Missing_prerequisite_92140_requires_45___test_41(self):
        """Missing prerequisite (92140 requires 45) - test 41 (Difficulty: moderate)"""
        codes = ['92140']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0442_Missing_prerequisite_92141_requires_45___test_42(self):
        """Missing prerequisite (92141 requires 45) - test 42 (Difficulty: moderate)"""
        codes = ['92141']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0443_Missing_prerequisite_92422_requires_2___test_43(self):
        """Missing prerequisite (92422 requires 2) - test 43 (Difficulty: moderate)"""
        codes = ['92422']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0444_Missing_prerequisite_92434_requires_45___test_44(self):
        """Missing prerequisite (92434 requires 45) - test 44 (Difficulty: moderate)"""
        codes = ['92434']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0445_Missing_prerequisite_92434_requires_2___test_45(self):
        """Missing prerequisite (92434 requires 2) - test 45 (Difficulty: moderate)"""
        codes = ['92434']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0446_Missing_prerequisite_92437_requires_45___test_46(self):
        """Missing prerequisite (92437 requires 45) - test 46 (Difficulty: moderate)"""
        codes = ['92437']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0447_Missing_prerequisite_92483_requires_45___test_47(self):
        """Missing prerequisite (92483 requires 45) - test 47 (Difficulty: moderate)"""
        codes = ['92483']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0448_Missing_prerequisite_92762_requires_45___test_48(self):
        """Missing prerequisite (92762 requires 45) - test 48 (Difficulty: moderate)"""
        codes = ['92762']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0449_Missing_prerequisite_92762_requires_2___test_49(self):
        """Missing prerequisite (92762 requires 2) - test 49 (Difficulty: moderate)"""
        codes = ['92762']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0450_Missing_prerequisite_92767_requires_45___test_50(self):
        """Missing prerequisite (92767 requires 45) - test 50 (Difficulty: moderate)"""
        codes = ['92767']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0451_Missing_prerequisite_92767_requires_2___test_51(self):
        """Missing prerequisite (92767 requires 2) - test 51 (Difficulty: moderate)"""
        codes = ['92767']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0452_Missing_prerequisite_127_requires_45___test_52(self):
        """Missing prerequisite (127 requires 45) - test 52 (Difficulty: moderate)"""
        codes = ['127']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0453_Missing_prerequisite_129_requires_45___test_53(self):
        """Missing prerequisite (129 requires 45) - test 53 (Difficulty: moderate)"""
        codes = ['129']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0454_Missing_prerequisite_132_requires_2___test_54(self):
        """Missing prerequisite (132 requires 2) - test 54 (Difficulty: moderate)"""
        codes = ['132']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0455_Missing_prerequisite_133_requires_20___test_55(self):
        """Missing prerequisite (133 requires 20) - test 55 (Difficulty: moderate)"""
        codes = ['133']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0456_Missing_prerequisite_133_requires_2___test_56(self):
        """Missing prerequisite (133 requires 2) - test 56 (Difficulty: moderate)"""
        codes = ['133']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0457_Missing_prerequisite_135_requires_45___test_57(self):
        """Missing prerequisite (135 requires 45) - test 57 (Difficulty: moderate)"""
        codes = ['135']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0458_Missing_prerequisite_137_requires_45___test_58(self):
        """Missing prerequisite (137 requires 45) - test 58 (Difficulty: moderate)"""
        codes = ['137']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0459_Missing_prerequisite_289_requires_45___test_59(self):
        """Missing prerequisite (289 requires 45) - test 59 (Difficulty: moderate)"""
        codes = ['289']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0460_Missing_prerequisite_289_requires_2___test_60(self):
        """Missing prerequisite (289 requires 2) - test 60 (Difficulty: moderate)"""
        codes = ['289']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0461_Missing_prerequisite_296_requires_45___test_61(self):
        """Missing prerequisite (296 requires 45) - test 61 (Difficulty: moderate)"""
        codes = ['296']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0462_Missing_prerequisite_297_requires_45___test_62(self):
        """Missing prerequisite (297 requires 45) - test 62 (Difficulty: moderate)"""
        codes = ['297']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0463_Missing_prerequisite_299_requires_45___test_63(self):
        """Missing prerequisite (299 requires 45) - test 63 (Difficulty: moderate)"""
        codes = ['299']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0464_Missing_prerequisite_300_requires_15___test_64(self):
        """Missing prerequisite (300 requires 15) - test 64 (Difficulty: moderate)"""
        codes = ['300']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0465_Missing_prerequisite_302_requires_15___test_65(self):
        """Missing prerequisite (302 requires 15) - test 65 (Difficulty: moderate)"""
        codes = ['302']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0466_Missing_prerequisite_304_requires_30___test_66(self):
        """Missing prerequisite (304 requires 30) - test 66 (Difficulty: moderate)"""
        codes = ['304']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0467_Missing_prerequisite_306_requires_45___test_67(self):
        """Missing prerequisite (306 requires 45) - test 67 (Difficulty: moderate)"""
        codes = ['306']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0468_Missing_prerequisite_308_requires_75___test_68(self):
        """Missing prerequisite (308 requires 75) - test 68 (Difficulty: moderate)"""
        codes = ['308']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0469_Missing_prerequisite_312_requires_15___test_69(self):
        """Missing prerequisite (312 requires 15) - test 69 (Difficulty: moderate)"""
        codes = ['312']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0470_Missing_prerequisite_314_requires_30___test_70(self):
        """Missing prerequisite (314 requires 30) - test 70 (Difficulty: moderate)"""
        codes = ['314']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0471_Missing_prerequisite_316_requires_45___test_71(self):
        """Missing prerequisite (316 requires 45) - test 71 (Difficulty: moderate)"""
        codes = ['316']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0472_Missing_prerequisite_318_requires_75___test_72(self):
        """Missing prerequisite (318 requires 75) - test 72 (Difficulty: moderate)"""
        codes = ['318']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0473_Missing_prerequisite_322_requires_15___test_73(self):
        """Missing prerequisite (322 requires 15) - test 73 (Difficulty: moderate)"""
        codes = ['322']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0474_Missing_prerequisite_324_requires_30___test_74(self):
        """Missing prerequisite (324 requires 30) - test 74 (Difficulty: moderate)"""
        codes = ['324']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0475_Missing_prerequisite_326_requires_45___test_75(self):
        """Missing prerequisite (326 requires 45) - test 75 (Difficulty: moderate)"""
        codes = ['326']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0476_Missing_prerequisite_328_requires_75___test_76(self):
        """Missing prerequisite (328 requires 75) - test 76 (Difficulty: moderate)"""
        codes = ['328']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0477_Missing_prerequisite_332_requires_15___test_77(self):
        """Missing prerequisite (332 requires 15) - test 77 (Difficulty: moderate)"""
        codes = ['332']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0478_Missing_prerequisite_334_requires_30___test_78(self):
        """Missing prerequisite (334 requires 30) - test 78 (Difficulty: moderate)"""
        codes = ['334']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0479_Missing_prerequisite_336_requires_45___test_79(self):
        """Missing prerequisite (336 requires 45) - test 79 (Difficulty: moderate)"""
        codes = ['336']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0480_Missing_prerequisite_338_requires_75___test_80(self):
        """Missing prerequisite (338 requires 75) - test 80 (Difficulty: moderate)"""
        codes = ['338']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0481_Missing_prerequisite_6023_requires_45___test_81(self):
        """Missing prerequisite (6023 requires 45) - test 81 (Difficulty: moderate)"""
        codes = ['6023']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0482_Missing_prerequisite_6023_requires_2___test_82(self):
        """Missing prerequisite (6023 requires 2) - test 82 (Difficulty: moderate)"""
        codes = ['6023']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0483_Missing_prerequisite_6057_requires_45___test_83(self):
        """Missing prerequisite (6057 requires 45) - test 83 (Difficulty: moderate)"""
        codes = ['6057']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0484_Missing_prerequisite_6057_requires_2___test_84(self):
        """Missing prerequisite (6057 requires 2) - test 84 (Difficulty: moderate)"""
        codes = ['6057']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0485_Missing_prerequisite_91869_requires_15___test_85(self):
        """Missing prerequisite (91869 requires 15) - test 85 (Difficulty: moderate)"""
        codes = ['91869']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0486_Missing_prerequisite_91870_requires_30___test_86(self):
        """Missing prerequisite (91870 requires 30) - test 86 (Difficulty: moderate)"""
        codes = ['91870']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0487_Missing_prerequisite_91871_requires_45___test_87(self):
        """Missing prerequisite (91871 requires 45) - test 87 (Difficulty: moderate)"""
        codes = ['91871']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0488_Missing_prerequisite_91872_requires_75___test_88(self):
        """Missing prerequisite (91872 requires 75) - test 88 (Difficulty: moderate)"""
        codes = ['91872']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0489_Missing_prerequisite_91873_requires_45___test_89(self):
        """Missing prerequisite (91873 requires 45) - test 89 (Difficulty: moderate)"""
        codes = ['91873']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0490_Missing_prerequisite_91880_requires_15___test_90(self):
        """Missing prerequisite (91880 requires 15) - test 90 (Difficulty: moderate)"""
        codes = ['91880']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0491_Missing_prerequisite_91881_requires_30___test_91(self):
        """Missing prerequisite (91881 requires 30) - test 91 (Difficulty: moderate)"""
        codes = ['91881']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0492_Missing_prerequisite_92140_requires_45___test_92(self):
        """Missing prerequisite (92140 requires 45) - test 92 (Difficulty: moderate)"""
        codes = ['92140']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0493_Missing_prerequisite_92141_requires_45___test_93(self):
        """Missing prerequisite (92141 requires 45) - test 93 (Difficulty: moderate)"""
        codes = ['92141']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0494_Missing_prerequisite_92422_requires_2___test_94(self):
        """Missing prerequisite (92422 requires 2) - test 94 (Difficulty: moderate)"""
        codes = ['92422']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0495_Missing_prerequisite_92434_requires_45___test_95(self):
        """Missing prerequisite (92434 requires 45) - test 95 (Difficulty: moderate)"""
        codes = ['92434']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0496_Missing_prerequisite_92434_requires_2___test_96(self):
        """Missing prerequisite (92434 requires 2) - test 96 (Difficulty: moderate)"""
        codes = ['92434']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0497_Missing_prerequisite_92437_requires_45___test_97(self):
        """Missing prerequisite (92437 requires 45) - test 97 (Difficulty: moderate)"""
        codes = ['92437']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0498_Missing_prerequisite_92483_requires_45___test_98(self):
        """Missing prerequisite (92483 requires 45) - test 98 (Difficulty: moderate)"""
        codes = ['92483']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0499_Missing_prerequisite_92762_requires_45___test_99(self):
        """Missing prerequisite (92762 requires 45) - test 99 (Difficulty: moderate)"""
        codes = ['92762']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0500_Missing_prerequisite_92762_requires_2___test_100(self):
        """Missing prerequisite (92762 requires 2) - test 100 (Difficulty: moderate)"""
        codes = ['92762']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0501_Missing_prerequisite_92767_requires_45___test_101(self):
        """Missing prerequisite (92767 requires 45) - test 101 (Difficulty: moderate)"""
        codes = ['92767']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0502_Missing_prerequisite_92767_requires_2___test_102(self):
        """Missing prerequisite (92767 requires 2) - test 102 (Difficulty: moderate)"""
        codes = ['92767']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0503_Missing_prerequisite_127_requires_45___test_103(self):
        """Missing prerequisite (127 requires 45) - test 103 (Difficulty: moderate)"""
        codes = ['127']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0504_Missing_prerequisite_129_requires_45___test_104(self):
        """Missing prerequisite (129 requires 45) - test 104 (Difficulty: moderate)"""
        codes = ['129']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0505_Missing_prerequisite_132_requires_2___test_105(self):
        """Missing prerequisite (132 requires 2) - test 105 (Difficulty: moderate)"""
        codes = ['132']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0506_Missing_prerequisite_133_requires_20___test_106(self):
        """Missing prerequisite (133 requires 20) - test 106 (Difficulty: moderate)"""
        codes = ['133']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0507_Missing_prerequisite_133_requires_2___test_107(self):
        """Missing prerequisite (133 requires 2) - test 107 (Difficulty: moderate)"""
        codes = ['133']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0508_Missing_prerequisite_135_requires_45___test_108(self):
        """Missing prerequisite (135 requires 45) - test 108 (Difficulty: moderate)"""
        codes = ['135']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0509_Missing_prerequisite_137_requires_45___test_109(self):
        """Missing prerequisite (137 requires 45) - test 109 (Difficulty: moderate)"""
        codes = ['137']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0510_Missing_prerequisite_289_requires_45___test_110(self):
        """Missing prerequisite (289 requires 45) - test 110 (Difficulty: moderate)"""
        codes = ['289']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0511_Missing_prerequisite_289_requires_2___test_111(self):
        """Missing prerequisite (289 requires 2) - test 111 (Difficulty: moderate)"""
        codes = ['289']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0512_Missing_prerequisite_296_requires_45___test_112(self):
        """Missing prerequisite (296 requires 45) - test 112 (Difficulty: moderate)"""
        codes = ['296']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0513_Missing_prerequisite_297_requires_45___test_113(self):
        """Missing prerequisite (297 requires 45) - test 113 (Difficulty: moderate)"""
        codes = ['297']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0514_Missing_prerequisite_299_requires_45___test_114(self):
        """Missing prerequisite (299 requires 45) - test 114 (Difficulty: moderate)"""
        codes = ['299']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0515_Missing_prerequisite_300_requires_15___test_115(self):
        """Missing prerequisite (300 requires 15) - test 115 (Difficulty: moderate)"""
        codes = ['300']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0516_Missing_prerequisite_302_requires_15___test_116(self):
        """Missing prerequisite (302 requires 15) - test 116 (Difficulty: moderate)"""
        codes = ['302']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0517_Missing_prerequisite_304_requires_30___test_117(self):
        """Missing prerequisite (304 requires 30) - test 117 (Difficulty: moderate)"""
        codes = ['304']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0518_Missing_prerequisite_306_requires_45___test_118(self):
        """Missing prerequisite (306 requires 45) - test 118 (Difficulty: moderate)"""
        codes = ['306']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0519_Missing_prerequisite_308_requires_75___test_119(self):
        """Missing prerequisite (308 requires 75) - test 119 (Difficulty: moderate)"""
        codes = ['308']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0520_Missing_prerequisite_312_requires_15___test_120(self):
        """Missing prerequisite (312 requires 15) - test 120 (Difficulty: moderate)"""
        codes = ['312']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0521_Missing_prerequisite_314_requires_30___test_121(self):
        """Missing prerequisite (314 requires 30) - test 121 (Difficulty: moderate)"""
        codes = ['314']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0522_Missing_prerequisite_316_requires_45___test_122(self):
        """Missing prerequisite (316 requires 45) - test 122 (Difficulty: moderate)"""
        codes = ['316']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0523_Missing_prerequisite_318_requires_75___test_123(self):
        """Missing prerequisite (318 requires 75) - test 123 (Difficulty: moderate)"""
        codes = ['318']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0524_Missing_prerequisite_322_requires_15___test_124(self):
        """Missing prerequisite (322 requires 15) - test 124 (Difficulty: moderate)"""
        codes = ['322']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0525_Missing_prerequisite_324_requires_30___test_125(self):
        """Missing prerequisite (324 requires 30) - test 125 (Difficulty: moderate)"""
        codes = ['324']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0526_Missing_prerequisite_326_requires_45___test_126(self):
        """Missing prerequisite (326 requires 45) - test 126 (Difficulty: moderate)"""
        codes = ['326']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0527_Missing_prerequisite_328_requires_75___test_127(self):
        """Missing prerequisite (328 requires 75) - test 127 (Difficulty: moderate)"""
        codes = ['328']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0528_Missing_prerequisite_332_requires_15___test_128(self):
        """Missing prerequisite (332 requires 15) - test 128 (Difficulty: moderate)"""
        codes = ['332']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0529_Missing_prerequisite_334_requires_30___test_129(self):
        """Missing prerequisite (334 requires 30) - test 129 (Difficulty: moderate)"""
        codes = ['334']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0530_Missing_prerequisite_336_requires_45___test_130(self):
        """Missing prerequisite (336 requires 45) - test 130 (Difficulty: moderate)"""
        codes = ['336']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0531_Missing_prerequisite_338_requires_75___test_131(self):
        """Missing prerequisite (338 requires 75) - test 131 (Difficulty: moderate)"""
        codes = ['338']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0532_Missing_prerequisite_6023_requires_45___test_132(self):
        """Missing prerequisite (6023 requires 45) - test 132 (Difficulty: moderate)"""
        codes = ['6023']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0533_Missing_prerequisite_6023_requires_2___test_133(self):
        """Missing prerequisite (6023 requires 2) - test 133 (Difficulty: moderate)"""
        codes = ['6023']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0534_Missing_prerequisite_6057_requires_45___test_134(self):
        """Missing prerequisite (6057 requires 45) - test 134 (Difficulty: moderate)"""
        codes = ['6057']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0535_Missing_prerequisite_6057_requires_2___test_135(self):
        """Missing prerequisite (6057 requires 2) - test 135 (Difficulty: moderate)"""
        codes = ['6057']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0536_Missing_prerequisite_91869_requires_15___test_136(self):
        """Missing prerequisite (91869 requires 15) - test 136 (Difficulty: moderate)"""
        codes = ['91869']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0537_Missing_prerequisite_91870_requires_30___test_137(self):
        """Missing prerequisite (91870 requires 30) - test 137 (Difficulty: moderate)"""
        codes = ['91870']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0538_Missing_prerequisite_91871_requires_45___test_138(self):
        """Missing prerequisite (91871 requires 45) - test 138 (Difficulty: moderate)"""
        codes = ['91871']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0539_Missing_prerequisite_91872_requires_75___test_139(self):
        """Missing prerequisite (91872 requires 75) - test 139 (Difficulty: moderate)"""
        codes = ['91872']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0540_Missing_prerequisite_91873_requires_45___test_140(self):
        """Missing prerequisite (91873 requires 45) - test 140 (Difficulty: moderate)"""
        codes = ['91873']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0541_Missing_prerequisite_91880_requires_15___test_141(self):
        """Missing prerequisite (91880 requires 15) - test 141 (Difficulty: moderate)"""
        codes = ['91880']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0542_Missing_prerequisite_91881_requires_30___test_142(self):
        """Missing prerequisite (91881 requires 30) - test 142 (Difficulty: moderate)"""
        codes = ['91881']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0543_Missing_prerequisite_92140_requires_45___test_143(self):
        """Missing prerequisite (92140 requires 45) - test 143 (Difficulty: moderate)"""
        codes = ['92140']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0544_Missing_prerequisite_92141_requires_45___test_144(self):
        """Missing prerequisite (92141 requires 45) - test 144 (Difficulty: moderate)"""
        codes = ['92141']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0545_Missing_prerequisite_92422_requires_2___test_145(self):
        """Missing prerequisite (92422 requires 2) - test 145 (Difficulty: moderate)"""
        codes = ['92422']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0546_Missing_prerequisite_92434_requires_45___test_146(self):
        """Missing prerequisite (92434 requires 45) - test 146 (Difficulty: moderate)"""
        codes = ['92434']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0547_Missing_prerequisite_92434_requires_2___test_147(self):
        """Missing prerequisite (92434 requires 2) - test 147 (Difficulty: moderate)"""
        codes = ['92434']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0548_Missing_prerequisite_92437_requires_45___test_148(self):
        """Missing prerequisite (92437 requires 45) - test 148 (Difficulty: moderate)"""
        codes = ['92437']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0549_Missing_prerequisite_92483_requires_45___test_149(self):
        """Missing prerequisite (92483 requires 45) - test 149 (Difficulty: moderate)"""
        codes = ['92483']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        
    def test_c2_0550_Missing_prerequisite_92762_requires_45___test_150(self):
        """Missing prerequisite (92762 requires 45) - test 150 (Difficulty: moderate)"""
        codes = ['92762']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C2', \
            f"Expected failed_check 'C2', got {result['failed_check']}"
        

    # ===== C3 Tests (100 tests) =====

    def test_c3_0551_Solo_only_code_alone_36___test_1(self):
        """Solo-only code alone (36) - test 1 (Difficulty: basic)"""
        codes = ['36']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0552_Solo_only_code_alone_44___test_2(self):
        """Solo-only code alone (44) - test 2 (Difficulty: basic)"""
        codes = ['44']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0553_Solo_only_code_alone_5040___test_3(self):
        """Solo-only code alone (5040) - test 3 (Difficulty: basic)"""
        codes = ['5040']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0554_Solo_only_code_alone_5060___test_4(self):
        """Solo-only code alone (5060) - test 4 (Difficulty: basic)"""
        codes = ['5060']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0555_Solo_only_code_alone_90043___test_5(self):
        """Solo-only code alone (90043) - test 5 (Difficulty: basic)"""
        codes = ['90043']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0556_Solo_only_code_alone_90051___test_6(self):
        """Solo-only code alone (90051) - test 6 (Difficulty: basic)"""
        codes = ['90051']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0557_Solo_only_code_alone_36___test_7(self):
        """Solo-only code alone (36) - test 7 (Difficulty: basic)"""
        codes = ['36']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0558_Solo_only_code_alone_44___test_8(self):
        """Solo-only code alone (44) - test 8 (Difficulty: basic)"""
        codes = ['44']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0559_Solo_only_code_alone_5040___test_9(self):
        """Solo-only code alone (5040) - test 9 (Difficulty: basic)"""
        codes = ['5040']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0560_Solo_only_code_alone_5060___test_10(self):
        """Solo-only code alone (5060) - test 10 (Difficulty: basic)"""
        codes = ['5060']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0561_Solo_only_code_alone_90043___test_11(self):
        """Solo-only code alone (90043) - test 11 (Difficulty: basic)"""
        codes = ['90043']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0562_Solo_only_code_alone_90051___test_12(self):
        """Solo-only code alone (90051) - test 12 (Difficulty: basic)"""
        codes = ['90051']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0563_Solo_only_code_alone_36___test_13(self):
        """Solo-only code alone (36) - test 13 (Difficulty: basic)"""
        codes = ['36']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0564_Solo_only_code_alone_44___test_14(self):
        """Solo-only code alone (44) - test 14 (Difficulty: basic)"""
        codes = ['44']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0565_Solo_only_code_alone_5040___test_15(self):
        """Solo-only code alone (5040) - test 15 (Difficulty: basic)"""
        codes = ['5040']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0566_Solo_only_code_alone_5060___test_16(self):
        """Solo-only code alone (5060) - test 16 (Difficulty: basic)"""
        codes = ['5060']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0567_Solo_only_code_alone_90043___test_17(self):
        """Solo-only code alone (90043) - test 17 (Difficulty: basic)"""
        codes = ['90043']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0568_Solo_only_code_alone_90051___test_18(self):
        """Solo-only code alone (90051) - test 18 (Difficulty: basic)"""
        codes = ['90051']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0569_Solo_only_code_alone_36___test_19(self):
        """Solo-only code alone (36) - test 19 (Difficulty: basic)"""
        codes = ['36']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0570_Solo_only_code_alone_44___test_20(self):
        """Solo-only code alone (44) - test 20 (Difficulty: basic)"""
        codes = ['44']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0571_Solo_only_code_alone_5040___test_21(self):
        """Solo-only code alone (5040) - test 21 (Difficulty: basic)"""
        codes = ['5040']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0572_Solo_only_code_alone_5060___test_22(self):
        """Solo-only code alone (5060) - test 22 (Difficulty: basic)"""
        codes = ['5060']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0573_Solo_only_code_alone_90043___test_23(self):
        """Solo-only code alone (90043) - test 23 (Difficulty: basic)"""
        codes = ['90043']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0574_Solo_only_code_alone_90051___test_24(self):
        """Solo-only code alone (90051) - test 24 (Difficulty: basic)"""
        codes = ['90051']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0575_Solo_only_code_alone_36___test_25(self):
        """Solo-only code alone (36) - test 25 (Difficulty: basic)"""
        codes = ['36']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0576_Solo_only_code_alone_44___test_26(self):
        """Solo-only code alone (44) - test 26 (Difficulty: basic)"""
        codes = ['44']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0577_Solo_only_code_alone_5040___test_27(self):
        """Solo-only code alone (5040) - test 27 (Difficulty: basic)"""
        codes = ['5040']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0578_Solo_only_code_alone_5060___test_28(self):
        """Solo-only code alone (5060) - test 28 (Difficulty: basic)"""
        codes = ['5060']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0579_Solo_only_code_alone_90043___test_29(self):
        """Solo-only code alone (90043) - test 29 (Difficulty: basic)"""
        codes = ['90043']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0580_Solo_only_code_alone_90051___test_30(self):
        """Solo-only code alone (90051) - test 30 (Difficulty: basic)"""
        codes = ['90051']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0581_Solo_only_code_alone_36___test_31(self):
        """Solo-only code alone (36) - test 31 (Difficulty: basic)"""
        codes = ['36']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0582_Solo_only_code_alone_44___test_32(self):
        """Solo-only code alone (44) - test 32 (Difficulty: basic)"""
        codes = ['44']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0583_Solo_only_code_alone_5040___test_33(self):
        """Solo-only code alone (5040) - test 33 (Difficulty: basic)"""
        codes = ['5040']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0584_Solo_only_code_alone_5060___test_34(self):
        """Solo-only code alone (5060) - test 34 (Difficulty: basic)"""
        codes = ['5060']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0585_Solo_only_code_alone_90043___test_35(self):
        """Solo-only code alone (90043) - test 35 (Difficulty: basic)"""
        codes = ['90043']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0586_Solo_only_code_alone_90051___test_36(self):
        """Solo-only code alone (90051) - test 36 (Difficulty: basic)"""
        codes = ['90051']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0587_Solo_only_code_alone_36___test_37(self):
        """Solo-only code alone (36) - test 37 (Difficulty: basic)"""
        codes = ['36']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0588_Solo_only_code_alone_44___test_38(self):
        """Solo-only code alone (44) - test 38 (Difficulty: basic)"""
        codes = ['44']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0589_Solo_only_code_alone_5040___test_39(self):
        """Solo-only code alone (5040) - test 39 (Difficulty: basic)"""
        codes = ['5040']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0590_Solo_only_code_alone_5060___test_40(self):
        """Solo-only code alone (5060) - test 40 (Difficulty: basic)"""
        codes = ['5060']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0591_Solo_only_code_alone_90043___test_41(self):
        """Solo-only code alone (90043) - test 41 (Difficulty: basic)"""
        codes = ['90043']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0592_Solo_only_code_alone_90051___test_42(self):
        """Solo-only code alone (90051) - test 42 (Difficulty: basic)"""
        codes = ['90051']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0593_Solo_only_code_alone_36___test_43(self):
        """Solo-only code alone (36) - test 43 (Difficulty: basic)"""
        codes = ['36']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0594_Solo_only_code_alone_44___test_44(self):
        """Solo-only code alone (44) - test 44 (Difficulty: basic)"""
        codes = ['44']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0595_Solo_only_code_alone_5040___test_45(self):
        """Solo-only code alone (5040) - test 45 (Difficulty: basic)"""
        codes = ['5040']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0596_Solo_only_code_alone_5060___test_46(self):
        """Solo-only code alone (5060) - test 46 (Difficulty: basic)"""
        codes = ['5060']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0597_Solo_only_code_alone_90043___test_47(self):
        """Solo-only code alone (90043) - test 47 (Difficulty: basic)"""
        codes = ['90043']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0598_Solo_only_code_alone_90051___test_48(self):
        """Solo-only code alone (90051) - test 48 (Difficulty: basic)"""
        codes = ['90051']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0599_Solo_only_code_alone_36___test_49(self):
        """Solo-only code alone (36) - test 49 (Difficulty: basic)"""
        codes = ['36']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0600_Solo_only_code_alone_44___test_50(self):
        """Solo-only code alone (44) - test 50 (Difficulty: basic)"""
        codes = ['44']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_c3_0601_Solo_only_code_with_other_36_with_104___test_1(self):
        """Solo-only code with other (36 with 104) - test 1 (Difficulty: moderate)"""
        codes = ['36', '104']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0602_Solo_only_code_with_other_44_with_105___test_2(self):
        """Solo-only code with other (44 with 105) - test 2 (Difficulty: moderate)"""
        codes = ['44', '105']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0603_Solo_only_code_with_other_5040_with_106___test_3(self):
        """Solo-only code with other (5040 with 106) - test 3 (Difficulty: moderate)"""
        codes = ['5040', '106']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0604_Solo_only_code_with_other_5060_with_107___test_4(self):
        """Solo-only code with other (5060 with 107) - test 4 (Difficulty: moderate)"""
        codes = ['5060', '107']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0605_Solo_only_code_with_other_90043_with_108___test_5(self):
        """Solo-only code with other (90043 with 108) - test 5 (Difficulty: moderate)"""
        codes = ['90043', '108']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0606_Solo_only_code_with_other_90051_with_10801___test_(self):
        """Solo-only code with other (90051 with 10801) - test 6 (Difficulty: moderate)"""
        codes = ['90051', '10801']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0607_Solo_only_code_with_other_36_with_10802___test_7(self):
        """Solo-only code with other (36 with 10802) - test 7 (Difficulty: moderate)"""
        codes = ['36', '10802']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0608_Solo_only_code_with_other_44_with_10803___test_8(self):
        """Solo-only code with other (44 with 10803) - test 8 (Difficulty: moderate)"""
        codes = ['44', '10803']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0609_Solo_only_code_with_other_5040_with_10804___test_9(self):
        """Solo-only code with other (5040 with 10804) - test 9 (Difficulty: moderate)"""
        codes = ['5040', '10804']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0610_Solo_only_code_with_other_5060_with_10805___test_1(self):
        """Solo-only code with other (5060 with 10805) - test 10 (Difficulty: moderate)"""
        codes = ['5060', '10805']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0611_Solo_only_code_with_other_90043_with_10806___test_(self):
        """Solo-only code with other (90043 with 10806) - test 11 (Difficulty: moderate)"""
        codes = ['90043', '10806']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0612_Solo_only_code_with_other_90051_with_10807___test_(self):
        """Solo-only code with other (90051 with 10807) - test 12 (Difficulty: moderate)"""
        codes = ['90051', '10807']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0613_Solo_only_code_with_other_36_with_10808___test_13(self):
        """Solo-only code with other (36 with 10808) - test 13 (Difficulty: moderate)"""
        codes = ['36', '10808']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0614_Solo_only_code_with_other_44_with_10809___test_14(self):
        """Solo-only code with other (44 with 10809) - test 14 (Difficulty: moderate)"""
        codes = ['44', '10809']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0615_Solo_only_code_with_other_5040_with_10816___test_1(self):
        """Solo-only code with other (5040 with 10816) - test 15 (Difficulty: moderate)"""
        codes = ['5040', '10816']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0616_Solo_only_code_with_other_5060_with_109___test_16(self):
        """Solo-only code with other (5060 with 109) - test 16 (Difficulty: moderate)"""
        codes = ['5060', '109']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0617_Solo_only_code_with_other_90043_with_10905___test_(self):
        """Solo-only code with other (90043 with 10905) - test 17 (Difficulty: moderate)"""
        codes = ['90043', '10905']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0618_Solo_only_code_with_other_90051_with_10907___test_(self):
        """Solo-only code with other (90051 with 10907) - test 18 (Difficulty: moderate)"""
        codes = ['90051', '10907']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0619_Solo_only_code_with_other_36_with_10910___test_19(self):
        """Solo-only code with other (36 with 10910) - test 19 (Difficulty: moderate)"""
        codes = ['36', '10910']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0620_Solo_only_code_with_other_44_with_10911___test_20(self):
        """Solo-only code with other (44 with 10911) - test 20 (Difficulty: moderate)"""
        codes = ['44', '10911']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0621_Solo_only_code_with_other_5040_with_10913___test_2(self):
        """Solo-only code with other (5040 with 10913) - test 21 (Difficulty: moderate)"""
        codes = ['5040', '10913']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0622_Solo_only_code_with_other_5060_with_10914___test_2(self):
        """Solo-only code with other (5060 with 10914) - test 22 (Difficulty: moderate)"""
        codes = ['5060', '10914']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0623_Solo_only_code_with_other_90043_with_10915___test_(self):
        """Solo-only code with other (90043 with 10915) - test 23 (Difficulty: moderate)"""
        codes = ['90043', '10915']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0624_Solo_only_code_with_other_90051_with_10916___test_(self):
        """Solo-only code with other (90051 with 10916) - test 24 (Difficulty: moderate)"""
        codes = ['90051', '10916']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0625_Solo_only_code_with_other_36_with_10918___test_25(self):
        """Solo-only code with other (36 with 10918) - test 25 (Difficulty: moderate)"""
        codes = ['36', '10918']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0626_Solo_only_code_with_other_44_with_10921___test_26(self):
        """Solo-only code with other (44 with 10921) - test 26 (Difficulty: moderate)"""
        codes = ['44', '10921']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0627_Solo_only_code_with_other_5040_with_10924___test_2(self):
        """Solo-only code with other (5040 with 10924) - test 27 (Difficulty: moderate)"""
        codes = ['5040', '10924']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0628_Solo_only_code_with_other_5060_with_10926___test_2(self):
        """Solo-only code with other (5060 with 10926) - test 28 (Difficulty: moderate)"""
        codes = ['5060', '10926']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0629_Solo_only_code_with_other_90043_with_10927___test_(self):
        """Solo-only code with other (90043 with 10927) - test 29 (Difficulty: moderate)"""
        codes = ['90043', '10927']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0630_Solo_only_code_with_other_90051_with_10928___test_(self):
        """Solo-only code with other (90051 with 10928) - test 30 (Difficulty: moderate)"""
        codes = ['90051', '10928']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0631_Solo_only_code_with_other_36_with_10929___test_31(self):
        """Solo-only code with other (36 with 10929) - test 31 (Difficulty: moderate)"""
        codes = ['36', '10929']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0632_Solo_only_code_with_other_44_with_10930___test_32(self):
        """Solo-only code with other (44 with 10930) - test 32 (Difficulty: moderate)"""
        codes = ['44', '10930']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0633_Solo_only_code_with_other_5040_with_10931___test_3(self):
        """Solo-only code with other (5040 with 10931) - test 33 (Difficulty: moderate)"""
        codes = ['5040', '10931']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0634_Solo_only_code_with_other_5060_with_10938___test_3(self):
        """Solo-only code with other (5060 with 10938) - test 34 (Difficulty: moderate)"""
        codes = ['5060', '10938']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0635_Solo_only_code_with_other_90043_with_10939___test_(self):
        """Solo-only code with other (90043 with 10939) - test 35 (Difficulty: moderate)"""
        codes = ['90043', '10939']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0636_Solo_only_code_with_other_90051_with_10940___test_(self):
        """Solo-only code with other (90051 with 10940) - test 36 (Difficulty: moderate)"""
        codes = ['90051', '10940']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0637_Solo_only_code_with_other_36_with_10941___test_37(self):
        """Solo-only code with other (36 with 10941) - test 37 (Difficulty: moderate)"""
        codes = ['36', '10941']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0638_Solo_only_code_with_other_44_with_10942___test_38(self):
        """Solo-only code with other (44 with 10942) - test 38 (Difficulty: moderate)"""
        codes = ['44', '10942']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0639_Solo_only_code_with_other_5040_with_10943___test_3(self):
        """Solo-only code with other (5040 with 10943) - test 39 (Difficulty: moderate)"""
        codes = ['5040', '10943']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0640_Solo_only_code_with_other_5060_with_10944___test_4(self):
        """Solo-only code with other (5060 with 10944) - test 40 (Difficulty: moderate)"""
        codes = ['5060', '10944']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0641_Solo_only_code_with_other_90043_with_10945___test_(self):
        """Solo-only code with other (90043 with 10945) - test 41 (Difficulty: moderate)"""
        codes = ['90043', '10945']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0642_Solo_only_code_with_other_90051_with_10946___test_(self):
        """Solo-only code with other (90051 with 10946) - test 42 (Difficulty: moderate)"""
        codes = ['90051', '10946']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0643_Solo_only_code_with_other_36_with_10950___test_43(self):
        """Solo-only code with other (36 with 10950) - test 43 (Difficulty: moderate)"""
        codes = ['36', '10950']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0644_Solo_only_code_with_other_44_with_10951___test_44(self):
        """Solo-only code with other (44 with 10951) - test 44 (Difficulty: moderate)"""
        codes = ['44', '10951']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0645_Solo_only_code_with_other_5040_with_10952___test_4(self):
        """Solo-only code with other (5040 with 10952) - test 45 (Difficulty: moderate)"""
        codes = ['5040', '10952']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0646_Solo_only_code_with_other_5060_with_10953___test_4(self):
        """Solo-only code with other (5060 with 10953) - test 46 (Difficulty: moderate)"""
        codes = ['5060', '10953']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0647_Solo_only_code_with_other_90043_with_10954___test_(self):
        """Solo-only code with other (90043 with 10954) - test 47 (Difficulty: moderate)"""
        codes = ['90043', '10954']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0648_Solo_only_code_with_other_90051_with_10955___test_(self):
        """Solo-only code with other (90051 with 10955) - test 48 (Difficulty: moderate)"""
        codes = ['90051', '10955']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0649_Solo_only_code_with_other_36_with_10956___test_49(self):
        """Solo-only code with other (36 with 10956) - test 49 (Difficulty: moderate)"""
        codes = ['36', '10956']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        
    def test_c3_0650_Solo_only_code_with_other_44_with_10957___test_50(self):
        """Solo-only code with other (44 with 10957) - test 50 (Difficulty: moderate)"""
        codes = ['44', '10957']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C3', \
            f"Expected failed_check 'C3', got {result['failed_check']}"
        

    # ===== C4 Tests (100 tests) =====

    def test_c4_0651_Duplicate_same_occasion_code_11729_x2___test_1(self):
        """Duplicate same_occasion code (11729 x2) - test 1 (Difficulty: moderate)"""
        codes = ['11729', '11729']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0652_Duplicate_same_occasion_code_11730_x2___test_2(self):
        """Duplicate same_occasion code (11730 x2) - test 2 (Difficulty: moderate)"""
        codes = ['11730', '11730']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0653_Duplicate_same_occasion_code_11732_x2___test_3(self):
        """Duplicate same_occasion code (11732 x2) - test 3 (Difficulty: moderate)"""
        codes = ['11732', '11732']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0654_Duplicate_same_occasion_code_12203_x2___test_4(self):
        """Duplicate same_occasion code (12203 x2) - test 4 (Difficulty: moderate)"""
        codes = ['12203', '12203']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0655_Duplicate_same_occasion_code_12204_x2___test_5(self):
        """Duplicate same_occasion code (12204 x2) - test 5 (Difficulty: moderate)"""
        codes = ['12204', '12204']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0656_Duplicate_same_occasion_code_12205_x2___test_6(self):
        """Duplicate same_occasion code (12205 x2) - test 6 (Difficulty: moderate)"""
        codes = ['12205', '12205']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0657_Duplicate_same_occasion_code_12207_x2___test_7(self):
        """Duplicate same_occasion code (12207 x2) - test 7 (Difficulty: moderate)"""
        codes = ['12207', '12207']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0658_Duplicate_same_occasion_code_12208_x2___test_8(self):
        """Duplicate same_occasion code (12208 x2) - test 8 (Difficulty: moderate)"""
        codes = ['12208', '12208']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0659_Duplicate_same_occasion_code_12210_x2___test_9(self):
        """Duplicate same_occasion code (12210 x2) - test 9 (Difficulty: moderate)"""
        codes = ['12210', '12210']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0660_Duplicate_same_occasion_code_12213_x2___test_10(self):
        """Duplicate same_occasion code (12213 x2) - test 10 (Difficulty: moderate)"""
        codes = ['12213', '12213']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0661_Duplicate_same_occasion_code_12215_x2___test_11(self):
        """Duplicate same_occasion code (12215 x2) - test 11 (Difficulty: moderate)"""
        codes = ['12215', '12215']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0662_Duplicate_same_occasion_code_12217_x2___test_12(self):
        """Duplicate same_occasion code (12217 x2) - test 12 (Difficulty: moderate)"""
        codes = ['12217', '12217']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0663_Duplicate_same_occasion_code_12250_x2___test_13(self):
        """Duplicate same_occasion code (12250 x2) - test 13 (Difficulty: moderate)"""
        codes = ['12250', '12250']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0664_Duplicate_same_occasion_code_12254_x2___test_14(self):
        """Duplicate same_occasion code (12254 x2) - test 14 (Difficulty: moderate)"""
        codes = ['12254', '12254']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0665_Duplicate_same_occasion_code_12258_x2___test_15(self):
        """Duplicate same_occasion code (12258 x2) - test 15 (Difficulty: moderate)"""
        codes = ['12258', '12258']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0666_Duplicate_same_occasion_code_12261_x2___test_16(self):
        """Duplicate same_occasion code (12261 x2) - test 16 (Difficulty: moderate)"""
        codes = ['12261', '12261']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0667_Duplicate_same_occasion_code_12265_x2___test_17(self):
        """Duplicate same_occasion code (12265 x2) - test 17 (Difficulty: moderate)"""
        codes = ['12265', '12265']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0668_Duplicate_same_occasion_code_12268_x2___test_18(self):
        """Duplicate same_occasion code (12268 x2) - test 18 (Difficulty: moderate)"""
        codes = ['12268', '12268']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0669_Duplicate_same_occasion_code_12272_x2___test_19(self):
        """Duplicate same_occasion code (12272 x2) - test 19 (Difficulty: moderate)"""
        codes = ['12272', '12272']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0670_Duplicate_same_occasion_code_18360_x2___test_20(self):
        """Duplicate same_occasion code (18360 x2) - test 20 (Difficulty: moderate)"""
        codes = ['18360', '18360']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0671_Duplicate_same_occasion_code_18375_x2___test_21(self):
        """Duplicate same_occasion code (18375 x2) - test 21 (Difficulty: moderate)"""
        codes = ['18375', '18375']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0672_Duplicate_same_occasion_code_18379_x2___test_22(self):
        """Duplicate same_occasion code (18379 x2) - test 22 (Difficulty: moderate)"""
        codes = ['18379', '18379']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0673_Duplicate_same_occasion_code_193_x2___test_23(self):
        """Duplicate same_occasion code (193 x2) - test 23 (Difficulty: moderate)"""
        codes = ['193', '193']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0674_Duplicate_same_occasion_code_195_x2___test_24(self):
        """Duplicate same_occasion code (195 x2) - test 24 (Difficulty: moderate)"""
        codes = ['195', '195']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0675_Duplicate_same_occasion_code_197_x2___test_25(self):
        """Duplicate same_occasion code (197 x2) - test 25 (Difficulty: moderate)"""
        codes = ['197', '197']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0676_Duplicate_same_occasion_code_199_x2___test_26(self):
        """Duplicate same_occasion code (199 x2) - test 26 (Difficulty: moderate)"""
        codes = ['199', '199']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0677_Duplicate_same_occasion_code_22052_x2___test_27(self):
        """Duplicate same_occasion code (22052 x2) - test 27 (Difficulty: moderate)"""
        codes = ['22052', '22052']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0678_Duplicate_same_occasion_code_22053_x2___test_28(self):
        """Duplicate same_occasion code (22053 x2) - test 28 (Difficulty: moderate)"""
        codes = ['22053', '22053']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0679_Duplicate_same_occasion_code_22054_x2___test_29(self):
        """Duplicate same_occasion code (22054 x2) - test 29 (Difficulty: moderate)"""
        codes = ['22054', '22054']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0680_Duplicate_same_occasion_code_34103_x2___test_30(self):
        """Duplicate same_occasion code (34103 x2) - test 30 (Difficulty: moderate)"""
        codes = ['34103', '34103']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0681_Duplicate_same_occasion_code_342_x2___test_31(self):
        """Duplicate same_occasion code (342 x2) - test 31 (Difficulty: moderate)"""
        codes = ['342', '342']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0682_Duplicate_same_occasion_code_344_x2___test_32(self):
        """Duplicate same_occasion code (344 x2) - test 32 (Difficulty: moderate)"""
        codes = ['344', '344']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0683_Duplicate_same_occasion_code_346_x2___test_33(self):
        """Duplicate same_occasion code (346 x2) - test 33 (Difficulty: moderate)"""
        codes = ['346', '346']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0684_Duplicate_same_occasion_code_41674_x2___test_34(self):
        """Duplicate same_occasion code (41674 x2) - test 34 (Difficulty: moderate)"""
        codes = ['41674', '41674']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0685_Duplicate_same_occasion_code_46150_x2___test_35(self):
        """Duplicate same_occasion code (46150 x2) - test 35 (Difficulty: moderate)"""
        codes = ['46150', '46150']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0686_Duplicate_same_occasion_code_46151_x2___test_36(self):
        """Duplicate same_occasion code (46151 x2) - test 36 (Difficulty: moderate)"""
        codes = ['46151', '46151']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0687_Duplicate_same_occasion_code_46152_x2___test_37(self):
        """Duplicate same_occasion code (46152 x2) - test 37 (Difficulty: moderate)"""
        codes = ['46152', '46152']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0688_Duplicate_same_occasion_code_46153_x2___test_38(self):
        """Duplicate same_occasion code (46153 x2) - test 38 (Difficulty: moderate)"""
        codes = ['46153', '46153']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0689_Duplicate_same_occasion_code_46154_x2___test_39(self):
        """Duplicate same_occasion code (46154 x2) - test 39 (Difficulty: moderate)"""
        codes = ['46154', '46154']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0690_Duplicate_same_occasion_code_46155_x2___test_40(self):
        """Duplicate same_occasion code (46155 x2) - test 40 (Difficulty: moderate)"""
        codes = ['46155', '46155']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0691_Duplicate_same_occasion_code_46156_x2___test_41(self):
        """Duplicate same_occasion code (46156 x2) - test 41 (Difficulty: moderate)"""
        codes = ['46156', '46156']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0692_Duplicate_same_occasion_code_46157_x2___test_42(self):
        """Duplicate same_occasion code (46157 x2) - test 42 (Difficulty: moderate)"""
        codes = ['46157', '46157']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0693_Duplicate_same_occasion_code_46158_x2___test_43(self):
        """Duplicate same_occasion code (46158 x2) - test 43 (Difficulty: moderate)"""
        codes = ['46158', '46158']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0694_Duplicate_same_occasion_code_47316_x2___test_44(self):
        """Duplicate same_occasion code (47316 x2) - test 44 (Difficulty: moderate)"""
        codes = ['47316', '47316']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0695_Duplicate_same_occasion_code_47319_x2___test_45(self):
        """Duplicate same_occasion code (47319 x2) - test 45 (Difficulty: moderate)"""
        codes = ['47319', '47319']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0696_Duplicate_same_occasion_code_53060_x2___test_46(self):
        """Duplicate same_occasion code (53060 x2) - test 46 (Difficulty: moderate)"""
        codes = ['53060', '53060']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0697_Duplicate_same_occasion_code_6028_x2___test_47(self):
        """Duplicate same_occasion code (6028 x2) - test 47 (Difficulty: moderate)"""
        codes = ['6028', '6028']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0698_Duplicate_same_occasion_code_75009_x2___test_48(self):
        """Duplicate same_occasion code (75009 x2) - test 48 (Difficulty: moderate)"""
        codes = ['75009', '75009']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0699_Duplicate_same_occasion_code_75010_x2___test_49(self):
        """Duplicate same_occasion code (75010 x2) - test 49 (Difficulty: moderate)"""
        codes = ['75010', '75010']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0700_Duplicate_same_occasion_code_75011_x2___test_50(self):
        """Duplicate same_occasion code (75011 x2) - test 50 (Difficulty: moderate)"""
        codes = ['75011', '75011']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0701_Duplicate_same_occasion_code_75012_x2___test_51(self):
        """Duplicate same_occasion code (75012 x2) - test 51 (Difficulty: moderate)"""
        codes = ['75012', '75012']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0702_Duplicate_same_occasion_code_75015_x2___test_52(self):
        """Duplicate same_occasion code (75015 x2) - test 52 (Difficulty: moderate)"""
        codes = ['75015', '75015']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0703_Duplicate_same_occasion_code_82115_x2___test_53(self):
        """Duplicate same_occasion code (82115 x2) - test 53 (Difficulty: moderate)"""
        codes = ['82115', '82115']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0704_Duplicate_same_occasion_code_92455_x2___test_54(self):
        """Duplicate same_occasion code (92455 x2) - test 54 (Difficulty: moderate)"""
        codes = ['92455', '92455']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0705_Duplicate_same_occasion_code_92456_x2___test_55(self):
        """Duplicate same_occasion code (92456 x2) - test 55 (Difficulty: moderate)"""
        codes = ['92456', '92456']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0706_Duplicate_same_occasion_code_92457_x2___test_56(self):
        """Duplicate same_occasion code (92457 x2) - test 56 (Difficulty: moderate)"""
        codes = ['92457', '92457']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0707_Duplicate_same_occasion_code_11729_x2___test_57(self):
        """Duplicate same_occasion code (11729 x2) - test 57 (Difficulty: moderate)"""
        codes = ['11729', '11729']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0708_Duplicate_same_occasion_code_11730_x2___test_58(self):
        """Duplicate same_occasion code (11730 x2) - test 58 (Difficulty: moderate)"""
        codes = ['11730', '11730']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0709_Duplicate_same_occasion_code_11732_x2___test_59(self):
        """Duplicate same_occasion code (11732 x2) - test 59 (Difficulty: moderate)"""
        codes = ['11732', '11732']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0710_Duplicate_same_occasion_code_12203_x2___test_60(self):
        """Duplicate same_occasion code (12203 x2) - test 60 (Difficulty: moderate)"""
        codes = ['12203', '12203']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0711_Duplicate_same_occasion_code_12204_x2___test_61(self):
        """Duplicate same_occasion code (12204 x2) - test 61 (Difficulty: moderate)"""
        codes = ['12204', '12204']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0712_Duplicate_same_occasion_code_12205_x2___test_62(self):
        """Duplicate same_occasion code (12205 x2) - test 62 (Difficulty: moderate)"""
        codes = ['12205', '12205']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0713_Duplicate_same_occasion_code_12207_x2___test_63(self):
        """Duplicate same_occasion code (12207 x2) - test 63 (Difficulty: moderate)"""
        codes = ['12207', '12207']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0714_Duplicate_same_occasion_code_12208_x2___test_64(self):
        """Duplicate same_occasion code (12208 x2) - test 64 (Difficulty: moderate)"""
        codes = ['12208', '12208']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0715_Duplicate_same_occasion_code_12210_x2___test_65(self):
        """Duplicate same_occasion code (12210 x2) - test 65 (Difficulty: moderate)"""
        codes = ['12210', '12210']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0716_Duplicate_same_occasion_code_12213_x2___test_66(self):
        """Duplicate same_occasion code (12213 x2) - test 66 (Difficulty: moderate)"""
        codes = ['12213', '12213']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0717_Duplicate_same_occasion_code_12215_x2___test_67(self):
        """Duplicate same_occasion code (12215 x2) - test 67 (Difficulty: moderate)"""
        codes = ['12215', '12215']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0718_Duplicate_same_occasion_code_12217_x2___test_68(self):
        """Duplicate same_occasion code (12217 x2) - test 68 (Difficulty: moderate)"""
        codes = ['12217', '12217']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0719_Duplicate_same_occasion_code_12250_x2___test_69(self):
        """Duplicate same_occasion code (12250 x2) - test 69 (Difficulty: moderate)"""
        codes = ['12250', '12250']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0720_Duplicate_same_occasion_code_12254_x2___test_70(self):
        """Duplicate same_occasion code (12254 x2) - test 70 (Difficulty: moderate)"""
        codes = ['12254', '12254']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0721_Multiple_duplicates_11729_x3___test_1(self):
        """Multiple duplicates (11729 x3) - test 1 (Difficulty: advanced)"""
        codes = ['11729', '11729', '11729']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0722_Multiple_duplicates_11730_x3___test_2(self):
        """Multiple duplicates (11730 x3) - test 2 (Difficulty: advanced)"""
        codes = ['11730', '11730', '11730']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0723_Multiple_duplicates_11732_x3___test_3(self):
        """Multiple duplicates (11732 x3) - test 3 (Difficulty: advanced)"""
        codes = ['11732', '11732', '11732']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0724_Multiple_duplicates_12203_x3___test_4(self):
        """Multiple duplicates (12203 x3) - test 4 (Difficulty: advanced)"""
        codes = ['12203', '12203', '12203']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0725_Multiple_duplicates_12204_x3___test_5(self):
        """Multiple duplicates (12204 x3) - test 5 (Difficulty: advanced)"""
        codes = ['12204', '12204', '12204']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0726_Multiple_duplicates_12205_x3___test_6(self):
        """Multiple duplicates (12205 x3) - test 6 (Difficulty: advanced)"""
        codes = ['12205', '12205', '12205']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0727_Multiple_duplicates_12207_x3___test_7(self):
        """Multiple duplicates (12207 x3) - test 7 (Difficulty: advanced)"""
        codes = ['12207', '12207', '12207']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0728_Multiple_duplicates_12208_x3___test_8(self):
        """Multiple duplicates (12208 x3) - test 8 (Difficulty: advanced)"""
        codes = ['12208', '12208', '12208']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0729_Multiple_duplicates_12210_x3___test_9(self):
        """Multiple duplicates (12210 x3) - test 9 (Difficulty: advanced)"""
        codes = ['12210', '12210', '12210']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0730_Multiple_duplicates_12213_x3___test_10(self):
        """Multiple duplicates (12213 x3) - test 10 (Difficulty: advanced)"""
        codes = ['12213', '12213', '12213']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0731_Multiple_duplicates_12215_x3___test_11(self):
        """Multiple duplicates (12215 x3) - test 11 (Difficulty: advanced)"""
        codes = ['12215', '12215', '12215']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0732_Multiple_duplicates_12217_x3___test_12(self):
        """Multiple duplicates (12217 x3) - test 12 (Difficulty: advanced)"""
        codes = ['12217', '12217', '12217']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0733_Multiple_duplicates_12250_x3___test_13(self):
        """Multiple duplicates (12250 x3) - test 13 (Difficulty: advanced)"""
        codes = ['12250', '12250', '12250']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0734_Multiple_duplicates_12254_x3___test_14(self):
        """Multiple duplicates (12254 x3) - test 14 (Difficulty: advanced)"""
        codes = ['12254', '12254', '12254']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0735_Multiple_duplicates_12258_x3___test_15(self):
        """Multiple duplicates (12258 x3) - test 15 (Difficulty: advanced)"""
        codes = ['12258', '12258', '12258']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0736_Multiple_duplicates_12261_x3___test_16(self):
        """Multiple duplicates (12261 x3) - test 16 (Difficulty: advanced)"""
        codes = ['12261', '12261', '12261']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0737_Multiple_duplicates_12265_x3___test_17(self):
        """Multiple duplicates (12265 x3) - test 17 (Difficulty: advanced)"""
        codes = ['12265', '12265', '12265']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0738_Multiple_duplicates_12268_x3___test_18(self):
        """Multiple duplicates (12268 x3) - test 18 (Difficulty: advanced)"""
        codes = ['12268', '12268', '12268']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0739_Multiple_duplicates_12272_x3___test_19(self):
        """Multiple duplicates (12272 x3) - test 19 (Difficulty: advanced)"""
        codes = ['12272', '12272', '12272']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0740_Multiple_duplicates_18360_x3___test_20(self):
        """Multiple duplicates (18360 x3) - test 20 (Difficulty: advanced)"""
        codes = ['18360', '18360', '18360']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0741_Multiple_duplicates_18375_x3___test_21(self):
        """Multiple duplicates (18375 x3) - test 21 (Difficulty: advanced)"""
        codes = ['18375', '18375', '18375']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0742_Multiple_duplicates_18379_x3___test_22(self):
        """Multiple duplicates (18379 x3) - test 22 (Difficulty: advanced)"""
        codes = ['18379', '18379', '18379']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0743_Multiple_duplicates_193_x3___test_23(self):
        """Multiple duplicates (193 x3) - test 23 (Difficulty: advanced)"""
        codes = ['193', '193', '193']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0744_Multiple_duplicates_195_x3___test_24(self):
        """Multiple duplicates (195 x3) - test 24 (Difficulty: advanced)"""
        codes = ['195', '195', '195']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0745_Multiple_duplicates_197_x3___test_25(self):
        """Multiple duplicates (197 x3) - test 25 (Difficulty: advanced)"""
        codes = ['197', '197', '197']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0746_Multiple_duplicates_199_x3___test_26(self):
        """Multiple duplicates (199 x3) - test 26 (Difficulty: advanced)"""
        codes = ['199', '199', '199']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0747_Multiple_duplicates_22052_x3___test_27(self):
        """Multiple duplicates (22052 x3) - test 27 (Difficulty: advanced)"""
        codes = ['22052', '22052', '22052']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0748_Multiple_duplicates_22053_x3___test_28(self):
        """Multiple duplicates (22053 x3) - test 28 (Difficulty: advanced)"""
        codes = ['22053', '22053', '22053']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0749_Multiple_duplicates_22054_x3___test_29(self):
        """Multiple duplicates (22054 x3) - test 29 (Difficulty: advanced)"""
        codes = ['22054', '22054', '22054']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        
    def test_c4_0750_Multiple_duplicates_34103_x3___test_30(self):
        """Multiple duplicates (34103 x3) - test 30 (Difficulty: advanced)"""
        codes = ['34103', '34103', '34103']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'NAY', \
            f"Expected NAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == 'C4', \
            f"Expected failed_check 'C4', got {result['failed_check']}"
        

    # ===== YAY Tests (250 tests) =====

    def test_yay_0751_Single_valid_code_104(self):
        """Single valid code (104) (Difficulty: basic)"""
        codes = ['104']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0752_Single_valid_code_105(self):
        """Single valid code (105) (Difficulty: basic)"""
        codes = ['105']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0753_Single_valid_code_106(self):
        """Single valid code (106) (Difficulty: basic)"""
        codes = ['106']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0754_Single_valid_code_107(self):
        """Single valid code (107) (Difficulty: basic)"""
        codes = ['107']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0755_Single_valid_code_108(self):
        """Single valid code (108) (Difficulty: basic)"""
        codes = ['108']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0756_Single_valid_code_10801(self):
        """Single valid code (10801) (Difficulty: basic)"""
        codes = ['10801']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0757_Single_valid_code_10802(self):
        """Single valid code (10802) (Difficulty: basic)"""
        codes = ['10802']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0758_Single_valid_code_10803(self):
        """Single valid code (10803) (Difficulty: basic)"""
        codes = ['10803']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0759_Single_valid_code_10804(self):
        """Single valid code (10804) (Difficulty: basic)"""
        codes = ['10804']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0760_Single_valid_code_10805(self):
        """Single valid code (10805) (Difficulty: basic)"""
        codes = ['10805']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0761_Single_valid_code_10806(self):
        """Single valid code (10806) (Difficulty: basic)"""
        codes = ['10806']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0762_Single_valid_code_10807(self):
        """Single valid code (10807) (Difficulty: basic)"""
        codes = ['10807']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0763_Single_valid_code_10808(self):
        """Single valid code (10808) (Difficulty: basic)"""
        codes = ['10808']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0764_Single_valid_code_10809(self):
        """Single valid code (10809) (Difficulty: basic)"""
        codes = ['10809']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0765_Single_valid_code_10816(self):
        """Single valid code (10816) (Difficulty: basic)"""
        codes = ['10816']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0766_Single_valid_code_109(self):
        """Single valid code (109) (Difficulty: basic)"""
        codes = ['109']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0767_Single_valid_code_10905(self):
        """Single valid code (10905) (Difficulty: basic)"""
        codes = ['10905']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0768_Single_valid_code_10907(self):
        """Single valid code (10907) (Difficulty: basic)"""
        codes = ['10907']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0769_Single_valid_code_10910(self):
        """Single valid code (10910) (Difficulty: basic)"""
        codes = ['10910']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0770_Single_valid_code_10911(self):
        """Single valid code (10911) (Difficulty: basic)"""
        codes = ['10911']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0771_Single_valid_code_10913(self):
        """Single valid code (10913) (Difficulty: basic)"""
        codes = ['10913']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0772_Single_valid_code_10914(self):
        """Single valid code (10914) (Difficulty: basic)"""
        codes = ['10914']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0773_Single_valid_code_10915(self):
        """Single valid code (10915) (Difficulty: basic)"""
        codes = ['10915']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0774_Single_valid_code_10916(self):
        """Single valid code (10916) (Difficulty: basic)"""
        codes = ['10916']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0775_Single_valid_code_10918(self):
        """Single valid code (10918) (Difficulty: basic)"""
        codes = ['10918']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0776_Single_valid_code_10921(self):
        """Single valid code (10921) (Difficulty: basic)"""
        codes = ['10921']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0777_Single_valid_code_10924(self):
        """Single valid code (10924) (Difficulty: basic)"""
        codes = ['10924']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0778_Single_valid_code_10926(self):
        """Single valid code (10926) (Difficulty: basic)"""
        codes = ['10926']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0779_Single_valid_code_10927(self):
        """Single valid code (10927) (Difficulty: basic)"""
        codes = ['10927']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0780_Single_valid_code_10928(self):
        """Single valid code (10928) (Difficulty: basic)"""
        codes = ['10928']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0781_Single_valid_code_10929(self):
        """Single valid code (10929) (Difficulty: basic)"""
        codes = ['10929']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0782_Single_valid_code_10930(self):
        """Single valid code (10930) (Difficulty: basic)"""
        codes = ['10930']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0783_Single_valid_code_10931(self):
        """Single valid code (10931) (Difficulty: basic)"""
        codes = ['10931']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0784_Single_valid_code_10938(self):
        """Single valid code (10938) (Difficulty: basic)"""
        codes = ['10938']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0785_Single_valid_code_10939(self):
        """Single valid code (10939) (Difficulty: basic)"""
        codes = ['10939']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0786_Single_valid_code_10940(self):
        """Single valid code (10940) (Difficulty: basic)"""
        codes = ['10940']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0787_Single_valid_code_10941(self):
        """Single valid code (10941) (Difficulty: basic)"""
        codes = ['10941']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0788_Single_valid_code_10942(self):
        """Single valid code (10942) (Difficulty: basic)"""
        codes = ['10942']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0789_Single_valid_code_10943(self):
        """Single valid code (10943) (Difficulty: basic)"""
        codes = ['10943']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0790_Single_valid_code_10944(self):
        """Single valid code (10944) (Difficulty: basic)"""
        codes = ['10944']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0791_Single_valid_code_10945(self):
        """Single valid code (10945) (Difficulty: basic)"""
        codes = ['10945']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0792_Single_valid_code_10946(self):
        """Single valid code (10946) (Difficulty: basic)"""
        codes = ['10946']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0793_Single_valid_code_10950(self):
        """Single valid code (10950) (Difficulty: basic)"""
        codes = ['10950']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0794_Single_valid_code_10951(self):
        """Single valid code (10951) (Difficulty: basic)"""
        codes = ['10951']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0795_Single_valid_code_10952(self):
        """Single valid code (10952) (Difficulty: basic)"""
        codes = ['10952']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0796_Single_valid_code_10953(self):
        """Single valid code (10953) (Difficulty: basic)"""
        codes = ['10953']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0797_Single_valid_code_10954(self):
        """Single valid code (10954) (Difficulty: basic)"""
        codes = ['10954']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0798_Single_valid_code_10955(self):
        """Single valid code (10955) (Difficulty: basic)"""
        codes = ['10955']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0799_Single_valid_code_10956(self):
        """Single valid code (10956) (Difficulty: basic)"""
        codes = ['10956']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0800_Single_valid_code_10957(self):
        """Single valid code (10957) (Difficulty: basic)"""
        codes = ['10957']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0801_Compatible_codes_104_and_10801___test_1(self):
        """Compatible codes (104 and 10801) - test 1 (Difficulty: moderate)"""
        codes = ['104', '10801']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0802_Compatible_codes_104_and_10802___test_2(self):
        """Compatible codes (104 and 10802) - test 2 (Difficulty: moderate)"""
        codes = ['104', '10802']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0803_Compatible_codes_104_and_10803___test_3(self):
        """Compatible codes (104 and 10803) - test 3 (Difficulty: moderate)"""
        codes = ['104', '10803']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0804_Compatible_codes_104_and_10804___test_4(self):
        """Compatible codes (104 and 10804) - test 4 (Difficulty: moderate)"""
        codes = ['104', '10804']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0805_Compatible_codes_104_and_10805___test_5(self):
        """Compatible codes (104 and 10805) - test 5 (Difficulty: moderate)"""
        codes = ['104', '10805']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0806_Compatible_codes_104_and_10806___test_6(self):
        """Compatible codes (104 and 10806) - test 6 (Difficulty: moderate)"""
        codes = ['104', '10806']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0807_Compatible_codes_104_and_10807___test_7(self):
        """Compatible codes (104 and 10807) - test 7 (Difficulty: moderate)"""
        codes = ['104', '10807']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0808_Compatible_codes_104_and_10808___test_8(self):
        """Compatible codes (104 and 10808) - test 8 (Difficulty: moderate)"""
        codes = ['104', '10808']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0809_Compatible_codes_104_and_10809___test_9(self):
        """Compatible codes (104 and 10809) - test 9 (Difficulty: moderate)"""
        codes = ['104', '10809']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0810_Compatible_codes_104_and_10816___test_10(self):
        """Compatible codes (104 and 10816) - test 10 (Difficulty: moderate)"""
        codes = ['104', '10816']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0811_Compatible_codes_104_and_10905___test_11(self):
        """Compatible codes (104 and 10905) - test 11 (Difficulty: moderate)"""
        codes = ['104', '10905']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0812_Compatible_codes_104_and_10907___test_12(self):
        """Compatible codes (104 and 10907) - test 12 (Difficulty: moderate)"""
        codes = ['104', '10907']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0813_Compatible_codes_104_and_10910___test_13(self):
        """Compatible codes (104 and 10910) - test 13 (Difficulty: moderate)"""
        codes = ['104', '10910']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0814_Compatible_codes_104_and_10911___test_14(self):
        """Compatible codes (104 and 10911) - test 14 (Difficulty: moderate)"""
        codes = ['104', '10911']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0815_Compatible_codes_104_and_10913___test_15(self):
        """Compatible codes (104 and 10913) - test 15 (Difficulty: moderate)"""
        codes = ['104', '10913']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0816_Compatible_codes_104_and_10914___test_16(self):
        """Compatible codes (104 and 10914) - test 16 (Difficulty: moderate)"""
        codes = ['104', '10914']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0817_Compatible_codes_104_and_10915___test_17(self):
        """Compatible codes (104 and 10915) - test 17 (Difficulty: moderate)"""
        codes = ['104', '10915']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0818_Compatible_codes_104_and_10916___test_18(self):
        """Compatible codes (104 and 10916) - test 18 (Difficulty: moderate)"""
        codes = ['104', '10916']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0819_Compatible_codes_104_and_10918___test_19(self):
        """Compatible codes (104 and 10918) - test 19 (Difficulty: moderate)"""
        codes = ['104', '10918']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0820_Compatible_codes_104_and_10921___test_20(self):
        """Compatible codes (104 and 10921) - test 20 (Difficulty: moderate)"""
        codes = ['104', '10921']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0821_Compatible_codes_104_and_10924___test_21(self):
        """Compatible codes (104 and 10924) - test 21 (Difficulty: moderate)"""
        codes = ['104', '10924']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0822_Compatible_codes_104_and_10926___test_22(self):
        """Compatible codes (104 and 10926) - test 22 (Difficulty: moderate)"""
        codes = ['104', '10926']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0823_Compatible_codes_104_and_10927___test_23(self):
        """Compatible codes (104 and 10927) - test 23 (Difficulty: moderate)"""
        codes = ['104', '10927']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0824_Compatible_codes_104_and_10928___test_24(self):
        """Compatible codes (104 and 10928) - test 24 (Difficulty: moderate)"""
        codes = ['104', '10928']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0825_Compatible_codes_104_and_10929___test_25(self):
        """Compatible codes (104 and 10929) - test 25 (Difficulty: moderate)"""
        codes = ['104', '10929']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0826_Compatible_codes_104_and_10930___test_26(self):
        """Compatible codes (104 and 10930) - test 26 (Difficulty: moderate)"""
        codes = ['104', '10930']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0827_Compatible_codes_104_and_10931___test_27(self):
        """Compatible codes (104 and 10931) - test 27 (Difficulty: moderate)"""
        codes = ['104', '10931']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0828_Compatible_codes_104_and_10938___test_28(self):
        """Compatible codes (104 and 10938) - test 28 (Difficulty: moderate)"""
        codes = ['104', '10938']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0829_Compatible_codes_104_and_10939___test_29(self):
        """Compatible codes (104 and 10939) - test 29 (Difficulty: moderate)"""
        codes = ['104', '10939']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0830_Compatible_codes_104_and_10940___test_30(self):
        """Compatible codes (104 and 10940) - test 30 (Difficulty: moderate)"""
        codes = ['104', '10940']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0831_Compatible_codes_104_and_10941___test_31(self):
        """Compatible codes (104 and 10941) - test 31 (Difficulty: moderate)"""
        codes = ['104', '10941']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0832_Compatible_codes_104_and_10942___test_32(self):
        """Compatible codes (104 and 10942) - test 32 (Difficulty: moderate)"""
        codes = ['104', '10942']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0833_Compatible_codes_104_and_10943___test_33(self):
        """Compatible codes (104 and 10943) - test 33 (Difficulty: moderate)"""
        codes = ['104', '10943']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0834_Compatible_codes_104_and_10944___test_34(self):
        """Compatible codes (104 and 10944) - test 34 (Difficulty: moderate)"""
        codes = ['104', '10944']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0835_Compatible_codes_104_and_10945___test_35(self):
        """Compatible codes (104 and 10945) - test 35 (Difficulty: moderate)"""
        codes = ['104', '10945']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0836_Compatible_codes_104_and_10946___test_36(self):
        """Compatible codes (104 and 10946) - test 36 (Difficulty: moderate)"""
        codes = ['104', '10946']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0837_Compatible_codes_104_and_10950___test_37(self):
        """Compatible codes (104 and 10950) - test 37 (Difficulty: moderate)"""
        codes = ['104', '10950']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0838_Compatible_codes_104_and_10951___test_38(self):
        """Compatible codes (104 and 10951) - test 38 (Difficulty: moderate)"""
        codes = ['104', '10951']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0839_Compatible_codes_104_and_10952___test_39(self):
        """Compatible codes (104 and 10952) - test 39 (Difficulty: moderate)"""
        codes = ['104', '10952']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0840_Compatible_codes_104_and_10953___test_40(self):
        """Compatible codes (104 and 10953) - test 40 (Difficulty: moderate)"""
        codes = ['104', '10953']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0841_Compatible_codes_104_and_10954___test_41(self):
        """Compatible codes (104 and 10954) - test 41 (Difficulty: moderate)"""
        codes = ['104', '10954']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0842_Compatible_codes_104_and_10955___test_42(self):
        """Compatible codes (104 and 10955) - test 42 (Difficulty: moderate)"""
        codes = ['104', '10955']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0843_Compatible_codes_104_and_10956___test_43(self):
        """Compatible codes (104 and 10956) - test 43 (Difficulty: moderate)"""
        codes = ['104', '10956']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0844_Compatible_codes_104_and_10957___test_44(self):
        """Compatible codes (104 and 10957) - test 44 (Difficulty: moderate)"""
        codes = ['104', '10957']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0845_Compatible_codes_104_and_10958___test_45(self):
        """Compatible codes (104 and 10958) - test 45 (Difficulty: moderate)"""
        codes = ['104', '10958']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0846_Compatible_codes_104_and_10959___test_46(self):
        """Compatible codes (104 and 10959) - test 46 (Difficulty: moderate)"""
        codes = ['104', '10959']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0847_Compatible_codes_104_and_10960___test_47(self):
        """Compatible codes (104 and 10960) - test 47 (Difficulty: moderate)"""
        codes = ['104', '10960']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0848_Compatible_codes_104_and_10962___test_48(self):
        """Compatible codes (104 and 10962) - test 48 (Difficulty: moderate)"""
        codes = ['104', '10962']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0849_Compatible_codes_104_and_10964___test_49(self):
        """Compatible codes (104 and 10964) - test 49 (Difficulty: moderate)"""
        codes = ['104', '10964']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0850_Compatible_codes_104_and_10966___test_50(self):
        """Compatible codes (104 and 10966) - test 50 (Difficulty: moderate)"""
        codes = ['104', '10966']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0851_Compatible_codes_104_and_10968___test_51(self):
        """Compatible codes (104 and 10968) - test 51 (Difficulty: moderate)"""
        codes = ['104', '10968']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0852_Compatible_codes_104_and_10970___test_52(self):
        """Compatible codes (104 and 10970) - test 52 (Difficulty: moderate)"""
        codes = ['104', '10970']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0853_Compatible_codes_104_and_10983___test_53(self):
        """Compatible codes (104 and 10983) - test 53 (Difficulty: moderate)"""
        codes = ['104', '10983']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0854_Compatible_codes_104_and_10987___test_54(self):
        """Compatible codes (104 and 10987) - test 54 (Difficulty: moderate)"""
        codes = ['104', '10987']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0855_Compatible_codes_104_and_10988___test_55(self):
        """Compatible codes (104 and 10988) - test 55 (Difficulty: moderate)"""
        codes = ['104', '10988']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0856_Compatible_codes_104_and_10989___test_56(self):
        """Compatible codes (104 and 10989) - test 56 (Difficulty: moderate)"""
        codes = ['104', '10989']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0857_Compatible_codes_104_and_10990___test_57(self):
        """Compatible codes (104 and 10990) - test 57 (Difficulty: moderate)"""
        codes = ['104', '10990']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0858_Compatible_codes_104_and_10991___test_58(self):
        """Compatible codes (104 and 10991) - test 58 (Difficulty: moderate)"""
        codes = ['104', '10991']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0859_Compatible_codes_104_and_10992___test_59(self):
        """Compatible codes (104 and 10992) - test 59 (Difficulty: moderate)"""
        codes = ['104', '10992']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0860_Compatible_codes_104_and_10997___test_60(self):
        """Compatible codes (104 and 10997) - test 60 (Difficulty: moderate)"""
        codes = ['104', '10997']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0861_Compatible_codes_104_and_110___test_61(self):
        """Compatible codes (104 and 110) - test 61 (Difficulty: moderate)"""
        codes = ['104', '110']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0862_Compatible_codes_104_and_11000___test_62(self):
        """Compatible codes (104 and 11000) - test 62 (Difficulty: moderate)"""
        codes = ['104', '11000']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0863_Compatible_codes_104_and_11003___test_63(self):
        """Compatible codes (104 and 11003) - test 63 (Difficulty: moderate)"""
        codes = ['104', '11003']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0864_Compatible_codes_104_and_11004___test_64(self):
        """Compatible codes (104 and 11004) - test 64 (Difficulty: moderate)"""
        codes = ['104', '11004']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0865_Compatible_codes_104_and_11005___test_65(self):
        """Compatible codes (104 and 11005) - test 65 (Difficulty: moderate)"""
        codes = ['104', '11005']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0866_Compatible_codes_104_and_11009___test_66(self):
        """Compatible codes (104 and 11009) - test 66 (Difficulty: moderate)"""
        codes = ['104', '11009']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0867_Compatible_codes_104_and_11012___test_67(self):
        """Compatible codes (104 and 11012) - test 67 (Difficulty: moderate)"""
        codes = ['104', '11012']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0868_Compatible_codes_104_and_11015___test_68(self):
        """Compatible codes (104 and 11015) - test 68 (Difficulty: moderate)"""
        codes = ['104', '11015']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0869_Compatible_codes_104_and_11018___test_69(self):
        """Compatible codes (104 and 11018) - test 69 (Difficulty: moderate)"""
        codes = ['104', '11018']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0870_Compatible_codes_104_and_11021___test_70(self):
        """Compatible codes (104 and 11021) - test 70 (Difficulty: moderate)"""
        codes = ['104', '11021']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0871_Compatible_codes_104_and_11024___test_71(self):
        """Compatible codes (104 and 11024) - test 71 (Difficulty: moderate)"""
        codes = ['104', '11024']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0872_Compatible_codes_104_and_11027___test_72(self):
        """Compatible codes (104 and 11027) - test 72 (Difficulty: moderate)"""
        codes = ['104', '11027']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0873_Compatible_codes_104_and_11200___test_73(self):
        """Compatible codes (104 and 11200) - test 73 (Difficulty: moderate)"""
        codes = ['104', '11200']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0874_Compatible_codes_104_and_11204___test_74(self):
        """Compatible codes (104 and 11204) - test 74 (Difficulty: moderate)"""
        codes = ['104', '11204']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0875_Compatible_codes_104_and_11205___test_75(self):
        """Compatible codes (104 and 11205) - test 75 (Difficulty: moderate)"""
        codes = ['104', '11205']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0876_Compatible_codes_104_and_11210___test_76(self):
        """Compatible codes (104 and 11210) - test 76 (Difficulty: moderate)"""
        codes = ['104', '11210']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0877_Compatible_codes_104_and_11211___test_77(self):
        """Compatible codes (104 and 11211) - test 77 (Difficulty: moderate)"""
        codes = ['104', '11211']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0878_Compatible_codes_104_and_11215___test_78(self):
        """Compatible codes (104 and 11215) - test 78 (Difficulty: moderate)"""
        codes = ['104', '11215']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0879_Compatible_codes_104_and_11218___test_79(self):
        """Compatible codes (104 and 11218) - test 79 (Difficulty: moderate)"""
        codes = ['104', '11218']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0880_Compatible_codes_104_and_11219___test_80(self):
        """Compatible codes (104 and 11219) - test 80 (Difficulty: moderate)"""
        codes = ['104', '11219']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0881_Compatible_codes_104_and_11220___test_81(self):
        """Compatible codes (104 and 11220) - test 81 (Difficulty: moderate)"""
        codes = ['104', '11220']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0882_Compatible_codes_104_and_11221___test_82(self):
        """Compatible codes (104 and 11221) - test 82 (Difficulty: moderate)"""
        codes = ['104', '11221']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0883_Compatible_codes_104_and_11224___test_83(self):
        """Compatible codes (104 and 11224) - test 83 (Difficulty: moderate)"""
        codes = ['104', '11224']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0884_Compatible_codes_104_and_11235___test_84(self):
        """Compatible codes (104 and 11235) - test 84 (Difficulty: moderate)"""
        codes = ['104', '11235']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0885_Compatible_codes_104_and_11237___test_85(self):
        """Compatible codes (104 and 11237) - test 85 (Difficulty: moderate)"""
        codes = ['104', '11237']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0886_Compatible_codes_104_and_11240___test_86(self):
        """Compatible codes (104 and 11240) - test 86 (Difficulty: moderate)"""
        codes = ['104', '11240']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0887_Compatible_codes_104_and_11241___test_87(self):
        """Compatible codes (104 and 11241) - test 87 (Difficulty: moderate)"""
        codes = ['104', '11241']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0888_Compatible_codes_104_and_11242___test_88(self):
        """Compatible codes (104 and 11242) - test 88 (Difficulty: moderate)"""
        codes = ['104', '11242']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0889_Compatible_codes_104_and_11243___test_89(self):
        """Compatible codes (104 and 11243) - test 89 (Difficulty: moderate)"""
        codes = ['104', '11243']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0890_Compatible_codes_104_and_11244___test_90(self):
        """Compatible codes (104 and 11244) - test 90 (Difficulty: moderate)"""
        codes = ['104', '11244']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0891_Compatible_codes_104_and_11300___test_91(self):
        """Compatible codes (104 and 11300) - test 91 (Difficulty: moderate)"""
        codes = ['104', '11300']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0892_Compatible_codes_104_and_11302___test_92(self):
        """Compatible codes (104 and 11302) - test 92 (Difficulty: moderate)"""
        codes = ['104', '11302']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0893_Compatible_codes_104_and_11303___test_93(self):
        """Compatible codes (104 and 11303) - test 93 (Difficulty: moderate)"""
        codes = ['104', '11303']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0894_Compatible_codes_104_and_11304___test_94(self):
        """Compatible codes (104 and 11304) - test 94 (Difficulty: moderate)"""
        codes = ['104', '11304']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0895_Compatible_codes_104_and_11306___test_95(self):
        """Compatible codes (104 and 11306) - test 95 (Difficulty: moderate)"""
        codes = ['104', '11306']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0896_Compatible_codes_104_and_11309___test_96(self):
        """Compatible codes (104 and 11309) - test 96 (Difficulty: moderate)"""
        codes = ['104', '11309']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0897_Compatible_codes_104_and_11312___test_97(self):
        """Compatible codes (104 and 11312) - test 97 (Difficulty: moderate)"""
        codes = ['104', '11312']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0898_Compatible_codes_104_and_11315___test_98(self):
        """Compatible codes (104 and 11315) - test 98 (Difficulty: moderate)"""
        codes = ['104', '11315']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0899_Compatible_codes_104_and_11318___test_99(self):
        """Compatible codes (104 and 11318) - test 99 (Difficulty: moderate)"""
        codes = ['104', '11318']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0900_Compatible_codes_104_and_11324___test_100(self):
        """Compatible codes (104 and 11324) - test 100 (Difficulty: moderate)"""
        codes = ['104', '11324']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0901_Compatible_codes_104_and_11332___test_101(self):
        """Compatible codes (104 and 11332) - test 101 (Difficulty: moderate)"""
        codes = ['104', '11332']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0902_Compatible_codes_104_and_11340___test_102(self):
        """Compatible codes (104 and 11340) - test 102 (Difficulty: moderate)"""
        codes = ['104', '11340']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0903_Compatible_codes_104_and_11341___test_103(self):
        """Compatible codes (104 and 11341) - test 103 (Difficulty: moderate)"""
        codes = ['104', '11341']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0904_Compatible_codes_104_and_11342___test_104(self):
        """Compatible codes (104 and 11342) - test 104 (Difficulty: moderate)"""
        codes = ['104', '11342']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0905_Compatible_codes_104_and_11343___test_105(self):
        """Compatible codes (104 and 11343) - test 105 (Difficulty: moderate)"""
        codes = ['104', '11343']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0906_Compatible_codes_104_and_11345___test_106(self):
        """Compatible codes (104 and 11345) - test 106 (Difficulty: moderate)"""
        codes = ['104', '11345']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0907_Compatible_codes_104_and_11503___test_107(self):
        """Compatible codes (104 and 11503) - test 107 (Difficulty: moderate)"""
        codes = ['104', '11503']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0908_Compatible_codes_104_and_11505___test_108(self):
        """Compatible codes (104 and 11505) - test 108 (Difficulty: moderate)"""
        codes = ['104', '11505']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0909_Compatible_codes_104_and_11506___test_109(self):
        """Compatible codes (104 and 11506) - test 109 (Difficulty: moderate)"""
        codes = ['104', '11506']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0910_Compatible_codes_104_and_11507___test_110(self):
        """Compatible codes (104 and 11507) - test 110 (Difficulty: moderate)"""
        codes = ['104', '11507']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0911_Compatible_codes_104_and_11508___test_111(self):
        """Compatible codes (104 and 11508) - test 111 (Difficulty: moderate)"""
        codes = ['104', '11508']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0912_Compatible_codes_104_and_11512___test_112(self):
        """Compatible codes (104 and 11512) - test 112 (Difficulty: moderate)"""
        codes = ['104', '11512']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0913_Compatible_codes_104_and_116___test_113(self):
        """Compatible codes (104 and 116) - test 113 (Difficulty: moderate)"""
        codes = ['104', '116']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0914_Compatible_codes_104_and_11600___test_114(self):
        """Compatible codes (104 and 11600) - test 114 (Difficulty: moderate)"""
        codes = ['104', '11600']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0915_Compatible_codes_104_and_11602___test_115(self):
        """Compatible codes (104 and 11602) - test 115 (Difficulty: moderate)"""
        codes = ['104', '11602']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0916_Compatible_codes_104_and_11604___test_116(self):
        """Compatible codes (104 and 11604) - test 116 (Difficulty: moderate)"""
        codes = ['104', '11604']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0917_Compatible_codes_104_and_11605___test_117(self):
        """Compatible codes (104 and 11605) - test 117 (Difficulty: moderate)"""
        codes = ['104', '11605']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0918_Compatible_codes_104_and_11607___test_118(self):
        """Compatible codes (104 and 11607) - test 118 (Difficulty: moderate)"""
        codes = ['104', '11607']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0919_Compatible_codes_104_and_11610___test_119(self):
        """Compatible codes (104 and 11610) - test 119 (Difficulty: moderate)"""
        codes = ['104', '11610']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0920_Compatible_codes_104_and_11611___test_120(self):
        """Compatible codes (104 and 11611) - test 120 (Difficulty: moderate)"""
        codes = ['104', '11611']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0921_Compatible_codes_104_and_11612___test_121(self):
        """Compatible codes (104 and 11612) - test 121 (Difficulty: moderate)"""
        codes = ['104', '11612']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0922_Compatible_codes_104_and_11614___test_122(self):
        """Compatible codes (104 and 11614) - test 122 (Difficulty: moderate)"""
        codes = ['104', '11614']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0923_Compatible_codes_104_and_11615___test_123(self):
        """Compatible codes (104 and 11615) - test 123 (Difficulty: moderate)"""
        codes = ['104', '11615']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0924_Compatible_codes_104_and_11627___test_124(self):
        """Compatible codes (104 and 11627) - test 124 (Difficulty: moderate)"""
        codes = ['104', '11627']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0925_Compatible_codes_104_and_117___test_125(self):
        """Compatible codes (104 and 117) - test 125 (Difficulty: moderate)"""
        codes = ['104', '117']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0926_Compatible_codes_104_and_11704___test_126(self):
        """Compatible codes (104 and 11704) - test 126 (Difficulty: moderate)"""
        codes = ['104', '11704']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0927_Compatible_codes_104_and_11705___test_127(self):
        """Compatible codes (104 and 11705) - test 127 (Difficulty: moderate)"""
        codes = ['104', '11705']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0928_Compatible_codes_104_and_11707___test_128(self):
        """Compatible codes (104 and 11707) - test 128 (Difficulty: moderate)"""
        codes = ['104', '11707']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0929_Compatible_codes_104_and_11713___test_129(self):
        """Compatible codes (104 and 11713) - test 129 (Difficulty: moderate)"""
        codes = ['104', '11713']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0930_Compatible_codes_104_and_11714___test_130(self):
        """Compatible codes (104 and 11714) - test 130 (Difficulty: moderate)"""
        codes = ['104', '11714']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0931_Compatible_codes_104_and_11716___test_131(self):
        """Compatible codes (104 and 11716) - test 131 (Difficulty: moderate)"""
        codes = ['104', '11716']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0932_Compatible_codes_104_and_11717___test_132(self):
        """Compatible codes (104 and 11717) - test 132 (Difficulty: moderate)"""
        codes = ['104', '11717']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0933_Compatible_codes_104_and_11719___test_133(self):
        """Compatible codes (104 and 11719) - test 133 (Difficulty: moderate)"""
        codes = ['104', '11719']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0934_Compatible_codes_104_and_11720___test_134(self):
        """Compatible codes (104 and 11720) - test 134 (Difficulty: moderate)"""
        codes = ['104', '11720']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0935_Compatible_codes_104_and_11721___test_135(self):
        """Compatible codes (104 and 11721) - test 135 (Difficulty: moderate)"""
        codes = ['104', '11721']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0936_Compatible_codes_104_and_11723___test_136(self):
        """Compatible codes (104 and 11723) - test 136 (Difficulty: moderate)"""
        codes = ['104', '11723']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0937_Compatible_codes_104_and_11724___test_137(self):
        """Compatible codes (104 and 11724) - test 137 (Difficulty: moderate)"""
        codes = ['104', '11724']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0938_Compatible_codes_104_and_11725___test_138(self):
        """Compatible codes (104 and 11725) - test 138 (Difficulty: moderate)"""
        codes = ['104', '11725']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0939_Compatible_codes_104_and_11726___test_139(self):
        """Compatible codes (104 and 11726) - test 139 (Difficulty: moderate)"""
        codes = ['104', '11726']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0940_Compatible_codes_104_and_11727___test_140(self):
        """Compatible codes (104 and 11727) - test 140 (Difficulty: moderate)"""
        codes = ['104', '11727']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0941_Compatible_codes_104_and_11728___test_141(self):
        """Compatible codes (104 and 11728) - test 141 (Difficulty: moderate)"""
        codes = ['104', '11728']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0942_Compatible_codes_104_and_11729___test_142(self):
        """Compatible codes (104 and 11729) - test 142 (Difficulty: moderate)"""
        codes = ['104', '11729']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0943_Compatible_codes_104_and_11730___test_143(self):
        """Compatible codes (104 and 11730) - test 143 (Difficulty: moderate)"""
        codes = ['104', '11730']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0944_Compatible_codes_104_and_11731___test_144(self):
        """Compatible codes (104 and 11731) - test 144 (Difficulty: moderate)"""
        codes = ['104', '11731']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0945_Compatible_codes_104_and_11732___test_145(self):
        """Compatible codes (104 and 11732) - test 145 (Difficulty: moderate)"""
        codes = ['104', '11732']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0946_Compatible_codes_104_and_11735___test_146(self):
        """Compatible codes (104 and 11735) - test 146 (Difficulty: moderate)"""
        codes = ['104', '11735']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0947_Compatible_codes_104_and_11736___test_147(self):
        """Compatible codes (104 and 11736) - test 147 (Difficulty: moderate)"""
        codes = ['104', '11736']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0948_Compatible_codes_104_and_11737___test_148(self):
        """Compatible codes (104 and 11737) - test 148 (Difficulty: moderate)"""
        codes = ['104', '11737']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0949_Compatible_codes_104_and_11800___test_149(self):
        """Compatible codes (104 and 11800) - test 149 (Difficulty: moderate)"""
        codes = ['104', '11800']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0950_Compatible_codes_104_and_11801___test_150(self):
        """Compatible codes (104 and 11801) - test 150 (Difficulty: moderate)"""
        codes = ['104', '11801']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0951_Compatible_codes_104_and_11810___test_151(self):
        """Compatible codes (104 and 11810) - test 151 (Difficulty: moderate)"""
        codes = ['104', '11810']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0952_Compatible_codes_104_and_11820___test_152(self):
        """Compatible codes (104 and 11820) - test 152 (Difficulty: moderate)"""
        codes = ['104', '11820']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0953_Compatible_codes_104_and_11823___test_153(self):
        """Compatible codes (104 and 11823) - test 153 (Difficulty: moderate)"""
        codes = ['104', '11823']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0954_Compatible_codes_104_and_11830___test_154(self):
        """Compatible codes (104 and 11830) - test 154 (Difficulty: moderate)"""
        codes = ['104', '11830']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0955_Compatible_codes_104_and_11833___test_155(self):
        """Compatible codes (104 and 11833) - test 155 (Difficulty: moderate)"""
        codes = ['104', '11833']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0956_Compatible_codes_104_and_119___test_156(self):
        """Compatible codes (104 and 119) - test 156 (Difficulty: moderate)"""
        codes = ['104', '119']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0957_Compatible_codes_104_and_11900___test_157(self):
        """Compatible codes (104 and 11900) - test 157 (Difficulty: moderate)"""
        codes = ['104', '11900']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0958_Compatible_codes_104_and_11912___test_158(self):
        """Compatible codes (104 and 11912) - test 158 (Difficulty: moderate)"""
        codes = ['104', '11912']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0959_Compatible_codes_104_and_11917___test_159(self):
        """Compatible codes (104 and 11917) - test 159 (Difficulty: moderate)"""
        codes = ['104', '11917']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0960_Compatible_codes_104_and_11919___test_160(self):
        """Compatible codes (104 and 11919) - test 160 (Difficulty: moderate)"""
        codes = ['104', '11919']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0961_Compatible_codes_104_and_120___test_161(self):
        """Compatible codes (104 and 120) - test 161 (Difficulty: moderate)"""
        codes = ['104', '120']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0962_Compatible_codes_104_and_12000___test_162(self):
        """Compatible codes (104 and 12000) - test 162 (Difficulty: moderate)"""
        codes = ['104', '12000']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0963_Compatible_codes_104_and_12001___test_163(self):
        """Compatible codes (104 and 12001) - test 163 (Difficulty: moderate)"""
        codes = ['104', '12001']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0964_Compatible_codes_104_and_12002___test_164(self):
        """Compatible codes (104 and 12002) - test 164 (Difficulty: moderate)"""
        codes = ['104', '12002']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0965_Compatible_codes_104_and_12003___test_165(self):
        """Compatible codes (104 and 12003) - test 165 (Difficulty: moderate)"""
        codes = ['104', '12003']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0966_Compatible_codes_104_and_12004___test_166(self):
        """Compatible codes (104 and 12004) - test 166 (Difficulty: moderate)"""
        codes = ['104', '12004']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0967_Compatible_codes_104_and_12005___test_167(self):
        """Compatible codes (104 and 12005) - test 167 (Difficulty: moderate)"""
        codes = ['104', '12005']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0968_Compatible_codes_104_and_12012___test_168(self):
        """Compatible codes (104 and 12012) - test 168 (Difficulty: moderate)"""
        codes = ['104', '12012']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0969_Compatible_codes_104_and_12017___test_169(self):
        """Compatible codes (104 and 12017) - test 169 (Difficulty: moderate)"""
        codes = ['104', '12017']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0970_Compatible_codes_104_and_12021___test_170(self):
        """Compatible codes (104 and 12021) - test 170 (Difficulty: moderate)"""
        codes = ['104', '12021']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0971_Compatible_codes_104_and_12022___test_171(self):
        """Compatible codes (104 and 12022) - test 171 (Difficulty: moderate)"""
        codes = ['104', '12022']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0972_Compatible_codes_104_and_12024___test_172(self):
        """Compatible codes (104 and 12024) - test 172 (Difficulty: moderate)"""
        codes = ['104', '12024']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0973_Compatible_codes_104_and_122___test_173(self):
        """Compatible codes (104 and 122) - test 173 (Difficulty: moderate)"""
        codes = ['104', '122']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0974_Compatible_codes_104_and_12200___test_174(self):
        """Compatible codes (104 and 12200) - test 174 (Difficulty: moderate)"""
        codes = ['104', '12200']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0975_Compatible_codes_104_and_12201___test_175(self):
        """Compatible codes (104 and 12201) - test 175 (Difficulty: moderate)"""
        codes = ['104', '12201']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0976_Compatible_codes_104_and_12203___test_176(self):
        """Compatible codes (104 and 12203) - test 176 (Difficulty: moderate)"""
        codes = ['104', '12203']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0977_Compatible_codes_104_and_12204___test_177(self):
        """Compatible codes (104 and 12204) - test 177 (Difficulty: moderate)"""
        codes = ['104', '12204']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0978_Compatible_codes_104_and_12205___test_178(self):
        """Compatible codes (104 and 12205) - test 178 (Difficulty: moderate)"""
        codes = ['104', '12205']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0979_Compatible_codes_104_and_12207___test_179(self):
        """Compatible codes (104 and 12207) - test 179 (Difficulty: moderate)"""
        codes = ['104', '12207']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0980_Compatible_codes_104_and_12208___test_180(self):
        """Compatible codes (104 and 12208) - test 180 (Difficulty: moderate)"""
        codes = ['104', '12208']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0981_Compatible_codes_104_and_12210___test_181(self):
        """Compatible codes (104 and 12210) - test 181 (Difficulty: moderate)"""
        codes = ['104', '12210']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0982_Compatible_codes_104_and_12213___test_182(self):
        """Compatible codes (104 and 12213) - test 182 (Difficulty: moderate)"""
        codes = ['104', '12213']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0983_Compatible_codes_104_and_12215___test_183(self):
        """Compatible codes (104 and 12215) - test 183 (Difficulty: moderate)"""
        codes = ['104', '12215']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0984_Compatible_codes_104_and_12217___test_184(self):
        """Compatible codes (104 and 12217) - test 184 (Difficulty: moderate)"""
        codes = ['104', '12217']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0985_Compatible_codes_104_and_12250___test_185(self):
        """Compatible codes (104 and 12250) - test 185 (Difficulty: moderate)"""
        codes = ['104', '12250']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0986_Compatible_codes_104_and_12254___test_186(self):
        """Compatible codes (104 and 12254) - test 186 (Difficulty: moderate)"""
        codes = ['104', '12254']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0987_Compatible_codes_104_and_12258___test_187(self):
        """Compatible codes (104 and 12258) - test 187 (Difficulty: moderate)"""
        codes = ['104', '12258']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0988_Compatible_codes_104_and_12261___test_188(self):
        """Compatible codes (104 and 12261) - test 188 (Difficulty: moderate)"""
        codes = ['104', '12261']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0989_Compatible_codes_104_and_12265___test_189(self):
        """Compatible codes (104 and 12265) - test 189 (Difficulty: moderate)"""
        codes = ['104', '12265']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0990_Compatible_codes_104_and_12268___test_190(self):
        """Compatible codes (104 and 12268) - test 190 (Difficulty: moderate)"""
        codes = ['104', '12268']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0991_Compatible_codes_104_and_12272___test_191(self):
        """Compatible codes (104 and 12272) - test 191 (Difficulty: moderate)"""
        codes = ['104', '12272']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0992_Compatible_codes_104_and_123___test_192(self):
        """Compatible codes (104 and 123) - test 192 (Difficulty: moderate)"""
        codes = ['104', '123']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0993_Compatible_codes_105_and_10801___test_193(self):
        """Compatible codes (105 and 10801) - test 193 (Difficulty: moderate)"""
        codes = ['105', '10801']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0994_Compatible_codes_105_and_10802___test_194(self):
        """Compatible codes (105 and 10802) - test 194 (Difficulty: moderate)"""
        codes = ['105', '10802']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0995_Compatible_codes_105_and_10803___test_195(self):
        """Compatible codes (105 and 10803) - test 195 (Difficulty: moderate)"""
        codes = ['105', '10803']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0996_Compatible_codes_105_and_10804___test_196(self):
        """Compatible codes (105 and 10804) - test 196 (Difficulty: moderate)"""
        codes = ['105', '10804']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0997_Compatible_codes_105_and_10805___test_197(self):
        """Compatible codes (105 and 10805) - test 197 (Difficulty: moderate)"""
        codes = ['105', '10805']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0998_Compatible_codes_105_and_10806___test_198(self):
        """Compatible codes (105 and 10806) - test 198 (Difficulty: moderate)"""
        codes = ['105', '10806']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_0999_Compatible_codes_105_and_10807___test_199(self):
        """Compatible codes (105 and 10807) - test 199 (Difficulty: moderate)"""
        codes = ['105', '10807']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        
    def test_yay_1000_Compatible_codes_105_and_10808___test_200(self):
        """Compatible codes (105 and 10808) - test 200 (Difficulty: moderate)"""
        codes = ['105', '10808']
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == 'YAY', \
            f"Expected YAY, got {result['decision']}. Reason: {result['reason']}"
        
        assert result['failed_check'] == None, \
            f"Expected failed_check None, got {result['failed_check']}"
        

if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
