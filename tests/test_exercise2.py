import os
import sqlite3
import subprocess

import pytest

import exercise2
from exercise2 import *


# bug report 1
def test_r1_clamp_with_middle_value():    
    assert clamp(10, 5, 15) == 10
