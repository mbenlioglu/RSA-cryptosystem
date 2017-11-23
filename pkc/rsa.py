"""
    Created by mbenlioglu on 11/22/2017
"""


def encrypt(msg, exp, mod):
    """
    Encrypts the message by calculating msg ** exp mod m
    :param msg: message to be encrypted
    :param exp: public key, exponent
    :param mod: public key, modulus that the encryption takes place
    :return:
    """
    return pow(msg, exp, mod)


def decrypt(cip, exp, mod):
    """
    Decrypts the cipher text by calculating cip ** exp mod m
    :param cip: cipher text
    :param exp: private key, exponent
    :param mod: public key, modulus that the decryption takes place
    :return:
    """
    return encrypt(cip, exp, mod)
