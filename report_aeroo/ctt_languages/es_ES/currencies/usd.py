#!/usr/bin/python
# -*- coding: utf8 -*-

from odoo.addons.report_aeroo.ctt_objects import ctt_currency


class usd(ctt_currency):

    def _init_currency(self):
        self.language = u'es_ES'
        self.code = u'USD'
        self.fractions = 100
        self.cur_singular = u' dólar Américano'
        self.cur_plural = u' dólares Américanos'
        self.frc_singular = u' centavo'
        self.frc_plural = u' centavos'
        # grammatical genders: f - feminine, m - masculine, n -neuter
        self.cur_gram_gender = 'm'
        self.frc_gram_gender = 'm'

usd()
