

FFT = lambda coeff_arr, w_n: (lambda f, *args: f(f, *args))((lambda fft_rec, coeff_arr, w_n, n: coeff_arr if n == 1 else (lambda f, *args: f(f, *args))(lambda for_rec, evens, odds, k, n, w, w_n, dft: dft if k == n // 2 else for_rec(for_rec, evens, odds, k + 1, n , w * w_n, w_n,[evens[k] + w * odds[k] if i == k else evens[k] - w * odds[k] if i == k + n // 2 else dft[i] for i in range(n)]), fft_rec(fft_rec, [coeff_arr[i] for i in range(0, n, 2)], w_n ** 2, len(range(0, n, 2))),fft_rec(fft_rec, [coeff_arr[i] for i in range(1, n, 2)], w_n ** 2, len(range(1, n, 2))), 0, n, 1, w_n, [0 for _ in range(n)])), coeff_arr, w_n, len(coeff_arr))
