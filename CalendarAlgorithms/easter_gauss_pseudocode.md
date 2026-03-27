FUNCTION easter_G(year)
    CALCULATE a(year)
    CALCULATE b(year)
    CALCULATE c(year)
    CALCULATE A and B (year)
    CALCULATE d(a, A)
    CALCULATE e(b, c, d, B)
    IF d == 29 and e == 6
        easter = "19-04-" + year
    ELSEIF d == 28 and e == 6
        easter = "18-04-" + year
    ELSE
        IF d + e > 9
            IF d + e < 19
                h = "0"
            else
                h = ""
            easter = h + d + e - 9 + "-04-" + year
        ELSE
            easter = 22 + d + e + "-03-" + year
    RETURN easter
END FUNCTION

FUNCTION easter_gauss_main(year)
    VALIDATE year
    RESULT = CALL easter_G(year)
    RETURN Result
END FUNCTION