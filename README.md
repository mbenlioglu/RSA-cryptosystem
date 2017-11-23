# RSA Crypto-system trials
Some basic examples for encryption, decryption and attacking on RSA

**Implemented by:**
 * [M.Mucahid Benlioglu](https://github.com/mbenlioglu)

## Getting started
In order to run examples implemented you need to run /rsa_cryptosystem.py with the following
instructions, while your current working directory is project root.
    
    $ python rsa_cryptosystem.py

Note that this project is written and tested under [Python 2.7.x](https://docs.python.org/2/)

### Usage:

Below you can see the explanations of the examples included this project

**Strength of Double Encryption:**

In this example a message is encrypted with textbook RSA twice, using public keys e1 and e2. To show it is no different
in an attacker's point of view, it is demonstrated that the cipher can be decrypted in a single step.

_Proof:_

_c<sub>2</sub> = (c<sub>1</sub>)<sup>e<sub>2</sub></sup> mod N = (m<sup>e<sub>1</sub></sup>)<sup>e<sub>2</sub></sup>  mod N
= m<sup>e<sub>3</sub></sup>  mod N, where e<sub>3</sub> = e<sub>1</sub> × e<sub>2</sub>  mod ϕ(N). Therefore, we can find a
d<sub>3</sub> = e<sub>3</sub><sup>-1</sup>  mod N so that c<sub>2</sub><sup>d<sub>3</sub></sup> = m mod N, because we know
that e<sub>1</sub> and e<sub>2</sub> has inverses in mod φ(N), say d<sub>1</sub> and d<sub>2</sub> (we know, because they
are selected as encryption keys) then, d<sub>3</sub> = e<sub>3</sub><sup>-1</sup>  mod ϕ(N) = (e<sub>1</sub> × e<sub>2</sub>)<sup>-1</sup> mod ϕ(N)
= e<sub>1</sub><sup>-1</sup> × e<sub>2</sub><sup>-1</sup> mod ϕ(N) = d<sub>1</sub> × d<sub>2</sub>  mod ϕ(N). Therefore,
we proved that there exists a d<sub>3</sub> such that c<sub>2</sub><sup>d<sub>3</sub></sup> = m mod N, so, an attacker
only needs to find this d<dub>3</dub>, which is no different than finding the decryption key in single encryption._

**4-Digit PIN code extraction:**

Since there are only 10000 4-digit numbers (which is quite few), we can easily devise a brute-force method, where every
possible PIN is encrypted using public key and the result is compared with the cipher text, we conclude that we found the
PIN if the encrypted value is same as obtained cipher text.

**Chosen cipher-text attack:**

In this example we have a remote oracle, which we can give any cipher text, c', (except the one wanted to be decrypted)
and obtain its decrypted version.

_Proof:_

_We know that the remote oracle will calculate c'<sup>d</sup>, with c’ provided by us. If we choose a random k in mod N,
where gcd(k,N)=1, and send c' = k<sup>e</sup> × c mod N = k<sup>e</sup> × m<sup>e</sup> mod N; and oracles result will be
m' = c'<sup>d</sup> mod N = k<sup>e × d mod ϕ(N)</sup> × m<sup>e × d mod ϕ(N)</sup> mod N = k × m mod N , from that we
can extract m = k<sup>-1</sup> × m' mod N, also we know k<sup>-1</sup> exists because we picked k such that gcd(k,N)=1._

In the implemented example random number picked as `k = 228160238 mod N` and remote oracle queried using this k and above
explanations. The result is returned from remote oracle is stored for demonstration.

Note that there is no random number generator for k or communication module with oracle, simply because it was available
for a short time. 
