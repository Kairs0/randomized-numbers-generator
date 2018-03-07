class MT(object):

    """
    The integer portion of the Mersenne twister algorithm does not involve any arithmetic in the sense of
    addition, subtraction, multiplication or division. All the operations are shifts, and's, or's, and xor's.

    All the elements of the state, except the last, are unsigned 32 bit random integers that form a cache which
    is carefully generated upon startup. This generation is triggered by a seed, a single integer that initiates
    the whole process.

    The last element of the state is a pointer into the cache. Each request for a random integer causes an
    element to be withdrawn from the cache and the pointer incremented. The element is "tempered" with additional
    logical operations to improve the randomness. When the pointer reaches the end of the cache, the cache is
    refilled with another 623 elements.

    The algorithm is analyzed by investigating the group theoretic properties of the permutation and tempering
    operations. The parameters have been chosen so that the period is the Mersenne prime 2^19937-1. This period
    is much longer than any other random number generator proposed before or since and is one of the reasons for
    MT's popularity.

    By design, the results generated satisfy an equidistribution property in a 623-dimensional cube.

    (description source : https://blogs.mathworks.com/cleve/2015/04/17/random-number-generator-mersenne-twister/)
    """

    def __init__(self):
        self.word_size = 32  # w for MT19937
        self.degree_of_recurrence = 624  # n for MT19937
        self.middle_word = 397  # m for MT19937
        self.separation_point_one_word = 31  # r for MT19937

        self.rnf_matrix_twist_coefs = 0x9908B0DF  # 9908B0DF for MT19937
        self.tempering_bitmask_b = 0x9D2C5680
        self.tempering_bitmask_c = 0xEFC60000

        self.tempering_bitshift_s = 7
        self.tempering_bitshift_t = 15

        self.state_vector = []

        self.parameter_generator = 1812433253  # f for MT19937

        self.counter = 0

        # additional Mersenne Twister tempering bit shifts/masks
        self.u = 11
        self.d = 0xFFFFFFFF
        self.i = 18

    def init_generator(self, seed=5489):
        self.state_vector[0] = seed

        # xi = f × (xi-1 ⊕ (xi-1 >> (w-2))) + i
        for i in range(1, self.degree_of_recurrence):
            self.state_vector[i] = self.parameter_generator * (
                    self.state_vector[i - 1] ^ (self.state_vector[i - 1] >> (self.word_size - 2))
            ) + i

    def generate(self):
        if self.counter >= self.degree_of_recurrence:
            # regenerate state vector
            pass

        y = self.state_vector[self.counter]
        self.counter += 1

        y = y ^ (y >> 11 & self.d)
        y = y ^ (y << self.tempering_bitshift_s) & self.tempering_bitmask_b
        y = y ^ (y << self.tempering_bitshift_t) & self.tempering_bitmask_c
        y = y ^ (y >> self.i)

        return y

    def re_init_generator(self):
        for i in range(self.degree_of_recurrence - self.middle_word):
            # tmp = (self.state_vector[i] & self.)
            pass
