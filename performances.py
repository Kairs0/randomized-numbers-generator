from linear_congruential import LCG


def test_performances():
    a = LCG()
    a.set_seed(23)
    array_result = [0 for i in range(100)]
    for i in range(10000000):
        generated = a.generate() % 100
        array_result[generated - 1] += 1

    result_per_cent = [str((number / 10000000) * 100) + "%" for number in array_result]
    print(result_per_cent)
