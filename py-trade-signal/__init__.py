#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .macd import MacdSignal


class TradeSignal:

    def __init__(self):
        """Initialize the TradeSignal class

        This class uses trading instrument agnostic technical indicators from peerchemist's finta Python module: https://github.com/peerchemist/finta
        """
        self.macd_signal = MacdSignal()