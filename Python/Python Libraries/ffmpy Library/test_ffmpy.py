# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 15:21:57 2022

@author: Zipeng 

This script runs the simulation enviroment created by Sajjid
"""

import ffmpy
ff = ffmpy.FFmpeg(
    inputs={'input.mp4':  None},
    outputs={'output.avi': None}
)
ff.run()