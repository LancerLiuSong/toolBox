import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import xml.etree.ElementTree as ET


tree = ET.parse('country_data.xml')
root = tree.getroot()

