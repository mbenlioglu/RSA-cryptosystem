"""
    Created by mbenlioglu on 11/22/2017
"""
import sys
from pkc import rsa, util
from values import example_params

# ======================================================================================================================
# decrypt double encryption in single exponentiation
prime_fact = (example_params.double_enc_p, example_params.double_enc_q)
phi_n = (prime_fact[0] - 1) * (prime_fact[1] - 1)

# calculate single step encryption key e3, from e1, e2
e3 = (example_params.double_enc_e1 * example_params.double_enc_e2) % phi_n
print 'Calculated encryption key that will encrypt the message in single step:'
print e3

# single decryption key derived from above keys (explained in report)
d3 = util.multiplicative_inverse(e3, phi_n)
print 'Calculated decryption key that will decrypt the cipher in single decryption:'
print d3

# obtain message withs single decryption operation
msg = rsa.decrypt(example_params.double_enc_c, d3, prime_fact[0] * prime_fact[1])
print 'Obtained plain message:'
print msg
print 'Is it correct?...', 'yes' if rsa.encrypt(rsa.encrypt(msg, example_params.double_enc_e1,
                                                            prime_fact[0] * prime_fact[1]),
                                                example_params.double_enc_e2,
                                                prime_fact[0] * prime_fact[1]) == example_params.double_enc_c else 'no'
print '\n'
# ======================================================================================================================
# find 4-digit pin
is_found = False
sys.stdout.write('Searching pin...')
for pin in xrange(9999):
    if rsa.encrypt(pin, example_params.pin_e, mod=example_params.pin_n) == example_params.pin_c:
        is_found = True
        sys.stdout.write('Found! Pin is:')
        sys.stdout.write(str(pin) + '\n')
if not is_found:
    sys.stdout.write("Couldn't find pin!\n")
print '\n'
# ======================================================================================================================
# extract message

print 'Calculating cipher text to be decrypted by remote oracle...'

c_prime = (pow(example_params.cha_rnd, example_params.cha_e, example_params.cha_n) * example_params.cha_c)
c_prime %= example_params.cha_n
print 'It is:\n', c_prime

print "\nCalculating plain text using remote oracle's answer"

# Note that the query is pre-made and stored, now we are directly using that result here
# refer to README for further explanation
msg = util.multiplicative_inverse(example_params.cha_rnd, example_params.cha_n) * example_params.cha_ans
msg %= example_params.cha_n
print 'Resulting plain message is:\n', msg
print 'Is it correct?...', 'yes' if rsa.encrypt(msg, example_params.cha_e,
                                                mod=example_params.cha_n) == example_params.cha_c else 'no'
