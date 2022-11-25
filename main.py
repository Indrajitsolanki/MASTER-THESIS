import sys
from ntru import *

N=7
p=29
q=491531

if (len(sys.argv)>1):
	N=int(sys.argv[1])
if (len(sys.argv)>2):
	p=int(sys.argv[2])
if (len(sys.argv)>3):
	q=int(sys.argv[3])

print("==== Bob generates public key =====")

Bob=Ntru(N,p,q)
print("Bob picks two polynomials (g and f):")
f=[1,1,-1,0,-1,1]
g=[-1,0,1,1,0,0,-1]
d=2

print("f(x)= ",f)
print("g(x)= ",g)
print("d   = ",d)

Bob.genPublicKey(f,g,2)
pub_key=Bob.getPublicKey()
print("Bob's Public Key: ",pub_key)
print("-------------------------------------------------")


print("\n==== Alice generates public key =====")

Alice=Ntru(N,p,q)

Alice.setPublicKey(pub_key)

msg=[1,0,1,0,1,1,1]

print("Alice's Message   : ",msg)
ranPol=[-1,-1,1,1]

print("Alice's Random Polynomial  : ",ranPol)

encrypt_msg=Alice.encrypt(msg,ranPol)
print("Encrypted Message          : ", encrypt_msg)
print("-------------------------------------------------")

print("\n==== Bob decrypts =====")

print("Decrypted Message          : ", Bob.decrypt(encrypt_msg))
