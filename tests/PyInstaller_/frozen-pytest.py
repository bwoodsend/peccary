# -*- coding: utf-8 -*-
"""
Freeze pytest.main() with peccary included.
"""
import sys
import peccary

import pytest

sys.exit(pytest.main(sys.argv[1:] + ["--no-cov", "--tb=native"]))
