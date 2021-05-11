from django import template

register = template.Library()

def dict_filter(dictionary,key):
    
    return dictionary[key]


register.filter("dict_filter", dict_filter)
