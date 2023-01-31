import os
import sys


class WRand:
    class _Rand(object):
        def __init__(self, block_sz = 48):
            import struct
            
            if block_sz < 4:
                raise ValueError
            self._block_sz = block_sz
            self._rand_big_int = None
            self._pos = 0

        def update(self):
            bt = os.urandom(self._block_sz)
            self._rand_big_int = int.from_bytes(bt, byteorder=sys.byteorder)
            self._pos = 0
        
        def get_next_int(self, sz_bt = 4):
            if sz_bt < 1:
                raise ValueError
            if not self._rand_big_int or \
            self._pos + sz_bt > self._block_sz:
                self.update()
            sz_bt_bit = sz_bt * 8
            msk = (2 ** sz_bt_bit - 1) << (self._pos * 8)
            ret = self._rand_big_int & msk
            ret >>= (self._pos * 8)
            self._pos += sz_bt
            return ret

    _rnd = None

    @staticmethod
    def get_int(from_n = 0, to_n = 16):
        if from_n < 0 or to_n <= from_n:
            raise ValueError(f"Invalid range: {from_n}, {to_n}")

        dlt = to_n - from_n
        dlt_sz_bit = sys.getsizeof(dlt)
        dlt_sz_bt = dlt_sz_bit // 8
        if dlt_sz_bit % 8:
            dlt_sz_bt += 1

        if not WRand._rnd:
            WRand._rnd = WRand._Rand(dlt_sz_bt * 12)
    
        if dlt > 1:
            dlt += 1
            ret = WRand._rnd.get_next_int(dlt_sz_bt) %  dlt
        elif (WRand._rnd.get_next_int(dlt_sz_bt) %  2) > 0:
            ret = 1
        else:
            ret = 0
        ret += from_n
        return ret

    @staticmethod
    def get_bool():
        if 1 == WRand.get_int(0, 1):
            return True
        return False

    @staticmethod
    def choice(lst):
        if not isinstance(lst, list):
            raise ValueError(f"Invalid type {type(lst)} for list")
        if 1 == len(lst):
            return lst[0]
        ret = WRand.get_int(0, len(lst)-1)
        return lst[ret]
