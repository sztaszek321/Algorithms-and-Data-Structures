FUNCTION easter_MJB(year)
    CALCULATE a(year)
    CALCULATE b(year)
    CALCULATE c(year)
    CALCULATE d(b)
    CALCULATE e(b)
    CALCULATE f(b)
    CALCULATE g(b, f)
    CALCULATE h(a, b, d, g)
    CALCULATE i(c)
    CALCULATE k(c)
    CALCULATE l(e, i, h, k)
    CALCULATE m(a, h, l)
    CALCULATE p(h, l, m)
    CALCULATE day(p)
    CALCULATE month(h, l, m)
    RETURN day + month + year
END FUNCTION

FUNCTION easter_mjb_main(year)
    VALIDATE year
    RESULT = CALL easter_MJB(year)
    RETURN Result
END FUNCTION