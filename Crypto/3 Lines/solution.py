import random
import hashlib
import string

ct = "99f2e803248f5923faccd5b74eeac9fdd1fe9485be324217b5d180d04dfcb87f2df9c7c23d39de0710ec45bb2348a2870f0e3fa24833955ae7be0fc6ff2540f89cca8d684240e24dd459f2d439fae30c45fa9beaa3d9ea2ad7a09cd68b6a33aeabe24565b93dbc1d1dda3429adcc926c0c2ecd5cb4ba7dae4f84402c5ebe87f566a18289224fcaca68694426ede468a05638b0be1bce3838bca75e14cfe0818ffcc4103fcaf40d4720096ea4ed0fa2a7b241600bbbbc8cfbba760be3f23083bcd8c3fc67def99b7b61593abe7920f3c0790303191a1deaa93200d05f786405ee4315fce0913a690ba14db3bd46a1c89ab241600bbbbc8cfbba760be3f23083bc45fa9beaa3d9ea2ad7a09cd68b6a33ae4dd3479a7d8a13e22518a22202f4da7b4f2663dcc42d6c7746733d2c9bcb669db6ac971e55bee482346a196c2a82365ad21f9fc127b9849fddfaf59354916108d8c3fc67def99b7b61593abe7920f3c051b2395680b833ec1f7b1a44a0bafe05348bd749ca9ee5f03b04b8a2f0befc79fcc4103fcaf40d4720096ea4ed0fa2a7d21f9fc127b9849fddfaf5935491610814a2750f09d061e1744e376eeaae46088bdb666d756911879b3f77e93d945da30f0e3fa24833955ae7be0fc6ff2540f8d21f9fc127b9849fddfaf59354916108b4a2d301ddc8a3e8c500551900bdffd44dd3479a7d8a13e22518a22202f4da7b638c5071774c3ddd8b600c3fe1b137890f0e3fa24833955ae7be0fc6ff2540f831bbeb867c695411485ebf8a2f748b6b"
# "P" == 99f2e803248f5923faccd5b74eeac9fd
output = ""
secret_number = 0

# find the secret number
for i in range(0, 1000000):
    if (
        hashlib.md5(str((ord("P") << 7) ^ i).encode()).hexdigest()
        == "99f2e803248f5923faccd5b74eeac9fd"
    ):
        secret_number = i
        break

# find each character that matches the corresponding hash
for i in range(0, len(ct), 32):
    for p in string.printable:
        if (
            hashlib.md5(str((ord(p) << 7) ^ secret_number).encode()).hexdigest()
            == ct[i : i + 32]
        ):
            output = output + p

print(output)
