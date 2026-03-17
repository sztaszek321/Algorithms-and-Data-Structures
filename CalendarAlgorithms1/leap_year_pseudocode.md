FUNCTION is_leap
    IF year % 400 == 0
        RETURN True
    IF year % 4 == 0
        IF year % 100 != 0
            RETURN True
    RETURN False
END FUNCTION

FUNCTION leap_year_main(year)
    VALIDATE year
    RESULT = CALL is_leap(year)
    RETURN Result
END FUNCTION