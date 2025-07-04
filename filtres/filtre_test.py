#!/usr/bin/python

def msg(data,str):
    return data + ' ' + str

class FilterModule(object):
    def filters(self):
        return {
            'filtre_test': msg
        }

